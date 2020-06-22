# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spell_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (
    QCoreApplication,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QUrl,
    Qt,
)
from PySide2.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QIcon,
    QLinearGradient,
    QPalette,
    QPainter,
    QPixmap,
    QRadialGradient,
)
from PySide2.QtWidgets import *


class Ui_spellDialog(object):
    def setupUi(self, spellDialog):
        if spellDialog.objectName():
            spellDialog.setObjectName(u"spellDialog")
        spellDialog.resize(400, 372)
        self.verticalLayout = QVBoxLayout(spellDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.preparedLabel = QLabel(spellDialog)
        self.preparedLabel.setObjectName(u"preparedLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.preparedLabel)

        self.preparedCheckBox = QCheckBox(spellDialog)
        self.preparedCheckBox.setObjectName(u"preparedCheckBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.preparedCheckBox)

        self.levelLabel = QLabel(spellDialog)
        self.levelLabel.setObjectName(u"levelLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.levelLabel)

        self.levelSpinBox = QSpinBox(spellDialog)
        self.levelSpinBox.setObjectName(u"levelSpinBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.levelSpinBox)

        self.spellNameLabel = QLabel(spellDialog)
        self.spellNameLabel.setObjectName(u"spellNameLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.spellNameLabel)

        self.spellNameLineEdit = QLineEdit(spellDialog)
        self.spellNameLineEdit.setObjectName(u"spellNameLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spellNameLineEdit)

        self.sourceLabel = QLabel(spellDialog)
        self.sourceLabel.setObjectName(u"sourceLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.sourceLabel)

        self.sourceLineEdit = QLineEdit(spellDialog)
        self.sourceLineEdit.setObjectName(u"sourceLineEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.sourceLineEdit)

        self.saveAttackLabel = QLabel(spellDialog)
        self.saveAttackLabel.setObjectName(u"saveAttackLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.saveAttackLabel)

        self.saveAttackLineEdit = QLineEdit(spellDialog)
        self.saveAttackLineEdit.setObjectName(u"saveAttackLineEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.saveAttackLineEdit)

        self.timeLabel = QLabel(spellDialog)
        self.timeLabel.setObjectName(u"timeLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.timeLabel)

        self.timeLineEdit = QLineEdit(spellDialog)
        self.timeLineEdit.setObjectName(u"timeLineEdit")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.timeLineEdit)

        self.rangeLabel = QLabel(spellDialog)
        self.rangeLabel.setObjectName(u"rangeLabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.rangeLabel)

        self.rangeLineEdit = QLineEdit(spellDialog)
        self.rangeLineEdit.setObjectName(u"rangeLineEdit")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.rangeLineEdit)

        self.componentsLabel = QLabel(spellDialog)
        self.componentsLabel.setObjectName(u"componentsLabel")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.componentsLabel)

        self.componentsLineEdit = QLineEdit(spellDialog)
        self.componentsLineEdit.setObjectName(u"componentsLineEdit")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.componentsLineEdit)

        self.durationLabel = QLabel(spellDialog)
        self.durationLabel.setObjectName(u"durationLabel")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.durationLabel)

        self.durationLineEdit = QLineEdit(spellDialog)
        self.durationLineEdit.setObjectName(u"durationLineEdit")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.durationLineEdit)

        self.pageReferenceLabel = QLabel(spellDialog)
        self.pageReferenceLabel.setObjectName(u"pageReferenceLabel")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.pageReferenceLabel)

        self.pageReferenceLineEdit = QLineEdit(spellDialog)
        self.pageReferenceLineEdit.setObjectName(u"pageReferenceLineEdit")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.pageReferenceLineEdit)

        self.notesLabel = QLabel(spellDialog)
        self.notesLabel.setObjectName(u"notesLabel")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.notesLabel)

        self.notesLineEdit = QLineEdit(spellDialog)
        self.notesLineEdit.setObjectName(u"notesLineEdit")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.notesLineEdit)

        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(spellDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(spellDialog)
        self.buttonBox.accepted.connect(spellDialog.accept)
        self.buttonBox.rejected.connect(spellDialog.reject)

        QMetaObject.connectSlotsByName(spellDialog)

    # setupUi

    def retranslateUi(self, spellDialog):
        spellDialog.setWindowTitle(
            QCoreApplication.translate("spellDialog", u"dialog", None)
        )
        self.preparedLabel.setText(
            QCoreApplication.translate("spellDialog", u"Prepared", None)
        )
        self.levelLabel.setText(
            QCoreApplication.translate("spellDialog", u"Level", None)
        )
        self.spellNameLabel.setText(
            QCoreApplication.translate("spellDialog", u"Spell Name", None)
        )
        self.sourceLabel.setText(
            QCoreApplication.translate("spellDialog", u"Source", None)
        )
        self.saveAttackLabel.setText(
            QCoreApplication.translate("spellDialog", u"Save/Attack", None)
        )
        self.timeLabel.setText(QCoreApplication.translate("spellDialog", u"Time", None))
        self.rangeLabel.setText(
            QCoreApplication.translate("spellDialog", u"Range", None)
        )
        self.componentsLabel.setText(
            QCoreApplication.translate("spellDialog", u"Components", None)
        )
        self.durationLabel.setText(
            QCoreApplication.translate("spellDialog", u"Duration", None)
        )
        self.pageReferenceLabel.setText(
            QCoreApplication.translate("spellDialog", u"Page Reference", None)
        )
        self.notesLabel.setText(
            QCoreApplication.translate("spellDialog", u"Notes", None)
        )

    # retranslateUi
