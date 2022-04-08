from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import *

from config import path


class Tool(QToolBar):

    call_pen = None
    call_rubber = None
    call_cut = None
    call_paint = None
    call_ellipse = None
    call_reset = None


    def __init__(self, parent=None):
        super(Tool, self).__init__(parent)
        print('Tool: init')

        # 펜 액션 생성
        self.pen_action = QAction(QIcon(path.UI_TOOL_PEN), 'pen', self)
        self.pen_action.triggered.connect(self.pen_button_click)

        # 지우개 액션 생성
        self.rubber_action = QAction(QIcon(path.UI_TOOL_RUBBER), 'rubber', self)
        self.rubber_action.triggered.connect(self.rubber_button_click)

        # 타원그리기 액션 생성
        self.ellipse_action = QAction(QIcon(path.UI_TOOL_ELLIPSE), 'ellipse', self)
        self.ellipse_action.triggered.connect(self.ellipse_button_click)

        # 자르기 액션 생성
        self.cut_action = QAction(QIcon(path.UI_TOOL_CUT), 'cut', self)
        self.cut_action.triggered.connect(self.cut_button_click)

        # 칠하기 액션 생성
        self.paint_action = QAction(QIcon(path.UI_TOOL_PAINT), 'paint', self)
        self.paint_action.triggered.connect(self.paint_button_click)

        # 화면 갱신 액션 생성
        self.reset_action = QAction(QIcon(path.UI_TOOL_RESET), 'reset', self)
        self.reset_action.triggered.connect(self.reset_button_click)

        # 액션 등록
        self.addAction(self.pen_action)
        self.addAction(self.rubber_action)
        self.addAction(self.ellipse_action)
        self.addAction(self.cut_action)
        self.addAction(self.paint_action)
        self.addAction(self.reset_action)


    # mark - Event call back method
    def pen_button_click(self):
        print('Tool: pen_button_click')
        call = self.call_pen
        call('pen')

    # mark - Event call back method
    def rubber_button_click(self):
        print('Tool: rubber_button_click')
        call = self.call_rubber
        call('rubber')

    # mark - Event call back method
    def ellipse_button_click(self):
        print('Tool: ellipse_button_click')
        call = self.call_ellipse
        call('ellipse')

    # mark - Event call back method
    def cut_button_click(self):
        print('Tool: cut_button_click')
        call = self.call_cut
        call('cut')

    # mark - Event call back method
    def paint_button_click(self):
        print('Tool: paint_button_click')
        call = self.call_paint
        call('paint')

    # mark - Event call back method
    def reset_button_click(self):
        print('Tool: reset_button_click')
        call = self.call_reset
        call('reset')

