import logging.config

import yaml
from PySide2.QtCore import QStandardPaths, QDir
from PySide2 import QtSvg, QtXml

with open("log_config.yml", "r") as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)

logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

from PySide2.QtWidgets import QApplication

import os, shutil


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


if __name__ == "__main__":
    logger.info("Application started")
    import sys

    app = QApplication(sys.argv)

    from cscreator.maincontroller import MainController

    qss = "qt_design/stylesheet.qss"
    with open(qss, "r") as fh:
        app.setStyleSheet(fh.read())

    app.setApplicationName("CSCreator")

    data_location = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
    data_dir = QDir(data_location)
    if not data_dir.exists():
        data_dir.mkpath(data_location)
    if not data_dir.exists("importers"):
        data_dir.mkdir("importers")

    if os.environ.get("DEBUG") is not None:
        copytree(
            "cscreator/plugins/importers", os.path.join(data_location, "importers")
        )

    main_controller = MainController()
    main_view = main_controller.get_window()
    main_view.show()
    sys.exit(app.exec_())
