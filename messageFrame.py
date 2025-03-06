from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt

class messageFrameClass(QWidget):

    def __init__(self, message, parent=None, isUser=True):
        super().__init__(parent)

        # Create a label to display the message
        self.messageLabel = QLabel(message, self)
        self.messageLabel.setAlignment(Qt.AlignTop)
        self.messageLabel.setWordWrap(True)
        self.messageLabel.setTextInteractionFlags(Qt.TextSelectableByMouse)

        # Create a layout to arrange the label and spacer
        self.layout = QHBoxLayout(self)

        if isUser:
            # Configure styles for user messages
            self.messageLabel.setMaximumWidth(1400)
            self.messageLabel.setStyleSheet("background-color: #2E5894;"
                                             "color: #FFFFFF;" 
                                             "border-radius: 12px;"
                                             "padding: 5px 10px;"
                                             "font-size: 16pt;"
                                             "font-family: 'Courier New Bold'")
            self.layout.addWidget(self.messageLabel)
            self.layout.setAlignment(Qt.AlignLeft)
            spacer = QWidget()
            spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
            self.layout.addWidget(spacer)
        else:
            # Configure styles for assistant messages
            self.messageLabel.setMinimumWidth(430)
            self.messageLabel.setMaximumWidth(1400)
            self.messageLabel.setStyleSheet("background-color: #D3D3D3;"
                                             "color: #000000;"
                                             "border-radius: 12px;"
                                             "padding: 5px 10px;"
                                             "font-size: 16pt;"
                                             "font-family: 'Courier New Bold'")
            spacer = QWidget()
            spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
            self.layout.addWidget(spacer)
            self.layout.addWidget(self.messageLabel)
            self.layout.setAlignment(Qt.AlignRight)

        self.setLayout(self.layout)