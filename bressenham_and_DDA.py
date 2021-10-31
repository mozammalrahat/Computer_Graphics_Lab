from graphics import *
import time

window_w = 1200
window_h = 800

def DrawAxis(win):
    
    for i in range(window_h):
        pt = Point(window_w/2,i)
        pt.draw(win)
    for i in range(window_w):
        pt = Point(i,window_h/2)
        pt.draw(win)

def ConvertPixel(xx,yy):
    xx+=window_w/2
    yy = -yy
    yy+=window_h/2
    return xx,yy

def DDA(x1,y1,x2,y2):
    x, y = x1, y1       
    win = GraphWin('DDA Line Drawing Algorithm', window_w, window_h)
    DrawAxis(win)

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


def BresenhamLine(x1,y1,x2,y2):
    
    x, y = x1, y1       
    win = GraphWin('Brasenham Line Drawing Algorithm', window_w, window_h)
    DrawAxis(win)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
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
    elif dy<dx:
        xIncrement = 0
        yIncrement = 0
        if x1<x2:
            xIncrement = 1
        else:
            xIncrement = -1
        if y1<y2:
            yIncrement = 1
        else:
            yIncrement = -1
        
        p = 2*dy-dx
        while x != x2:
            if p>0:
                p=p+2*(dy-dx)
                y+=yIncrement
            else:
                p = p+2*dy
            x+=xIncrement
            PutPixle(win,x,y)
    else:
        xIncrement = 0
        yIncrement = 0
        if x1<x2:
            xIncrement = 1
        else:
            xIncrement = -1
        if y1<y2:
            yIncrement = 1
        else:
            yIncrement = -1
        
        p = 2*dx-dy
        while y != y2:
            if p>0:
                p=p+2*(dx-dy)
                x+=xIncrement
            else:
                p = p+2*dx
            y+=yIncrement
            PutPixle(win,x,y)

    PutPixle(win,x2,y2)
    win.getMouse()
    win.close()

def PutPixle(win, x, y):
    x, y = ConvertPixel(x,y)
    pt = Point(x,y)
    pt.draw(win)

def main():
    x1 = int(input("Enter Start X: "))
    y1 = int(input("Enter Start Y: "))
    x2 = int(input("Enter End X: "))
    y2 = int(input("Enter End Y: "))
    option = int(input("Enter 1 for BressenhamLine Drawing Algorithm or 2 for DDA \n"))
    
    if option==1:
        BresenhamLine(x1, y1, x2, y2)
    elif option==2:
        DDA(x1,y1,x2,y2)

if __name__ == "__main__":
    main()