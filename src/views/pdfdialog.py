from PySide2.QtCore import Qt, QMetaObject, QCoreApplication
from PySide2.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QLabel,
    QComboBox,
    QDialogButtonBox,
)


class PdfDialog(QDialog):
    def __init__(self, parent, importers_stringlist):
        super(PdfDialog, self).__init__(parent)
        self.resize(320, 240)

        self.importer_selected = 0

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.selected_file_label = QLabel(self)
        self.selected_file_label.setObjectName("selected_file_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.selected_file_label)

        self.importer_label = QLabel(self)
        self.importer_label.setObjectName("importer_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.importer_label)

        self.importer_combo_box = QComboBox(self)
        self.importer_combo_box.setObjectName("importer_combo_box")
        self.importer_combo_box.addItems(importers_stringlist)

        def set_importer_selected(x):
            self.importer_selected = x

        self.importer_combo_box.currentIndexChanged.connect(set_importer_selected)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.importer_combo_box)

        self.selected_label = QLabel(self)
        self.selected_label.setObjectName("selected_label")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.selected_label)

        self.importer_status = QLabel(self)
        self.importer_status.setObjectName("importer_status")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.importer_status)

        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(
            QCoreApplication.translate("dialog", "Import Character Sheet", None)
        )
        self.selected_file_label.setText(
            QCoreApplication.translate("dialog", "Selected File", None)
        )
        self.importer_label.setText(
            QCoreApplication.translate("dialog", "Importer", None)
        )
        self.selected_label.setText(
            QCoreApplication.translate("dialog", "TextLabel", None)
        )
        self.importer_status.setText(
            QCoreApplication.translate("dialog", "TextLabel", None)
        )
