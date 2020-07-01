from typing import List

from PySide2.QtWidgets import QHBoxLayout, QLayout

from src.controllers.charactercontroller import CharacterController
from src.controllers.pagecontroller import PageController
from src.views.sheetview import SheetView


class SheetController:
    def __init__(self, active_character_controller: CharacterController) -> None:
        self.page_controllers: List[PageController] = []
        self.add_page_controller(PageController(active_character_controller))
        self.set_active_page(0)
        self.sheet_view = None

    def set_active_page(self, page_number: int) -> None:
        self.active_page = 0
        self.current_page_view = self.page_controllers[self.active_page].page_view

    def add_page_controller(self, page_controller: PageController) -> None:
        self.page_controllers.append(page_controller)

    def get_layout(self) -> QLayout:
        sheet_view = SheetView(self.current_page_view)
        layout = QHBoxLayout()
        layout.addWidget(sheet_view)
        return layout
