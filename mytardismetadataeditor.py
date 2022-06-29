import os, sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QWizard, QTableWidget, QTableWidgetItem, QLineEdit,QWizardPage, QVBoxLayout, QLabel,QFileDialog, QTreeWidget,QTreeWidgetItem
from PyQt5.QtCore import QPersistentModelIndex,QModelIndex
from isort import file
import yaml
# from mainwindow import Ui_MainWindow
from models import IngestionMetadata, Project, Experiment, Dataset, Datafile, FileInfo

class MyTardisMetadataEditor(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        # load the ui file
        uic.loadUi('MainWindow.ui', self)
        self.metadata = IngestionMetadata()

        # define our widgets
        self.actionImport_data_files.triggered.connect(self.openWizardWindow)
        self.actionSave.triggered.connect(self.save_to_yaml)
        self.show()

    @QtCore.pyqtSlot('PyQt_PyObject','PyQt_PyObject','PyQt_PyObject','PyQt_PyObject')
    def reFresh(self,project_info, experiment_info, dataset_info, datafile_info):
        self.project,self.experiment,self.dataset,self.datafile = project_info, experiment_info, dataset_info, datafile_info 
        self.metadata.projects.append(project_info)
        self.metadata.experiments.append(experiment_info)
        self.metadata.datasets.append(dataset_info)
        self.metadata.datafiles.append(datafile_info)

        l1 = QTreeWidgetItem([self.dataset.dataset_name,self.dataset.metadata['Size'],self.experiment.experiment_name])
        l2 = QTreeWidgetItem([self.experiment.experiment_name,self.experiment.metadata['Size'],self.project.project_name])
        l3 = QTreeWidgetItem([self.project.project_name,self.project.metadata['Size']])
        
        for file in self.datafile.files:
            file_name = file.name
            file_size = file.metadata['Size']
            l1_child = QTreeWidgetItem([file_name,file_size,""])
            l1.addChild(l1_child)
        self.datasetTreeWidget.addTopLevelItem(l1)
        self.experimentTreeWidget.addTopLevelItem(l2)
        self.projectTreeWidget.addTopLevelItem(l3)

    def openWizardWindow(self):  
        self.ui = WindowWizard()
        self.ui.submitted.connect(self.reFresh)
        self.ui.show()
    
    # Save to yaml files
    def save_to_yaml(self):
        filename = QFileDialog.getSaveFileName(self,"Save File",directory = "test.yaml", initialFilter='Yaml File(*.yaml)')[0]
        if filename:
            with open(filename, 'w') as file:
                file.write(self.metadata.to_yaml())

class WindowWizard(QWizard):

    submitted = QtCore.pyqtSignal('PyQt_PyObject','PyQt_PyObject','PyQt_PyObject','PyQt_PyObject')

    def __init__(self):
        super(QWizard, self).__init__()
        uic.loadUi('add-files-wizard.ui', self)

        # define out widgets
        self.datafileAddPushButton.clicked.connect(self.addFiles_handler)
        self.datafileDeletePushButton.clicked.connect(self.deleteFiles_handler)
        self.button(QtWidgets.QWizard.FinishButton).clicked.connect(self.on_submit)

    def addFiles_handler(self):
        table = self.datafiletableWidget
        rows = self.open_dialog_box()
        self.addTableRow(table,rows)

    def deleteFiles_handler(self):
        index_list = []
        for model_index in self.datafiletableWidget.selectionModel().selectedRows():
            index = QtCore.QPersistentModelIndex(model_index)
            index_list.append(index)
        for index in index_list:
            self.datafiletableWidget.removeRow(index.row())

    def fpath(self):
        return self._fpath

    # calculate sizes of added datafiles in bytes,KB,MB,GB,TB
    def convert_bytes(self,size):
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return "%3.1f %s" % (size, x)
            size /= 1024.0

    def open_dialog_box(self):
        filename_mode = QFileDialog()
        filename_mode.setFileMode(QFileDialog.ExistingFiles)
        filename = filename_mode.getOpenFileNames(self, "Open files")  
        fpath = filename[0]
        self._fpath = fpath

        newrows = []
        for f in self._fpath:
            if f !="":
                info = QtCore.QFileInfo(f)
                size = info.size()
                fname = info.fileName()
                size_converted = self.convert_bytes(size)
            newrow = [fname,size_converted, f]
            if newrow not in newrows:
                newrows.append(newrow)
            else:
                continue
        return newrows
    
    def addTableRow(self,table,row_data):
        for lines in row_data:
            row = table.rowCount()
            table.setRowCount(row+1)
            col = 0
            for item in lines:
                cell = QTableWidgetItem(str(item))
                table.setItem(row, col, cell)
                col += 1
    
    def on_submit(self):
        project_info = Project()
        experiment_info = Experiment()
        dataset_info = Dataset()
        datafile_info = Datafile()

        project_info.project_name = self.projectNameLineEdit.text()
        project_info.project_id = self.projectIDLineEdit.text()
        project_info.description = self.projectDescriptionLineEdit.text()
        experiment_info.experiment_name = self.experimentNameLineEdit.text()
        experiment_info.experiment_id = self.experimentIDLineEdit.text()
        experiment_info.project_id = self.projectIDLineEdit.text()
        experiment_info.description = self.experimentdescriptionLineEdit.text()
        dataset_info.dataset_name = self.datasetNameLineEdit.text()
        dataset_info.dataset_id = self.instrumentIDLineEdit.text()
        dataset_info.experiment_id = self.experimentIDLineEdit.text()

        table = self.datafiletableWidget
        ### Calculate the size of dataset, experiment, project - need to modify if "Add data into existing Projects/experiment/datasets" enabled
        B, K, M, G = [], [], [], []
        for row in range(table.rowCount()):
            file_name = table.item(row,0).text()
            size = table.item(row,1).text()
            file_info = FileInfo(name = file_name)
            file_info.metadata['Size'] = size
            datafile_info.files.append(file_info)
            
            l = len(size)
            if size[l-2:] == "bytes":
                B.append(float(size[:l-2]))
            elif size[l-2:] == "KB":
                K.append(float(size[:l-2]))
            elif size[l-2:] == "MB":
                M.append(float(size[:l-2]))
            elif size[l-2:] == "GB":
                G.append(float(size[:l-2]))
        for i in K:
            K[K.index(i)] = i * 1000
        for i in M:
            M[M.index(i)] = i * 1000000
        for i in G: # to convert GigaBytes numbers to KiloBytes
            G[G.index(i)] = i * 1000000000
        size_sum_b = sum(B+K+M+G)
        size_sum = self.convert_bytes(size_sum_b)

        dataset_info.metadata['Size'] = size_sum
        experiment_info.metadata['Size'] = size_sum
        project_info.metadata['Size'] = size_sum

        self.submitted.emit(project_info, experiment_info, dataset_info, datafile_info)
        self.close()

if __name__ == "__main__":
    app = QApplication([])
    window = MyTardisMetadataEditor()
    window.show()
    sys.exit(app.exec_())
