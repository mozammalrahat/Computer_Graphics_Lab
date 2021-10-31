from graphics import *
import time

window_w = 800
window_h = 800
axis = True
toggle = False
def drawAxis(win):
    
    for i in range(window_h):
        pt = Point(window_w/2,i)
        pt.draw(win)
    for i in range(window_w):
        pt = Point(i,window_h/2)
        pt.draw(win)
def convertPixel(xx,yy):
    xx+=window_w/2
    yy = -yy
    yy+=window_h/2
    return xx,yy

def DDA(x1,y1,x2,y2):
    """ Bresenham Line Drawing Algorithm For All Kind Of Slopes Of Line """
    x, y = x1, y1       
    win = GraphWin('Brasenham Line Drawing Algorithm', window_w, window_h)
    # drawAxis(win)

    if x1==x2 and y1==y2 :
        PutPixle(win,x1,y1)
    
    elif y1==y2:
        if x1<x2:
           while x != x2 :
               PutPixle(win,x,y)
               x+=1
        else:
           while x != x2 :
               PutPixle(win,x,y)
               x-=1
    elif (x1==x2):
        if y1<y2:
            while y!=y2:
                PutPixle(win,x,y)
                y+=1
        else:
            while y!=y2:
                PutPixle(win,x,y)
                y-=1

    else:
        steps = 0
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        slope = dy/float(dx)
        if dx>dy:
            steps = dx
        else:
            steps = dy
           
        
        xIncrement = (x2-x1)/float(steps)
        yIncrement = (y2-y1)/float(steps)
        x=x1
        y=y1
        PutPixle(win,x,y)
        for i in range(steps):
            x+=xIncrement
            y+=yIncrement
            x = round(x)
            y = round(y)
            PutPixle(win,x,y)
            
    PutPixle(win,x2,y2)
    win.getMouse()
    win.close()

def PutPixle(win, x, y):
    """ Plot A Pixle In The Windows At Point (x, y) """
    
    newx, newy = convertPixel(x,y)
    print("Converted x and y",newx , newy)
    pt = Point(newx,newy)
    pt.draw(win)

def main():
    x1 = int(input("Enter Start X: "))
    y1 = int(input("Enter Start Y: "))
    x2 = int(input("Enter End X: "))
    y2 = int(input("Enter End Y: "))

    DDA(x1, y1, x2, y2)

if __name__ == "__main__":
    main()