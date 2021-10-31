from bressenham_and_DDA import main
from graphics import *

window_w = 800
window_h = 800
points=[]
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

def BresenhamLine(x1,y1,x2,y2,win):
    
    x, y = x1, y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if x1==x2 and y1==y2 :
        PutPixle(win,x,y)
        
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
    
def PutPixle(win, x, y):
    newx, newy = ConvertPixel(x,y)
    points[int(newx)][int(newy)]="bc"
    print(newx,newy)
    pt = Point(newx,newy)
    pt.draw(win)


def flood_fill(window):
	print("Click anywhere inside the polgon to fill it::\n")
	seed_point=(window.getMouse())
	lis=[]
	lis.append(seed_point)
	fc="fc"
	oc="blue"
	while(len(lis)!=0):
            pt=lis[len(lis)-1]
            lis.pop()
            x = int(pt.getX())
            y = int(pt.getY())
            if(points[x][y]!=fc and points[x][y]==oc):
                window.plot(x,y,"red")
                points[x][y]=fc
                pt=Point(x+1,y)
                if(points[x+1][y]==oc and points[x+1][y]!=fc):
                    lis.append(pt)
                pt=Point(x,y+1)
                if(points[x][y+1]==oc and points[x][y+1]!=fc):
                    lis.append(pt)
                pt=Point(x-1,y)
                if(points[x-1][y]==oc and points[x-1][y]!=fc):
                    lis.append(pt)
                pt=Point(x,y-1)
                if(points[x][y-1]==oc and points[x][y-1]!=fc):
                    lis.append(pt)


def FloodFillInit():
    for i in range(window_w):
        points.append([])
        for j in range(window_h):
            points[i].append("blue")
      
    print("Enter no. of sides in polygon:")
    s=int(input("Enter sides:"))
    print("Enter the points:")
    po=[]
    for i in range(s):
            print("enter x coordinate of point-",i+1,":")
            x=int(input())
            print("enter y coordinate of point-",i+1,":")
            y=int(input())
            a=[x,y]
            po.append(a)
        
        
    window=GraphWin("Flood Fill Polygon Filling Algorithm",window_w,window_h)
    window.setBackground("blue")
    DrawAxis(window)
    for i in range(s):
            x1 = po[i][0]
            y1 = po[i][1]
            x2 = po[(i+1)%s][0]
            y2 = po[(i+1)%s][1]
            BresenhamLine(x1,y1,x2,y2,window)
            
    flood_fill(window)
    window.getMouse()
    window.close()

def main():
    FloodFillInit()
    FloodFillInit()

if __name__ == "__main__":
    main()
