from FrontendArchitecture.UI.UiComponentPointer import *
from FrontendArchitecture.SimpleFunctions.FrontendInteractions import *

class cCommonConnect():
    def __init__(self) -> None:
        pass
    pass

class cExampleConnect(cCommonConnect):
    def __init__(self) -> None:
        super().__init__()
        self.oExamplePointerEstablishment = cExamplePointerEstablishment()
        pass

    def connect_button_to_instructions(self):
        self.oExamplePointerEstablishment.container_buttons["sf1Btn"].clicked.connect(cExampleInstructions.sf1Btn_clicked)
        self.oExamplePointerEstablishment.container_buttons["cm1Btn"].clicked.connect(cExampleInstructions.cm1Btn_clicked)
        self.oExamplePointerEstablishment.container_buttons["ls1Btn"].clicked.connect(cExampleInstructions.ls1Btn_clicked)
        pass

    def connect_other_active_widgets_to_instructions(self):
        self.oExamplePointerEstablishment.container_other_widgets["sf1Input"].textChanged.connect(cExampleInstructions.sf1Input_text_changed)
        self.oExamplePointerEstablishment.container_other_widgets["cm1Input"].textChanged.connect(cExampleInstructions.cm1Input_text_changed)
        self.oExamplePointerEstablishment.container_other_widgets["ls1Input"].textChanged.connect(cExampleInstructions.ls1Input_text_changed)
        pass
    pass

class cExampleInstructions():
    def __init__(self) -> None:
        super().__init__()
        pass

    #linear procedures for sf1Btn clicked event
    def sf1Btn_clicked(self):
        cExampleFrontendInteraction.sf1Btn_frontend_interaction(cExampleFrontendInteraction)
        pass
    
    #linear procedures for cm1Btn clicked event
    def cm1Btn_clicked(self):
        cExampleFrontendInteraction.cm1Btn_frontend_interaction(cExampleFrontendInteraction)
        pass

    #linear procedures for ls1Btn clicked event
    def ls1Btn_clicked(self):
        cExampleFrontendInteraction.ls1Btn_frontend_interaction(cExampleFrontendInteraction)
        pass

    #linear procedures for sf1Input text changed event
    def sf1Input_text_changed(self):
        cExampleFrontendInteraction.sf1Input_frontend_interaction(cExampleFrontendInteraction)
        pass
    
    #linear procedures for cm1Input text changed event
    def cm1Input_text_changed(self):
        cExampleFrontendInteraction.cm1Input_frontend_interaction(cExampleFrontendInteraction)
        pass

    #linear procedures for ls1Input text changed event
    def ls1Input_text_changed(self):
        cExampleFrontendInteraction.ls1Input_frontend_interaction(cExampleFrontendInteraction)
        pass
    
    pass