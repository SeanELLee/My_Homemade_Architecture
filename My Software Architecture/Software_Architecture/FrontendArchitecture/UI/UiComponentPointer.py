from PyQt6.QtCore import *
from PyQt6.QtCore import QObject


class cCommonPointerContainer(QObject):
    container_buttons = {}
    container_other_widgets = {}
    container_public ={}

    def __init__(self):
        super().__init__()
        pass
    
    pass

class cExamplePointerEstablishment(cCommonPointerContainer):
    def __init__(self):
        super().__init__()

    def register_button_pointers(self, ui):
        self.container_buttons["sf1Btn"] = ui.sf1Btn
        self.container_buttons["cm1Btn"] = ui.cm1Btn
        self.container_buttons["ls1Btn"] = ui.ls1Btn
        pass

    def register_other_widget_pointers(self, ui):
        self.container_other_widgets["sf1Display"] = ui.sf1Display
        self.container_other_widgets["cm1Display"] = ui.cm1Display
        self.container_other_widgets["ls1Display"] = ui.ls1Display
        self.container_other_widgets["sf1Input"] = ui.sf1Input
        self.container_other_widgets["cm1Input"] = ui.cm1Input
        self.container_other_widgets["ls1Input"] = ui.ls1Input
        pass

    def register_public_pointers(self, ui):
        self.container_public["ui"] = ui
        pass

    pass
