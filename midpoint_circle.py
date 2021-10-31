from graphics import *
import time

window_w = 800
window_h = 800

def eightWaySymmetricPlot(xc,yc,x,y,win):
   
    PutPixle(win,x+xc,y+yc)  
    PutPixle(win,x+xc,-y+yc)  
    PutPixle(win,-x+xc,-y+yc)  
    PutPixle(win,-x+xc,y+yc)  
    PutPixle(win,y+xc,x+yc)  
    PutPixle(win,y+xc,-x+yc)  
    PutPixle(win,-y+xc,-x+yc)  
    PutPixle(win,-y+xc,x+yc)  

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

def midPointCircle(xc,yc,r):
    x = 0
    y=r
    d = 5/float(4)-r

    win = GraphWin('Midpoint Circle drawing Algorithm', window_w, window_h)
    drawAxis(win)
    eightWaySymmetricPlot(xc,yc,x,y,win)
    while x<=y:
        if d<0:
            d =d+2*x+1 
        else:
            d = d+2*(x-y)+1
            y-=1
        x+=1
        eightWaySymmetricPlot(xc,yc,x,y,win)
    win.getMouse()
    win.close()

def PutPixle(win, x, y):
    """ Plot A Pixle In The Windows At Point (x, y) """
    
    newx, newy = convertPixel(x,y)
    print("Converted x and y",newx , newy)
    pt = Point(newx,newy)
    # pt.setFill(color_rgb(50,50,250))
    pt.draw(win)

def main():
    xc = int(input("Enter center X: "))
    yc = int(input("Enter center Y: "))
    r = int(input("Enter Radious r: "))

    midPointCircle(xc,yc,r)

if __name__ == "__main__":
    main()