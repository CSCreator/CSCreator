# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'equipment_dialog.ui'
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


class Ui_EquipmentDialog(object):
    def setupUi(self, EquipmentDialog):
        if EquipmentDialog.objectName():
            EquipmentDialog.setObjectName(u"EquipmentDialog")
        EquipmentDialog.setWindowModality(Qt.WindowModal)
        EquipmentDialog.resize(400, 162)
        self.verticalLayout = QVBoxLayout(EquipmentDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.nameLabel = QLabel(EquipmentDialog)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(EquipmentDialog)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameLineEdit)

        self.amountLabel = QLabel(EquipmentDialog)
        self.amountLabel.setObjectName(u"amountLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.amountLabel)

        self.amountSpinBox = QSpinBox(EquipmentDialog)
        self.amountSpinBox.setObjectName(u"amountSpinBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.amountSpinBox)

        self.weightLabel = QLabel(EquipmentDialog)
        self.weightLabel.setObjectName(u"weightLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.weightLabel)

        self.weightLineEdit = QLineEdit(EquipmentDialog)
        self.weightLineEdit.setObjectName(u"weightLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.weightLineEdit)

        self.attunedLabel = QLabel(EquipmentDialog)
        self.attunedLabel.setObjectName(u"attunedLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.attunedLabel)

        self.attunedCheckBox = QCheckBox(EquipmentDialog)
        self.attunedCheckBox.setObjectName(u"attunedCheckBox")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.attunedCheckBox)

        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(EquipmentDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(EquipmentDialog)
        self.buttonBox.accepted.connect(EquipmentDialog.accept)
        self.buttonBox.rejected.connect(EquipmentDialog.reject)

        QMetaObject.connectSlotsByName(EquipmentDialog)

    # setupUi

    def retranslateUi(self, EquipmentDialog):
        EquipmentDialog.setWindowTitle(
            QCoreApplication.translate("EquipmentDialog", u"dialog", None)
        )
        self.nameLabel.setText(
            QCoreApplication.translate("EquipmentDialog", u"Name", None)
        )
        self.amountLabel.setText(
            QCoreApplication.translate("EquipmentDialog", u"Amount", None)
        )
        self.weightLabel.setText(
            QCoreApplication.translate("EquipmentDialog", u"Weight", None)
        )
        self.attunedLabel.setText(
            QCoreApplication.translate("EquipmentDialog", u"Attuned", None)
        )

    # retranslateUi
