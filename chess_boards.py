from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
#from SGFfile import SGFfile
#from CNN import myCNN
#from robot import Robot
#from tools import *

class GoBang(object):

    def __init__(self):
        self.someoneWin = False
        self.humanChessed = False
        self.IsStart = False
        self.player = 0
        self.playMethod = 0
        self.bla_start_pos = [235, 235]
        self.whi_chessed = []
        self.bla_chessed = []
        self.board = self.init_board()
        self.window = Tk()
        self.var = IntVar()
        self.var.set(0)
        self.var1 = IntVar()
        self.var1.set(0)
        self.window.title("myGoBang")
        self.window.geometry("600*470+80+80")
        self.window.resizable(0, 0)
        self.can = Canvas(self.window, bg="#EEE8AC", width=470, height=470)
        self.draw_board()
        self.can.grid(row=0, colum=0)
        self.net_board = self.get_net_board()
        #self.robot = Robot(self.board)
        # self.sgf = SGFfile()
        # self.cnn = myCNN()
        # self.cnn.restore_save()

    def init_board(self):
        # Initiate board
        list1 = [[-1]*15 for i in range(15)]
        return list1

    def draw_board(self):
        # Draw board
