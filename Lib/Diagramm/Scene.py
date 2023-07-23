import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget
from Lib.Config.SceneCfg import SceneCfg

class Scene(QWidget):
    DEFAULT_WIDTH = SceneCfg.DEFAULT_WIDTH
    DEFAULT_HEIGHT = SceneCfg.DEFALUT_HEIGHT

    def __init__(self, parent: QWidget | None = ..., ) -> None:
        super().__init__(parent)
        self._x = 0
        self._y = 0
        self._width = 100
        self._height = 100

    @property
    def width(self):
        return self._width if self._width > 0 else self.DEFAULT_WIDTH
    
    @property
    def height(self):
        return self._height if self._height > 0 else self.DEFAULT_HEIGHT
    
    @property
    def x(self): return self._x
    
    @property
    def y(self): return self._y
    
    @x.setter
    def x(self, value): self._x = value

    @y.setter
    def y(self, value): self._y = value

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
    
    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value 

    

    