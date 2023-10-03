from CommunicationCoordinator import *
from FrontendArchitecture.FrontendCentralDataPoint import *

class cCm1CommunicationFrontend():
    def __init__(self) -> None:
        pass

    def execute_backend(self):
        cCentralCm1Communication.write_to_backend(cCentralCm1Communication)
        cCentralCm1Communication.execute_cm1(cCentralCm1Communication)
        pass

    pass
