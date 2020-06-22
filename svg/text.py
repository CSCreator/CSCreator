from PySide2.QtGui import QFont, QFontMetrics


def text_width(text, font="Arial", fontsize=10):
    font = QFont(font, fontsize)
    fm = QFontMetrics(font)
    points_wide = fm.boundingRect(text).width()
    return points_wide
