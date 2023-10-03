from FrontendArchitecture.SimpleFunctions.InitiationHandler import cExampleUiInitiation

#Initiation procedures
if __name__ == "__main__":
    #Create ExampleUiInitiation Object
    oInitiator = cExampleUiInitiation()

    #Create UI Object from oInitiator (packaged)
    oInitiator.setup_ui()

    #Create pointers for UI components (easy reference)
    oInitiator.establish_ui_component_pointers()

    #Connect pointers to instructions (UI-Functions Interfaces)
    oInitiator.connect_ui_components()

    #Clear pycache
    oInitiator.clear_pycache()

    #Setup initial parameters
    oInitiator.setup_initial_parameters()

    #Initiate local services
    oInitiator.initiate_local_services()

    #Display UI
    oInitiator.display_ui()

    #Setup closing procedures
    oInitiator.setup_closing_procedures()

    
    pass