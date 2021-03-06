import logging

from PySide2.QtCore import QStandardPaths, Qt
from PySide2.QtGui import QDesktopServices, QKeySequence
from obsub import event

from src.exporters.exportview import ExportPdfWizardFactory
from src.importers.importview import PdfWizardFactory
from src.importers.pdfimporter import PDFImporter

logger = logging.getLogger(__name__)

from PySide2.QtWidgets import (
    QMainWindow,
    QApplication,
    QTabWidget,
    QWidget,
    QHBoxLayout,
    QLabel,
)


class MainView(QMainWindow):
    def __init__(self, parent=None):
        super(MainView, self).__init__(parent)
        self.tabs = QTabWidget()

        self.setup_menus()

        self.character_tab = QWidget()
        self.sheet_tab = QWidget()
        self.setup_tabs()

        self.setWindowTitle("Charactersheet Creator")

        # self.puzzleWidget.clear()
        logger.debug("MainView constructed")

        self.pdf_wizard_factory = PdfWizardFactory()
        self.export_pdf_wizard_factory = ExportPdfWizardFactory()

        self.export_debug_action = None

    @event
    def create_new_player(self):
        logger.info("New player creation requested")

    @event
    def export_to_sheet(self):
        logger.info("New sheet creation requested")

    def setup_menus(self):

        file_menu = self.menuBar().addMenu("&File")

        exit_action = file_menu.addAction("E&xit")
        exit_action.setShortcut(QKeySequence("Ctrl+Q"))

        character_menu = self.menuBar().addMenu("&Character")
        import_action = character_menu.addAction("&Import from PDF")
        import_action.triggered.connect(lambda: self.pdf_wizard_factory.create(self))
        import_action = character_menu.addAction("&Create new Character")
        import_action.triggered.connect(self.create_new_player)

        export_menu = self.menuBar().addMenu("&Export")
        export_debug_action = export_menu.addAction("Export Debug")
        export_debug_action.triggered.connect(
            lambda: self.export_pdf_wizard_factory.create(self)
        )

        resource_menu = self.menuBar().addMenu("&Resources")
        open_app_data = resource_menu.addAction("Open Appdata Folder")
        dir_to_open = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
        open_app_data.triggered.connect(lambda: QDesktopServices.openUrl(dir_to_open))

        exit_action.triggered.connect(QApplication.instance().quit)

        logger.debug("Menus set-up")
        # restart_action.triggered.connect(self.setup_overview)

    def setup_tabs(self):

        # Initialize tab screen
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.character_tab, "Character")
        self.tabs.addTab(self.sheet_tab, "Sheet")

        self.setCentralWidget(self.tabs)

        temp_layout = QHBoxLayout()
        label = QLabel(
            'No Character added yet.\nImport one or create a new one via the "Character" menu.'
        )
        label.setAlignment(Qt.AlignCenter)
        temp_layout.addWidget(label)
        self.character_tab.setLayout(temp_layout)

        logger.debug("Tabs set-up")

    def set_character_layout(self, qt_layout):
        current_layout = self.character_tab.layout()

        # By assigning the current layout to a unused widget, deletion is forced
        garbage_collecting_widget = QWidget()
        garbage_collecting_widget.setLayout(current_layout)

        self.character_tab.setLayout(qt_layout)
        logger.debug("Character layout set")

    def set_sheet_layout(self, qt_layout):

        self.sheet_tab.setLayout(qt_layout)
        logger.debug("Sheet layout set")
