import logging

from PySide2.QtCore import QStandardPaths

from cscreator.plugins.importers.dndbeyond import DNDBeyond
from cscreator.plugins.importers.importerplugin import ImporterPlugin

logger = logging.getLogger(__name__)


class PluginManager:
    def __init__(self):
        self.plugin_dir = QStandardPaths.writableLocation(
            QStandardPaths.AppDataLocation
        )
        self.importers = [DNDBeyond]
        self.exporters = []

    def get_importer(self, name: str) -> ImporterPlugin:
        for importer in self.importers:
            if importer.name == name:
                return importer
