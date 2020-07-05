import logging

from PySide2.QtWidgets import (
    QSpinBox,
    QTextEdit,
    QCheckBox,
    QDialog,
)
from PySide2.QtWidgets import QWidget, QLabel, QLineEdit

from src.models.charactermodel import CHProperty, Equipment, CharacterProperty
from src.models.charactersubmodel import Spell
from qt_design.character_ui import Ui_Form
from qt_design.equipment_ui import Ui_EquipmentDialog
from qt_design.spell_dialog import Ui_spellDialog

logger = logging.getLogger(__name__)


class CharacterView(QWidget):
    def __init__(self, player_model, parent=None):
        super(CharacterView, self).__init__(parent)
        self.char_layout = Ui_Form()
        self.char_layout.setupUi(self)
        self.player_model = player_model

    def register_signals(self, player_model):
        for value in CHProperty:
            logger.debug(f"Checking if {value} exists in UI")
            if hasattr(self.char_layout, value.name):
                attribute = getattr(self.char_layout, value.name)
                self.register_signal_for_generic_widget(
                    attribute, player_model.character_view_changed_event, value
                )
            else:
                logger.info(f"{value} does not exists in UI")

    def character_model_changed_event(self, subject, character_property, value):
        logger.debug(
            f"Event fired from subject {subject} with arg {character_property}"
        )
        if not hasattr(self.char_layout, character_property.name):
            logger.debug(
                f"CharacterView does not have a property {character_property}. Ignoring event."
            )
            return
        attribute = getattr(self.char_layout, character_property.name)
        # TODO it might be more elegant to simply use "character_property" here, but this might cause some weird race-conditions
        self.set_value_for_generic_widget(
            attribute, subject.get_ch_property(character_property)
        )

    def set_value_for_generic_widget(self, attribute: QWidget, ch_property: CharacterProperty) -> None:
        #TODO typechecking here of property_value we are setting
        if isinstance(attribute, QLineEdit):
            attribute.setText(str(ch_property.property_value)) #TODO this casting should occur somewhere else
        elif isinstance(attribute, QSpinBox):
            try:
                int_value = int(ch_property.property_value)
                attribute.setValue(int_value)
            except ValueError:
                logging.warning(
                    f"Attempting to set SpinBox {attribute} with str character_property {ch_property.property_value}, which is not castable to int."
                )
        elif isinstance(attribute, QLabel):
            attribute.setText(ch_property.property_value)
        elif isinstance(attribute, QTextEdit):
            attribute.blockSignals(True)
            attribute.setText(ch_property.property_value)
            attribute.blockSignals(False)
        elif isinstance(attribute, QCheckBox):
            attribute.setChecked(ch_property.property_value)
        else:
            logging.warning(
                f"Attempting to set attribute of unknown type {type(attribute)}"
            )

    def register_signal_for_generic_widget(self, attribute, method, character_property):
        # Signals from QT do not pass the emitter as argument.
        # We however do not want to create a different signal handler for each property.
        # Therefore we add this cool lambda here.
        # We add a fixed parameter "character_property" while connecting to the signal.
        # Then, when the signal is emitted, we get the new character_property.
        lambda_method = lambda changed_value: method(character_property, changed_value)
        if isinstance(attribute, QLineEdit):
            attribute.textEdited.connect(lambda_method)
        elif isinstance(attribute, QSpinBox):
            attribute.valueChanged.connect(lambda_method)
        elif isinstance(attribute, QTextEdit):
            lambda_method = lambda: method(character_property, attribute.toPlainText())
            attribute.textChanged.connect(lambda_method)
        elif isinstance(attribute, QCheckBox):
            lambda_method = lambda changed_value: method(
                character_property, True if changed_value > 0 else False
            )

            attribute.stateChanged.connect(lambda_method)
        elif isinstance(attribute, QLabel):
            pass  # logger.debug("QLabels shouldn't change without the Model doing so.")
        else:
            logging.warning(
                f"Attempting to register signal of unknown type {attribute}"
            )
