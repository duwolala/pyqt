# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(787, 537)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 781, 491))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(10, 250, 751, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(10, 100, 751, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.frame_2 = QtWidgets.QFrame(self.groupBox)
        self.frame_2.setGeometry(QtCore.QRect(23, 120, 711, 131))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 681, 114))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.edt_energy1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.edt_energy1.setObjectName("edt_energy1")
        self.horizontalLayout.addWidget(self.edt_energy1)
        self.edt_energy2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.edt_energy2.setObjectName("edt_energy2")
        self.horizontalLayout.addWidget(self.edt_energy2)
        self.edt_energy3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.edt_energy3.setObjectName("edt_energy3")
        self.horizontalLayout.addWidget(self.edt_energy3)
        self.edt_energy4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.edt_energy4.setObjectName("edt_energy4")
        self.horizontalLayout.addWidget(self.edt_energy4)
        self.edt_energy5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.edt_energy5.setObjectName("edt_energy5")
        self.horizontalLayout.addWidget(self.edt_energy5)
        self.edt_energy6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.edt_energy6.setObjectName("edt_energy6")
        self.horizontalLayout.addWidget(self.edt_energy6)
        self.edt_energy7 = QtWidgets.QLineEdit(self.layoutWidget)
        self.edt_energy7.setObjectName("edt_energy7")
        self.horizontalLayout.addWidget(self.edt_energy7)
        self.edt_energy8 = QtWidgets.QLineEdit(self.layoutWidget)
        self.edt_energy8.setObjectName("edt_energy8")
        self.horizontalLayout.addWidget(self.edt_energy8)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(45, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.lbl_Gap1 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Gap1.sizePolicy().hasHeightForWidth())
        self.lbl_Gap1.setSizePolicy(sizePolicy)
        self.lbl_Gap1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Gap1.setObjectName("lbl_Gap1")
        self.horizontalLayout_8.addWidget(self.lbl_Gap1)
        self.lbl_Gap2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Gap2.sizePolicy().hasHeightForWidth())
        self.lbl_Gap2.setSizePolicy(sizePolicy)
        self.lbl_Gap2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Gap2.setObjectName("lbl_Gap2")
        self.horizontalLayout_8.addWidget(self.lbl_Gap2)
        self.lbl_Gap3 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Gap3.sizePolicy().hasHeightForWidth())
        self.lbl_Gap3.setSizePolicy(sizePolicy)
        self.lbl_Gap3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Gap3.setObjectName("lbl_Gap3")
        self.horizontalLayout_8.addWidget(self.lbl_Gap3)
        self.lbl_Gap4 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Gap4.sizePolicy().hasHeightForWidth())
        self.lbl_Gap4.setSizePolicy(sizePolicy)
        self.lbl_Gap4.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Gap4.setObjectName("lbl_Gap4")
        self.horizontalLayout_8.addWidget(self.lbl_Gap4)
        self.lbl_Gap5 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Gap5.sizePolicy().hasHeightForWidth())
        self.lbl_Gap5.setSizePolicy(sizePolicy)
        self.lbl_Gap5.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Gap5.setObjectName("lbl_Gap5")
        self.horizontalLayout_8.addWidget(self.lbl_Gap5)
        self.lbl_Gap6 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Gap6.sizePolicy().hasHeightForWidth())
        self.lbl_Gap6.setSizePolicy(sizePolicy)
        self.lbl_Gap6.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Gap6.setObjectName("lbl_Gap6")
        self.horizontalLayout_8.addWidget(self.lbl_Gap6)
        self.lbl_Gap7 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Gap7.sizePolicy().hasHeightForWidth())
        self.lbl_Gap7.setSizePolicy(sizePolicy)
        self.lbl_Gap7.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Gap7.setObjectName("lbl_Gap7")
        self.horizontalLayout_8.addWidget(self.lbl_Gap7)
        spacerItem1 = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.edt_step1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.edt_step1.setAlignment(QtCore.Qt.AlignCenter)
        self.edt_step1.setObjectName("edt_step1")
        self.horizontalLayout_7.addWidget(self.edt_step1)
        self.edt_step2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.edt_step2.setAlignment(QtCore.Qt.AlignCenter)
        self.edt_step2.setObjectName("edt_step2")
        self.horizontalLayout_7.addWidget(self.edt_step2)
        self.edt_step3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.edt_step3.setAlignment(QtCore.Qt.AlignCenter)
        self.edt_step3.setObjectName("edt_step3")
        self.horizontalLayout_7.addWidget(self.edt_step3, 0, QtCore.Qt.AlignHCenter)
        self.edt_step4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.edt_step4.setAlignment(QtCore.Qt.AlignCenter)
        self.edt_step4.setObjectName("edt_step4")
        self.horizontalLayout_7.addWidget(self.edt_step4, 0, QtCore.Qt.AlignHCenter)
        self.edt_step5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.edt_step5.setAlignment(QtCore.Qt.AlignCenter)
        self.edt_step5.setObjectName("edt_step5")
        self.horizontalLayout_7.addWidget(self.edt_step5)
        self.edt_step6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.edt_step6.setAlignment(QtCore.Qt.AlignCenter)
        self.edt_step6.setObjectName("edt_step6")
        self.horizontalLayout_7.addWidget(self.edt_step6)
        self.edt_step7 = QtWidgets.QLineEdit(self.layoutWidget)
        self.edt_step7.setAlignment(QtCore.Qt.AlignCenter)
        self.edt_step7.setObjectName("edt_step7")
        self.horizontalLayout_7.addWidget(self.edt_step7)
        spacerItem3 = QtWidgets.QSpacerItem(59, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        spacerItem4 = QtWidgets.QSpacerItem(57, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.edt_time1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.edt_time1.setAlignment(QtCore.Qt.AlignCenter)
        self.edt_time1.setObjectName("edt_time1")
        self.horizontalLayout_9.addWidget(self.edt_time1)
        self.edt_time2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.edt_time2.setAlignment(QtCore.Qt.AlignCenter)
        self.edt_time2.setObjectName("edt_time2")
        self.horizontalLayout_9.addWidget(self.edt_time2)
        self.edt_time3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.edt_time3.setAlignment(QtCore.Qt.AlignCenter)
        self.edt_time3.setObjectName("edt_time3")
        self.horizontalLayout_9.addWidget(self.edt_time3, 0, QtCore.Qt.AlignHCenter)
        self.edt_time4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.edt_time4.setAlignment(QtCore.Qt.AlignCenter)
        self.edt_time4.setObjectName("edt_time4")
        self.horizontalLayout_9.addWidget(self.edt_time4, 0, QtCore.Qt.AlignHCenter)
        self.edt_time5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.edt_time5.setAlignment(QtCore.Qt.AlignCenter)
        self.edt_time5.setObjectName("edt_time5")
        self.horizontalLayout_9.addWidget(self.edt_time5)
        self.edt_time6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.edt_time6.setAlignment(QtCore.Qt.AlignCenter)
        self.edt_time6.setObjectName("edt_time6")
        self.horizontalLayout_9.addWidget(self.edt_time6)
        self.edt_time7 = QtWidgets.QLineEdit(self.layoutWidget)
        self.edt_time7.setAlignment(QtCore.Qt.AlignCenter)
        self.edt_time7.setObjectName("edt_time7")
        self.horizontalLayout_9.addWidget(self.edt_time7)
        spacerItem5 = QtWidgets.QSpacerItem(59, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.frame_3 = QtWidgets.QFrame(self.groupBox)
        self.frame_3.setGeometry(QtCore.QRect(23, 270, 711, 161))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.layoutWidget1 = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 10, 681, 134))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_10.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)
        self.edt_drv_energy = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edt_drv_energy.sizePolicy().hasHeightForWidth())
        self.edt_drv_energy.setSizePolicy(sizePolicy)
        self.edt_drv_energy.setReadOnly(True)
        self.edt_drv_energy.setObjectName("edt_drv_energy")
        self.gridLayout.addWidget(self.edt_drv_energy, 0, 1, 1, 1)
        self.lbl_energy_rb = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_energy_rb.sizePolicy().hasHeightForWidth())
        self.lbl_energy_rb.setSizePolicy(sizePolicy)
        self.lbl_energy_rb.setSizeIncrement(QtCore.QSize(0, 0))
        self.lbl_energy_rb.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_energy_rb.setLineWidth(1)
        self.lbl_energy_rb.setMidLineWidth(0)
        self.lbl_energy_rb.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_energy_rb.setObjectName("lbl_energy_rb")
        self.gridLayout.addWidget(self.lbl_energy_rb, 0, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_14.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 0, 1, 1)
        self.edt_drv_gap = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edt_drv_gap.sizePolicy().hasHeightForWidth())
        self.edt_drv_gap.setSizePolicy(sizePolicy)
        self.edt_drv_gap.setReadOnly(True)
        self.edt_drv_gap.setObjectName("edt_drv_gap")
        self.gridLayout.addWidget(self.edt_drv_gap, 1, 1, 1, 1)
        self.lbl_gap_rb = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_gap_rb.sizePolicy().hasHeightForWidth())
        self.lbl_gap_rb.setSizePolicy(sizePolicy)
        self.lbl_gap_rb.setSizeIncrement(QtCore.QSize(0, 0))
        self.lbl_gap_rb.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_gap_rb.setLineWidth(1)
        self.lbl_gap_rb.setMidLineWidth(0)
        self.lbl_gap_rb.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_gap_rb.setObjectName("lbl_gap_rb")
        self.gridLayout.addWidget(self.lbl_gap_rb, 1, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 1)
        self.edt_ion = QtWidgets.QLineEdit(self.layoutWidget1)
        self.edt_ion.setObjectName("edt_ion")
        self.gridLayout.addWidget(self.edt_ion, 2, 1, 1, 1)
        self.lbl_ion_rb = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_ion_rb.sizePolicy().hasHeightForWidth())
        self.lbl_ion_rb.setSizePolicy(sizePolicy)
        self.lbl_ion_rb.setSizeIncrement(QtCore.QSize(0, 0))
        self.lbl_ion_rb.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_ion_rb.setLineWidth(1)
        self.lbl_ion_rb.setMidLineWidth(0)
        self.lbl_ion_rb.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ion_rb.setObjectName("lbl_ion_rb")
        self.gridLayout.addWidget(self.lbl_ion_rb, 2, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_gap_start = QtWidgets.QLabel(self.layoutWidget1)
        self.lbl_gap_start.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_gap_start.setObjectName("lbl_gap_start")
        self.horizontalLayout_2.addWidget(self.lbl_gap_start)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lbl_gap_cmd = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_gap_cmd.sizePolicy().hasHeightForWidth())
        self.lbl_gap_cmd.setSizePolicy(sizePolicy)
        self.lbl_gap_cmd.setSizeIncrement(QtCore.QSize(0, 0))
        self.lbl_gap_cmd.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_gap_cmd.setLineWidth(1)
        self.lbl_gap_cmd.setMidLineWidth(0)
        self.lbl_gap_cmd.setObjectName("lbl_gap_cmd")
        self.horizontalLayout_2.addWidget(self.lbl_gap_cmd)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(43, 80, 361, 24))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setLineWidth(0)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_3.addWidget(self.label_13)
        spacerItem6 = QtWidgets.QSpacerItem(33, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.edt_edge = QtWidgets.QLineEdit(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edt_edge.sizePolicy().hasHeightForWidth())
        self.edt_edge.setSizePolicy(sizePolicy)
        self.edt_edge.setObjectName("edt_edge")
        self.horizontalLayout_3.addWidget(self.edt_edge)
        self.cmb_edge = QtWidgets.QComboBox(self.layoutWidget2)
        self.cmb_edge.setCurrentText("")
        self.cmb_edge.setObjectName("cmb_edge")
        self.horizontalLayout_3.addWidget(self.cmb_edge)
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget3.setGeometry(QtCore.QRect(560, 50, 168, 25))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_check = QtWidgets.QPushButton(self.layoutWidget3)
        self.btn_check.setEnabled(True)
        self.btn_check.setDefault(False)
        self.btn_check.setObjectName("btn_check")
        self.horizontalLayout_4.addWidget(self.btn_check)
        self.btn_start = QtWidgets.QPushButton(self.layoutWidget3)
        self.btn_start.setEnabled(False)
        self.btn_start.setDefault(False)
        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout_4.addWidget(self.btn_start)
        self.btn_abort = QtWidgets.QPushButton(self.groupBox)
        self.btn_abort.setGeometry(QtCore.QRect(650, 450, 81, 22))
        self.btn_abort.setAcceptDrops(False)
        self.btn_abort.setObjectName("btn_abort")
        self.edt_path = QtWidgets.QLineEdit(self.groupBox)
        self.edt_path.setGeometry(QtCore.QRect(40, 50, 361, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edt_path.sizePolicy().hasHeightForWidth())
        self.edt_path.setSizePolicy(sizePolicy)
        self.edt_path.setText("")
        self.edt_path.setObjectName("edt_path")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(40, 30, 105, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setLineWidth(0)
        self.label_15.setObjectName("label_15")
        self.prgBar = QtWidgets.QProgressBar(self.groupBox)
        self.prgBar.setGeometry(QtCore.QRect(30, 450, 571, 23))
        self.prgBar.setProperty("value", 0)
        self.prgBar.setObjectName("prgBar")
        self.btn_path = QtWidgets.QToolButton(self.groupBox)
        self.btn_path.setGeometry(QtCore.QRect(400, 50, 28, 21))
        self.btn_path.setObjectName("btn_path")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Energy_scan"))
        self.label.setText(_translate("MainWindow", "Energy(ev)"))
        self.edt_energy1.setText(_translate("MainWindow", "-200"))
        self.edt_energy2.setText(_translate("MainWindow", "-20"))
        self.edt_energy3.setText(_translate("MainWindow", "50"))
        self.edt_energy4.setText(_translate("MainWindow", "150"))
        self.edt_energy5.setText(_translate("MainWindow", "300"))
        self.edt_energy6.setText(_translate("MainWindow", "600"))
        self.edt_energy7.setText(_translate("MainWindow", "800"))
        self.edt_energy8.setText(_translate("MainWindow", "1000"))
        self.label_3.setText(_translate("MainWindow", "Gap(cal)"))
        self.lbl_Gap1.setText(_translate("MainWindow", "Gap1"))
        self.lbl_Gap2.setText(_translate("MainWindow", "Gap2"))
        self.lbl_Gap3.setText(_translate("MainWindow", "Gap3"))
        self.lbl_Gap4.setText(_translate("MainWindow", "Gap4"))
        self.lbl_Gap5.setText(_translate("MainWindow", "Gap5"))
        self.lbl_Gap6.setText(_translate("MainWindow", "Gap6"))
        self.lbl_Gap7.setText(_translate("MainWindow", "Gap7"))
        self.label_2.setText(_translate("MainWindow", "Step(ev)"))
        self.edt_step1.setText(_translate("MainWindow", "5"))
        self.edt_step2.setText(_translate("MainWindow", "0.5"))
        self.edt_step3.setText(_translate("MainWindow", "1"))
        self.edt_step4.setText(_translate("MainWindow", "2"))
        self.edt_step5.setText(_translate("MainWindow", "3"))
        self.edt_step6.setText(_translate("MainWindow", "4"))
        self.edt_step7.setText(_translate("MainWindow", "5"))
        self.label_5.setText(_translate("MainWindow", "Integer time"))
        self.edt_time1.setText(_translate("MainWindow", "1"))
        self.edt_time2.setText(_translate("MainWindow", "1"))
        self.edt_time3.setText(_translate("MainWindow", "1"))
        self.edt_time4.setText(_translate("MainWindow", "1"))
        self.edt_time5.setText(_translate("MainWindow", "1"))
        self.edt_time6.setText(_translate("MainWindow", "1"))
        self.edt_time7.setText(_translate("MainWindow", "1"))
        self.label_10.setText(_translate("MainWindow", "DriveEnergy"))
        self.edt_drv_energy.setText(_translate("MainWindow", "X17U1:OP:Mono:soft_bragg.VAL"))
        self.lbl_energy_rb.setText(_translate("MainWindow", "EnergyVal"))
        self.label_14.setText(_translate("MainWindow", "Drive Gap"))
        self.edt_drv_gap.setText(_translate("MainWindow", "SR-ID:H17IVU27:CmdGap"))
        self.lbl_gap_rb.setText(_translate("MainWindow", "Gap Val"))
        self.label_12.setText(_translate("MainWindow", "Read"))
        self.edt_ion.setText(_translate("MainWindow", "X17U1:OP:ION1"))
        self.lbl_ion_rb.setText(_translate("MainWindow", "Ion Val"))
        self.lbl_gap_start.setText(_translate("MainWindow", "SR-ID:H17IVU27:CmdStart_Gap"))
        self.label_4.setText(_translate("MainWindow", ":"))
        self.lbl_gap_cmd.setText(_translate("MainWindow", "GapCmd"))
        self.label_13.setText(_translate("MainWindow", "Energy_edge(ev)"))
        self.edt_edge.setText(_translate("MainWindow", "12662"))
        self.btn_check.setText(_translate("MainWindow", "Check"))
        self.btn_start.setText(_translate("MainWindow", "Start"))
        self.btn_abort.setText(_translate("MainWindow", "Abort"))
        self.label_15.setText(_translate("MainWindow", "Path"))
        self.btn_path.setText(_translate("MainWindow", "..."))
