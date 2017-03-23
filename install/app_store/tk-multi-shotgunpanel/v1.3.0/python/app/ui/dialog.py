# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(479, 800)
        self.verticalLayout_17 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.top_group = QtGui.QFrame(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_group.sizePolicy().hasHeightForWidth())
        self.top_group.setSizePolicy(sizePolicy)
        self.top_group.setFrameShape(QtGui.QFrame.StyledPanel)
        self.top_group.setFrameShadow(QtGui.QFrame.Raised)
        self.top_group.setObjectName("top_group")
        self.verticalLayout_18 = QtGui.QVBoxLayout(self.top_group)
        self.verticalLayout_18.setSpacing(4)
        self.verticalLayout_18.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.header_stack = QtGui.QStackedWidget(self.top_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_stack.sizePolicy().hasHeightForWidth())
        self.header_stack.setSizePolicy(sizePolicy)
        self.header_stack.setObjectName("header_stack")
        self.navigation_page = QtGui.QWidget()
        self.navigation_page.setObjectName("navigation_page")
        self.horizontalLayout = QtGui.QHBoxLayout(self.navigation_page)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.navigation_home = QtGui.QToolButton(self.navigation_page)
        self.navigation_home.setMinimumSize(QtCore.QSize(30, 30))
        self.navigation_home.setMaximumSize(QtCore.QSize(30, 30))
        self.navigation_home.setObjectName("navigation_home")
        self.horizontalLayout.addWidget(self.navigation_home)
        self.navigation_prev = QtGui.QToolButton(self.navigation_page)
        self.navigation_prev.setMinimumSize(QtCore.QSize(30, 30))
        self.navigation_prev.setMaximumSize(QtCore.QSize(30, 30))
        self.navigation_prev.setObjectName("navigation_prev")
        self.horizontalLayout.addWidget(self.navigation_prev)
        self.navigation_next = QtGui.QToolButton(self.navigation_page)
        self.navigation_next.setMinimumSize(QtCore.QSize(30, 30))
        self.navigation_next.setMaximumSize(QtCore.QSize(30, 30))
        self.navigation_next.setObjectName("navigation_next")
        self.horizontalLayout.addWidget(self.navigation_next)
        self.details_text_header = QtGui.QLabel(self.navigation_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.details_text_header.sizePolicy().hasHeightForWidth())
        self.details_text_header.setSizePolicy(sizePolicy)
        self.details_text_header.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.details_text_header.setWordWrap(False)
        self.details_text_header.setObjectName("details_text_header")
        self.horizontalLayout.addWidget(self.details_text_header)
        self.search = QtGui.QToolButton(self.navigation_page)
        self.search.setMinimumSize(QtCore.QSize(30, 30))
        self.search.setMaximumSize(QtCore.QSize(30, 30))
        self.search.setObjectName("search")
        self.horizontalLayout.addWidget(self.search)
        self.current_user = QtGui.QPushButton(self.navigation_page)
        self.current_user.setMinimumSize(QtCore.QSize(30, 30))
        self.current_user.setMaximumSize(QtCore.QSize(30, 30))
        self.current_user.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tk_multi_infopanel/default_user_thumb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.current_user.setIcon(icon)
        self.current_user.setIconSize(QtCore.QSize(30, 30))
        self.current_user.setAutoDefault(False)
        self.current_user.setFlat(False)
        self.current_user.setObjectName("current_user")
        self.horizontalLayout.addWidget(self.current_user)
        self.header_stack.addWidget(self.navigation_page)
        self.search_page = QtGui.QWidget()
        self.search_page.setObjectName("search_page")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.search_page)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtGui.QLabel(self.search_page)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/tk_multi_infopanel/search.png"))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.search_input = GlobalSearchWidget(self.search_page)
        self.search_input.setObjectName("search_input")
        self.horizontalLayout_3.addWidget(self.search_input)
        self.cancel_search = QtGui.QPushButton(self.search_page)
        self.cancel_search.setObjectName("cancel_search")
        self.horizontalLayout_3.addWidget(self.cancel_search)
        self.header_stack.addWidget(self.search_page)
        self.verticalLayout_18.addWidget(self.header_stack)
        self.line = QtGui.QFrame(self.top_group)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_18.addWidget(self.line)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setContentsMargins(-1, 4, -1, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.details_thumb = ShotgunPlaybackLabel(self.top_group)
        self.details_thumb.setMinimumSize(QtCore.QSize(96, 75))
        self.details_thumb.setMaximumSize(QtCore.QSize(96, 75))
        self.details_thumb.setText("")
        self.details_thumb.setPixmap(QtGui.QPixmap(":/tk_multi_infopanel/rect_512x400.png"))
        self.details_thumb.setScaledContents(True)
        self.details_thumb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.details_thumb.setObjectName("details_thumb")
        self.verticalLayout_7.addWidget(self.details_thumb)
        spacerItem = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        self.verticalLayout_7.addItem(spacerItem)
        self.verticalLayout_7.setStretch(1, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.details_text_middle = QtGui.QLabel(self.top_group)
        self.details_text_middle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.details_text_middle.setWordWrap(True)
        self.details_text_middle.setObjectName("details_text_middle")
        self.horizontalLayout_4.addWidget(self.details_text_middle)
        self.verticalLayout_22 = QtGui.QVBoxLayout()
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setContentsMargins(-1, -1, 6, -1)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.action_button = QtGui.QPushButton(self.top_group)
        self.action_button.setMaximumSize(QtCore.QSize(16, 16))
        self.action_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.action_button.setObjectName("action_button")
        self.verticalLayout_22.addWidget(self.action_button)
        self.label_2 = QtGui.QLabel(self.top_group)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_22.addWidget(self.label_2)
        self.verticalLayout_22.setStretch(1, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_22)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout_18.addLayout(self.horizontalLayout_4)
        self.verticalLayout_17.addWidget(self.top_group)
        self.page_stack = QtGui.QStackedWidget(Dialog)
        self.page_stack.setObjectName("page_stack")
        self.entity_page = QtGui.QWidget()
        self.entity_page.setObjectName("entity_page")
        self.verticalLayout = QtGui.QVBoxLayout(self.entity_page)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.entity_tab_widget = QtGui.QTabWidget(self.entity_page)
        self.entity_tab_widget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.entity_tab_widget.setObjectName("entity_tab_widget")
        self.entity_activity_tab = QtGui.QWidget()
        self.entity_activity_tab.setObjectName("entity_activity_tab")
        self.verticalLayout_16 = QtGui.QVBoxLayout(self.entity_activity_tab)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.entity_activity_stream = ActivityStreamWidget(self.entity_activity_tab)
        self.entity_activity_stream.setObjectName("entity_activity_stream")
        self.verticalLayout_16.addWidget(self.entity_activity_stream)
        self.entity_tab_widget.addTab(self.entity_activity_tab, "")
        self.entity_note_tab = QtGui.QWidget()
        self.entity_note_tab.setObjectName("entity_note_tab")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.entity_note_tab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.entity_note_view = QtGui.QListView(self.entity_note_tab)
        self.entity_note_view.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.entity_note_view.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.entity_note_view.setUniformItemSizes(True)
        self.entity_note_view.setObjectName("entity_note_view")
        self.verticalLayout_2.addWidget(self.entity_note_view)
        self.entity_tab_widget.addTab(self.entity_note_tab, "")
        self.entity_version_tab = QtGui.QWidget()
        self.entity_version_tab.setObjectName("entity_version_tab")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.entity_version_tab)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.entity_version_view = QtGui.QListView(self.entity_version_tab)
        self.entity_version_view.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.entity_version_view.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.entity_version_view.setUniformItemSizes(True)
        self.entity_version_view.setObjectName("entity_version_view")
        self.verticalLayout_3.addWidget(self.entity_version_view)
        self.pending_versions_only = QtGui.QCheckBox(self.entity_version_tab)
        self.pending_versions_only.setObjectName("pending_versions_only")
        self.verticalLayout_3.addWidget(self.pending_versions_only)
        self.entity_tab_widget.addTab(self.entity_version_tab, "")
        self.entity_publish_tab = QtGui.QWidget()
        self.entity_publish_tab.setObjectName("entity_publish_tab")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.entity_publish_tab)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.entity_publish_view = QtGui.QListView(self.entity_publish_tab)
        self.entity_publish_view.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.entity_publish_view.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.entity_publish_view.setUniformItemSizes(True)
        self.entity_publish_view.setObjectName("entity_publish_view")
        self.verticalLayout_4.addWidget(self.entity_publish_view)
        self.latest_publishes_only = QtGui.QCheckBox(self.entity_publish_tab)
        self.latest_publishes_only.setChecked(True)
        self.latest_publishes_only.setObjectName("latest_publishes_only")
        self.verticalLayout_4.addWidget(self.latest_publishes_only)
        self.entity_tab_widget.addTab(self.entity_publish_tab, "")
        self.entity_tasks_tab = QtGui.QWidget()
        self.entity_tasks_tab.setObjectName("entity_tasks_tab")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.entity_tasks_tab)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.entity_task_view = QtGui.QListView(self.entity_tasks_tab)
        self.entity_task_view.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.entity_task_view.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.entity_task_view.setUniformItemSizes(True)
        self.entity_task_view.setObjectName("entity_task_view")
        self.verticalLayout_8.addWidget(self.entity_task_view)
        self.entity_tab_widget.addTab(self.entity_tasks_tab, "")
        self.entity_info_tab = QtGui.QWidget()
        self.entity_info_tab.setObjectName("entity_info_tab")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.entity_info_tab)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.entity_info_widget = AllFieldsWidget(self.entity_info_tab)
        self.entity_info_widget.setObjectName("entity_info_widget")
        self.verticalLayout_9.addWidget(self.entity_info_widget)
        self.entity_tab_widget.addTab(self.entity_info_tab, "")
        self.verticalLayout.addWidget(self.entity_tab_widget)
        self.page_stack.addWidget(self.entity_page)
        self.publish_page = QtGui.QWidget()
        self.publish_page.setObjectName("publish_page")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.publish_page)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.publish_tab_widget = QtGui.QTabWidget(self.publish_page)
        self.publish_tab_widget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.publish_tab_widget.setObjectName("publish_tab_widget")
        self.publish_history_tab = QtGui.QWidget()
        self.publish_history_tab.setObjectName("publish_history_tab")
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.publish_history_tab)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.publish_history_view = QtGui.QListView(self.publish_history_tab)
        self.publish_history_view.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.publish_history_view.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.publish_history_view.setUniformItemSizes(True)
        self.publish_history_view.setObjectName("publish_history_view")
        self.verticalLayout_15.addWidget(self.publish_history_view)
        self.publish_tab_widget.addTab(self.publish_history_tab, "")
        self.publish_upstream_tab = QtGui.QWidget()
        self.publish_upstream_tab.setObjectName("publish_upstream_tab")
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.publish_upstream_tab)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.publish_upstream_view = QtGui.QListView(self.publish_upstream_tab)
        self.publish_upstream_view.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.publish_upstream_view.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.publish_upstream_view.setUniformItemSizes(True)
        self.publish_upstream_view.setObjectName("publish_upstream_view")
        self.verticalLayout_13.addWidget(self.publish_upstream_view)
        self.publish_tab_widget.addTab(self.publish_upstream_tab, "")
        self.publish_downstream_tab = QtGui.QWidget()
        self.publish_downstream_tab.setObjectName("publish_downstream_tab")
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.publish_downstream_tab)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.publish_downstream_view = QtGui.QListView(self.publish_downstream_tab)
        self.publish_downstream_view.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.publish_downstream_view.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.publish_downstream_view.setUniformItemSizes(True)
        self.publish_downstream_view.setObjectName("publish_downstream_view")
        self.verticalLayout_14.addWidget(self.publish_downstream_view)
        self.publish_tab_widget.addTab(self.publish_downstream_tab, "")
        self.publish_info_tab = QtGui.QWidget()
        self.publish_info_tab.setObjectName("publish_info_tab")
        self.verticalLayout_19 = QtGui.QVBoxLayout(self.publish_info_tab)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.publish_info_widget = AllFieldsWidget(self.publish_info_tab)
        self.publish_info_widget.setObjectName("publish_info_widget")
        self.verticalLayout_19.addWidget(self.publish_info_widget)
        self.publish_tab_widget.addTab(self.publish_info_tab, "")
        self.verticalLayout_6.addWidget(self.publish_tab_widget)
        self.page_stack.addWidget(self.publish_page)
        self.version_page = QtGui.QWidget()
        self.version_page.setObjectName("version_page")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.version_page)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.version_tab_widget = QtGui.QTabWidget(self.version_page)
        self.version_tab_widget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.version_tab_widget.setObjectName("version_tab_widget")
        self.version_activity_tab = QtGui.QWidget()
        self.version_activity_tab.setObjectName("version_activity_tab")
        self.verticalLayout_20 = QtGui.QVBoxLayout(self.version_activity_tab)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.version_activity_stream = ActivityStreamWidget(self.version_activity_tab)
        self.version_activity_stream.setObjectName("version_activity_stream")
        self.verticalLayout_20.addWidget(self.version_activity_stream)
        self.version_tab_widget.addTab(self.version_activity_tab, "")
        self.version_note_tab = QtGui.QWidget()
        self.version_note_tab.setObjectName("version_note_tab")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.version_note_tab)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.version_note_view = QtGui.QListView(self.version_note_tab)
        self.version_note_view.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.version_note_view.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.version_note_view.setUniformItemSizes(True)
        self.version_note_view.setObjectName("version_note_view")
        self.verticalLayout_11.addWidget(self.version_note_view)
        self.version_tab_widget.addTab(self.version_note_tab, "")
        self.version_publish_tab = QtGui.QWidget()
        self.version_publish_tab.setObjectName("version_publish_tab")
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.version_publish_tab)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.version_publish_view = QtGui.QListView(self.version_publish_tab)
        self.version_publish_view.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.version_publish_view.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.version_publish_view.setUniformItemSizes(True)
        self.version_publish_view.setObjectName("version_publish_view")
        self.verticalLayout_12.addWidget(self.version_publish_view)
        self.version_tab_widget.addTab(self.version_publish_tab, "")
        self.version_info_tab = QtGui.QWidget()
        self.version_info_tab.setObjectName("version_info_tab")
        self.verticalLayout_21 = QtGui.QVBoxLayout(self.version_info_tab)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.version_info_widget = AllFieldsWidget(self.version_info_tab)
        self.version_info_widget.setObjectName("version_info_widget")
        self.verticalLayout_21.addWidget(self.version_info_widget)
        self.version_tab_widget.addTab(self.version_info_tab, "")
        self.verticalLayout_10.addWidget(self.version_tab_widget)
        self.page_stack.addWidget(self.version_page)
        self.note_page = QtGui.QWidget()
        self.note_page.setObjectName("note_page")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.note_page)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.note_reply_widget = ReplyListWidget(self.note_page)
        self.note_reply_widget.setObjectName("note_reply_widget")
        self.verticalLayout_5.addWidget(self.note_reply_widget)
        self.page_stack.addWidget(self.note_page)
        self.verticalLayout_17.addWidget(self.page_stack)

        self.retranslateUi(Dialog)
        self.header_stack.setCurrentIndex(0)
        self.page_stack.setCurrentIndex(0)
        self.entity_tab_widget.setCurrentIndex(2)
        self.publish_tab_widget.setCurrentIndex(3)
        self.version_tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Shotgun Browser", None, QtGui.QApplication.UnicodeUTF8))
        self.navigation_home.setToolTip(QtGui.QApplication.translate("Dialog", "Click to go to your work area", None, QtGui.QApplication.UnicodeUTF8))
        self.navigation_prev.setToolTip(QtGui.QApplication.translate("Dialog", "Click to go back", None, QtGui.QApplication.UnicodeUTF8))
        self.navigation_next.setToolTip(QtGui.QApplication.translate("Dialog", "Click to go forward", None, QtGui.QApplication.UnicodeUTF8))
        self.details_text_header.setText(QtGui.QApplication.translate("Dialog", "Header Text", None, QtGui.QApplication.UnicodeUTF8))
        self.search.setToolTip(QtGui.QApplication.translate("Dialog", "Search for things in Shotgun", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_search.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.details_text_middle.setText(QtGui.QApplication.translate("Dialog", "Details Text", None, QtGui.QApplication.UnicodeUTF8))
        self.entity_tab_widget.setTabText(self.entity_tab_widget.indexOf(self.entity_activity_tab), QtGui.QApplication.translate("Dialog", "Activity", None, QtGui.QApplication.UnicodeUTF8))
        self.entity_tab_widget.setTabText(self.entity_tab_widget.indexOf(self.entity_note_tab), QtGui.QApplication.translate("Dialog", "Notes", None, QtGui.QApplication.UnicodeUTF8))
        self.pending_versions_only.setText(QtGui.QApplication.translate("Dialog", "Only show versions pending review", None, QtGui.QApplication.UnicodeUTF8))
        self.entity_tab_widget.setTabText(self.entity_tab_widget.indexOf(self.entity_version_tab), QtGui.QApplication.translate("Dialog", "Versions", None, QtGui.QApplication.UnicodeUTF8))
        self.latest_publishes_only.setText(QtGui.QApplication.translate("Dialog", "Only show latest versions", None, QtGui.QApplication.UnicodeUTF8))
        self.entity_tab_widget.setTabText(self.entity_tab_widget.indexOf(self.entity_publish_tab), QtGui.QApplication.translate("Dialog", "Publishes", None, QtGui.QApplication.UnicodeUTF8))
        self.entity_tab_widget.setTabText(self.entity_tab_widget.indexOf(self.entity_tasks_tab), QtGui.QApplication.translate("Dialog", "Tasks", None, QtGui.QApplication.UnicodeUTF8))
        self.entity_tab_widget.setTabText(self.entity_tab_widget.indexOf(self.entity_info_tab), QtGui.QApplication.translate("Dialog", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.publish_tab_widget.setTabText(self.publish_tab_widget.indexOf(self.publish_history_tab), QtGui.QApplication.translate("Dialog", "Version History", None, QtGui.QApplication.UnicodeUTF8))
        self.publish_tab_widget.setTabText(self.publish_tab_widget.indexOf(self.publish_upstream_tab), QtGui.QApplication.translate("Dialog", "Uses", None, QtGui.QApplication.UnicodeUTF8))
        self.publish_tab_widget.setTabText(self.publish_tab_widget.indexOf(self.publish_downstream_tab), QtGui.QApplication.translate("Dialog", "Used By", None, QtGui.QApplication.UnicodeUTF8))
        self.publish_tab_widget.setTabText(self.publish_tab_widget.indexOf(self.publish_info_tab), QtGui.QApplication.translate("Dialog", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.version_tab_widget.setTabText(self.version_tab_widget.indexOf(self.version_activity_tab), QtGui.QApplication.translate("Dialog", "Activity", None, QtGui.QApplication.UnicodeUTF8))
        self.version_tab_widget.setTabText(self.version_tab_widget.indexOf(self.version_note_tab), QtGui.QApplication.translate("Dialog", "Notes", None, QtGui.QApplication.UnicodeUTF8))
        self.version_tab_widget.setTabText(self.version_tab_widget.indexOf(self.version_publish_tab), QtGui.QApplication.translate("Dialog", "Publishes", None, QtGui.QApplication.UnicodeUTF8))
        self.version_tab_widget.setTabText(self.version_tab_widget.indexOf(self.version_info_tab), QtGui.QApplication.translate("Dialog", "Info", None, QtGui.QApplication.UnicodeUTF8))

from ..qtwidgets import ShotgunPlaybackLabel, ActivityStreamWidget, ReplyListWidget, GlobalSearchWidget
from ..widget_all_fields import AllFieldsWidget
from . import resources_rc
