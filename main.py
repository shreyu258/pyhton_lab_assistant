from eventHandler import eventHandlerClass
from PyQt5.QtWidgets import QApplication

def main():
    # Create a QApplication instance
    app = QApplication([])

    # Create an instance of the eventHandlerClass
    eventHandler = eventHandlerClass()

    # Show the eventHandler window
    eventHandler.show()

    # Start the application event loop
    app.exec_()

if __name__ == "__main__":
    # Call the main function if this script is the main program
    main()