import logging
import typing
from enum import Enum, auto

import PySide2
from PySide2 import QtCore
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import QModelIndex, Qt
from PySide2.QtGui import QStandardItemModel
from PySide2.QtGui import Qt
from PySide2.QtWidgets import (
    QDataWidgetMapper,
    QVBoxLayout,
    QPlainTextEdit,
    QSpinBox,
    QTextEdit,
    QCheckBox,
    QDialog,
)
from PySide2.QtWidgets import QWidget, QListView, QGridLayout, QLabel, QLineEdit

from models.charactermodel import CH, Equipment
from models.charactersubmodel import Spell
from qt_design.character_ui import Ui_Form
from qt_design.equipment_ui import Ui_EquipmentDialog
from qt_design.spell_dialog import Ui_spellDialog
from views.itemdeligates.checkboxdelegate import CheckBoxDelegate
from views.itemdeligates.spinboxdelegate import SpinBoxDelegate

logger = logging.getLogger(__name__)

CH_value_string = {
    CH.CHARACTER_NAME: "Character Name",
    CH.CLASS_LEVEL: "Class and Level",
    CH.PLAYER_NAME: "Player Name",
    CH.RACE: "Race",
    CH.BACKGROUND: "Background",
    CH.XP: "Experience",
    CH.STR: "Strength",
    CH.DEX: "Dexterity",
    CH.CON: "Constitution",
    CH.INT: "Intelligence",
    CH.WIS: "Wisdom",
    CH.CHA: "Charisme",
    CH.STR_MOD: "Strength Modifier",
    CH.DEX_MOD: "Dextirity Modifier",
    CH.CON_MOD: "Constitution Modifier",
    CH.INT_MOD: "Intelligence Modifier",
    CH.WIS_MOD: "Wisdom Modifier",
    CH.CHA_MOD: "Charisma Modifier",
    CH.STR_ST_PROF: "Strength Saving Throw Proficiency",
    CH.DEX_ST_PROF: "Dexterity Proficiency",
    CH.CON_ST_PROF: "Constitution Proficiency",
    CH.INT_ST_PROF: "Intelligence Saving Throw Proficiency",
    CH.WIS_ST_PROF: "Wisdom Saving Throw Proficiency",
    CH.CHA_ST_PROF: "Charisma Saving Throw Proficiency",
    CH.STR_ST_MOD: "Strength Saving Throw Modifier",
    CH.DEX_ST_MOD: "Dexterity Modifier",
    CH.CON_ST_MOD: "Constitution Modifier",
    CH.INT_ST_MOD: "Intelligence Saving Throw Modifier",
    CH.WIS_ST_MOD: "Wisdom Saving Throw Modifier",
    CH.CHA_ST_MOD: "Charisma Saving Throw Modifier",
    CH.DEFENSES: "Defenses",
    CH.SAVE_MODIFIERS: "Saving throw modifiers",
    CH.PASSIVE_PERCEPTION: "Passive Perception",
    CH.PASSIVE_WISDOM: "Passive Wisdom",
    CH.PASSIVE_INVESTIGATION: "Passive Investigation",
    CH.SENSES: "Senses",
    CH.INITIATIVE: "Initiative modifier",
    CH.AC: "Armor Class",
    CH.PROF_BONUS: "Proficiency bonus",
    CH.ABILITYSAVEDC1: "CH.ABILITYSAVEDC1",
    CH.ABILITYSAVESCORE1: "CH.ABILITYSAVESCORE1",
    CH.ABILITYSAVESCORE2: "CH.ABILITYSAVESCORE2",
    CH.ABILITYSAVEDC2: "CH.ABILITYSAVEDC2",
    CH.SPEED: "Speed",
    CH.MAX_HP: "Maximum HP",
    CH.CURRENT_HP: "Current HP",
    CH.TEMP_HP: "Temporary HP",
    CH.TOTAL_HIT_DICE: "Total Hit Dice",
    CH.HIT_DICE: "Hit Dice Value",
    CH.SUCCESSFUL_SAVE_1: None,
    CH.SUCCESSFUL_SAVE_2: None,
    CH.SUCCESSFUL_SAVE_3: None,
    CH.FAILED_SAVE_1: None,
    CH.FAILED_SAVE_2: None,
    CH.FAILED_SAVE_3: None,
    CH.PROFICIENCIES_LANGUAGES: "Proficiencies and Languages",
    CH.ACTIONS: "Actions",
    CH.ATTACKS: "Attacks",
    CH.FEATURES_TRAITS: "Features & Traits",
    CH.CP: "CP",
    CH.SP: "SP",
    CH.EP: "EP",
    CH.GP: "GP",
    CH.PP: "PP",
    CH.WEIGHT_CARRIED: "Weight Carried",
    CH.ENCUMBERED: "Encumbered",
    CH.PUSH_DRAG_LIFT: "Push/drag/lift",
    CH.GENDER: "Gender",
    CH.AGE: "Age",
    CH.SIZE: "Size",
    CH.HEIGHT: "Height",
    CH.WEIGHT: "Weight",
    CH.ALIGNMENT: "Alignment",
    CH.FAITH: "Faith",
    CH.SKIN: "Skin",
    CH.EYES: "Eyes",
    CH.HAIR: "Hair",
    CH.CHARACTER_IMAGE: "Character Image",
    CH.ALLIES_ORGANIZATIONS: "Allies & Organizations",
    CH.PERSONALITY_TRAITS: "Personlity Traits",
    CH.IDEALS: "Ideals",
    CH.BONDS: "Bonds",
    CH.APPEARANCE: "Appearance",
    CH.FLAWS: "Flaws",
    CH.BACKSTORY: "Backstory",
    CH.ADDITIONAL_NOTES: "Additional Notes",
    CH.SPELLCASTINGABILITY0: "Spellcasting Ability",
    CH.SPELLSAVEDC0: "Spell Save DC",
    CH.SPELLATKBONUS0: "Spell Attack Bonus",
    CH.SPELLCASTINGCLASS0: "Spellcasting Class",
}


class CharacterView(QWidget):
    def __init__(self, player_model, parent=None):
        super(CharacterView, self).__init__(parent)
        self.char_layout = Ui_Form()
        self.char_layout.setupUi(self)
        self.player_model = player_model
        self.char_layout.equipment_add.clicked.connect(self.add_equipment)
        self.char_layout.equipment_remove.clicked.connect(self.remove_equipment)
        self.char_layout.spell_add.clicked.connect(self.add_spell)
        self.char_layout.spell_remove.clicked.connect(self.remove_spell)
        self.register_deligates()

    def register_deligates(self):
        spell_model_view = self.char_layout.SPELL_TABLE
        spell_model_delegates = self.player_model.spell_model.delegates
        for delegate in spell_model_delegates:
            this_delegate = spell_model_delegates[delegate]
            spell_model_view.setItemDelegateForColumn(delegate, this_delegate)

        equipment_model_view = self.char_layout.EQUIPMENT_TABLE
        equipment_delegates = self.player_model.equipment_model.delegates
        for delegate in equipment_delegates:
            this_delegate = equipment_delegates[delegate]
            equipment_model_view.setItemDelegateForColumn(delegate, this_delegate)

    def register_signals(self, player_model):
        for value in CH:
            logging.debug(f"Checking if {value} exists in UI")
            if hasattr(self.char_layout, value.name):
                attribute = getattr(self.char_layout, value.name)
                self.register_signal_for_generic_widget(
                    attribute, player_model.character_view_changed_event, value
                )
            else:
                logging.info(f"{value} does not exists in UI")

    def character_model_changed_event(self, subject, character_property, value):
        logging.debug(
            f"Event fired from subject {subject} with arg {character_property}"
        )
        if not hasattr(self.char_layout, character_property):
            logging.debug(
                f"CharacterView does not have a property {character_property}. Ignoring event."
            )
            return
        attribute = getattr(self.char_layout, character_property)
        # TODO it might be more elegant to simply use "character_property" here, but this might cause some weird race-conditions
        self.set_value_for_generic_widget(
            attribute, getattr(subject, character_property)
        )

    def set_value_for_generic_widget(self, attribute, value):
        if isinstance(attribute, QLineEdit):
            attribute.setText(value)
        elif isinstance(attribute, QSpinBox):
            try:
                int_value = int(value)
                attribute.setValue(int_value)
            except ValueError:
                logging.warning(
                    f"Attempting to set SpinBox {attribute} with str character_property {value}, which is not castable to int."
                )
        elif isinstance(attribute, QLabel):
            attribute.setText(value)
        elif isinstance(attribute, QTextEdit):
            attribute.blockSignals(True)
            attribute.setText(value)
            attribute.blockSignals(False)
        elif isinstance(attribute, QCheckBox):
            attribute.setChecked(value)
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
            pass  # logging.debug("QLabels shouldn't change without the Model doing so.")
        else:
            logging.warning(
                f"Attempting to register signal of unknown type {attribute}"
            )

    def add_equipment(self):
        dialogg = QDialog()
        dialog = Ui_EquipmentDialog()
        dialog.setupUi(dialogg)
        result = dialogg.exec_()
        if result == QDialog.Rejected:
            return
        name = dialog.nameLineEdit.text()
        quantity = dialog.amountSpinBox.value()
        weight = dialog.weightLineEdit.text()
        attuned = dialog.attunedCheckBox.isChecked()
        self.player_model.equipment_model.add_item(
            Equipment(name, quantity, weight, attuned)
        )

    def remove_equipment(self):
        if not self.char_layout.EQUIPMENT_TABLE.selectionModel().hasSelection():
            return
        index_selected = self.char_layout.EQUIPMENT_TABLE.currentIndex().row()
        self.player_model.equipment_model.remove_item(index_selected)

    def add_spell(self):
        dialogg = QDialog()
        dialog = Ui_spellDialog()
        dialog.setupUi(dialogg)
        result = dialogg.exec_()
        if result == QDialog.Rejected:
            return

        prepared = dialog.preparedCheckBox.isChecked()
        name = dialog.spellNameLineEdit.text()
        source = dialog.sourceLineEdit.text()
        save_hit = dialog.saveAttackLineEdit.text()
        time = dialog.timeLineEdit.text()
        spell_range = dialog.rangeLineEdit.text()
        components = dialog.componentsLineEdit.text()
        duration = dialog.durationLineEdit.text()
        page = dialog.pageReferenceLineEdit.text()
        notes = dialog.notesLineEdit.text()
        level = dialog.levelSpinBox.value()

        self.player_model.spell_model.add_item(
            Spell(
                prepared,
                name,
                source,
                save_hit,
                time,
                spell_range,
                components,
                duration,
                page,
                notes,
                level,
            )
        )

    def remove_spell(self):
        if not self.char_layout.SPELL_TABLE.selectionModel().hasSelection():
            return
        index_selected = self.char_layout.SPELL_TABLE.currentIndex().row()
        self.player_model.remove_equipment(index_selected)
