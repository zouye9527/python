import os
from delphivcl import *

class Form1(Form):

    def __init__(self, owner):
        self.Label1 = Label(self)
        self.Button1 = Button(self)
        self.Edit2 = Edit(self)
        self.Edit1 = Edit(self)
        self.Label1 = Label(self)
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Unit1.pydfm"))
        self.身高.Onhange = self.Edit1Change
        self.Label1.OnClick = self.Label1Click




    def Label1Click(self, Sender):
        pass

    def Edit1Change(self, Sender):
        pass