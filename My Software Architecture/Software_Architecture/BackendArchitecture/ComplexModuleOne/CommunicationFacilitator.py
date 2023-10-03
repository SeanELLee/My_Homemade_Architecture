from BackendArchitecture.BackendCentralDataPoint import *
from BackendArchitecture.ComplexModuleOne.DataPoint import *

class cCm1CommunicationFacilitator():
    def Communication_Input():
        cInput.input_1 = cCm1DataBackend.input_1
        cInput.input_2 = cCm1DataBackend.input_2
        pass

    def Communication_Output():
        cCm1DataBackend.output_1 = cOutput.output_1
        pass
