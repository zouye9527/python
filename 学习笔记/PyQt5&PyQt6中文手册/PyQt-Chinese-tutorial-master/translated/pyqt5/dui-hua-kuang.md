# 对话框

对话框是一个现代GUI应用不可或缺的一部分。对话是两个人之间的交流，对话框就是人与电脑之间的对话。对话框用来输入数据，修改数据，修改应用设置等等。

## 输入文字

`QInputDialog`提供了一个简单方便的对话框，可以输入字符串，数字或列表。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we receive data from
a QInputDialog dialog. 

Aauthor: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, 
    QInputDialog, QApplication)
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()


    def showDialog(self):

        text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter your name:')

        if ok:
            self.le.setText(str(text))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

这个示例有一个按钮和一个输入框，点击按钮显示对话框，输入的文本会显示在输入框里。

```text
text, ok = QInputDialog.getText(self, 'Input Dialog',
    'Enter your name:')
```

这是显示一个输入框的代码。第一个参数是输入框的标题，第二个参数是输入框的占位符。对话框返回输入内容和一个布尔值，如果点击的是OK按钮，布尔值就返回True。

```text
if ok:
    self.le.setText(str(text))
```

把得到的字符串放到输入框里。

程序展示：

![input dialog](images/5-inputdialog.png)

## 选取颜色

QColorDialog提供颜色的选择。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we select a color value
from the QColorDialog and change the background
color of a QFrame widget. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, 
    QColorDialog, QApplication)
from PyQt5.QtGui import QColor
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        col = QColor(0, 0, 0) 

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" 
            % col.name())
        self.frm.setGeometry(130, 22, 100, 100)            

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()


    def showDialog(self):

        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                % col.name())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

例子里有一个按钮和一个`QFrame`，默认的背景颜色为黑色，我们可以使用`QColorDialog`改变背景颜色。

```text
col = QColor(0, 0, 0)
```

初始化`QtGui.QFrame`的背景颜色。

```text
col = QColorDialog.getColor()
```

弹出一个`QColorDialog`对话框。

```text
if col.isValid():
    self.frm.setStyleSheet("QWidget { background-color: %s }"
        % col.name())
```

我们可以预览颜色，如果点击取消按钮，没有颜色值返回，如果颜色是我们想要的，就从取色框里选择这个颜色。

程序展示：

![color dialog](images/5-colordialog.png)

## 选择字体

`QFontDialog`能做字体的选择。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we select a font name
and change the font of a label. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, 
    QSizePolicy, QLabel, QFontDialog, QApplication)
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        vbox = QVBoxLayout()

        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed,
            QSizePolicy.Fixed)

        btn.move(20, 20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)          

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')
        self.show()


    def showDialog(self):

        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

我们创建了一个有一个按钮和一个标签的`QFontDialog`的对话框，我们可以使用这个功能修改字体样式。

```text
font, ok = QFontDialog.getFont()
```

弹出一个字体选择对话框。`getFont()`方法返回一个字体名称和状态信息。状态信息有OK和其他两种。

```text
if ok:
    self.label.setFont(font)
```

如果点击OK，标签的字体就会随之更改。

程序展示：

![font dialog](images/5-fontdialog.png)

## 选择文件

`QFileDialog`给用户提供文件或者文件夹选择的功能。能打开和保存文件。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we select a file with a
QFileDialog and display its contents
in a QTextEdit.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QMainWindow, QTextEdit, 
    QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
import sys

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)       

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()


    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

本例中有一个菜单栏，一个置中的文本编辑框，一个状态栏。点击菜单栏选项会弹出一个`QtGui.QFileDialog`对话框，在这个对话框里，你能选择文件，然后文件的内容就会显示在文本编辑框里。

```text
class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
```

这里设置了一个文本编辑框，文本编辑框是基于`QMainWindow`组件的。

```text
fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
```

弹出`QFileDialog`窗口。`getOpenFileName()`方法的第一个参数是说明文字，第二个参数是默认打开的文件夹路径。默认情况下显示所有类型的文件。

```text
if fname[0]:
    f = open(fname[0], 'r')

    with f:
        data = f.read()
        self.textEdit.setText(data)
```

读取选中的文件，并显示在文本编辑框内（但是打开HTML文件时，是渲染后的结果，汗）。

程序展示：

![file Dialog](images/5-filedialog.png)

