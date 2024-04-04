#PRESS ALT + SHIFT + M
import maya.cmds as mc

from PySide2.QtWidgets import QWidget

class CreateControllerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("create IKFK Limb")
        

controllerWidget = CreateControllerWidget()
controllerWidget.show()        