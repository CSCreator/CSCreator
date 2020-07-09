import json
import logging
import os

from PySide2.QtCore import QStandardPaths
from fitz import Widget

from exceptions import DefinitionFileUnreadableException
from src.data.importers.dndbeyond import DNDBeyond
from src.data.importers.importerplugin import ImporterPlugin
from src.models.charactermodel import CHProperty

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
