# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ccam.ui'
#
# Created: Wed Jul 13 21:40:13 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1051, 797)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = ImageView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 0, 581, 541))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(820, 90, 231, 231))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayoutWidget_2 = QtGui.QWidget(self.groupBox)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 50, 201, 171))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_7 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.outputfile_bx = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.outputfile_bx.setObjectName(_fromUtf8("outputfile_bx"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.outputfile_bx)
        self.label_8 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_8)
        self.groupname_bx = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.groupname_bx.setObjectName(_fromUtf8("groupname_bx"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.groupname_bx)
        self.label_14 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_14)
        self.numimages_bx = QtGui.QSpinBox(self.formLayoutWidget_2)
        self.numimages_bx.setMaximum(9999)
        self.numimages_bx.setProperty("value", 1)
        self.numimages_bx.setObjectName(_fromUtf8("numimages_bx"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.numimages_bx)
        self.label_15 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_15)
        self.numimagesets_bx = QtGui.QSpinBox(self.formLayoutWidget_2)
        self.numimagesets_bx.setMaximum(9999)
        self.numimagesets_bx.setProperty("value", 1)
        self.numimagesets_bx.setObjectName(_fromUtf8("numimagesets_bx"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.numimagesets_bx)
        self.appendtogroup = QtGui.QCheckBox(self.formLayoutWidget_2)
        self.appendtogroup.setObjectName(_fromUtf8("appendtogroup"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.appendtogroup)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(820, 330, 221, 101))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.formLayoutWidget_3 = QtGui.QWidget(self.groupBox_2)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(20, 30, 201, 121))
        self.formLayoutWidget_3.setObjectName(_fromUtf8("formLayoutWidget_3"))
        self.formLayout_3 = QtGui.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setMargin(0)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_9 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_9)
        self.beamenergy_bx = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.beamenergy_bx.setObjectName(_fromUtf8("beamenergy_bx"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.beamenergy_bx)
        self.label_10 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_10)
        self.normalisation_bx = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.normalisation_bx.setObjectName(_fromUtf8("normalisation_bx"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.normalisation_bx)
        self.graphicsView_2 = PlotWidget(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 550, 581, 192))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(600, 90, 221, 351))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.formLayoutWidget = QtGui.QWidget(self.groupBox_3)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 50, 191, 293))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.rows_bx = QtGui.QSpinBox(self.formLayoutWidget)
        self.rows_bx.setMaximum(99999)
        self.rows_bx.setProperty("value", 1300)
        self.rows_bx.setObjectName(_fromUtf8("rows_bx"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.rows_bx)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.cols_bx = QtGui.QSpinBox(self.formLayoutWidget)
        self.cols_bx.setMaximum(99999)
        self.cols_bx.setProperty("value", 1056)
        self.cols_bx.setObjectName(_fromUtf8("cols_bx"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cols_bx)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.timeunits_bx = QtGui.QComboBox(self.formLayoutWidget)
        self.timeunits_bx.setObjectName(_fromUtf8("timeunits_bx"))
        self.timeunits_bx.addItem(_fromUtf8(""))
        self.timeunits_bx.addItem(_fromUtf8(""))
        self.timeunits_bx.addItem(_fromUtf8(""))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.timeunits_bx)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.inttime_bx = QtGui.QLineEdit(self.formLayoutWidget)
        self.inttime_bx.setObjectName(_fromUtf8("inttime_bx"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.inttime_bx)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.framemode_bx = QtGui.QComboBox(self.formLayoutWidget)
        self.framemode_bx.setObjectName(_fromUtf8("framemode_bx"))
        self.framemode_bx.addItem(_fromUtf8(""))
        self.framemode_bx.addItem(_fromUtf8(""))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.framemode_bx)
        self.label_6 = QtGui.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_11 = QtGui.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_11)
        self.vss_bx = QtGui.QLineEdit(self.formLayoutWidget)
        self.vss_bx.setObjectName(_fromUtf8("vss_bx"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.vss_bx)
        self.label_12 = QtGui.QLabel(self.formLayoutWidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_12)
        self.label_13 = QtGui.QLabel(self.formLayoutWidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_13)
        self.pfile_bx = QtGui.QLineEdit(self.formLayoutWidget)
        self.pfile_bx.setObjectName(_fromUtf8("pfile_bx"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.pfile_bx)
        self.vfile_bx = QtGui.QLineEdit(self.formLayoutWidget)
        self.vfile_bx.setObjectName(_fromUtf8("vfile_bx"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.vfile_bx)
        self.hv_bx = QtGui.QSpinBox(self.formLayoutWidget)
        self.hv_bx.setMaximum(210)
        self.hv_bx.setObjectName(_fromUtf8("hv_bx"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.hv_bx)
        self.apply_settings = QtGui.QPushButton(self.centralwidget)
        self.apply_settings.setGeometry(QtCore.QRect(760, 440, 111, 31))
        self.apply_settings.setObjectName(_fromUtf8("apply_settings"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(610, 10, 391, 81))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.ccd_loading = QtGui.QProgressBar(self.groupBox_4)
        self.ccd_loading.setGeometry(QtCore.QRect(177, 30, 201, 31))
        self.ccd_loading.setProperty("value", 24)
        self.ccd_loading.setObjectName(_fromUtf8("ccd_loading"))
        self.ccdon = QtGui.QPushButton(self.groupBox_4)
        self.ccdon.setGeometry(QtCore.QRect(30, 30, 98, 27))
        self.ccdon.setObjectName(_fromUtf8("ccdon"))
        self.groupBox_5 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(790, 480, 241, 251))
        self.groupBox_5.setAutoFillBackground(False)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.grab = QtGui.QPushButton(self.groupBox_5)
        self.grab.setGeometry(QtCore.QRect(80, 30, 98, 27))
        self.grab.setObjectName(_fromUtf8("grab"))
        self.pause = QtGui.QPushButton(self.groupBox_5)
        self.pause.setGeometry(QtCore.QRect(80, 210, 98, 27))
        self.pause.setObjectName(_fromUtf8("pause"))
        self.captureprogress = QtGui.QProgressBar(self.groupBox_5)
        self.captureprogress.setGeometry(QtCore.QRect(10, 60, 241, 16))
        self.captureprogress.setProperty("value", 0)
        self.captureprogress.setObjectName(_fromUtf8("captureprogress"))
        self.readtime = QtGui.QLCDNumber(self.groupBox_5)
        self.readtime.setGeometry(QtCore.QRect(40, 130, 171, 61))
        self.readtime.setObjectName(_fromUtf8("readtime"))
        self.label_17 = QtGui.QLabel(self.groupBox_5)
        self.label_17.setGeometry(QtCore.QRect(90, 110, 81, 20))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.hdf5view = QtGui.QTextEdit(self.centralwidget)
        self.hdf5view.setGeometry(QtCore.QRect(620, 500, 141, 231))
        self.hdf5view.setReadOnly(True)
        self.hdf5view.setObjectName(_fromUtf8("hdf5view"))
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(640, 480, 111, 17))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1051, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_Current_Dataset = QtGui.QAction(MainWindow)
        self.actionSave_Current_Dataset.setObjectName(_fromUtf8("actionSave_Current_Dataset"))
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "CavaCam GUI", None))
        self.groupBox.setTitle(_translate("MainWindow", "Output Options", None))
        self.label_7.setText(_translate("MainWindow", "Output", None))
        self.outputfile_bx.setText(_translate("MainWindow", "out.hdf5", None))
        self.label_8.setText(_translate("MainWindow", "Group", None))
        self.groupname_bx.setText(_translate("MainWindow", "GroupName", None))
        self.label_14.setText(_translate("MainWindow", "#Images", None))
        self.label_15.setText(_translate("MainWindow", "#Sets", None))
        self.appendtogroup.setText(_translate("MainWindow", "Append", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Beam Line Params", None))
        self.label_9.setText(_translate("MainWindow", "Energy", None))
        self.beamenergy_bx.setText(_translate("MainWindow", "0", None))
        self.label_10.setText(_translate("MainWindow", "Normalisation", None))
        self.normalisation_bx.setText(_translate("MainWindow", "0", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Camera Settings", None))
        self.label.setText(_translate("MainWindow", "Rows", None))
        self.label_2.setText(_translate("MainWindow", "Columns", None))
        self.label_3.setText(_translate("MainWindow", "Time Units", None))
        self.timeunits_bx.setItemText(0, _translate("MainWindow", "s", None))
        self.timeunits_bx.setItemText(1, _translate("MainWindow", "1/100 s", None))
        self.timeunits_bx.setItemText(2, _translate("MainWindow", "ms", None))
        self.label_4.setText(_translate("MainWindow", "Int Time", None))
        self.inttime_bx.setText(_translate("MainWindow", "1000", None))
        self.label_5.setText(_translate("MainWindow", "Mode", None))
        self.framemode_bx.setItemText(0, _translate("MainWindow", "FF", None))
        self.framemode_bx.setItemText(1, _translate("MainWindow", "FT", None))
        self.label_6.setText(_translate("MainWindow", "HV", None))
        self.label_11.setText(_translate("MainWindow", "VSS", None))
        self.vss_bx.setText(_translate("MainWindow", "96", None))
        self.label_12.setText(_translate("MainWindow", "V File", None))
        self.label_13.setText(_translate("MainWindow", "P File", None))
        self.apply_settings.setText(_translate("MainWindow", "Apply", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "CCD Setup", None))
        self.ccdon.setText(_translate("MainWindow", "Turn CCD ON", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Capture Controls", None))
        self.grab.setText(_translate("MainWindow", "Start", None))
        self.pause.setText(_translate("MainWindow", "Pause", None))
        self.label_17.setText(_translate("MainWindow", "Read Time", None))
        self.label_16.setText(_translate("MainWindow", "Current Groups", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionSave_Current_Dataset.setText(_translate("MainWindow", "Save Current Dataset", None))

from pyqtgraph import ImageView, PlotWidget
