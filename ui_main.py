# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QToolBox, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1016, 673)
        MainWindow.setMaximumSize(QSize(1016, 673))
        MainWindow.setStyleSheet(u"background-color: rgb(47, 79, 79);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"\n"
"	border:none;	\n"
"}\n"
"QLabel{\n"
"	color:rgb(255, 255, 255);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.left_container = QFrame(self.centralwidget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMinimumSize(QSize(0, 0))
        self.left_container.setMaximumSize(QSize(9, 16777215))
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.frame = QFrame(self.left_container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(69, 116, 116);\n"
"	border-radius: 5px;\n"
"	border-right: 1px solid rgb(255,255,255);\n"
"	\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(47, 79, 79);\n"
"	text-align:left;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QFrame{\n"
"	border:1px solid rgb(47, 79, 79);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#4d86bf;\n"
"	border-top-left-radius:15px;\n"
"	\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 116, 510))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(11)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_cadastrar = QPushButton(self.page)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_cadastrar)

        self.btn_pg_cadastro = QPushButton(self.page)
        self.btn_pg_cadastro.setObjectName(u"btn_pg_cadastro")
        self.btn_pg_cadastro.setMinimumSize(QSize(0, 30))
        self.btn_pg_cadastro.setFont(font)
        self.btn_pg_cadastro.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_pg_cadastro)

        self.btn_sobre = QPushButton(self.page)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 30))
        self.btn_sobre.setFont(font)
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 16, 527))
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 100, 47, 13))
        self.toolBox.addItem(self.page_2, u"Page 2")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_container)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_toggle = QPushButton(self.top_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_toggle, 0, Qt.AlignLeft)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setStyleSheet(u"")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_6 = QVBoxLayout(self.pg_home)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.logo = QLabel(self.pg_home)
        self.logo.setObjectName(u"logo")

        self.verticalLayout_6.addWidget(self.logo)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastrar = QWidget()
        self.pg_cadastrar.setObjectName(u"pg_cadastrar")
        self.verticalLayout_7 = QVBoxLayout(self.pg_cadastrar)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tabWidget = QTabWidget(self.pg_cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(47, 79, 79, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.tabWidget.setPalette(palette)
        self.tabWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.verticalLayout_10 = QVBoxLayout(self.tab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QLineEdit{\n"
"\n"
"	background-color:rgb(255, 255, 255);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QFrame{\n"
"	\n"
"	\n"
"	border-radius:5px;\n"
"	background-color: rgb(200, 180, 163);\n"
"\n"
"}\n"
"QLineEdit{\n"
"	border-radius:5px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_logradouro = QLineEdit(self.frame_4)
        self.txt_logradouro.setObjectName(u"txt_logradouro")
        self.txt_logradouro.setMinimumSize(QSize(0, 30))
        self.txt_logradouro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_logradouro, 7, 0, 1, 1)

        self.txt_complemento = QLineEdit(self.frame_4)
        self.txt_complemento.setObjectName(u"txt_complemento")
        self.txt_complemento.setMinimumSize(QSize(0, 30))
        self.txt_complemento.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_complemento, 7, 2, 1, 1)

        self.txt_municipio = QLineEdit(self.frame_4)
        self.txt_municipio.setObjectName(u"txt_municipio")
        self.txt_municipio.setMinimumSize(QSize(0, 30))
        self.txt_municipio.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_municipio, 12, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 1, 1, 1, 1)

        self.lbs_cadastro = QLabel(self.frame_4)
        self.lbs_cadastro.setObjectName(u"lbs_cadastro")
        self.lbs_cadastro.setStyleSheet(u"background-color: rgba(47, 79, 79, 0.80);")

        self.gridLayout.addWidget(self.lbs_cadastro, 0, 0, 1, 3)

        self.txt_numeroemp = QLineEdit(self.frame_4)
        self.txt_numeroemp.setObjectName(u"txt_numeroemp")
        self.txt_numeroemp.setMinimumSize(QSize(0, 30))
        self.txt_numeroemp.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_numeroemp, 7, 1, 1, 1)

        self.txt_dtabertura = QLineEdit(self.frame_4)
        self.txt_dtabertura.setObjectName(u"txt_dtabertura")
        self.txt_dtabertura.setMinimumSize(QSize(0, 30))
        self.txt_dtabertura.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_dtabertura, 3, 1, 1, 1)

        self.txt_cnpj = QLineEdit(self.frame_4)
        self.txt_cnpj.setObjectName(u"txt_cnpj")
        self.txt_cnpj.setMinimumSize(QSize(0, 30))
        self.txt_cnpj.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cnpj, 3, 0, 1, 1)

        self.txt_estado = QLineEdit(self.frame_4)
        self.txt_estado.setObjectName(u"txt_estado")
        self.txt_estado.setMinimumSize(QSize(0, 30))
        self.txt_estado.setMaximumSize(QSize(16777215, 16777215))
        self.txt_estado.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_estado, 12, 1, 1, 1)

        self.txt_nomempresa = QLineEdit(self.frame_4)
        self.txt_nomempresa.setObjectName(u"txt_nomempresa")
        self.txt_nomempresa.setMinimumSize(QSize(0, 30))
        self.txt_nomempresa.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_nomempresa, 5, 0, 1, 2)

        self.txt_porte = QLineEdit(self.frame_4)
        self.txt_porte.setObjectName(u"txt_porte")
        self.txt_porte.setMinimumSize(QSize(0, 30))
        self.txt_porte.setAlignment(Qt.AlignCenter)
        self.txt_porte.setReadOnly(False)

        self.gridLayout.addWidget(self.txt_porte, 3, 2, 1, 1)

        self.txt_userread = QLineEdit(self.frame_4)
        self.txt_userread.setObjectName(u"txt_userread")
        self.txt_userread.setMinimumSize(QSize(0, 30))
        self.txt_userread.setAlignment(Qt.AlignCenter)
        self.txt_userread.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_userread, 13, 0, 1, 1)

        self.txt_situacao = QLineEdit(self.frame_4)
        self.txt_situacao.setObjectName(u"txt_situacao")
        self.txt_situacao.setMinimumSize(QSize(0, 30))
        self.txt_situacao.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_situacao, 5, 2, 1, 1)

        self.txt_tipo_cadastro = QComboBox(self.frame_4)
        self.txt_tipo_cadastro.addItem("")
        self.txt_tipo_cadastro.addItem("")
        self.txt_tipo_cadastro.setObjectName(u"txt_tipo_cadastro")
        self.txt_tipo_cadastro.setMinimumSize(QSize(0, 30))
        palette1 = QPalette()
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.txt_tipo_cadastro.setPalette(palette1)
        font1 = QFont()
        font1.setPointSize(10)
        self.txt_tipo_cadastro.setFont(font1)
        self.txt_tipo_cadastro.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")

        self.gridLayout.addWidget(self.txt_tipo_cadastro, 13, 1, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_4)

        self.btn_cadastraremp = QPushButton(self.tab)
        self.btn_cadastraremp.setObjectName(u"btn_cadastraremp")
        self.btn_cadastraremp.setMinimumSize(QSize(160, 30))
        font2 = QFont()
        font2.setPointSize(12)
        self.btn_cadastraremp.setFont(font2)
        self.btn_cadastraremp.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastraremp.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(108, 190, 217);\n"
"	border-radius:15px;\n"
"	color: #fff\n"
"}\n"
"\n"
"QPushButton{\n"
"			border-radius:15px;\n"
"	background-color:rgb(243, 243, 243);\n"
"\n"
"}")

        self.verticalLayout_10.addWidget(self.btn_cadastraremp, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_9 = QVBoxLayout(self.tab_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_9.addWidget(self.label_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tableWidget = QTableWidget(self.tab_2)
        if (self.tableWidget.columnCount() < 12):
            self.tableWidget.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"	background-color:rgb(148,148,148);\n"
"	color:rgb(255,255,255);\n"
"	font: 10pt \"MS Shell dlg2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color:rgb(252,252,252);\n"
"\n"
"\n"
"}")

        self.horizontalLayout_5.addWidget(self.tableWidget)

        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"\n"
"	border-radius:15px;\n"
"	background-color:rgb(255,255,255);\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(0,24,74);\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"\n"
"	background-color:rgb(230,230,230);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btn_excel = QPushButton(self.frame_3)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(120, 30))
        self.btn_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color:rgb(255,255,255);\n"
"	background-color:rgb(49,147,0);\n"
"\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_excel)

        self.btn_alterar = QPushButton(self.frame_3)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(120, 30))
        self.btn_alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar.setStyleSheet(u"QPushButton:hover{\n"
"	color:rgb(255,255,255);\n"
"	background-color:rgb(255,170,0);\n"
"\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_3)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(120, 30))
        self.btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(199,66,0);\n"
"	color:rgb(255,255,255);\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_excluir)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_cadastrar)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_12 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_6 = QLabel(self.pg_cadastro)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color: rgb(69, 116, 116);\n"
"border-radius: 5px;")

        self.verticalLayout_12.addWidget(self.label_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(50, -1, 90, -1)
        self.label_7 = QLabel(self.pg_cadastro)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.txt_nomeuser = QLineEdit(self.pg_cadastro)
        self.txt_nomeuser.setObjectName(u"txt_nomeuser")
        self.txt_nomeuser.setStyleSheet(u"color:rgba(211, 239, 251,1);\n"
"border-bottom:1px solid white;\n"
"border-radius: 5px;\n"
"font-family:Trebuchet MS; \n"
"font-size:18px;\n"
"background-color: rgb(69, 116, 116);")

        self.horizontalLayout_9.addWidget(self.txt_nomeuser)


        self.verticalLayout_12.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(50, -1, 90, -1)
        self.label_10 = QLabel(self.pg_cadastro)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_6.addWidget(self.label_10)

        self.cb_perfil = QComboBox(self.pg_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cb_perfil.sizePolicy().hasHeightForWidth())
        self.cb_perfil.setSizePolicy(sizePolicy1)
        self.cb_perfil.setFont(font2)
        self.cb_perfil.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(69, 116, 116);\n"
"border-radius: 5px;")

        self.horizontalLayout_6.addWidget(self.cb_perfil)


        self.verticalLayout_12.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_13 = QLabel(self.pg_cadastro)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_10.addWidget(self.label_13)

        self.btn_cadastraruser = QPushButton(self.pg_cadastro)
        self.btn_cadastraruser.setObjectName(u"btn_cadastraruser")
        self.btn_cadastraruser.setMinimumSize(QSize(0, 35))
        self.btn_cadastraruser.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"    border-radius: 10px; \n"
"	font-size: 16px; \n"
"	background-color: #fff;\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 255, 255);\n"
"	 color:black\n"
"}\n"
"\n"
"")

        self.horizontalLayout_10.addWidget(self.btn_cadastraruser)

        self.label_12 = QLabel(self.pg_cadastro)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_10.addWidget(self.label_12)


        self.verticalLayout_12.addLayout(self.horizontalLayout_10)

        self.Pages.addWidget(self.pg_cadastro)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_11 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_8 = QLabel(self.pg_sobre)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_11.addWidget(self.label_8)

        self.label_9 = QLabel(self.pg_sobre)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_9)

        self.Pages.addWidget(self.pg_sobre)

        self.verticalLayout_5.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_cadastrar, self.txt_cnpj)
        QWidget.setTabOrder(self.txt_cnpj, self.txt_dtabertura)
        QWidget.setTabOrder(self.txt_dtabertura, self.txt_porte)
        QWidget.setTabOrder(self.txt_porte, self.txt_nomempresa)
        QWidget.setTabOrder(self.txt_nomempresa, self.txt_situacao)
        QWidget.setTabOrder(self.txt_situacao, self.txt_logradouro)
        QWidget.setTabOrder(self.txt_logradouro, self.txt_numeroemp)
        QWidget.setTabOrder(self.txt_numeroemp, self.txt_complemento)
        QWidget.setTabOrder(self.txt_complemento, self.txt_municipio)
        QWidget.setTabOrder(self.txt_municipio, self.txt_estado)
        QWidget.setTabOrder(self.txt_estado, self.txt_userread)
        QWidget.setTabOrder(self.txt_userread, self.btn_cadastraremp)
        QWidget.setTabOrder(self.btn_cadastraremp, self.btn_home)
        QWidget.setTabOrder(self.btn_home, self.btn_pg_cadastro)
        QWidget.setTabOrder(self.btn_pg_cadastro, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.btn_excel)
        QWidget.setTabOrder(self.btn_excel, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.txt_nomeuser)
        QWidget.setTabOrder(self.txt_nomeuser, self.cb_perfil)
        QWidget.setTabOrder(self.cb_perfil, self.btn_cadastraruser)
        QWidget.setTabOrder(self.btn_cadastraruser, self.btn_toggle)
        QWidget.setTabOrder(self.btn_toggle, self.btn_alterar)
        QWidget.setTabOrder(self.btn_alterar, self.btn_sobre)
        QWidget.setTabOrder(self.btn_sobre, self.btn_excluir)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Nome da Empresa S.A</span></p></body></html>", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_pg_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.btn_toggle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Sistema de Gerenciamento</span></p></body></html>", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/images.png\"/></p></body></html>", None))
        self.txt_logradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.txt_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.txt_municipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Munic\u00edpio", None))
        self.lbs_cadastro.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Cadastro de Empresas</span></p></body></html>", None))
        self.txt_numeroemp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.txt_dtabertura.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data de Abertura", None))
        self.txt_cnpj.setText("")
        self.txt_cnpj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ da Empresa", None))
        self.txt_estado.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.txt_nomempresa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome da Empresa", None))
        self.txt_porte.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Porte da Empresa", None))
        self.txt_userread.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.txt_situacao.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Situa\u00e7\u00e3o da Empresa", None))
        self.txt_tipo_cadastro.setItemText(0, QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.txt_tipo_cadastro.setItemText(1, QCoreApplication.translate("MainWindow", u"Fornecedor", None))

        self.btn_cadastraremp.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cadastro de Empresas", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Empresas Cadastradas</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Data Abertura", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Raz\u00e3o Social", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Situa\u00e7\u00e3o", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Complemento", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Municipio", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Estado", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Porte Empresa", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Tipo Cadastro", None));
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Empresas Cadastradas", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">CADASTRAR USU\u00c1RIO</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nome de Usu\u00e1rio:</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Perfil do Usu\u00e1rio:</span></p></body></html>", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_13.setText("")
        self.btn_cadastraruser.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_12.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">SOBRE</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Este sistema foi criado apenas para realizar um controle de abertura de R.O's, para controle e registro de status da abertura dos R.O's</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u00a9 Nome da Empresa 2022</span></p></body></html>", None))
    # retranslateUi

