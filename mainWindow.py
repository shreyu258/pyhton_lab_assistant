from PyQt5.QtWidgets import (
    QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QTextEdit, QPushButton,
    QScrollArea, QLabel, QMessageBox
)
from PyQt5.QtCore import Qt, QTimer
from messageFrame import messageFrameClass

class mainWindowClass(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Lab Assistant")
        self.setGeometry(100, 100, 1200, 800)
        self.createWidgets()
        self.createLayout()
        self.conversationHistory = []
        self.addMessage("Welcome to the Python Programming Lab Assistant!", isUser=False)
        self.setStyleSheet("font-family: 'Times New Roman'")

    def createWidgets(self):
        # Heading
        self.heading = QLabel("PyGuide\n")
        self.heading.setAlignment(Qt.AlignCenter)
        self.heading.setStyleSheet("font-size: 30px; font-weight: bold;")

        # Instructions
        self.instructions = QLabel(
            "<b>How to Use Python Lab Assistant:</b>"
            "<ul>"
            "<li><b>Ask Question:</b> For Python-related questions or concepts, type in the box and click 'Ask Question'. Your questions will be answered in a detailed, step-by-step manner in bullet point format.</li>"
            "<li><b>Code Debugging:</b> To get help with your Python code, paste the code snippet in the text box and click 'Code Assistance'. Queries within code are also handled.</li>"
            "<li><b>Clear History:</b> To erase the chat history and start fresh, click 'Clear History'.</li>"
            "</ul>"
        )
        self.instructions.setAlignment(Qt.AlignCenter)
        self.instructions.setStyleSheet("font-size: 16px;")

       # Chat Display
        self.chatDisplayLayout = QVBoxLayout()
        self.chatDisplayLayout.setAlignment(Qt.AlignBottom)
        self.chatDisplayLayout.setSpacing(10)
        
        # Chat Display Scroll Area
        self.chatScrollArea = QScrollArea()
        self.chatScrollArea.setWidgetResizable(True)
        self.chatDisplayWidget = QWidget()
        self.chatDisplayWidget.setLayout(self.chatDisplayLayout)

        self.chatScrollArea.setWidget(self.chatDisplayWidget)
        self.chatScrollArea.setStyleSheet("""
                                    QScrollBar:vertical {
                                        border: 2px solid #999999;
                                        background: white;
                                        width: 15px;
                                        margin: 15px 0 15px 0;
                                    }
                                    QScrollBar::handle:vertical {
                                        background: #cccccc;
                                        min-height: 20px;
                                    }
                                    QScrollBar::add-line:vertical {
                                        border: 1px solid #999999;
                                        background: #cccccc;
                                        height: 15px;
                                        subcontrol-position: bottom;
                                        subcontrol-origin: margin;
                                    }

                                    QScrollBar::sub-line:vertical {
                                        border: 1px solid #999999;
                                        background: #cccccc;
                                        height: 15px;
                                        subcontrol-position: top;
                                        subcontrol-origin: margin;
                                    }
                                    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                                        border: 2px solid #999999;
                                        width: 3px;
                                        height: 3px;
                                        background: white;
                                    }

                                    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                                        background: none;
                                    }
                                """)

        # User Input
        self.userInput = QTextEdit()
        self.userInput.setPlaceholderText("Enter your query or code here...")
        self.userInput.setFixedHeight(140)
        self.userInput.setStyleSheet(
            "border: 1px solid #ccc; border-radius: 5px; padding: 5px; font-size: 14pt; font-family: 'Comic Sans'"
        )
  
        # Buttons
        self.questionButton = QPushButton("Ask Question")
        self.questionButton.setStyleSheet("""
            padding: 10px;
            font-size: 14pt;
            background-color: #89ABE3;
            border: 1px solid #ccc;
            border-radius: 5px;
            color: #333333;                               
        """)

        self.codeButton = QPushButton("Code Debugging")
        self.codeButton.setStyleSheet("""
            padding: 10px;
            font-size: 14pt;
            background-color: #98DDCA;
            border: 1px solid #ccc;
            border-radius: 5px;
        """)

        self.historyButton = QPushButton("Clear History")
        self.historyButton.setStyleSheet("""
            padding: 10px;
            font-size: 14pt;
            background-color: #FEC89A;
            border: 1px solid #ccc;
            border-radius: 5px;
        """)

    def createLayout(self):
        mainLayout = QVBoxLayout()

        # Top bar layout for heading
        topBarLayout = QHBoxLayout()
        topBarLayout.addWidget(self.heading, 1)
        mainLayout.addLayout(topBarLayout)

        # Add Instructions
        mainLayout.addWidget(self.instructions)

        # Add Chat Display
        mainLayout.addWidget(self.chatScrollArea)

        # Add User Input
        mainLayout.addWidget(self.userInput)

        # Buttons Layout
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.questionButton)
        buttonLayout.addWidget(self.codeButton)
        buttonLayout.addWidget(self.historyButton)
        mainLayout.addLayout(buttonLayout)

        centralWidget = QWidget()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)

    def addMessage(self, message, isUser=True):
        messageFrameLayout = messageFrameClass(message, None, isUser)
        self.chatDisplayLayout.addWidget(messageFrameLayout)

        # Ensure the layout and the scroll area update before scrolling
        self.chatDisplayLayout.update()
        self.chatScrollArea.update()

        # Scroll to the end
        self.chatScrollArea.ensureWidgetVisible(self.chatScrollArea, 0, 0)
        QTimer.singleShot(100, self.scrollToBottom)

    def scrollToBottom(self):
        # Scroll to the end function
        self.chatScrollArea.verticalScrollBar().setValue(
            self.chatScrollArea.verticalScrollBar().maximum())
        
    def closeEvent(self, event):
        # Exit Function
        reply = QMessageBox.question(self, 'Confirm Exit',
                                    'Are you sure you want to exit the application?', QMessageBox.Yes | 
                                    QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
            self.conversationHistory.clear()
        else:
            event.ignore()