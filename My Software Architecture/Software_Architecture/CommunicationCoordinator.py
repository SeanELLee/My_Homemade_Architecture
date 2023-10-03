from FrontendArchitecture.FrontendCentralDataPoint import *
from BackendArchitecture.BackendCentralDataPoint import *
from BackendArchitecture.BackendCommunicationFacilitator import *

class cCentralCm1Communication():
    def __init__(self) -> None:
        pass

    def write_to_backend(self):
        cCm1DataBackend.input_1 = cCm1DataFrontend.input_1
        cCm1DataBackend.input_2 = cCm1DataFrontend.input_2
        pass

    def write_to_frontend(self):
        cCm1DataFrontend.output_1 = cCm1DataBackend.output_1
        pass

    def execute_cm1(self):
        cCm1CommunicationBackend.execute_cm1(cCm1CommunicationBackend)
        self.write_to_frontend(cCentralCm1Communication)
        pass

    pass
