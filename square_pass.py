from graphics import *

window_w = 1200
window_h = 800
points=[]

def ConvertPixel(xx,yy):
    xx+=window_w/2
    yy = -yy
    yy+=window_h/2
    return xx,yy

def BresenhamLine(x1,y1,x2,y2,win,color=None):
    
    x, y = x1, y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if x1==x2 and y1==y2 :
        PutPixle(win,x,y,color=color)
        
    elif y1==y2:
        if x1<x2:
           while x != x2 :
            PutPixle(win,x,y,color=color)
            x+=1
        else:
           while x != x2 :
            PutPixle(win,x,y,color=color)
            x-=1
               
    elif (x1==x2):
        if y1<y2:
            while y!=y2:
                PutPixle(win,x,y,color=color)
                y+=1
        else:
            while y!=y2:
                PutPixle(win,x,y,color=color)
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
            PutPixle(win,x,y,color=color)
            
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
            PutPixle(win,x,y,color=color)
            
    PutPixle(win,x2,y2,color=color)
    
def PutPixle(win, x, y,color=None):
    
    converted_x, converted_y = ConvertPixel(x,y)
    
    if points[int(converted_x)][int(converted_y)]=='yellow':
        message_x, message_y = ConvertPixel(0,250)
        output = Text(Point(message_x,message_y),"You Failed!!\nClick To Close Window")
        output.setOutline('black')
        output.setStyle('bold')
        output.setSize(36)
        output.draw(win)
        win.getMouse()
        win.close()
        
    if color=='grey':
        points[int(converted_x)][int(converted_y)]='blue'
    elif color!=None:
        points[int(converted_x)][int(converted_y)]=color
    else:
        points[int(converted_x)][int(converted_y)]="bc"
    
    pt = Point(converted_x,converted_y)
    
    if color !=None:
        pt.setFill(color)
    pt.draw(win)


def flood_fill(seed_point,window):
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
                pt=Point(x,y+1)
                if(points[x][y+1]==oc and points[x][y+1]!=fc):
                    lis.append(pt)
                pt=Point(x+1,y)
                if(points[x+1][y]==oc and points[x+1][y]!=fc):
                    lis.append(pt)
                pt=Point(x-1,y)
                if(points[x-1][y]==oc and points[x-1][y]!=fc):
                    lis.append(pt)
                pt=Point(x,y-1)
                if(points[x][y-1]==oc and points[x][y-1]!=fc):
                    lis.append(pt)

def move_object(ll,lr,ul,ur,window):
    
    while True:
        
        key = window.getKey()
        
        absolute_half_width = window_w/2
        absolute_half_height = window_h/2
                            
        if key=='Right':
            
            step = 20
            if abs(lr[0])+step>absolute_half_width:
                continue
            
            for i in range(step):
                BresenhamLine(ll[0]+i,ll[1],ul[0]+i,ul[1],window,color='grey')
            
            BresenhamLine(ll[0]+step,ll[1],ul[0]+step,ul[1],window,color='black')
            ll[0]+=step
            ul[0]+=step
            
            BresenhamLine(lr[0],lr[1]+1,ur[0],ur[1]-1,window,color='red')
            BresenhamLine(lr[0]+step,lr[1],ur[0]+step,ur[1],window,color='black')
            lr[0]=lr[0]+step
            ur[0] = ur[0]+step
            BresenhamLine(ul[0],ul[1],ur[0],ur[1],window,color='black')
            BresenhamLine(ll[0],ll[1],lr[0],lr[1],window,color='black')
            xxx,yyy = ConvertPixel(lr[0]-2,lr[1]+2)
            flood_fill(Point(xxx,yyy),window)
            BresenhamLine(ul[0],ul[1],ur[0],ur[1],window,color='black')
            
        elif key=="Left":
            step = -20
            if abs(ll[0])+abs(step)>absolute_half_width:
                continue
            
            for i in range(abs(step)):
                BresenhamLine(lr[0]-i,lr[1],ur[0]-i,ur[1],window,color='grey')
                
            BresenhamLine(lr[0]+step,lr[1],ur[0]+step,ur[1],window,color='black')
            
            lr[0]+=step
            ur[0]+=step
            
            BresenhamLine(ll[0],ll[1]+1,ul[0],ul[1]-1,window,color='red')
            BresenhamLine(ll[0]+step,ll[1],ul[0]+step,ul[1],window,color='black')
            ll[0]=ll[0]+step
            ul[0] = ul[0]+step
            BresenhamLine(ul[0],ul[1],ur[0],ur[1],window,color='black')
            BresenhamLine(ll[0],ll[1],lr[0],lr[1],window,color='black')
            xxx,yyy = ConvertPixel(ll[0]+2,ll[1]+2)
            flood_fill(Point(xxx,yyy),window)
            BresenhamLine(ul[0],ul[1],ur[0],ur[1],window,color='black')
            BresenhamLine(ll[0],ll[1],ul[0],ul[1],window,color='black')
            
        elif key=='Up':
            step = 20
            if abs(ul[1])+step>absolute_half_height:
                continue
            
            for i in range(step):
                BresenhamLine(ll[0],ll[1]+i,lr[0],lr[1]+i,window,color='grey')
                
            BresenhamLine(ll[0],ll[1]+step,lr[0],lr[1]+step,window,color='black')
            ll[1]+=step
            lr[1]+=step
            
            BresenhamLine(ul[0]+1,ul[1],ur[0]-1,ur[1],window,color='red')
            BresenhamLine(ul[0],ul[1]+step,ur[0],ur[1]+step,window,color='black')
            ur[1]=ur[1]+step
            ul[1] = ul[1]+step
            BresenhamLine(ul[0],ul[1],ll[0],ll[1],window,color='black')
            BresenhamLine(ur[0],ur[1],lr[0],lr[1],window,color='black')
            xxx,yyy = ConvertPixel(ur[0]-2,ur[1]-2)
            flood_fill(Point(xxx,yyy),window)
            BresenhamLine(ul[0],ul[1],ll[0],ll[1],window,color='black')
            BresenhamLine(ur[0],ur[1],lr[0],lr[1],window,color='black')
            
        elif key=='Down':
            step = -20
            if abs(lr[1])+abs(step)>absolute_half_height:
                continue
            
            for i in range(abs(step)):
                BresenhamLine(ul[0],ul[1]-i,ur[0],ur[1]-i,window,color='grey')
                
            BresenhamLine(ul[0],ul[1]+step,ur[0],ur[1]+step,window,color='black')
            ul[1]+=step
            ur[1]+=step
            
            BresenhamLine(ll[0]+1,ll[1],lr[0]-1,lr[1],window,color='red')
            BresenhamLine(ll[0],ll[1]+step,lr[0],lr[1]+step,window,color='black')
            ll[1]=ll[1]+step
            lr[1] = lr[1]+step
            BresenhamLine(ul[0],ul[1],ll[0],ll[1],window,color='black')
            BresenhamLine(ur[0],ur[1],lr[0],lr[1],window,color='black')
            xxx,yyy = ConvertPixel(lr[0]-2,lr[1]+2)
            flood_fill(Point(xxx,yyy),window)
            BresenhamLine(ul[0],ul[1],ll[0],ll[1],window,color='black')
            BresenhamLine(ur[0],ur[1],lr[0],lr[1],window,color='black')
        else:
            continue
        
def square_pass():
    for i in range(window_w):
        points.append([])
        for j in range(window_h):
            points[i].append("blue")
            
    ll = [-250,-250]
    lr = [-150,-250]
    ur = [-150,-150]
    ul = [-250,-150]
    po=[ll,lr,ur,ul]        
    s = 4   
    
    straightline1 = [[0,5],[400,5]]
    straightline2 = [[0,120],[400,120]]
    
    window=GraphWin("SQUARE PASS\nFirst Fill The Square(Click Inside The Square) And Pass The Square Through the Yellow Lines",window_w,window_h,autoflush=False)
    window.setBackground("grey")
    
    for i in range(s):
            x1 = po[i][0]
            y1 = po[i][1]
            x2 = po[(i+1)%s][0]
            y2 = po[(i+1)%s][1]
            BresenhamLine(x1,y1,x2,y2,window)
    
    BresenhamLine(straightline1[0][0],straightline1[0][1],straightline1[1][0],straightline1[1][1],window,color='yellow')
    BresenhamLine(straightline1[0][0],straightline1[0][1]+1,straightline1[1][0],straightline1[1][1]+1,window,color='yellow')
    BresenhamLine(straightline2[0][0],straightline2[0][1],straightline2[1][0],straightline2[1][1],window,color='yellow')
    BresenhamLine(straightline2[0][0],straightline2[0][1]-1,straightline2[1][0],straightline2[1][1]-1,window,color='yellow')      
    
        
    
    seed_point=(window.getMouse())
    seed_x = seed_point.getX()
    seed_y = seed_point.getY()
    
    converted_llx, converted_lly = ConvertPixel(ll[0],ll[1])
    converted_urx,converted_ury = ConvertPixel(ur[0],ur[1])
    
    while True:
        if (seed_x>converted_llx and seed_x<converted_urx) and (seed_y<converted_lly and seed_y>converted_ury):
            break
        else:
            seed_point=(window.getMouse())
            seed_x = seed_point.getX()
            seed_y = seed_point.getY()
            continue
        
    window.autoflush=True
    
    flood_fill(seed_point,window)
    
    window.autoflush=False
    move_object(ll,lr,ul,ur,window)
    
    window.getMouse()
    window.close()

def main():
    square_pass()
    
if __name__ == "__main__":
    main()
