test = False

if test == False:
    from BackendArchitecture.ComplexModuleOne.Functions import *
    from BackendArchitecture.ComplexModuleOne.DataPoint import *
    from BackendArchitecture.ComplexModuleOne.CommunicationFacilitator import *
else:
    from Functions import *
    from DataPoint import *

#For Integration
class cCm1Initiator():
    def __init__(self) -> None:
        pass

    def main():
        #Get Input
        cCm1CommunicationFacilitator.Communication_Input()

        #Actual Function
        value = cCm1Functions.calculation(cInput.input_1, cInput.input_2)
        cOutput.output_1 = value

        #Export Output
        cCm1CommunicationFacilitator.Communication_Output()
        pass
    
    def main_test(input_1, input_2):
        value = cCm1Functions.calculation(input_1, input_2)
        cOutput.output_1 = value
        return value
    pass

#For Module Developer Test
if __name__ == "__main__":
    value = cCm1Initiator.main_test(1,2)
    print(value)
    