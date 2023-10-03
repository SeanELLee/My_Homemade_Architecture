from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
import os
import shutil
from FrontendArchitecture.UI.UiComponentPointer import cExamplePointerEstablishment
from FrontendArchitecture.UI.UiConnection import cExampleConnect
from FrontendArchitecture.FrontendCentralDataPoint import *
from FrontendArchitecture.FrontendParameters import *
from FrontendArchitecture.LocalServices.LocalServiceOne import *
from FrontendArchitecture.UI.UiModuleCode.example_ui import Ui_MainWindow as ExampleUi

class cCommonInitiation():
    def __init__(self):
        self.ui = None
        self.app = None
        self.end_app = None
        self.main_window = None
        pass

    pass

class cExampleUiInitiation(cCommonInitiation):
    def __init__(self):
        super().__init__()
        self.oExamplePointerEstablishment = None
        self.oExampleConnect = None
        pass

    def setup_ui(self):
        self.app = QApplication(sys.argv)
        self.main_window = QMainWindow()
        self.ui = ExampleUi()
        self.ui.setupUi(self.main_window)
        self.oExamplePointerEstablishment = cExamplePointerEstablishment()
        self.oExampleConnect = cExampleConnect()
        pass

    def establish_ui_component_pointers(self):
        #register button widget to pointers
        self.oExamplePointerEstablishment.register_button_pointers(self.ui)
        #register other widget to pointers
        self.oExamplePointerEstablishment.register_other_widget_pointers(self.ui)
        #register public asset to pointers
        self.oExamplePointerEstablishment.register_public_pointers(self.ui)
        pass

    def connect_ui_components(self):
        #connect button widget to instruction
        self.oExampleConnect.connect_button_to_instructions()
        #connect active widget to instruction
        self.oExampleConnect.connect_other_active_widgets_to_instructions()
        pass

    def clear_pycache(self):
        if os.path.exists(cPycacheLocation.pycache_location_1):
            shutil.rmtree(cPycacheLocation.pycache_location_1)
        if os.path.exists(cPycacheLocation.pycache_location_2):
            shutil.rmtree(cPycacheLocation.pycache_location_2)
        if os.path.exists(cPycacheLocation.pycache_location_3):
            shutil.rmtree(cPycacheLocation.pycache_location_3)
        if os.path.exists(cPycacheLocation.pycache_location_4):
            shutil.rmtree(cPycacheLocation.pycache_location_4)
        if os.path.exists(cPycacheLocation.pycache_location_5):
            shutil.rmtree(cPycacheLocation.pycache_location_5)
        if os.path.exists(cPycacheLocation.pycache_location_6):
            shutil.rmtree(cPycacheLocation.pycache_location_6)
        if os.path.exists(cPycacheLocation.pycache_location_7):
            shutil.rmtree(cPycacheLocation.pycache_location_7)
        if os.path.exists(cPycacheLocation.pycache_location_8):
            shutil.rmtree(cPycacheLocation.pycache_location_8)
        pass

    def setup_initial_parameters(self):
        cFrontendData.sf1_input = cInitialParameters.sf1_input_init
        cFrontendData.cm1_input = cInitialParameters.cm1_input_init
        cFrontendData.ls1_input = cInitialParameters.ls1_input_init
        cFrontendControl.ls1_control = cInitialParameters.ls1_control_init
        pass

    def initiate_local_services(self):
        cFrontendThread.ls1_thread = cLocalService1()
        cFrontendThread.ls1_thread.start()
        pass

    def display_ui(self):
        self.main_window.show()
        self.end_app = self.app.exec()
        pass

    def setup_closing_procedures(self):
        sys.exit(self.end_app)
        pass

    pass