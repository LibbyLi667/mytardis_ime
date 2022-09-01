# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ime/ui/ui_access_control_tab.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AccessControlTab(object):
    def setupUi(self, AccessControlTab):
        AccessControlTab.setObjectName("AccessControlTab")
        AccessControlTab.resize(725, 1100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(AccessControlTab.sizePolicy().hasHeightForWidth())
        AccessControlTab.setSizePolicy(sizePolicy)
        AccessControlTab.setMinimumSize(QtCore.QSize(400, 1100))
        self.formLayout = QtWidgets.QFormLayout(AccessControlTab)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setContentsMargins(-1, -1, -1, 20)
        self.formLayout.setObjectName("formLayout")
        self.label_29 = QtWidgets.QLabel(AccessControlTab)
        self.label_29.setObjectName("label_29")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.adminGroupsList = AccessControlList(AccessControlTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.adminGroupsList.sizePolicy().hasHeightForWidth())
        self.adminGroupsList.setSizePolicy(sizePolicy)
        self.adminGroupsList.setObjectName("adminGroupsList")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.adminGroupsList)
        self.readGroupsList = AccessControlList(AccessControlTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.readGroupsList.sizePolicy().hasHeightForWidth())
        self.readGroupsList.setSizePolicy(sizePolicy)
        self.readGroupsList.setObjectName("readGroupsList")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.readGroupsList)
        self.label_31 = QtWidgets.QLabel(AccessControlTab)
        self.label_31.setObjectName("label_31")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_31)
        self.downloadGroupsList = AccessControlList(AccessControlTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.downloadGroupsList.sizePolicy().hasHeightForWidth())
        self.downloadGroupsList.setSizePolicy(sizePolicy)
        self.downloadGroupsList.setObjectName("downloadGroupsList")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.downloadGroupsList)
        self.label_32 = QtWidgets.QLabel(AccessControlTab)
        self.label_32.setObjectName("label_32")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_32)
        self.sensitiveGroupsList = AccessControlList(AccessControlTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.sensitiveGroupsList.sizePolicy().hasHeightForWidth())
        self.sensitiveGroupsList.setSizePolicy(sizePolicy)
        self.sensitiveGroupsList.setObjectName("sensitiveGroupsList")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sensitiveGroupsList)
        self.label_33 = QtWidgets.QLabel(AccessControlTab)
        self.label_33.setObjectName("label_33")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_33)
        self.adminUsersList = AccessControlList(AccessControlTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.adminUsersList.sizePolicy().hasHeightForWidth())
        self.adminUsersList.setSizePolicy(sizePolicy)
        self.adminUsersList.setObjectName("adminUsersList")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.adminUsersList)
        self.label_34 = QtWidgets.QLabel(AccessControlTab)
        self.label_34.setObjectName("label_34")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_34)
        self.readUsersList = AccessControlList(AccessControlTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.readUsersList.sizePolicy().hasHeightForWidth())
        self.readUsersList.setSizePolicy(sizePolicy)
        self.readUsersList.setObjectName("readUsersList")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.readUsersList)
        self.label_35 = QtWidgets.QLabel(AccessControlTab)
        self.label_35.setObjectName("label_35")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_35)
        self.downloadUsersList = AccessControlList(AccessControlTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.downloadUsersList.sizePolicy().hasHeightForWidth())
        self.downloadUsersList.setSizePolicy(sizePolicy)
        self.downloadUsersList.setObjectName("downloadUsersList")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.downloadUsersList)
        self.sensitiveUsersLabel = QtWidgets.QLabel(AccessControlTab)
        self.sensitiveUsersLabel.setObjectName("sensitiveUsersLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.sensitiveUsersLabel)
        self.sensitiveUsersList = AccessControlList(AccessControlTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.sensitiveUsersList.sizePolicy().hasHeightForWidth())
        self.sensitiveUsersList.setSizePolicy(sizePolicy)
        self.sensitiveUsersList.setObjectName("sensitiveUsersList")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.sensitiveUsersList)
        self.label_30 = QtWidgets.QLabel(AccessControlTab)
        self.label_30.setObjectName("label_30")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_30)

        self.retranslateUi(AccessControlTab)
        QtCore.QMetaObject.connectSlotsByName(AccessControlTab)

    def retranslateUi(self, AccessControlTab):
        _translate = QtCore.QCoreApplication.translate
        AccessControlTab.setWindowTitle(_translate("AccessControlTab", "Form"))
        self.label_29.setText(_translate("AccessControlTab", "Admin groups"))
        self.label_31.setText(_translate("AccessControlTab", "Download groups"))
        self.label_32.setText(_translate("AccessControlTab", "Sensitive groups"))
        self.label_33.setText(_translate("AccessControlTab", "Admin users"))
        self.label_34.setText(_translate("AccessControlTab", "Read users"))
        self.label_35.setText(_translate("AccessControlTab", "Download users"))
        self.sensitiveUsersLabel.setText(_translate("AccessControlTab", "Sensitive users"))
        self.label_30.setText(_translate("AccessControlTab", "Read groups"))
from ime.widgets.access_control_list import AccessControlList
