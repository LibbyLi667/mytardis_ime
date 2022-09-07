from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QFileDialog, QTreeWidget,QTreeWidgetItem
from PyQt5.QtCore import Qt
from typing import Any, Callable

from ime.ui.ui_main_window import Ui_MainWindow
from ime.models import IngestionMetadata, Project, Experiment, Dataset
import logging
from ime.widgets.add_files_wizard import AddFilesWizard, AddFilesWizardResult
from ime.qt_models import IngestionMetadataModel

# Import the resources file
import default_rc
from .utils import file_size_to_str

class MyTardisMetadataEditor(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # load the ui file
        # uic.loadUi('MainWindow.ui', self)
        
        self.metadata = IngestionMetadata()

        # define our widgets
        self.ui.actionImport_data_files.triggered.connect(self.openWizardWindow)
        self.ui.actionSave.triggered.connect(self.save_to_yaml)
        self.ui.actionLoad.triggered.connect(self.loadYaml)

        self.ui.datasetTreeWidget.itemClicked.connect(self.onClickedDataset)
        self.ui.experimentTreeWidget.itemClicked.connect(self.onClickedExperiment)
        self.ui.projectTreeWidget.itemClicked.connect(self.onClickedProject)
        self.show()

    def onSelectDataset(self, dataset: Dataset):
        # Update property editor with new object
        self.ui.datasetProperties.set_dataset(dataset)


    def onSelectDatafile(self, dataset: Dataset, file_name: str):
        # First, look up the dataset value
        files = self.metadata.get_files_by_dataset(dataset)
        # Next, look up FileInfo
        fileinfo_lookup = [
            fileinfo
            for fileinfo in files
            if fileinfo.name == file_name
        ]
        if (len(fileinfo_lookup) != 1):
            logging.warning("Datafile name %s could not be found or there are " + 
            "more than one entries.", file_name)
        fileinfo = fileinfo_lookup[0]
        # Set controls with value
        self.ui.datafileProperties.set_fileinfo(fileinfo)


    def onClickedDataset(self):
            item: QTreeWidgetItem = self.ui.datasetTreeWidget.currentItem()
            item_data = item.data(0, Qt.ItemDataRole.UserRole)
            props_widget : QStackedWidget = self.ui.datasetTabProps
            if item.parent() is None:
                # This indicates we are looking at a dataset,
                # change stacked widget to show dataset properties
                props_widget.setCurrentIndex(0)
                self.onSelectDataset(item_data)
            else:
                parent = item.parent()
                dataset = parent.data(0, Qt.ItemDataRole.UserRole)
                props_widget.setCurrentIndex(1)
                self.onSelectDatafile(dataset, item_data)

    def onClickedExperiment(self):
            item = self.ui.experimentTreeWidget.currentItem()
            exp = item.data(0, Qt.ItemDataRole.UserRole)
            props_widget : QStackedWidget = self.ui.experimentTabProps
            props_widget.setCurrentIndex(0)
            self.ui.expProperties.set_experiment(exp)

    def onClickedProject(self):
            item = self.ui.projectTreeWidget.currentItem()
            project: Project = item.data(0, Qt.ItemDataRole.UserRole)
            props_widget : QStackedWidget = self.ui.projectTabProps
            props_widget.setCurrentIndex(0)
            self.ui.projectProperties.set_project(project)

    def dataset_size(self, dataset: Dataset):
        dataset_files = self.metadata.get_files_by_dataset(dataset)
        return sum([file.size for file in dataset_files])

    def experiment_size(self, exp: Experiment):
        exp_datasets = self.metadata.get_datasets_by_experiment(exp)
        return sum([self.dataset_size(dataset) for dataset in exp_datasets])

    def project_size(self, project: Project):
        proj_exps = self.metadata.get_experiments_by_project(project)
        return sum([self.experiment_size(exp) for exp in proj_exps])

    def find_item_in_tree(self, treeWidget: QTreeWidget, predicate: Callable[[Any],bool]):
        count = treeWidget.topLevelItemCount()
        for i in range(0, count):
            item = treeWidget.topLevelItem(i)
            data = item.data(0, QtCore.Qt.ItemDataRole.UserRole)
            if predicate(data):
                return item
        raise Exception("Could not find item in tree.")

    def reFresh(self,result: AddFilesWizardResult):
        """
        Method for adding the newly created classes from the wizard into IngestionMetadata,
        and refreshing the project/experiment/dataset/datafile widgets with the new data.
        """
        # Modify IngestionMetadata to insert or modify models
        if result.is_new_dataset:
            self.metadata.datasets.append(result.dataset)
        if result.is_new_project:
            self.metadata.projects.append(result.project)
        if result.is_new_experiment:
            self.metadata.experiments.append(result.experiment)
        self.metadata.datafiles.append(result.datafile)
        # Calculate sizes by summing all the files' sizes
        dataset_size = file_size_to_str(self.dataset_size(result.dataset))
        exp_size = file_size_to_str(self.experiment_size(result.experiment))
        proj_size = file_size_to_str(self.project_size(result.project))
        # Create tree widget item for the dataset
        ds_item = None
        if result.is_new_dataset:
            ds_item = QTreeWidgetItem([result.dataset.dataset_name, dataset_size,result.experiment.experiment_name])
            ds_item.setData(0, QtCore.Qt.ItemDataRole.UserRole, result.dataset)
            self.ui.datasetTreeWidget.addTopLevelItem(ds_item)
        else:
            # Update dataset size.
            ds_item = self.find_item_in_tree(self.ui.datasetTreeWidget, lambda data: (
                data.dataset_id == result.dataset.dataset_id
            ))
            ds_item.setData(1, QtCore.Qt.ItemDataRole.DisplayRole, dataset_size)        
        # Add datafile under dataset
        for file in result.datafile.files:
            file_name = file.name
            file_size = file_size_to_str(file.size)
            l1_child = QTreeWidgetItem([file_name,file_size,""])
            l1_child.setData(0, QtCore.Qt.ItemDataRole.UserRole, file_name)
            ds_item.addChild(l1_child)
        # Create or tree widget item for the experiment, or find existing and update size.
        if result.is_new_experiment:
            l2 = QTreeWidgetItem([result.experiment.experiment_name,exp_size,result.project.project_name])
            l2.setData(0, QtCore.Qt.ItemDataRole.UserRole, result.experiment)
            self.ui.experimentTreeWidget.addTopLevelItem(l2)
        else:
            exp_item = self.find_item_in_tree(self.ui.experimentTreeWidget, lambda data:(
                data.experiment_id == result.experiment.experiment_id
            ))
            exp_item.setData(1, QtCore.Qt.ItemDataRole.DisplayRole, exp_size)
        # Create tree widget item for the project, or find existing and update size.
        if result.is_new_project:
            l3 = QTreeWidgetItem([result.project.project_name,proj_size])
            l3.setData(0, QtCore.Qt.ItemDataRole.UserRole, result.project)
            self.ui.projectTreeWidget.addTopLevelItem(l3)
        else:
            proj_item = self.find_item_in_tree(self.ui.projectTreeWidget, lambda data:(
                data.project_id == result.project.project_id
            ))
            proj_item.setData(1, QtCore.Qt.ItemDataRole.DisplayRole, proj_size)

    def openWizardWindow(self):  
        model = IngestionMetadataModel(self.metadata)
        self.import_wizard_ui = AddFilesWizard(model)
        self.import_wizard_ui.submitted.connect(self.reFresh)
        self.import_wizard_ui.show()

    # Import metadata from a yaml file
    def loadYaml(self):
        fileName = QFileDialog.getOpenFileName(self, "Open File",'', "Yaml(*.yaml);;AllFiles(*.*)")[0]
        f = open(fileName)
        data_load = f.read()
        data_yaml = IngestionMetadata.from_yaml(data_load)
        self.display_load_data(data_yaml)
  
    # Display loaded metadata
    def display_load_data(self,data_loaded):
        ### load metadata with only one project
        projects =  data_loaded.projects[0]
        experiments  = data_loaded.experiments[0]
        datasets = data_loaded.datasets[0]
        datafiles = data_loaded.datafiles[0]

        self.metadata.projects.append(projects)
        self.metadata.experiments.append(experiments)
        self.metadata.datasets.append(datasets)
        self.metadata.datafiles.append(datafiles)

        self.reFresh(projects, experiments, datasets, datafiles)

    # Save to yaml files
    def save_to_yaml(self):
        filename = QFileDialog.getSaveFileName(self,"Save File",directory = "test.yaml", initialFilter='Yaml File(*.yaml)')[0]
        if filename:
            with open(filename, 'w') as file:
                file.write(self.metadata.to_yaml())
