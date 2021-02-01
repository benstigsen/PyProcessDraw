# Drawing Options
colorEraser = ""
colorCurrent = ""

# Screen Options
screenW = 800
screenH = 800

# Processing Options
strokeW = 3

# Palette
class Palette(object):
    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

# Color Class
class Color(Palette):
    def __init__(self, x, y, w, h, c):
        super(Color, self).__init__(x, y, w, h)
        self.c = c
    
    def isMouseOn(self):
        if (mouseX >= self.x) and (mouseX <= self.x + self.w):
            if (mouseY >= self.y) and (mouseY <= self.y + self.h):
                return True
            
# Color Palette
palette = Palette()
colors = [
    Color(10, 10, 30, 30, "#FF4444"),  # Red
    Color(50, 10, 30, 30, "#33DD33"),  # Green
    Color(90, 10, 30, 30, "#6666FF"),  # Blue
    Color(130, 10, 30, 30, "#FFFFFF"), # White
    Color(170, 10, 30, 30, "#000000"), # Black
    Color(10, 50, 30, 30, "#FFAA66"),  # Orange
    Color(50, 50, 30, 30, "#FFFF66"),  # Yellow
    Color(90, 50, 30, 30, "#FF66FF"),  # Pink
    Color(130, 50, 30, 30, "#66FFFF"), # Cyan
    Color(170, 50, 30, 30, "#885555"), # Brown
]

# Setup
def setup():
    # Set current color and eraser color
    global colorEraser, colorCurrent
    colorEraser = g.backgroundColor
    colorCurrent = colors[0].c
    
    # Set options
    size(screenW, screenH)
    noStroke()
    
    # Set palette width and height
    for c in colors:
        if ((c.x + c.w) > palette.w):
            palette.w = c.x + c.w + strokeW
        if ((c.y + c.h) > palette.h):
            palette.h = c.y + c.h + strokeW
    
    # Clear the screen
    clear()

# Draw Loop
def draw():
    pass

# Clear Screen
def clear():
    background(colorEraser)
    drawPalette()
    drawColorCurrent()

# Draw Palette
def drawPalette():
    strokeWeight(strokeW)
    stroke(0)

    # Draw color palette
    for c in colors:
        fill(c.c)
        rect(c.x, c.y, c.w, c.h)
    
    noStroke()
    
# Draw Current Color
def drawColorCurrent():
    strokeWeight(strokeW)
    stroke(0)
    fill(colorCurrent)
    
    # Draw
    rect(screenW - 40, 10, 30, 30)
    noStroke()

# Mouse Release
def mouseReleased():
    global colorCurrent
    
    # Set currently selected color
    for c in colors:
        if (c.isMouseOn()):
            colorCurrent = c.c
            drawColorCurrent()
            break

# Mouse Drag (draw / erase)
def mouseDragged():
    # Draw
    if (mouseButton == LEFT):
        fill(colorCurrent)
        rect(mouseX - 10, mouseY - 10, 20, 20)
    # Erase
    elif (mouseButton == RIGHT):
        fill(colorEraser)
        rect(mouseX - 10, mouseY - 10, 20, 20)
    
    # Only redraw palette when drawn over / erased
    if (mouseX < palette.w + 10) and (mouseY < palette.h + 10):
        drawPalette()

    # Only redraw current color when drawn over / erased
    elif (mouseX > screenW - (50 + strokeW)) and (mouseY < (50 + strokeW)):
        drawColorCurrent()

# Key Release
def keyReleased():
    # Clear the screen
    if (str(key).lower() == 'c'):
        clear()
    # Go Crazy
    elif (str(key).lower() == 'g'):
        goCrazy(int(random(3, 20)))

# Go Crazy
def goCrazy(n):
    if (n > 0):
        strokeWeight(int(random(2, 25)))
        stroke(
            int(random(80, 210)), 
            int(random(80, 210)),
            int(random(80, 210))
        )

        line(
             int(random(-50, screenW + 50)), 0, 
             int(random(-50, screenW + 50)), screenH
        )

        goCrazy(n - 1)
    
    noStroke()
    drawPalette()
    drawColorCurrent()
    
