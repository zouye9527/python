from delphivcl import *
from Unit1 import *

def main():
    Application.Initialize()
    Application.Title = 'Project1'
    MainForm = Form1(Application)
    MainForm.Show()
    FreeConsole()
    Application.Run()

if __name__ == '__main__':
    main()
