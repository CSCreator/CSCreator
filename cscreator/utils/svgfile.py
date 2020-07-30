from lxml import etree
from copy import deepcopy
import codecs

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

SVG_NAMESPACE = "http://www.w3.org/2000/svg"
XLINK_NAMESPACE = "http://www.w3.org/1999/xlink"
SVG = "{%s}" % SVG_NAMESPACE
XLINK = "{%s}" % XLINK_NAMESPACE
NSMAP = {None: SVG_NAMESPACE,
         'xlink': XLINK_NAMESPACE}


class FigureElement:
    """Base class representing single figure element"""
    def __init__(self, xml_element):
        self.root = xml_element

    def moveto(self, x, y, scale=1):
        """Move and scale element.

        Parameters
        ----------
        x, y : float
             displacement in x and y coordinates in user units ('px').
        scale : float
             scaling factor. To scale down scale < 1,  scale up scale > 1.
             For no scaling scale = 1.
        """
        self.root.set("transform", "translate(%s, %s) scale(%s) %s" %
                      (x, y, scale, self.root.get("transform") or ''))

    def rotate(self, angle, x=0, y=0):
        """Rotate element by given angle around given pivot.

        Parameters
        ----------
        angle : float
            rotation angle in degrees
        x, y : float
            pivot coordinates in user coordinate system (defaults to top-left
            corner of the figure)
        """
        self.root.set("transform", "%s rotate(%f %f %f)" %
                      (self.root.get("transform") or '', angle, x, y))

    def skew(self, x=0, y=0):
        """Skew the element by x and y degrees
        Convenience function which calls skew_x and skew_y

        Parameters
        ----------
        x,y : float, float
            skew angle in degrees (default 0)

            If an x/y angle is given as zero degrees, that transformation is omitted.
        """
        if x is not 0:
            self.skew_x(x)
        if y is not 0:
            self.skew_y(y)

        return self

    def skew_x(self, x):
        """Skew element along the x-axis by the given angle.

        Parameters
        ----------
        x : float
            x-axis skew angle in degrees
        """
        self.root.set("transform", "%s skewX(%f)" %
                      (self.root.get("transform") or '', x))
        return self

    def skew_y(self, y):
        """Skew element along the y-axis by the given angle.

        Parameters
        ----------
        y : float
            y-axis skew angle in degrees
        """
        self.root.set("transform", "%s skewY(%f)" %
                      (self.root.get("transform") or '', y))
        return self

    def scale_xy(self, x=0, y=None):
        """Scale element separately across the two axes x and y.
            If y is not provided, it is assumed equal to x (according to the
            W3 specification).

        Parameters
        ----------
        x : float
            x-axis scaling factor. To scale down x < 1, scale up x > 1.
        y : (optional) float
            y-axis scaling factor. To scale down y < 1, scale up y > 1.

        """
        self.root.set("transform", "%s scale(%f %f)" %
                      (self.root.get("transform") or '',
                       x, y if y is not None else ''))

    def __getitem__(self, i):
        return FigureElement(self.root.getchildren()[i])

    def copy(self):
        """Make a copy of the element"""
        return deepcopy(self.root)

    def tostr(self):
        """String representation of the element"""
        return etree.tostring(self.root, pretty_print=True)

    def find_id(self, element_id):
        """Find element by its id.

        Parameters
        ----------
        element_id : str
            ID of the element to find

        Returns
        -------
        FigureElement
            one of the children element with the given ID."""
        find = etree.XPath("//*[@id=$id]")
        return FigureElement(find(self.root, id=element_id)[0])


class TextElement(FigureElement):
    """Text element.

    Corresponds to SVG ``<text>`` tag."""
    def __init__(self, x, y, text, size=8, font="Verdana",
                 weight="normal", letterspacing=0, anchor='start',
                 color='black'):
        txt = etree.Element(SVG+"text", {"x": str(x), "y": str(y),
                                         "font-size": str(size),
                                         "font-family": font,
                                         "font-weight": weight,
                                         "letter-spacing": str(letterspacing),
                                         "text-anchor": str(anchor),
                                         "fill": str(color)})
        txt.text = text
        FigureElement.__init__(self, txt)


class ImageElement(FigureElement):
    """Inline image element.

    Correspoonds to SVG ``<image>`` tag. Image data encoded as base64 string.
    """
    def __init__(self, stream, width, height, format='png'):
        base64str = codecs.encode(stream.read(), 'base64').rstrip()
        uri = "data:image/{};base64,{}".format(format,
                                               base64str.decode('ascii'))
        attrs = {
                'width': str(width),
                'height': str(height),
                XLINK+'href': uri
                }
        img = etree.Element(SVG+"image", attrs)
        FigureElement.__init__(self, img)


class LineElement(FigureElement):
    """Line element.

    Corresponds to SVG ``<path>`` tag. It handles only piecewise
    straight segments
    """
    def __init__(self, points, width=1, color='black'):
        linedata = "M{} {} ".format(*points[0])
        linedata += " ".join(map(lambda x: "L{} {}".format(*x), points[1:]))
        line = etree.Element(SVG+"path",
                             {"d": linedata,
                              "stroke-width": str(width),
                              "stroke": color})
        FigureElement.__init__(self, line)


class GroupElement(FigureElement):
    """Group element.

    Container for other elements. Corresponds to SVG ``<g>`` tag.
    """
    def __init__(self, element_list, attrib=None):
        new_group = etree.Element(SVG+"g", attrib=attrib)
        for e in element_list:
            if isinstance(e, FigureElement):
                new_group.append(e.root)
            else:
                new_group.append(e)
        self.root = new_group


class SVGFile:
    """SVG Figure.

    It setups standalone SVG tree. It corresponds to SVG ``<svg>`` tag.
    """
    def __init__(self, width=None, height=None):
        self.root = etree.Element(SVG+"svg", nsmap=NSMAP)
        self.root.set("version", "1.1")

        self._width = 0
        self._height = 0

        if width:
            self._width = width
        if height:
            self._height = height

    @property
    def width(self):
        """Figure width"""
        return self.root.get("width")

    @width.setter
    def width(self, value):
        self._width = value.value
        self.root.set('width', str(value))
        self.root.set("viewBox", "0 0 %s %s" % (self._width, self._height))

    @width.getter
    def width(self):
        return self._width

    @property
    def height(self):
        """Figure height"""
        return self.root.get("height")

    @height.setter
    def height(self, value):
        self._height = value.value
        self.root.set('height', str(value))
        self.root.set("viewBox", "0 0 %s %s" % (self._width, self._height))

    @height.getter
    def height(self):
        return self._height

    def append(self, element):
        """Append new element to the SVG figure"""
        try:
            self.root.append(element.root)
        except AttributeError:
            self.root.append(GroupElement(element).root)

    def getroot(self):
        """Return the root element of the figure.

        The root element is a group of elements after stripping the toplevel
        ``<svg>`` tag.

        Returns
        -------
        GroupElement
            All elements of the figure without the ``<svg>`` tag.
        """
        if 'class' in self.root.attrib:
            attrib = {'class': self.root.attrib['class']}
        else:
            attrib = None
        return GroupElement(self.root.getchildren(), attrib=attrib)

    def to_str(self):
        """
        Returns a string of the SVG figure.
        """
        return etree.tostring(self.root, xml_declaration=True,
                              standalone=True,
                              pretty_print=True)

    def save(self, fname, encoding="UTF-8"):
        """
        Save figure to a file
        Default encoding is "ASCII" when None is specified, as dictated by lxml .
        """
        out = etree.tostring(self.root,
                             xml_declaration=True,
                             standalone=True,
                             pretty_print=True,
                             encoding=encoding)
        with open(fname, 'wb') as fid:
            fid.write(out)

    def find_id(self, element_id):
        """Find elements with the given ID"""
        find = etree.XPath("//*[@id=$id]")
        return FigureElement(find(self.root, id=element_id)[0])

    def get_size(self):
        """Get figure size"""
        return self.root.get('width'), self.root.get('height')

    def set_size(self, size):
        """Set figure size"""
        w, h = size
        self.root.set('width', str(w))
        self.root.set('height', str(h))


def fromfile(fname):
    """Open SVG figure from file.

    Parameters
    ----------
    fname : str
        name of the SVG file

    Returns
    -------
    SVGFile
        newly created :py:class:`SVGFile` initialised with the file content
    """
    fig = SVGFile()
    with open(fname) as fid:
        svg_file = etree.parse(fid)

    fig.root = svg_file.getroot()
    return fig


def fromstring(text):
    """Create a SVG figure from a string.

    Parameters
    ----------
    text : str
        string representing the SVG content. Must be valid SVG.

    Returns
    -------
    SVGFile
        newly created :py:class:`SVGFile` initialised with the string
        content.
    """
    fig = SVGFile()
    svg = etree.fromstring(text.encode())

    fig.root = svg

    return fig