# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ime/ui/ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1183, 505)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.editorTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.editorTabs.setObjectName("editorTabs")
        self.dataset_tab = QtWidgets.QWidget()
        self.dataset_tab.setObjectName("dataset_tab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.dataset_tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.datasetTreeWidget = QtWidgets.QTreeWidget(self.dataset_tab)
        self.datasetTreeWidget.setObjectName("datasetTreeWidget")
        self.horizontalLayout_2.addWidget(self.datasetTreeWidget)
        self.datasetTabProps = QtWidgets.QStackedWidget(self.dataset_tab)
        self.datasetTabProps.setObjectName("datasetTabProps")
        self.datasetProperties = DatasetPropertyEditor()
        self.datasetProperties.setObjectName("datasetProperties")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.datasetProperties)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.datasetTabProps.addWidget(self.datasetProperties)
        self.datafileProperties = DatafilePropertyEditor()
        self.datafileProperties.setObjectName("datafileProperties")
        self.gridLayout = QtWidgets.QGridLayout(self.datafileProperties)
        self.gridLayout.setObjectName("gridLayout")
        self.datasetTabProps.addWidget(self.datafileProperties)
        self.noDatasetSelectedProps = QtWidgets.QWidget()
        self.noDatasetSelectedProps.setObjectName("noDatasetSelectedProps")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.noDatasetSelectedProps)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.label_43 = QtWidgets.QLabel(self.noDatasetSelectedProps)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy)
        self.label_43.setMinimumSize(QtCore.QSize(0, 0))
        self.label_43.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_43.setFont(font)
        self.label_43.setText("")
        self.label_43.setPixmap(QtGui.QPixmap(":/resources/noun-empty-2900960.svg"))
        self.label_43.setScaledContents(True)
        self.label_43.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_43.setObjectName("label_43")
        self.verticalLayout_3.addWidget(self.label_43, 0, QtCore.Qt.AlignHCenter)
        self.label_44 = QtWidgets.QLabel(self.noDatasetSelectedProps)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Display")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.verticalLayout_3.addWidget(self.label_44)
        self.label_45 = QtWidgets.QLabel(self.noDatasetSelectedProps)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.label_45.setFont(font)
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setWordWrap(True)
        self.label_45.setObjectName("label_45")
        self.verticalLayout_3.addWidget(self.label_45)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.gridLayout_8.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.datasetTabProps.addWidget(self.noDatasetSelectedProps)
        self.horizontalLayout_2.addWidget(self.datasetTabProps)
        self.editorTabs.addTab(self.dataset_tab, "")
        self.experiment_tab = QtWidgets.QWidget()
        self.experiment_tab.setObjectName("experiment_tab")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.experiment_tab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.experimentTreeWidget = QtWidgets.QTreeWidget(self.experiment_tab)
        self.experimentTreeWidget.setObjectName("experimentTreeWidget")
        self.horizontalLayout_4.addWidget(self.experimentTreeWidget)
        self.experimentTabProps = QtWidgets.QStackedWidget(self.experiment_tab)
        self.experimentTabProps.setObjectName("experimentTabProps")
        self.expProperties = ExperimentPropertyEditor()
        self.expProperties.setObjectName("expProperties")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.expProperties)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.experimentTabProps.addWidget(self.expProperties)
        self.page_13 = QtWidgets.QWidget()
        self.page_13.setObjectName("page_13")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.page_13)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.label_46 = QtWidgets.QLabel(self.page_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy)
        self.label_46.setMinimumSize(QtCore.QSize(0, 0))
        self.label_46.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_46.setFont(font)
        self.label_46.setText("")
        self.label_46.setPixmap(QtGui.QPixmap(":/resources/noun-empty-2900960.svg"))
        self.label_46.setScaledContents(True)
        self.label_46.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_46.setObjectName("label_46")
        self.verticalLayout_6.addWidget(self.label_46, 0, QtCore.Qt.AlignHCenter)
        self.label_47 = QtWidgets.QLabel(self.page_13)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Display")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.verticalLayout_6.addWidget(self.label_47)
        self.label_48 = QtWidgets.QLabel(self.page_13)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.label_48.setFont(font)
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setWordWrap(True)
        self.label_48.setObjectName("label_48")
        self.verticalLayout_6.addWidget(self.label_48)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.gridLayout_10.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.experimentTabProps.addWidget(self.page_13)
        self.horizontalLayout_4.addWidget(self.experimentTabProps)
        self.editorTabs.addTab(self.experiment_tab, "")
        self.project_tab = QtWidgets.QWidget()
        self.project_tab.setObjectName("project_tab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.project_tab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.projectTreeWidget = QtWidgets.QTreeWidget(self.project_tab)
        self.projectTreeWidget.setObjectName("projectTreeWidget")
        self.horizontalLayout_3.addWidget(self.projectTreeWidget)
        self.projectTabProps = QtWidgets.QStackedWidget(self.project_tab)
        self.projectTabProps.setObjectName("projectTabProps")
        self.projectProperties = ProjectPropertyEditor()
        self.projectProperties.setObjectName("projectProperties")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.projectProperties)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.projectTabProps.addWidget(self.projectProperties)
        self.page_15 = QtWidgets.QWidget()
        self.page_15.setObjectName("page_15")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.page_15)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem4)
        self.label_52 = QtWidgets.QLabel(self.page_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy)
        self.label_52.setMinimumSize(QtCore.QSize(0, 0))
        self.label_52.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_52.setFont(font)
        self.label_52.setText("")
        self.label_52.setPixmap(QtGui.QPixmap(":/resources/noun-empty-2900960.svg"))
        self.label_52.setScaledContents(True)
        self.label_52.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_52.setObjectName("label_52")
        self.verticalLayout_8.addWidget(self.label_52, 0, QtCore.Qt.AlignHCenter)
        self.label_53 = QtWidgets.QLabel(self.page_15)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Display")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_53.setFont(font)
        self.label_53.setAlignment(QtCore.Qt.AlignCenter)
        self.label_53.setObjectName("label_53")
        self.verticalLayout_8.addWidget(self.label_53)
        self.label_54 = QtWidgets.QLabel(self.page_15)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.label_54.setFont(font)
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setWordWrap(True)
        self.label_54.setObjectName("label_54")
        self.verticalLayout_8.addWidget(self.label_54)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem5)
        self.gridLayout_12.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        self.projectTabProps.addWidget(self.page_15)
        self.horizontalLayout_3.addWidget(self.projectTabProps)
        self.editorTabs.addTab(self.project_tab, "")
        self.verticalLayout_2.addWidget(self.editorTabs)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNewFile = QtWidgets.QAction(MainWindow)
        self.actionNewFile.setObjectName("actionNewFile")
        self.actionFrom_a_template = QtWidgets.QAction(MainWindow)
        self.actionFrom_a_template.setObjectName("actionFrom_a_template")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as_template = QtWidgets.QAction(MainWindow)
        self.actionSave_as_template.setObjectName("actionSave_as_template")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionImport_data_files = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/noun-file-add-4877075.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImport_data_files.setIcon(icon)
        self.actionImport_data_files.setObjectName("actionImport_data_files")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.toolBar.addAction(self.actionNewFile)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionImport_data_files)

        self.retranslateUi(MainWindow)
        self.editorTabs.setCurrentIndex(0)
        self.datasetTabProps.setCurrentIndex(2)
        self.experimentTabProps.setCurrentIndex(1)
        self.projectTabProps.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MyTardis Ingestion Editor"))
        self.datasetTreeWidget.headerItem().setText(0, _translate("MainWindow", "Name"))
        self.datasetTreeWidget.headerItem().setText(1, _translate("MainWindow", "Size"))
        self.datasetTreeWidget.headerItem().setText(2, _translate("MainWindow", "Linked experiment"))
        self.label_44.setText(_translate("MainWindow", "No dataset or file selected."))
        self.label_45.setText(_translate("MainWindow", "Select a dataset or file to edit metadata and access controls."))
        self.editorTabs.setTabText(self.editorTabs.indexOf(self.dataset_tab), _translate("MainWindow", "Datasets"))
        self.experimentTreeWidget.headerItem().setText(0, _translate("MainWindow", "Name"))
        self.experimentTreeWidget.headerItem().setText(1, _translate("MainWindow", "Size"))
        self.experimentTreeWidget.headerItem().setText(2, _translate("MainWindow", "Linked project"))
        self.label_47.setText(_translate("MainWindow", "No experiment selected."))
        self.label_48.setText(_translate("MainWindow", "Select an experiment to edit metadata and access control properties."))
        self.editorTabs.setTabText(self.editorTabs.indexOf(self.experiment_tab), _translate("MainWindow", "Experiments"))
        self.projectTreeWidget.headerItem().setText(0, _translate("MainWindow", "Name"))
        self.projectTreeWidget.headerItem().setText(1, _translate("MainWindow", "Size"))
        self.label_53.setText(_translate("MainWindow", "No project selected."))
        self.label_54.setText(_translate("MainWindow", "Select a project to edit metadata and access control properties."))
        self.editorTabs.setTabText(self.editorTabs.indexOf(self.project_tab), _translate("MainWindow", "Projects"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNewFile.setText(_translate("MainWindow", "New..."))
        self.actionNewFile.setToolTip(_translate("MainWindow", "Create a new metadata file"))
        self.actionFrom_a_template.setText(_translate("MainWindow", "From a template..."))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_as_template.setText(_translate("MainWindow", "Save as template"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionImport_data_files.setText(_translate("MainWindow", "Import data files"))
        self.actionImport_data_files.setToolTip(_translate("MainWindow", "Launch guide to import new data files"))
        self.actionImport_data_files.setShortcut(_translate("MainWindow", "Ctrl+Shift+I"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setToolTip(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
from ime.widgets.prop_editor import DatafilePropertyEditor, DatasetPropertyEditor, ExperimentPropertyEditor, ProjectPropertyEditor
import default_rc
