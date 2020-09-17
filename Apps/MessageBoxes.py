"""Facade pattern class for creating simple message boxes or
error message boxes"""

from PyQt5.QtWidgets import QErrorMessage,QMessageBox


class MessageBox:
    def __init__(self, message):
        if not str(message):
            raise InvalidInput(
                "A (error)message box only accepts string as input"
            )
        self.message = message

class ErrorMessage(MessageBox):
    def __init__(self, message):
        super().__init__(message)
        error_dialog = QErrorMessage()
        error_dialog.showMessage(message)
        error_dialog.show()
        error_dialog.exec_()


class InvalidInput(Exception):
    pass
