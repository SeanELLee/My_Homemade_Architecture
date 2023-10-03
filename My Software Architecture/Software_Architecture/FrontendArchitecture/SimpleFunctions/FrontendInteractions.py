from FrontendArchitecture.FrontendCentralDataPoint import *
from FrontendArchitecture.UI.UiComponentPointer import *
from FrontendArchitecture.FrontendCommunicationFacilitator import *

class cCommonFrontendInteraction():
    def __init__(self) -> None:
        pass
    pass

class cExampleFrontendInteraction(cCommonFrontendInteraction):
    def __init__(self) -> None:
        super().__init__()
        pass
    
    def sf1Btn_frontend_interaction(self):
        value = "SF1 Hi " + cFrontendData.sf1_input
        cExamplePointerEstablishment.container_other_widgets["sf1Display"].setText(value)
        return value

    def cm1Btn_frontend_interaction(self):
        value = cFrontendData.cm1_input
        cCm1DataFrontend.input_1 = value
        cCm1DataFrontend.input_2 = value
        cCm1CommunicationFrontend.execute_backend(cCm1CommunicationFrontend)
        cExamplePointerEstablishment.container_other_widgets["cm1Display"].setText(cCm1DataFrontend.output_1)
        pass

    def ls1Btn_frontend_interaction(self):
        if cFrontendControl.ls1_control == False:
            cFrontendControl.ls1_control = True
            print('True')
        else:
            cFrontendControl.ls1_control = False
            print('False')
        pass

    def sf1Input_frontend_interaction(self):
        value = cExamplePointerEstablishment.container_other_widgets["sf1Input"].text()
        cFrontendData.sf1_input = value
        return value
    
    def cm1Input_frontend_interaction(self):
        value = cExamplePointerEstablishment.container_other_widgets["cm1Input"].text()
        cFrontendData.cm1_input = value
        return value
    
    def ls1Input_frontend_interaction(self):
        value = cExamplePointerEstablishment.container_other_widgets["ls1Input"].text()
        cFrontendData.ls1_input = value
        return value
    pass