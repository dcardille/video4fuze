# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ssorgatem/Documents/python/video4fuze/GUI/Preferences.ui'
#
# Created: Wed Apr 28 10:51:48 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        PreferencesDialog.setObjectName("PreferencesDialog")
        PreferencesDialog.resize(493, 529)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PreferencesDialog.setWindowIcon(icon)
        self.verticalLayout_3 = QtGui.QVBoxLayout(PreferencesDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtGui.QLabel(PreferencesDialog)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.frame_2 = QtGui.QFrame(PreferencesDialog)
        self.frame_2.setEnabled(True)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtGui.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.mencoderpass1Edit = QtGui.QPlainTextEdit(self.frame_2)
        self.mencoderpass1Edit.setObjectName("mencoderpass1Edit")
        self.verticalLayout.addWidget(self.mencoderpass1Edit)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Pass2Check = QtGui.QCheckBox(PreferencesDialog)
        self.Pass2Check.setChecked(False)
        self.Pass2Check.setObjectName("Pass2Check")
        self.horizontalLayout.addWidget(self.Pass2Check)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.frame = QtGui.QFrame(PreferencesDialog)
        self.frame.setEnabled(True)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.mencoderpass2Edit = QtGui.QPlainTextEdit(self.frame)
        self.mencoderpass2Edit.setObjectName("mencoderpass2Edit")
        self.verticalLayout_2.addWidget(self.mencoderpass2Edit)
        self.verticalLayout_3.addWidget(self.frame)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtGui.QLabel(PreferencesDialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.Wiline = QtGui.QLineEdit(PreferencesDialog)
        self.Wiline.setObjectName("Wiline")
        self.horizontalLayout_4.addWidget(self.Wiline)
        self.label_5 = QtGui.QLabel(PreferencesDialog)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.Heline = QtGui.QLineEdit(PreferencesDialog)
        self.Heline.setObjectName("Heline")
        self.horizontalLayout_4.addWidget(self.Heline)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem4 = QtGui.QSpacerItem(131, 31, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem4)
        self.DefaultsButton = QtGui.QPushButton(PreferencesDialog)
        self.DefaultsButton.setObjectName("DefaultsButton")
        self.hboxlayout.addWidget(self.DefaultsButton)
        self.okButton = QtGui.QPushButton(PreferencesDialog)
        self.okButton.setObjectName("okButton")
        self.hboxlayout.addWidget(self.okButton)
        self.cancelButton = QtGui.QPushButton(PreferencesDialog)
        self.cancelButton.setDefault(True)
        self.cancelButton.setFlat(False)
        self.cancelButton.setObjectName("cancelButton")
        self.hboxlayout.addWidget(self.cancelButton)
        self.verticalLayout_3.addLayout(self.hboxlayout)

        self.retranslateUi(PreferencesDialog)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL("clicked()"), PreferencesDialog.accept)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), PreferencesDialog.reject)
        QtCore.QObject.connect(self.Pass2Check, QtCore.SIGNAL("toggled(bool)"), self.frame.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(PreferencesDialog)

    def retranslateUi(self, PreferencesDialog):
        PreferencesDialog.setWindowTitle(QtGui.QApplication.translate("PreferencesDialog", "video4fuze preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("PreferencesDialog", "Caution: Modify these settings only if you really know what you do. You have been warned", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PreferencesDialog", "Mencoder pass 1 command line:", None, QtGui.QApplication.UnicodeUTF8))
        self.Pass2Check.setText(QtGui.QApplication.translate("PreferencesDialog", "Two passes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PreferencesDialog", "Mencoder pass 2 command line:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("PreferencesDialog", "Converted image size:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("PreferencesDialog", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.DefaultsButton.setText(QtGui.QApplication.translate("PreferencesDialog", "Defaults", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("PreferencesDialog", "&OK", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("PreferencesDialog", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))

import video4fuze_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PreferencesDialog = QtGui.QDialog()
    ui = Ui_PreferencesDialog()
    ui.setupUi(PreferencesDialog)
    PreferencesDialog.show()
    sys.exit(app.exec_())

