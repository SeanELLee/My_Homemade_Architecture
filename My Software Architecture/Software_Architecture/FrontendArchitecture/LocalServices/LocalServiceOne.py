from PyQt6.QtCore import QThread
from time import sleep
from FrontendArchitecture.UI.UiComponentPointer import *
from FrontendArchitecture.FrontendCentralDataPoint import *

class cLocalService1(QThread):
    def run(self):
        def continuous_function():
            value = "CM1 Hi " + cFrontendData.ls1_input

            if cFrontendControl.ls1_control == True:
                cExamplePointerEstablishment.container_other_widgets["ls1Display"].setText(value)
            else:
                pass

            pass

        while 1:
            continuous_function()
            sleep(0.005)
        pass
