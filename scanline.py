import time

from graphics import *

window_h=1000
window_w=800
st_y = -6000
en_y = 6000
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


def BressenhamLine(x1,y1,x2,y2,win):
    
    x, y = x1, y1       
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

def PutPixle(win, x, y):
    newx, newy = ConvertPixel(x,y)
    pt = Point(newx,newy)
    time.sleep(0.0005)
    pt.draw(win)



def ScanLine(edge_table, window):
    
    y_current = window_h/2
    active_edge_table = []
    
    for i in range(len(edge_table)):
        if y_current > edge_table[i][1]:
            y_current = edge_table[i][1]
    
    while len(edge_table) != 0 or len(active_edge_table) != 0:
        p = -1
        count_y = 0
        
        for i in range(len(edge_table)):
            if edge_table[i][1] == y_current:
                count_y += 1
                
        for i in range(0, count_y):
            for j in range(len(edge_table)):
                if edge_table[j][1] == y_current:
                    break
            active_edge_table.append(edge_table[j])
            del edge_table[j:j+1]
        
        active_edge_table.sort()
        cnt = 0
        
        for i in range(len(active_edge_table)):
            if active_edge_table[i][3] == y_current:
                cnt += 1
        
        for i in range(0, cnt):
            for j in range(len(active_edge_table)):
                if active_edge_table[j][3] == y_current:
                    break
            del active_edge_table[j:j+1]
        check = True
        
        for i in range(len(active_edge_table)-1):
            xfrom = active_edge_table[i][0]
            xto = active_edge_table[i+1][0]
            
            
            if check == True:
                j = xfrom
                while j <= xto:
                    xx,yy = ConvertPixel(j,y_current)
                    window.plot(xx, yy, "red")
                    j += 1
                check = False
            else:
                check = True
        
        y_current += 1
        
        for i in range(len(active_edge_table)):
            active_edge_table[i][0] += active_edge_table[i][4]

def ScanLineClass(edge_list, window):
    
    global st_y
    global en_y
    edge_list.sort(key=lambda x:x[0])
    n = len(edge_list)

    for i in range(n):
        if edge_list[i][1] in uni_map:
            edge_list[i][1]=edge_list[i][1]-1 

    for y in range(st_y,en_y+1):
        int_points = []
        # print("Int points",int_points)
        for i in range(n):
            if y>=edge_list[i][0] and y <= edge_list[i][1]:
                int_points.append([edge_list[i][2],y])
                print("points",edge_list[i][2],y)
                edge_list[i][2]+=edge_list[i][3]

        int_points.sort(key=lambda x:x[0])
        # print(int_points)
        for i in range(0,(len(int_points)-1),2):
            BressenhamLine(int_points[i][0],int_points[i][1],int_points[i+1][0],int_points[i+1][1],window)
            print(int_points[i][0],int_points[i][1],int_points[i+1][0],int_points[i+1][1])


def main():
    global st_y
    global en_y
    option = int(input("Enter 1 for Edgelist and Active Edgelist ScanLine and \nEnter 2 for Edgelist ScanLine Algorithm \n"))
    print("Enter no. of sides in polygon:")
    s = int(input("Enter sides:"))
    print("Enter the points:")
    points = []
    for i in range(s):
        print("enter x coordinate of point-", i+1, ":")
        x = int(input())
        print("enter y coordinate of point-", i+1, ":")
        y = int(input())
        a = [x, y]
        points.append(a)


    window = GraphWin("ScanLine_POLYGON Filling", window_w,window_h)
    window.setBackground("gray")


    edge_table = [] 
    edge_list = []
    global uni_map
    uni_map = {}
    
    for i in range(s):
        x1 = points[i][0]
        y1 = points[i][1]
        x2 = points[(i+1)%s][0]
        y2 = points[(i+1)%s][1]
        if y2-y1 != 0:
            if y1 > y2:
                y1, y2 = y2, y1
                x1, x2 = x2, x1
            m = (x2-x1)/(y2-y1)
            
            edge_table.append([x1, y1, x2, y2, m])
            edge_list.append([min(y1,y2),max(y1,y2),x1 if y1<y2 else x2,m])
            
            st_y = min(st_y,min(y1,y2))
            en_y = max(en_y,max(y1,y2))
            uni_map[min(y1,y2)] = 1

    
        BressenhamLine(x1, y1, x2, y2, window)
    
    if option ==1:
        ScanLine(edge_table,window)
    elif option==2:
        ScanLineClass(edge_list,window)
    
    window.getMouse()
        
if __name__ == "__main__":
    main()

