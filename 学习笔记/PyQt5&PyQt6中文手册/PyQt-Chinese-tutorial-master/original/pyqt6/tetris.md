# Tetris in PyQt6
*last modified May 5, 2021*

In this chapter, we create a Tetris game clone.

## Tetris
The Tetris game is one of the most popular computer games ever created. The original game was designed and programmed by a Russian programmer *Alexey Pajitnov* in 1985. Since then, Tetris is available on almost every computer platform in lots of variations.

Tetris is called a falling block puzzle game. In this game, we have seven different shapes called tetrominoes: an S-shape, a Z-shape, a T-shape, an L-shape, a Line-shape, a MirroredL-shape, and a Square-shape. Each of these shapes is formed with four squares. The shapes are falling down the board. The object of the Tetris game is to move and rotate the shapes so that they fit as much as possible. If we manage to form a row, the row is destroyed and we score. We play the Tetris game until we top out.

![Tetrominoes](./images/tetrominoes.png)

Figure: Tetrominoes

PyQt6 is a toolkit designed to create applications. There are other libraries which are targeted at creating computer games. Nevertheless, PyQt6 and other application toolkits can be used to create simple games.

Creating a computer game is a good way for enhancing programming skills.

## The development
We do not have images for our Tetris game, we draw the tetrominoes using the drawing API available in the PyQt6 programming toolkit. Behind every computer game, there is a mathematical model. So it is in Tetris.

Some ideas behind the game:

 - We use a `QtCore.QBasicTimer` to create a game cycle.
 - The tetrominoes are drawn.
 - The shapes move on a square by square basis (not pixel by pixel).
 - Mathematically a board is a simple list of numbers.

The code consists of four classes: `Tetris`, `Board`, `Tetrominoe` and `Shape`. The `Tetris` class sets up the game. The `Board` is where the game logic is written. The `Tetrominoe` class contains names for all tetris pieces and the `Shape` class contains the code for a tetris piece.

``` python
# files: tetris.py
#!/usr/bin/python

"""
ZetCode PyQt6 tutorial

This is a Tetris game clone.

Author: Jan Bodnar
Website: zetcode.com
"""

import random
import sys

from PyQt6.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QFrame, QApplication


class Tetris(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        """initiates application UI"""

        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)

        self.statusbar = self.statusBar()
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)

        self.tboard.start()

        self.resize(180, 380)
        self.center()
        self.setWindowTitle('Tetris')
        self.show()


    def center(self):
        """centers the window on the screen"""

        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())


class Board(QFrame):

    msg2Statusbar = pyqtSignal(str)

    BoardWidth = 10
    BoardHeight = 22
    Speed = 300


    def __init__(self, parent):
        super().__init__(parent)

        self.initBoard()


    def initBoard(self):
        """initiates board"""

        self.timer = QBasicTimer()
        self.isWaitingAfterLine = False

        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0
        self.board = []

        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.isStarted = False
        self.isPaused = False
        self.clearBoard()


    def shapeAt(self, x, y):
        """determines shape at the board position"""

        return self.board[(y * Board.BoardWidth) + x]


    def setShapeAt(self, x, y, shape):
        """sets a shape at the board"""

        self.board[(y * Board.BoardWidth) + x] = shape


    def squareWidth(self):
        """returns the width of one square"""

        return self.contentsRect().width() // Board.BoardWidth


    def squareHeight(self):
        """returns the height of one square"""

        return self.contentsRect().height() // Board.BoardHeight


    def start(self):
        """starts game"""

        if self.isPaused:
            return

        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clearBoard()

        self.msg2Statusbar.emit(str(self.numLinesRemoved))

        self.newPiece()
        self.timer.start(Board.Speed, self)


    def pause(self):
        """pauses game"""

        if not self.isStarted:
            return

        self.isPaused = not self.isPaused

        if self.isPaused:
            self.timer.stop()
            self.msg2Statusbar.emit("paused")

        else:
            self.timer.start(Board.Speed, self)
            self.msg2Statusbar.emit(str(self.numLinesRemoved))

        self.update()


    def paintEvent(self, event):
        """paints all shapes of the game"""

        painter = QPainter(self)
        rect = self.contentsRect()

        boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()

        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                shape = self.shapeAt(j, Board.BoardHeight - i - 1)

                if shape != Tetrominoe.NoShape:
                    self.drawSquare(painter,
                                    rect.left() + j * self.squareWidth(),
                                    boardTop + i * self.squareHeight(), shape)

        if self.curPiece.shape() != Tetrominoe.NoShape:

            for i in range(4):
                x = self.curX + self.curPiece.x(i)
                y = self.curY - self.curPiece.y(i)
                self.drawSquare(painter, rect.left() + x * self.squareWidth(),
                            boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(),
                            self.curPiece.shape())


    def keyPressEvent(self, event):
        """processes key press events"""

        if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape:
            super(Board, self).keyPressEvent(event)
            return

        key = event.key()

        if key == Qt.Key.Key_P:
            self.pause()
            return

        if self.isPaused:
            return

        elif key == Qt.Key.Key_Left.value:
            self.tryMove(self.curPiece, self.curX - 1, self.curY)

        elif key == Qt.Key.Key_Right.value:
            self.tryMove(self.curPiece, self.curX + 1, self.curY)

        elif key == Qt.Key.Key_Down.value:
            self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)

        elif key == Qt.Key.Key_Up.value:
            self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)

        elif key == Qt.Key.Key_Space.value:
            self.dropDown()

        elif key == Qt.Key.Key_D.value:
            self.oneLineDown()

        else:
            super(Board, self).keyPressEvent(event)


    def timerEvent(self, event):
        """handles timer event"""

        if event.timerId() == self.timer.timerId():

            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.newPiece()
            else:
                self.oneLineDown()

        else:
            super(Board, self).timerEvent(event)


    def clearBoard(self):
        """clears shapes from the board"""

        for i in range(Board.BoardHeight * Board.BoardWidth):
            self.board.append(Tetrominoe.NoShape)


    def dropDown(self):
        """drops down a shape"""

        newY = self.curY

        while newY > 0:

            if not self.tryMove(self.curPiece, self.curX, newY - 1):
                break

            newY -= 1

        self.pieceDropped()


    def oneLineDown(self):
        """goes one line down with a shape"""

        if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
            self.pieceDropped()


    def pieceDropped(self):
        """after dropping shape, remove full lines and create new shape"""

        for i in range(4):
            x = self.curX + self.curPiece.x(i)
            y = self.curY - self.curPiece.y(i)
            self.setShapeAt(x, y, self.curPiece.shape())

        self.removeFullLines()

        if not self.isWaitingAfterLine:
            self.newPiece()


    def removeFullLines(self):
        """removes all full lines from the board"""

        numFullLines = 0
        rowsToRemove = []

        for i in range(Board.BoardHeight):

            n = 0
            for j in range(Board.BoardWidth):
                if not self.shapeAt(j, i) == Tetrominoe.NoShape:
                    n = n + 1

            if n == 10:
                rowsToRemove.append(i)

        rowsToRemove.reverse()

        for m in rowsToRemove:

            for k in range(m, Board.BoardHeight):
                for l in range(Board.BoardWidth):
                    self.setShapeAt(l, k, self.shapeAt(l, k + 1))

        numFullLines = numFullLines + len(rowsToRemove)

        if numFullLines > 0:
            self.numLinesRemoved = self.numLinesRemoved + numFullLines
            self.msg2Statusbar.emit(str(self.numLinesRemoved))

            self.isWaitingAfterLine = True
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.update()


    def newPiece(self):
        """creates a new shape"""

        self.curPiece = Shape()
        self.curPiece.setRandomShape()
        self.curX = Board.BoardWidth // 2 + 1
        self.curY = Board.BoardHeight - 1 + self.curPiece.minY()

        if not self.tryMove(self.curPiece, self.curX, self.curY):

            self.curPiece.setShape(Tetrominoe.NoShape)
            self.timer.stop()
            self.isStarted = False
            self.msg2Statusbar.emit("Game over")


    def tryMove(self, newPiece, newX, newY):
        """tries to move a shape"""

        for i in range(4):

            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)

            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
                return False

            if self.shapeAt(x, y) != Tetrominoe.NoShape:
                return False

        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        self.update()

        return True


    def drawSquare(self, painter, x, y, shape):
        """draws a square of a shape"""

        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color = QColor(colorTable[shape])
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2,
                         self.squareHeight() - 2, color)

        painter.setPen(color.lighter())
        painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        painter.drawLine(x, y, x + self.squareWidth() - 1, y)

        painter.setPen(color.darker())
        painter.drawLine(x + 1, y + self.squareHeight() - 1,
                         x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1,
                         y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)


class Tetrominoe:

    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7


class Shape:

    coordsTable = (
        ((0, 0), (0, 0), (0, 0), (0, 0)),
        ((0, -1), (0, 0), (-1, 0), (-1, 1)),
        ((0, -1), (0, 0), (1, 0), (1, 1)),
        ((0, -1), (0, 0), (0, 1), (0, 2)),
        ((-1, 0), (0, 0), (1, 0), (0, 1)),
        ((0, 0), (1, 0), (0, 1), (1, 1)),
        ((-1, -1), (0, -1), (0, 0), (0, 1)),
        ((1, -1), (0, -1), (0, 0), (0, 1))
    )

    def __init__(self):

        self.coords = [[0, 0] for i in range(4)]
        self.pieceShape = Tetrominoe.NoShape

        self.setShape(Tetrominoe.NoShape)


    def shape(self):
        """returns shape"""

        return self.pieceShape


    def setShape(self, shape):
        """sets a shape"""

        table = Shape.coordsTable[shape]

        for i in range(4):
            for j in range(2):
                self.coords[i][j] = table[i][j]

        self.pieceShape = shape


    def setRandomShape(self):
        """chooses a random shape"""

        self.setShape(random.randint(1, 7))


    def x(self, index):
        """returns x coordinate"""

        return self.coords[index][0]


    def y(self, index):
        """returns y coordinate"""

        return self.coords[index][1]


    def setX(self, index, x):
        """sets x coordinate"""

        self.coords[index][0] = x


    def setY(self, index, y):
        """sets y coordinate"""

        self.coords[index][1] = y
        

    def minX(self):
        """returns min x value"""

        m = self.coords[0][0]
        for i in range(4):
            m = min(m, self.coords[i][0])

        return m


    def maxX(self):
        """returns max x value"""

        m = self.coords[0][0]
        for i in range(4):
            m = max(m, self.coords[i][0])

        return m


    def minY(self):
        """returns min y value"""

        m = self.coords[0][1]
        for i in range(4):
            m = min(m, self.coords[i][1])

        return m


    def maxY(self):
        """returns max y value"""

        m = self.coords[0][1]
        for i in range(4):
            m = max(m, self.coords[i][1])

        return m


    def rotateLeft(self):
        """rotates shape to the left"""

        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape

        for i in range(4):
            result.setX(i, self.y(i))
            result.setY(i, -self.x(i))

        return result


    def rotateRight(self):
        """rotates shape to the right"""

        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape

        for i in range(4):
            result.setX(i, -self.y(i))
            result.setY(i, self.x(i))

        return result


def main():

    app = QApplication([])
    tetris = Tetris()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
```

The game is simplified a bit so that it is easier to understand. The game starts immediately after it is launched. We can pause the game by pressing the p key. The `Space` key will drop the tetris piece instantly to the bottom. The game goes at constant speed, no acceleration is implemented. The score is the number of lines that we have removed.

```python
self.tboard = Board(self)
self.setCentralWidget(self.tboard)
```
An instance of the Board class is created and set to be the central widget of the application.

```python
self.statusbar = self.statusBar()
self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)
```
We create a statusbar where we will display messages. We will display three possible messages: the number of lines already removed, the paused message, or the game over message. The msg2Statusbar is a custom signal that is implemented in the Board class. The showMessage is a built-in method that displays a message on a statusbar.

``` python
self.tboard.start()
```
This line initiates the game.

```python
class Board(QFrame):

    msg2Statusbar = pyqtSignal(str)
...
```
A custom signal is created with `pyqtSignal`. The `msg2Statusbar` is a signal that is emitted when we want to write a message or the score to the statusbar.

``` python
BoardWidth = 10
BoardHeight = 22
Speed = 300
```
These are `Board`'s class variables. The `BoardWidth` and the `BoardHeight` define the size of the board in blocks. The `Speed` defines the speed of the game. Each 300 ms a new game cycle will start.

``` python
...
self.curX = 0
self.curY = 0
self.numLinesRemoved = 0
self.board = []
...
```
In the `initBoard` method we initialize some important variables. The `self.board` variable is a list of numbers from 0 to 7. It represents the position of various shapes and remains of the shapes on the board.

``` python
def shapeAt(self, x, y):
    """determines shape at the board position"""

    return self.board[(y * Board.BoardWidth) + x]
```
The `shapeAt` method determines the type of a shape at a given block.

```python
def squareWidth(self):
    """returns the width of one square"""

    return self.contentsRect().width() // Board.BoardWidth
```
The board can be dynamically resized. As a consequence, the size of a block may change. The `squareWidth` calculates the width of the single square in pixels and returns it. The `Board.BoardWidth` is the size of the board in blocks.

```python
def pause(self):
    """pauses game"""

    if not self.isStarted:
        return

    self.isPaused = not self.isPaused

    if self.isPaused:
        self.timer.stop()
        self.msg2Statusbar.emit("paused")

    else:
        self.timer.start(Board.Speed, self)
        self.msg2Statusbar.emit(str(self.numLinesRemoved))

    self.update()
```
The `pause` method pauses the game. It stops the timer and displays a message on the statusbar.

```python
def paintEvent(self, event):
    """paints all shapes of the game"""

    painter = QPainter(self)
    rect = self.contentsRect()
...
```
The painting happens in the `paintEvent` method. The `QPainter` is responsible for all low-level painting in PyQt6.

```python
for i in range(Board.BoardHeight):
    for j in range(Board.BoardWidth):
        shape = self.shapeAt(j, Board.BoardHeight - i - 1)

        if shape != Tetrominoe.NoShape:
            self.drawSquare(painter,
                rect.left() + j * self.squareWidth(),
                boardTop + i * self.squareHeight(), shape)
```
The painting of the game is divided into two steps. In the first step, we draw all the shapes, or remains of the shapes that have been dropped to the bottom of the board. All the squares are remembered in the `self.board` list variable. The variable is accessed using the `shapeAt` method.

```python
if self.curPiece.shape() != Tetrominoe.NoShape:

    for i in range(4):

        x = self.curX + self.curPiece.x(i)
        y = self.curY - self.curPiece.y(i)
        self.drawSquare(painter, rect.left() + x * self.squareWidth(),
            boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(),
            self.curPiece.shape())
```
The next step is the drawing of the actual piece that is falling down.

```python
elif key == Qt.Key.Key_Right.value:
    self.tryMove(self.curPiece, self.curX + 1, self.curY)
```
In the `keyPressEvent` method we check for pressed keys. If we press the right arrow key, we try to move the piece to the right. We say try because the piece might not be able to move.

```python
elif key == Qt.Key.Key_Up.value:
    self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)
```
The `Up` arrow key will rotate the falling piece to the left.

```python
elif key == Qt.Key.Key_Space.value:
    self.dropDown()
```
The `Space` key will drop the falling piece instantly to the bottom.

```python
elif key == Qt.Key.Key_D.value:
    self.oneLineDown()
```
Pressing the d key, the piece will go one block down. It can be used to accellerate the falling of a piece a bit.

```python
def timerEvent(self, event):
    """handles timer event"""

    if event.timerId() == self.timer.timerId():

        if self.isWaitingAfterLine:
            self.isWaitingAfterLine = False
            self.newPiece()
        else:
            self.oneLineDown()

    else:
        super(Board, self).timerEvent(event)
```
In the timer event, we either create a new piece after the previous one was dropped to the bottom or we move a falling piece one line down.

```python
def clearBoard(self):
    """clears shapes from the board"""

    for i in range(Board.BoardHeight * Board.BoardWidth):
        self.board.append(Tetrominoe.NoShape)
```
The `clearBoard` method clears the board by setting `Tetrominoe.NoShape` at each block of the board.

```python
def removeFullLines(self):
    """removes all full lines from the board"""

    numFullLines = 0
    rowsToRemove = []

    for i in range(Board.BoardHeight):

        n = 0
        for j in range(Board.BoardWidth):
            if not self.shapeAt(j, i) == Tetrominoe.NoShape:
                n = n + 1

        if n == 10:
            rowsToRemove.append(i)

    rowsToRemove.reverse()


    for m in rowsToRemove:

        for k in range(m, Board.BoardHeight):
            for l in range(Board.BoardWidth):
                    self.setShapeAt(l, k, self.shapeAt(l, k + 1))

    numFullLines = numFullLines + len(rowsToRemove)
 ...
```
If the piece hits the bottom, we call the `removeFullLines` method. We find out all full lines and remove them. We do it by moving all lines above the current full line to be removed one line down. Notice that we reverse the order of the lines to be removed. Otherwise, it would not work correctly. In our case we use a `naive gravity`. This means that the pieces may be floating above empty gaps.

```python
def newPiece(self):
    """creates a new shape"""

    self.curPiece = Shape()
    self.curPiece.setRandomShape()
    self.curX = Board.BoardWidth // 2 + 1
    self.curY = Board.BoardHeight - 1 + self.curPiece.minY()

    if not self.tryMove(self.curPiece, self.curX, self.curY):

        self.curPiece.setShape(Tetrominoe.NoShape)
        self.timer.stop()
        self.isStarted = False
        self.msg2Statusbar.emit("Game over")
```
The `newPiece` method creates randomly a new tetris piece. If the piece cannot go into its initial position, the game is over.

``` python
def tryMove(self, newPiece, newX, newY):
    """tries to move a shape"""

    for i in range(4):

        x = newX + newPiece.x(i)
        y = newY - newPiece.y(i)

        if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
            return False

        if self.shapeAt(x, y) != Tetrominoe.NoShape:
            return False

    self.curPiece = newPiece
    self.curX = newX
    self.curY = newY
    self.update()

    return True
```
In the `tryMove` method we try to move our shapes. If the shape is at the edge of the board or is adjacent to some other piece, we return `False`. Otherwise we place the current falling piece to a new position.

``` python
class Tetrominoe:

    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7
```
The `Tetrominoe` class holds names of all possible shapes. We have also a `NoShape` for an empty space.

The Shape class saves information about a tetris piece.

``` python
class Shape(object):

    coordsTable = (
        ((0, 0),     (0, 0),     (0, 0),     (0, 0)),
        ((0, -1),    (0, 0),     (-1, 0),    (-1, 1)),
        ...
    )
...
```
The `coordsTable` tuple holds all possible coordinate values of our tetris pieces. This is a template from which all pieces take their coordinate values.

```python
self.coords = [[0,0] for i in range(4)]
```
Upon creation we create an empty coordinates list. The list will save the coordinates of the tetris piece.

![Coordinates](./images/coordinates.png)

Figure: Coordinates

The above image will help understand the coordinate values a bit more. For example, the tuples (0, -1), (0, 0), (-1, 0), (-1, -1) represent a Z-shape. The diagram illustrates the shape.

``` python
def rotateLeft(self):
    """rotates shape to the left"""

    if self.pieceShape == Tetrominoe.SquareShape:
        return self

    result = Shape()
    result.pieceShape = self.pieceShape

    for i in range(4):

        result.setX(i, self.y(i))
        result.setY(i, -self.x(i))

    return result
```
The `rotateLeft` method rotates a piece to the left. The square does not have to be rotated. That is why we simply return the reference to the current object. A new piece is created and its coordinates are set to the ones of the rotated piece.

![Tetris](./images/tetris.png)

Figure: Tetris

This was Tetris game in PyQt6.