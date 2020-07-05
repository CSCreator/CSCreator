from PySide2.QtGui import QFont, QFontMetrics


def text_width(text: str, font: str = "Arial", fontsize: int = 10) -> int:
    font = QFont(font, fontsize)
    fm = QFontMetrics(font)
    points_wide = fm.boundingRect(text).width()
    return points_wide
