# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'character.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1200, 900)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.groupBox_9 = QGroupBox(Form)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_38 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.SAVE_MODIFIERS = QTextEdit(self.groupBox_9)
        self.SAVE_MODIFIERS.setObjectName(u"SAVE_MODIFIERS")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SAVE_MODIFIERS.sizePolicy().hasHeightForWidth())
        self.SAVE_MODIFIERS.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.SAVE_MODIFIERS.setFont(font)

        self.verticalLayout_38.addWidget(self.SAVE_MODIFIERS)


        self.verticalLayout_25.addWidget(self.groupBox_9)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.formLayout = QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName(u"formLayout")
        self.PASSIVE_PERCEPTION = QSpinBox(self.groupBox_3)
        self.PASSIVE_PERCEPTION.setObjectName(u"PASSIVE_PERCEPTION")
        self.PASSIVE_PERCEPTION.setMinimumSize(QSize(40, 20))
        self.PASSIVE_PERCEPTION.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.PASSIVE_PERCEPTION.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.PASSIVE_PERCEPTION)

        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setBold(False)
        font2.setWeight(50)
        self.label_13.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_13)

        self.PASSIVE_INVESTIGATION = QSpinBox(self.groupBox_3)
        self.PASSIVE_INVESTIGATION.setObjectName(u"PASSIVE_INVESTIGATION")
        self.PASSIVE_INVESTIGATION.setMinimumSize(QSize(40, 20))
        self.PASSIVE_INVESTIGATION.setBaseSize(QSize(0, 0))
        self.PASSIVE_INVESTIGATION.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.PASSIVE_INVESTIGATION)

        self.PASSIVE_WISDOM = QSpinBox(self.groupBox_3)
        self.PASSIVE_WISDOM.setObjectName(u"PASSIVE_WISDOM")
        self.PASSIVE_WISDOM.setMinimumSize(QSize(40, 20))
        self.PASSIVE_WISDOM.setBaseSize(QSize(0, 0))
        self.PASSIVE_WISDOM.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.PASSIVE_WISDOM)

        self.SENSES = QTextEdit(self.groupBox_3)
        self.SENSES.setObjectName(u"SENSES")
        sizePolicy.setHeightForWidth(self.SENSES.sizePolicy().hasHeightForWidth())
        self.SENSES.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.SENSES)

        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_14)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_15)


        self.verticalLayout_25.addWidget(self.groupBox_3)


        self.horizontalLayout_9.addLayout(self.verticalLayout_25)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_12 = QGroupBox(Form)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.various_tabs = QTabWidget(self.groupBox_12)
        self.various_tabs.setObjectName(u"various_tabs")
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setWeight(50)
        self.various_tabs.setFont(font3)
        self.various_tabs.setAutoFillBackground(True)
        self.various_tabs.setTabPosition(QTabWidget.North)
        self.various_tabs.setElideMode(Qt.ElideNone)
        self.various_tabs.setUsesScrollButtons(True)
        self.various_tabs.setDocumentMode(True)
        self.various_tabs.setTabsClosable(False)
        self.various_tabs.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setAutoFillBackground(False)
        self.verticalLayout_20 = QVBoxLayout(self.tab)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.CP = QSpinBox(self.tab)
        self.CP.setObjectName(u"CP")
        self.CP.setMaximum(99999)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.CP)

        self.label_24 = QLabel(self.tab)
        self.label_24.setObjectName(u"label_24")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.label_24)

        self.SP = QSpinBox(self.tab)
        self.SP.setObjectName(u"SP")
        self.SP.setMaximum(99999)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.SP)

        self.label_25 = QLabel(self.tab)
        self.label_25.setObjectName(u"label_25")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.label_25)

        self.GP = QSpinBox(self.tab)
        self.GP.setObjectName(u"GP")
        self.GP.setMaximum(99999)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.GP)

        self.label_26 = QLabel(self.tab)
        self.label_26.setObjectName(u"label_26")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.label_26)

        self.PP = QSpinBox(self.tab)
        self.PP.setObjectName(u"PP")
        self.PP.setMaximum(99999)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.PP)

        self.label_27 = QLabel(self.tab)
        self.label_27.setObjectName(u"label_27")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.label_27)

        self.EP = QSpinBox(self.tab)
        self.EP.setObjectName(u"EP")
        self.EP.setMaximum(99999)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.EP)

        self.label_28 = QLabel(self.tab)
        self.label_28.setObjectName(u"label_28")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.label_28)


        self.verticalLayout_41.addLayout(self.formLayout_2)

        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_29 = QLabel(self.tab)
        self.label_29.setObjectName(u"label_29")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy2)

        self.verticalLayout_43.addWidget(self.label_29)

        self.WEIGHT_CARRIED = QLineEdit(self.tab)
        self.WEIGHT_CARRIED.setObjectName(u"WEIGHT_CARRIED")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.WEIGHT_CARRIED.sizePolicy().hasHeightForWidth())
        self.WEIGHT_CARRIED.setSizePolicy(sizePolicy3)

        self.verticalLayout_43.addWidget(self.WEIGHT_CARRIED)

        self.label_30 = QLabel(self.tab)
        self.label_30.setObjectName(u"label_30")
        sizePolicy2.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy2)

        self.verticalLayout_43.addWidget(self.label_30)

        self.ENCUMBERED = QLineEdit(self.tab)
        self.ENCUMBERED.setObjectName(u"ENCUMBERED")
        sizePolicy3.setHeightForWidth(self.ENCUMBERED.sizePolicy().hasHeightForWidth())
        self.ENCUMBERED.setSizePolicy(sizePolicy3)

        self.verticalLayout_43.addWidget(self.ENCUMBERED)

        self.label_31 = QLabel(self.tab)
        self.label_31.setObjectName(u"label_31")
        sizePolicy2.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy2)

        self.verticalLayout_43.addWidget(self.label_31)

        self.PUSH_DRAG_LIFT = QLineEdit(self.tab)
        self.PUSH_DRAG_LIFT.setObjectName(u"PUSH_DRAG_LIFT")
        sizePolicy3.setHeightForWidth(self.PUSH_DRAG_LIFT.sizePolicy().hasHeightForWidth())
        self.PUSH_DRAG_LIFT.setSizePolicy(sizePolicy3)

        self.verticalLayout_43.addWidget(self.PUSH_DRAG_LIFT)


        self.verticalLayout_41.addLayout(self.verticalLayout_43)


        self.horizontalLayout_5.addLayout(self.verticalLayout_41)

        self.EQUIPMENT_LAYOUT = QHBoxLayout()
        self.EQUIPMENT_LAYOUT.setObjectName(u"EQUIPMENT_LAYOUT")

        self.horizontalLayout_5.addLayout(self.EQUIPMENT_LAYOUT)


        self.verticalLayout_20.addLayout(self.horizontalLayout_5)

        self.various_tabs.addTab(self.tab, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_44 = QVBoxLayout(self.tab_6)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_32 = QLabel(self.tab_6)
        self.label_32.setObjectName(u"label_32")
        sizePolicy1.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy1)

        self.verticalLayout_45.addWidget(self.label_32)

        self.SPELLCASTINGCLASS0 = QLineEdit(self.tab_6)
        self.SPELLCASTINGCLASS0.setObjectName(u"SPELLCASTINGCLASS0")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.SPELLCASTINGCLASS0.sizePolicy().hasHeightForWidth())
        self.SPELLCASTINGCLASS0.setSizePolicy(sizePolicy4)

        self.verticalLayout_45.addWidget(self.SPELLCASTINGCLASS0)

        self.label_33 = QLabel(self.tab_6)
        self.label_33.setObjectName(u"label_33")
        sizePolicy2.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy2)

        self.verticalLayout_45.addWidget(self.label_33)

        self.SPELLCASTINGABILITY0 = QLineEdit(self.tab_6)
        self.SPELLCASTINGABILITY0.setObjectName(u"SPELLCASTINGABILITY0")
        sizePolicy4.setHeightForWidth(self.SPELLCASTINGABILITY0.sizePolicy().hasHeightForWidth())
        self.SPELLCASTINGABILITY0.setSizePolicy(sizePolicy4)

        self.verticalLayout_45.addWidget(self.SPELLCASTINGABILITY0)

        self.label_34 = QLabel(self.tab_6)
        self.label_34.setObjectName(u"label_34")
        sizePolicy2.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy2)

        self.verticalLayout_45.addWidget(self.label_34)

        self.SPELLSAVEDC0 = QLineEdit(self.tab_6)
        self.SPELLSAVEDC0.setObjectName(u"SPELLSAVEDC0")
        sizePolicy4.setHeightForWidth(self.SPELLSAVEDC0.sizePolicy().hasHeightForWidth())
        self.SPELLSAVEDC0.setSizePolicy(sizePolicy4)

        self.verticalLayout_45.addWidget(self.SPELLSAVEDC0)

        self.label_35 = QLabel(self.tab_6)
        self.label_35.setObjectName(u"label_35")
        sizePolicy2.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy2)

        self.verticalLayout_45.addWidget(self.label_35)

        self.SPELLATKBONUS0 = QLineEdit(self.tab_6)
        self.SPELLATKBONUS0.setObjectName(u"SPELLATKBONUS0")
        sizePolicy4.setHeightForWidth(self.SPELLATKBONUS0.sizePolicy().hasHeightForWidth())
        self.SPELLATKBONUS0.setSizePolicy(sizePolicy4)

        self.verticalLayout_45.addWidget(self.SPELLATKBONUS0)

        self.SPELLSLOT_LAYOUT = QHBoxLayout()
        self.SPELLSLOT_LAYOUT.setObjectName(u"SPELLSLOT_LAYOUT")

        self.verticalLayout_45.addLayout(self.SPELLSLOT_LAYOUT)


        self.horizontalLayout_7.addLayout(self.verticalLayout_45)

        self.SPELL_LAYOUT = QHBoxLayout()
        self.SPELL_LAYOUT.setObjectName(u"SPELL_LAYOUT")

        self.horizontalLayout_7.addLayout(self.SPELL_LAYOUT)


        self.verticalLayout_44.addLayout(self.horizontalLayout_7)

        self.various_tabs.addTab(self.tab_6, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_6 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.groupBox_20 = QGroupBox(self.tab_2)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.horizontalLayout_18 = QHBoxLayout(self.groupBox_20)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.LANGUAGES_LAYOUT = QHBoxLayout()
        self.LANGUAGES_LAYOUT.setObjectName(u"LANGUAGES_LAYOUT")

        self.horizontalLayout_18.addLayout(self.LANGUAGES_LAYOUT)


        self.gridLayout_10.addWidget(self.groupBox_20, 0, 0, 1, 1)

        self.groupBox_21 = QGroupBox(self.tab_2)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_21)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.ARMOR_LAYOUT = QHBoxLayout()
        self.ARMOR_LAYOUT.setObjectName(u"ARMOR_LAYOUT")

        self.verticalLayout_21.addLayout(self.ARMOR_LAYOUT)


        self.gridLayout_10.addWidget(self.groupBox_21, 1, 0, 1, 1)

        self.groupBox_22 = QGroupBox(self.tab_2)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_22)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.TOOLS_LAYOUT = QHBoxLayout()
        self.TOOLS_LAYOUT.setObjectName(u"TOOLS_LAYOUT")

        self.verticalLayout_2.addLayout(self.TOOLS_LAYOUT)


        self.gridLayout_10.addWidget(self.groupBox_22, 0, 1, 1, 1)

        self.groupBox_13 = QGroupBox(self.tab_2)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.verticalLayout_42 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.WEAPONS_LAYOUT = QHBoxLayout()
        self.WEAPONS_LAYOUT.setObjectName(u"WEAPONS_LAYOUT")

        self.verticalLayout_42.addLayout(self.WEAPONS_LAYOUT)


        self.gridLayout_10.addWidget(self.groupBox_13, 1, 1, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_10, 1, 0, 1, 1)

        self.groupBox_14 = QGroupBox(self.tab_2)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.verticalLayout_40 = QVBoxLayout(self.groupBox_14)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.DEFENSES = QTextEdit(self.groupBox_14)
        self.DEFENSES.setObjectName(u"DEFENSES")

        self.verticalLayout_40.addWidget(self.DEFENSES)


        self.gridLayout_9.addWidget(self.groupBox_14, 1, 3, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_9)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.various_tabs.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_61 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.FEATURES_TRAITS = QTextEdit(self.tab_3)
        self.FEATURES_TRAITS.setObjectName(u"FEATURES_TRAITS")

        self.verticalLayout_31.addWidget(self.FEATURES_TRAITS)


        self.horizontalLayout_61.addLayout(self.verticalLayout_31)

        self.various_tabs.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayout_62 = QHBoxLayout(self.tab_4)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.BACKSTORY = QTextEdit(self.tab_4)
        self.BACKSTORY.setObjectName(u"BACKSTORY")

        self.verticalLayout_32.addWidget(self.BACKSTORY)


        self.horizontalLayout_62.addLayout(self.verticalLayout_32)

        self.various_tabs.addTab(self.tab_4, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.horizontalLayout_63 = QHBoxLayout(self.tab_7)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.ALLIES_ORGANIZATIONS = QTextEdit(self.tab_7)
        self.ALLIES_ORGANIZATIONS.setObjectName(u"ALLIES_ORGANIZATIONS")

        self.verticalLayout_33.addWidget(self.ALLIES_ORGANIZATIONS)


        self.horizontalLayout_63.addLayout(self.verticalLayout_33)

        self.various_tabs.addTab(self.tab_7, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.horizontalLayout_64 = QHBoxLayout(self.tab_5)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.ADDITIONAL_NOTES = QTextEdit(self.tab_5)
        self.ADDITIONAL_NOTES.setObjectName(u"ADDITIONAL_NOTES")

        self.verticalLayout_34.addWidget(self.ADDITIONAL_NOTES)


        self.horizontalLayout_64.addLayout(self.verticalLayout_34)

        self.various_tabs.addTab(self.tab_5, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.horizontalLayout_65 = QHBoxLayout(self.tab_9)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_15 = QGroupBox(self.tab_9)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.verticalLayout = QVBoxLayout(self.groupBox_15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ATTACK_LAYOUT = QHBoxLayout()
        self.ATTACK_LAYOUT.setObjectName(u"ATTACK_LAYOUT")

        self.verticalLayout.addLayout(self.ATTACK_LAYOUT)


        self.horizontalLayout_2.addWidget(self.groupBox_15)

        self.groupBox_16 = QGroupBox(self.tab_9)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_16)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.ACTIONS = QTextEdit(self.groupBox_16)
        self.ACTIONS.setObjectName(u"ACTIONS")

        self.verticalLayout_15.addWidget(self.ACTIONS)


        self.horizontalLayout_2.addWidget(self.groupBox_16)


        self.verticalLayout_35.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_65.addLayout(self.verticalLayout_35)

        self.various_tabs.addTab(self.tab_9, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.horizontalLayout_66 = QHBoxLayout(self.tab_11)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.groupBox_5 = QGroupBox(self.tab_11)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_341 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_341.setObjectName(u"verticalLayout_341")
        self.PERSONALITY_TRAITS = QTextEdit(self.groupBox_5)
        self.PERSONALITY_TRAITS.setObjectName(u"PERSONALITY_TRAITS")

        self.verticalLayout_341.addWidget(self.PERSONALITY_TRAITS)


        self.gridLayout_8.addWidget(self.groupBox_5, 1, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.tab_11)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_351 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_351.setObjectName(u"verticalLayout_351")
        self.IDEALS = QTextEdit(self.groupBox_6)
        self.IDEALS.setObjectName(u"IDEALS")

        self.verticalLayout_351.addWidget(self.IDEALS)


        self.gridLayout_8.addWidget(self.groupBox_6, 1, 1, 1, 1)

        self.groupBox_7 = QGroupBox(self.tab_11)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_361 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_361.setObjectName(u"verticalLayout_361")
        self.BONDS = QTextEdit(self.groupBox_7)
        self.BONDS.setObjectName(u"BONDS")

        self.verticalLayout_361.addWidget(self.BONDS)


        self.gridLayout_8.addWidget(self.groupBox_7, 2, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.tab_11)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_37 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.FLAWS = QTextEdit(self.groupBox_8)
        self.FLAWS.setObjectName(u"FLAWS")

        self.verticalLayout_37.addWidget(self.FLAWS)


        self.gridLayout_8.addWidget(self.groupBox_8, 2, 1, 1, 1)

        self.groupBox_17 = QGroupBox(self.tab_11)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_17)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.ALIGNMENT = QTextEdit(self.groupBox_17)
        self.ALIGNMENT.setObjectName(u"ALIGNMENT")

        self.verticalLayout_18.addWidget(self.ALIGNMENT)


        self.gridLayout_8.addWidget(self.groupBox_17, 0, 0, 1, 1)

        self.groupBox_18 = QGroupBox(self.tab_11)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_18)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.FAITH = QTextEdit(self.groupBox_18)
        self.FAITH.setObjectName(u"FAITH")

        self.verticalLayout_19.addWidget(self.FAITH)


        self.gridLayout_8.addWidget(self.groupBox_18, 0, 1, 1, 1)


        self.verticalLayout_36.addLayout(self.gridLayout_8)


        self.horizontalLayout_66.addLayout(self.verticalLayout_36)

        self.various_tabs.addTab(self.tab_11, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.horizontalLayout_67 = QHBoxLayout(self.tab_12)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_4 = QGroupBox(self.tab_12)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy5)
        self.horizontalLayout_24 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.APPEARANCE = QTextEdit(self.groupBox_4)
        self.APPEARANCE.setObjectName(u"APPEARANCE")

        self.horizontalLayout_24.addWidget(self.APPEARANCE)


        self.gridLayout_4.addWidget(self.groupBox_4, 1, 0, 1, 1)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_17 = QLabel(self.tab_12)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_27.addWidget(self.label_17)

        self.HEIGHT = QLineEdit(self.tab_12)
        self.HEIGHT.setObjectName(u"HEIGHT")

        self.verticalLayout_27.addWidget(self.HEIGHT)


        self.gridLayout_7.addLayout(self.verticalLayout_27, 0, 1, 1, 1)

        self.verticalLayout_311 = QVBoxLayout()
        self.verticalLayout_311.setObjectName(u"verticalLayout_311")
        self.label_21 = QLabel(self.tab_12)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_311.addWidget(self.label_21)

        self.HAIR = QLineEdit(self.tab_12)
        self.HAIR.setObjectName(u"HAIR")

        self.verticalLayout_311.addWidget(self.HAIR)


        self.gridLayout_7.addLayout(self.verticalLayout_311, 1, 2, 1, 1)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_16 = QLabel(self.tab_12)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_26.addWidget(self.label_16)

        self.AGE = QLineEdit(self.tab_12)
        self.AGE.setObjectName(u"AGE")

        self.verticalLayout_26.addWidget(self.AGE)


        self.gridLayout_7.addLayout(self.verticalLayout_26, 0, 0, 1, 1)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_18 = QLabel(self.tab_12)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_28.addWidget(self.label_18)

        self.WEIGHT = QLineEdit(self.tab_12)
        self.WEIGHT.setObjectName(u"WEIGHT")

        self.verticalLayout_28.addWidget(self.WEIGHT)


        self.gridLayout_7.addLayout(self.verticalLayout_28, 0, 2, 1, 1)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_19 = QLabel(self.tab_12)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_29.addWidget(self.label_19)

        self.SKIN = QLineEdit(self.tab_12)
        self.SKIN.setObjectName(u"SKIN")

        self.verticalLayout_29.addWidget(self.SKIN)


        self.gridLayout_7.addLayout(self.verticalLayout_29, 1, 0, 1, 1)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_20 = QLabel(self.tab_12)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_30.addWidget(self.label_20)

        self.EYES = QLineEdit(self.tab_12)
        self.EYES.setObjectName(u"EYES")

        self.verticalLayout_30.addWidget(self.EYES)


        self.gridLayout_7.addLayout(self.verticalLayout_30, 1, 1, 1, 1)

        self.verticalLayout_321 = QVBoxLayout()
        self.verticalLayout_321.setObjectName(u"verticalLayout_321")
        self.label_23 = QLabel(self.tab_12)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_321.addWidget(self.label_23)

        self.SIZE = QLineEdit(self.tab_12)
        self.SIZE.setObjectName(u"SIZE")

        self.verticalLayout_321.addWidget(self.SIZE)


        self.gridLayout_7.addLayout(self.verticalLayout_321, 0, 3, 1, 1)

        self.verticalLayout_331 = QVBoxLayout()
        self.verticalLayout_331.setObjectName(u"verticalLayout_331")
        self.label_22 = QLabel(self.tab_12)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_331.addWidget(self.label_22)

        self.GENDER = QLineEdit(self.tab_12)
        self.GENDER.setObjectName(u"GENDER")

        self.verticalLayout_331.addWidget(self.GENDER)


        self.gridLayout_7.addLayout(self.verticalLayout_331, 1, 3, 1, 1)


        self.verticalLayout_24.addLayout(self.gridLayout_7)


        self.gridLayout_4.addLayout(self.verticalLayout_24, 0, 0, 1, 1)


        self.verticalLayout_39.addLayout(self.gridLayout_4)


        self.horizontalLayout_67.addLayout(self.verticalLayout_39)

        self.various_tabs.addTab(self.tab_12, "")

        self.verticalLayout_16.addWidget(self.various_tabs)


        self.horizontalLayout_4.addWidget(self.groupBox_12)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.horizontalLayout_9, 2, 0, 1, 1)

        self.character_view_layout = QVBoxLayout()
        self.character_view_layout.setObjectName(u"character_view_layout")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setSizeConstraint(QLayout.SetMaximumSize)
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy6)
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.character_info = QGridLayout()
        self.character_info.setSpacing(15)
        self.character_info.setObjectName(u"character_info")
        self.character_info.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.character_info.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_13.addWidget(self.label_5)

        self.CHARACTER_NAME = QLineEdit(self.groupBox_2)
        self.CHARACTER_NAME.setObjectName(u"CHARACTER_NAME")
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(10)
        self.CHARACTER_NAME.setFont(font4)
        self.CHARACTER_NAME.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.verticalLayout_13.addWidget(self.CHARACTER_NAME)


        self.character_info.addLayout(self.verticalLayout_13, 0, 0, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_12.addWidget(self.label_8)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.CLASS_LEVEL = QLineEdit(self.groupBox_2)
        self.CLASS_LEVEL.setObjectName(u"CLASS_LEVEL")
        self.CLASS_LEVEL.setFont(font4)

        self.horizontalLayout.addWidget(self.CLASS_LEVEL)


        self.verticalLayout_12.addLayout(self.horizontalLayout)


        self.character_info.addLayout(self.verticalLayout_12, 1, 0, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_10.addWidget(self.label_7)

        self.PLAYER_NAME = QLineEdit(self.groupBox_2)
        self.PLAYER_NAME.setObjectName(u"PLAYER_NAME")
        self.PLAYER_NAME.setFont(font4)

        self.verticalLayout_10.addWidget(self.PLAYER_NAME)


        self.character_info.addLayout(self.verticalLayout_10, 0, 2, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_9.addWidget(self.label_9)

        self.BACKGROUND = QLineEdit(self.groupBox_2)
        self.BACKGROUND.setObjectName(u"BACKGROUND")
        self.BACKGROUND.setFont(font4)

        self.verticalLayout_9.addWidget(self.BACKGROUND)


        self.character_info.addLayout(self.verticalLayout_9, 1, 1, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_8.addWidget(self.label_10)

        self.XP = QLineEdit(self.groupBox_2)
        self.XP.setObjectName(u"XP")
        self.XP.setFont(font4)

        self.verticalLayout_8.addWidget(self.XP)


        self.character_info.addLayout(self.verticalLayout_8, 1, 2, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_11.addWidget(self.label_6)

        self.RACE = QLineEdit(self.groupBox_2)
        self.RACE.setObjectName(u"RACE")
        self.RACE.setFont(font4)

        self.verticalLayout_11.addWidget(self.RACE)


        self.character_info.addLayout(self.verticalLayout_11, 0, 1, 1, 1)


        self.gridLayout_5.addLayout(self.character_info, 0, 0, 1, 1)


        self.verticalLayout_14.addWidget(self.groupBox_2)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.groupBox_10 = QGroupBox(Form)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.horizontalLayout_36 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.wis_layout = QVBoxLayout()
        self.wis_layout.setObjectName(u"wis_layout")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.wis_title = QLabel(self.groupBox_10)
        self.wis_title.setObjectName(u"wis_title")
        sizePolicy3.setHeightForWidth(self.wis_title.sizePolicy().hasHeightForWidth())
        self.wis_title.setSizePolicy(sizePolicy3)
        self.wis_title.setMinimumSize(QSize(0, 36))
        self.wis_title.setFrameShape(QFrame.NoFrame)
        self.wis_title.setScaledContents(True)
        self.wis_title.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_27.addWidget(self.wis_title)


        self.wis_layout.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.WIS = QSpinBox(self.groupBox_10)
        self.WIS.setObjectName(u"WIS")
        sizePolicy4.setHeightForWidth(self.WIS.sizePolicy().hasHeightForWidth())
        self.WIS.setSizePolicy(sizePolicy4)
        self.WIS.setMinimumSize(QSize(40, 40))
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(12)
        self.WIS.setFont(font5)
        self.WIS.setAlignment(Qt.AlignCenter)
        self.WIS.setProperty("showGroupSeparator", False)

        self.horizontalLayout_3.addWidget(self.WIS)


        self.wis_layout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.WIS_MOD = QSpinBox(self.groupBox_10)
        self.WIS_MOD.setObjectName(u"WIS_MOD")
        sizePolicy4.setHeightForWidth(self.WIS_MOD.sizePolicy().hasHeightForWidth())
        self.WIS_MOD.setSizePolicy(sizePolicy4)
        self.WIS_MOD.setMinimum(-5)
        self.WIS_MOD.setMaximum(5)

        self.horizontalLayout_33.addWidget(self.WIS_MOD)


        self.wis_layout.addLayout(self.horizontalLayout_33)


        self.gridLayout_3.addLayout(self.wis_layout, 0, 3, 1, 1)

        self.cha_layout = QVBoxLayout()
        self.cha_layout.setObjectName(u"cha_layout")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.cha_title = QLabel(self.groupBox_10)
        self.cha_title.setObjectName(u"cha_title")
        sizePolicy3.setHeightForWidth(self.cha_title.sizePolicy().hasHeightForWidth())
        self.cha_title.setSizePolicy(sizePolicy3)
        self.cha_title.setMinimumSize(QSize(0, 36))
        self.cha_title.setFrameShape(QFrame.NoFrame)
        self.cha_title.setScaledContents(True)
        self.cha_title.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_29.addWidget(self.cha_title)


        self.cha_layout.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.CHA = QSpinBox(self.groupBox_10)
        self.CHA.setObjectName(u"CHA")
        sizePolicy4.setHeightForWidth(self.CHA.sizePolicy().hasHeightForWidth())
        self.CHA.setSizePolicy(sizePolicy4)
        self.CHA.setMinimumSize(QSize(40, 40))
        self.CHA.setFont(font5)
        self.CHA.setAlignment(Qt.AlignCenter)
        self.CHA.setProperty("showGroupSeparator", False)

        self.horizontalLayout_31.addWidget(self.CHA)


        self.cha_layout.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.CHA_MOD = QSpinBox(self.groupBox_10)
        self.CHA_MOD.setObjectName(u"CHA_MOD")
        sizePolicy4.setHeightForWidth(self.CHA_MOD.sizePolicy().hasHeightForWidth())
        self.CHA_MOD.setSizePolicy(sizePolicy4)
        self.CHA_MOD.setMinimum(-5)
        self.CHA_MOD.setMaximum(5)

        self.horizontalLayout_35.addWidget(self.CHA_MOD)


        self.cha_layout.addLayout(self.horizontalLayout_35)


        self.gridLayout_3.addLayout(self.cha_layout, 0, 5, 1, 1)

        self.str_layout = QVBoxLayout()
        self.str_layout.setObjectName(u"str_layout")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.str_title = QLabel(self.groupBox_10)
        self.str_title.setObjectName(u"str_title")
        sizePolicy3.setHeightForWidth(self.str_title.sizePolicy().hasHeightForWidth())
        self.str_title.setSizePolicy(sizePolicy3)
        self.str_title.setMinimumSize(QSize(0, 36))
        self.str_title.setFrameShape(QFrame.NoFrame)
        self.str_title.setScaledContents(True)
        self.str_title.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_17.addWidget(self.str_title)


        self.str_layout.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.STR = QSpinBox(self.groupBox_10)
        self.STR.setObjectName(u"STR")
        sizePolicy4.setHeightForWidth(self.STR.sizePolicy().hasHeightForWidth())
        self.STR.setSizePolicy(sizePolicy4)
        self.STR.setMinimumSize(QSize(40, 40))
        self.STR.setFont(font5)
        self.STR.setAlignment(Qt.AlignCenter)
        self.STR.setProperty("showGroupSeparator", False)

        self.horizontalLayout_32.addWidget(self.STR)


        self.str_layout.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.STR_MOD = QSpinBox(self.groupBox_10)
        self.STR_MOD.setObjectName(u"STR_MOD")
        sizePolicy4.setHeightForWidth(self.STR_MOD.sizePolicy().hasHeightForWidth())
        self.STR_MOD.setSizePolicy(sizePolicy4)
        self.STR_MOD.setMinimum(-5)
        self.STR_MOD.setMaximum(5)

        self.horizontalLayout_30.addWidget(self.STR_MOD)


        self.str_layout.addLayout(self.horizontalLayout_30)


        self.gridLayout_3.addLayout(self.str_layout, 0, 0, 1, 1)

        self.int_layout = QVBoxLayout()
        self.int_layout.setObjectName(u"int_layout")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.int_title = QLabel(self.groupBox_10)
        self.int_title.setObjectName(u"int_title")
        sizePolicy3.setHeightForWidth(self.int_title.sizePolicy().hasHeightForWidth())
        self.int_title.setSizePolicy(sizePolicy3)
        self.int_title.setMinimumSize(QSize(0, 36))
        self.int_title.setFrameShape(QFrame.NoFrame)
        self.int_title.setScaledContents(True)
        self.int_title.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_28.addWidget(self.int_title)


        self.int_layout.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.INT = QSpinBox(self.groupBox_10)
        self.INT.setObjectName(u"INT")
        sizePolicy4.setHeightForWidth(self.INT.sizePolicy().hasHeightForWidth())
        self.INT.setSizePolicy(sizePolicy4)
        self.INT.setMinimumSize(QSize(40, 40))
        self.INT.setFont(font5)
        self.INT.setAlignment(Qt.AlignCenter)
        self.INT.setProperty("showGroupSeparator", False)

        self.horizontalLayout_34.addWidget(self.INT)


        self.int_layout.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_341 = QHBoxLayout()
        self.horizontalLayout_341.setObjectName(u"horizontalLayout_341")
        self.INT_MOD = QSpinBox(self.groupBox_10)
        self.INT_MOD.setObjectName(u"INT_MOD")
        sizePolicy4.setHeightForWidth(self.INT_MOD.sizePolicy().hasHeightForWidth())
        self.INT_MOD.setSizePolicy(sizePolicy4)
        self.INT_MOD.setMinimum(-5)
        self.INT_MOD.setMaximum(5)

        self.horizontalLayout_341.addWidget(self.INT_MOD)


        self.int_layout.addLayout(self.horizontalLayout_341)


        self.gridLayout_3.addLayout(self.int_layout, 0, 4, 1, 1)

        self.con_layout = QVBoxLayout()
        self.con_layout.setObjectName(u"con_layout")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.con_title = QLabel(self.groupBox_10)
        self.con_title.setObjectName(u"con_title")
        sizePolicy3.setHeightForWidth(self.con_title.sizePolicy().hasHeightForWidth())
        self.con_title.setSizePolicy(sizePolicy3)
        self.con_title.setMinimumSize(QSize(0, 36))
        self.con_title.setFrameShape(QFrame.NoFrame)
        self.con_title.setScaledContents(True)
        self.con_title.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_26.addWidget(self.con_title)


        self.con_layout.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.CON = QSpinBox(self.groupBox_10)
        self.CON.setObjectName(u"CON")
        sizePolicy4.setHeightForWidth(self.CON.sizePolicy().hasHeightForWidth())
        self.CON.setSizePolicy(sizePolicy4)
        self.CON.setMinimumSize(QSize(40, 40))
        self.CON.setFont(font5)
        self.CON.setAlignment(Qt.AlignCenter)
        self.CON.setProperty("showGroupSeparator", False)

        self.horizontalLayout_38.addWidget(self.CON)


        self.con_layout.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_321 = QHBoxLayout()
        self.horizontalLayout_321.setObjectName(u"horizontalLayout_321")
        self.CON_MOD = QSpinBox(self.groupBox_10)
        self.CON_MOD.setObjectName(u"CON_MOD")
        sizePolicy4.setHeightForWidth(self.CON_MOD.sizePolicy().hasHeightForWidth())
        self.CON_MOD.setSizePolicy(sizePolicy4)
        self.CON_MOD.setMinimum(-5)
        self.CON_MOD.setMaximum(5)

        self.horizontalLayout_321.addWidget(self.CON_MOD)


        self.con_layout.addLayout(self.horizontalLayout_321)


        self.gridLayout_3.addLayout(self.con_layout, 0, 2, 1, 1)

        self.dex_layout = QVBoxLayout()
        self.dex_layout.setObjectName(u"dex_layout")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.dex_title = QLabel(self.groupBox_10)
        self.dex_title.setObjectName(u"dex_title")
        sizePolicy3.setHeightForWidth(self.dex_title.sizePolicy().hasHeightForWidth())
        self.dex_title.setSizePolicy(sizePolicy3)
        self.dex_title.setMinimumSize(QSize(0, 36))
        self.dex_title.setFrameShape(QFrame.NoFrame)
        self.dex_title.setScaledContents(True)
        self.dex_title.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_25.addWidget(self.dex_title)


        self.dex_layout.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.DEX = QSpinBox(self.groupBox_10)
        self.DEX.setObjectName(u"DEX")
        sizePolicy4.setHeightForWidth(self.DEX.sizePolicy().hasHeightForWidth())
        self.DEX.setSizePolicy(sizePolicy4)
        self.DEX.setMinimumSize(QSize(40, 40))
        self.DEX.setFont(font5)
        self.DEX.setAlignment(Qt.AlignCenter)
        self.DEX.setProperty("showGroupSeparator", False)

        self.horizontalLayout_39.addWidget(self.DEX)


        self.dex_layout.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_311 = QHBoxLayout()
        self.horizontalLayout_311.setObjectName(u"horizontalLayout_311")
        self.DEX_MOD = QSpinBox(self.groupBox_10)
        self.DEX_MOD.setObjectName(u"DEX_MOD")
        sizePolicy4.setHeightForWidth(self.DEX_MOD.sizePolicy().hasHeightForWidth())
        self.DEX_MOD.setSizePolicy(sizePolicy4)
        self.DEX_MOD.setMinimum(-5)
        self.DEX_MOD.setMaximum(5)

        self.horizontalLayout_311.addWidget(self.DEX_MOD)


        self.dex_layout.addLayout(self.horizontalLayout_311)


        self.gridLayout_3.addLayout(self.dex_layout, 0, 1, 1, 1)


        self.horizontalLayout_36.addLayout(self.gridLayout_3)


        self.horizontalLayout_37.addWidget(self.groupBox_10)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.DEX_ST_PROF = QCheckBox(self.groupBox)
        self.DEX_ST_PROF.setObjectName(u"DEX_ST_PROF")
        self.DEX_ST_PROF.setFont(font1)

        self.gridLayout_6.addWidget(self.DEX_ST_PROF, 1, 1, 1, 1)

        self.CON_ST_PROF = QCheckBox(self.groupBox)
        self.CON_ST_PROF.setObjectName(u"CON_ST_PROF")
        self.CON_ST_PROF.setFont(font1)

        self.gridLayout_6.addWidget(self.CON_ST_PROF, 2, 1, 1, 1)

        self.WIS_ST_PROF = QCheckBox(self.groupBox)
        self.WIS_ST_PROF.setObjectName(u"WIS_ST_PROF")
        self.WIS_ST_PROF.setFont(font1)

        self.gridLayout_6.addWidget(self.WIS_ST_PROF, 0, 3, 1, 1)

        self.INT_ST_PROF = QCheckBox(self.groupBox)
        self.INT_ST_PROF.setObjectName(u"INT_ST_PROF")
        self.INT_ST_PROF.setFont(font1)

        self.gridLayout_6.addWidget(self.INT_ST_PROF, 1, 3, 1, 1)

        self.STR_ST_PROF = QCheckBox(self.groupBox)
        self.STR_ST_PROF.setObjectName(u"STR_ST_PROF")
        self.STR_ST_PROF.setFont(font1)

        self.gridLayout_6.addWidget(self.STR_ST_PROF, 0, 1, 1, 1)

        self.CHA_ST_PROF = QCheckBox(self.groupBox)
        self.CHA_ST_PROF.setObjectName(u"CHA_ST_PROF")
        self.CHA_ST_PROF.setFont(font1)

        self.gridLayout_6.addWidget(self.CHA_ST_PROF, 2, 3, 1, 1)

        self.DEX_ST_MOD = QSpinBox(self.groupBox)
        self.DEX_ST_MOD.setObjectName(u"DEX_ST_MOD")

        self.gridLayout_6.addWidget(self.DEX_ST_MOD, 1, 0, 1, 1)

        self.CON_ST_MOD = QSpinBox(self.groupBox)
        self.CON_ST_MOD.setObjectName(u"CON_ST_MOD")

        self.gridLayout_6.addWidget(self.CON_ST_MOD, 2, 0, 1, 1)

        self.STR_ST_MOD = QSpinBox(self.groupBox)
        self.STR_ST_MOD.setObjectName(u"STR_ST_MOD")

        self.gridLayout_6.addWidget(self.STR_ST_MOD, 0, 0, 1, 1)

        self.WIS_ST_MOD = QSpinBox(self.groupBox)
        self.WIS_ST_MOD.setObjectName(u"WIS_ST_MOD")

        self.gridLayout_6.addWidget(self.WIS_ST_MOD, 0, 2, 1, 1)

        self.INT_ST_MOD = QSpinBox(self.groupBox)
        self.INT_ST_MOD.setObjectName(u"INT_ST_MOD")

        self.gridLayout_6.addWidget(self.INT_ST_MOD, 1, 2, 1, 1)

        self.CHA_ST_MOD = QSpinBox(self.groupBox)
        self.CHA_ST_MOD.setObjectName(u"CHA_ST_MOD")

        self.gridLayout_6.addWidget(self.CHA_ST_MOD, 2, 2, 1, 1)


        self.horizontalLayout_37.addWidget(self.groupBox)


        self.verticalLayout_14.addLayout(self.horizontalLayout_37)

        self.verticalLayout_14.setStretch(0, 3)

        self.horizontalLayout_8.addLayout(self.verticalLayout_14)

        self.groupBox_19 = QGroupBox(Form)
        self.groupBox_19.setObjectName(u"groupBox_19")
        sizePolicy1.setHeightForWidth(self.groupBox_19.sizePolicy().hasHeightForWidth())
        self.groupBox_19.setSizePolicy(sizePolicy1)
        self.verticalLayout_47 = QVBoxLayout(self.groupBox_19)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.SKILL_LAYOUT = QHBoxLayout()
        self.SKILL_LAYOUT.setObjectName(u"SKILL_LAYOUT")

        self.verticalLayout_47.addLayout(self.SKILL_LAYOUT)


        self.horizontalLayout_8.addWidget(self.groupBox_19)

        self.groupBox_11 = QGroupBox(Form)
        self.groupBox_11.setObjectName(u"groupBox_11")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(1)
        sizePolicy7.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy7)
        self.verticalLayout_391 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_391.setObjectName(u"verticalLayout_391")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_3 = QLabel(self.groupBox_11)
        self.label_3.setObjectName(u"label_3")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy8)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.horizontalLayout_40.addWidget(self.label_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.INITIATIVE = QSpinBox(self.groupBox_11)
        self.INITIATIVE.setObjectName(u"INITIATIVE")
        sizePolicy1.setHeightForWidth(self.INITIATIVE.sizePolicy().hasHeightForWidth())
        self.INITIATIVE.setSizePolicy(sizePolicy1)
        self.INITIATIVE.setMinimumSize(QSize(40, 20))
        self.INITIATIVE.setBaseSize(QSize(0, 0))
        font6 = QFont()
        font6.setPointSize(10)
        self.INITIATIVE.setFont(font6)

        self.horizontalLayout_12.addWidget(self.INITIATIVE)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)


        self.verticalLayout_17.addLayout(self.verticalLayout_6)


        self.gridLayout_2.addLayout(self.verticalLayout_17, 1, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_381 = QHBoxLayout()
        self.horizontalLayout_381.setObjectName(u"horizontalLayout_381")
        self.label = QLabel(self.groupBox_11)
        self.label.setObjectName(u"label")
        sizePolicy8.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy8)
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.horizontalLayout_381.addWidget(self.label)


        self.verticalLayout_4.addLayout(self.horizontalLayout_381)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.PROF_BONUS = QSpinBox(self.groupBox_11)
        self.PROF_BONUS.setObjectName(u"PROF_BONUS")
        sizePolicy1.setHeightForWidth(self.PROF_BONUS.sizePolicy().hasHeightForWidth())
        self.PROF_BONUS.setSizePolicy(sizePolicy1)
        self.PROF_BONUS.setMinimumSize(QSize(40, 20))
        self.PROF_BONUS.setBaseSize(QSize(0, 0))
        self.PROF_BONUS.setFont(font6)

        self.horizontalLayout_10.addWidget(self.PROF_BONUS)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_4 = QLabel(self.groupBox_11)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)

        self.horizontalLayout_41.addWidget(self.label_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.AC = QSpinBox(self.groupBox_11)
        self.AC.setObjectName(u"AC")
        sizePolicy1.setHeightForWidth(self.AC.sizePolicy().hasHeightForWidth())
        self.AC.setSizePolicy(sizePolicy1)
        self.AC.setMinimumSize(QSize(40, 20))
        self.AC.setBaseSize(QSize(0, 0))
        self.AC.setFont(font6)

        self.horizontalLayout_13.addWidget(self.AC)


        self.verticalLayout_7.addLayout(self.horizontalLayout_13)


        self.gridLayout_2.addLayout(self.verticalLayout_7, 1, 1, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_391 = QHBoxLayout()
        self.horizontalLayout_391.setObjectName(u"horizontalLayout_391")
        self.label_2 = QLabel(self.groupBox_11)
        self.label_2.setObjectName(u"label_2")
        sizePolicy8.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy8)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)

        self.horizontalLayout_391.addWidget(self.label_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_391)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.SPEED = QLineEdit(self.groupBox_11)
        self.SPEED.setObjectName(u"SPEED")
        sizePolicy2.setHeightForWidth(self.SPEED.sizePolicy().hasHeightForWidth())
        self.SPEED.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.SPEED)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)


        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 1, 1, 1)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_11 = QLabel(self.groupBox_11)
        self.label_11.setObjectName(u"label_11")
        sizePolicy8.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy8)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_42.addWidget(self.label_11)


        self.verticalLayout_22.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.MAX_HP = QSpinBox(self.groupBox_11)
        self.MAX_HP.setObjectName(u"MAX_HP")
        sizePolicy1.setHeightForWidth(self.MAX_HP.sizePolicy().hasHeightForWidth())
        self.MAX_HP.setSizePolicy(sizePolicy1)
        self.MAX_HP.setMinimumSize(QSize(40, 20))
        self.MAX_HP.setBaseSize(QSize(0, 0))
        self.MAX_HP.setFont(font6)
        self.MAX_HP.setMaximum(9998)

        self.horizontalLayout_14.addWidget(self.MAX_HP)


        self.verticalLayout_22.addLayout(self.horizontalLayout_14)


        self.gridLayout_2.addLayout(self.verticalLayout_22, 2, 0, 1, 1)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_12 = QLabel(self.groupBox_11)
        self.label_12.setObjectName(u"label_12")
        sizePolicy8.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy8)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_43.addWidget(self.label_12)


        self.verticalLayout_23.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.TOTAL_HIT_DICE = QLineEdit(self.groupBox_11)
        self.TOTAL_HIT_DICE.setObjectName(u"TOTAL_HIT_DICE")
        sizePolicy2.setHeightForWidth(self.TOTAL_HIT_DICE.sizePolicy().hasHeightForWidth())
        self.TOTAL_HIT_DICE.setSizePolicy(sizePolicy2)

        self.horizontalLayout_15.addWidget(self.TOTAL_HIT_DICE)


        self.verticalLayout_23.addLayout(self.horizontalLayout_15)


        self.gridLayout_2.addLayout(self.verticalLayout_23, 2, 1, 1, 1)


        self.verticalLayout_391.addLayout(self.gridLayout_2)


        self.horizontalLayout_8.addWidget(self.groupBox_11)


        self.character_view_layout.addLayout(self.horizontalLayout_8)


        self.gridLayout.addLayout(self.character_view_layout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.various_tabs.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Form", u"Saving Throw Modifiers", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Senses", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Passive Perception ", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Passive Investigation", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Passive Insight", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("Form", u"Various", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"CP", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"SP", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"GP", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"PP", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"EP", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"Weight Carried", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"Encumbered", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"Push/Drag/Lift", None))
        self.various_tabs.setTabText(self.various_tabs.indexOf(self.tab), QCoreApplication.translate("Form", u"Equipment", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"Spellcasting Class", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"Spellcasting Ability", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"Spell Save DC", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"Spell Attack Bonus", None))
        self.various_tabs.setTabText(self.various_tabs.indexOf(self.tab_6), QCoreApplication.translate("Form", u"Spells", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("Form", u"Languages", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("Form", u"Armor", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("Form", u"Tools", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("Form", u"Weapons", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("Form", u"Defenses", None))
        self.various_tabs.setTabText(self.various_tabs.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Proficiencies and Languages", None))
        self.various_tabs.setTabText(self.various_tabs.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Features and Traits", None))
        self.various_tabs.setTabText(self.various_tabs.indexOf(self.tab_4), QCoreApplication.translate("Form", u"Backstory", None))
        self.various_tabs.setTabText(self.various_tabs.indexOf(self.tab_7), QCoreApplication.translate("Form", u"Allies and Organizations", None))
        self.various_tabs.setTabText(self.various_tabs.indexOf(self.tab_5), QCoreApplication.translate("Form", u"Notes", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("Form", u"Attacks", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("Form", u"Actions", None))
        self.various_tabs.setTabText(self.various_tabs.indexOf(self.tab_9), QCoreApplication.translate("Form", u"Attacks and Actions", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"Personality Traits", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"Ideals", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Form", u"Bonds", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Form", u"Flaws", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("Form", u"Alignment", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("Form", u"Faith", None))
        self.various_tabs.setTabText(self.various_tabs.indexOf(self.tab_11), QCoreApplication.translate("Form", u"Personality", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"Appearance", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Height", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Hair", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Age", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Weight", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Skin", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Eyes", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Size", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Gender", None))
        self.various_tabs.setTabText(self.various_tabs.indexOf(self.tab_12), QCoreApplication.translate("Form", u"Characteristics", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Character Information", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Character Name", None))
        self.CHARACTER_NAME.setPlaceholderText(QCoreApplication.translate("Form", u"CHARACTER_NAME", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Level and Class", None))
        self.CLASS_LEVEL.setPlaceholderText(QCoreApplication.translate("Form", u"CLASS_LEVEL", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Player Name", None))
        self.PLAYER_NAME.setPlaceholderText(QCoreApplication.translate("Form", u"PLAYER_NAME", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Background", None))
        self.BACKGROUND.setPlaceholderText(QCoreApplication.translate("Form", u"BACKGROUND", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Experience", None))
        self.XP.setPlaceholderText(QCoreApplication.translate("Form", u"XP", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Race", None))
        self.RACE.setPlaceholderText(QCoreApplication.translate("Form", u"RACE", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("Form", u"Abilities", None))
        self.wis_title.setText(QCoreApplication.translate("Form", u"WIS", None))
        self.cha_title.setText(QCoreApplication.translate("Form", u"CHA", None))
        self.str_title.setText(QCoreApplication.translate("Form", u"STR", None))
        self.int_title.setText(QCoreApplication.translate("Form", u"INT", None))
        self.con_title.setText(QCoreApplication.translate("Form", u"CON", None))
        self.dex_title.setText(QCoreApplication.translate("Form", u"DEX", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Saving Throws", None))
        self.DEX_ST_PROF.setText(QCoreApplication.translate("Form", u"Dexterity", None))
        self.CON_ST_PROF.setText(QCoreApplication.translate("Form", u"Constitution", None))
        self.WIS_ST_PROF.setText(QCoreApplication.translate("Form", u"Wisdom", None))
        self.INT_ST_PROF.setText(QCoreApplication.translate("Form", u"Intelligence", None))
        self.STR_ST_PROF.setText(QCoreApplication.translate("Form", u"Strength", None))
        self.CHA_ST_PROF.setText(QCoreApplication.translate("Form", u"Charisma", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("Form", u"Skills", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("Form", u"Stats", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Initiative", None))
        self.label.setText(QCoreApplication.translate("Form", u"Proficiency Bonus", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Armor Class", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Walking Speed", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Max HP", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Hit Dice", None))
    # retranslateUi

