import random
from turtle import Screen, Turtle

#creating our base grid
 #counter 
c=0
charging_station = []

GRID_SIZE = 600

sub_divisions = 20

cell_size = GRID_SIZE / float(sub_divisions)  # force float for Python 2

screen = Screen()

turtle = Turtle()

turtle.speed(0)
#turtle.color("white")
turtle.penup()
turtle.goto(-GRID_SIZE/2, GRID_SIZE/2)
turtle.pendown()

angle = 90

for _ in range(4):
    turtle.forward(GRID_SIZE)
    turtle.right(angle)

for _ in range(2):
    for _ in range(1, sub_divisions):
        turtle.forward(cell_size)
        ran= (random.uniform(0, 1))
        if ran<0.4:
            turtle.dot(15, "orange")
        turtle.right(angle)
        for _ in range (20):
            turtle.forward(cell_size)
            c=c+1
            #placing random chargers at 3% probability
            ran= (random.uniform(0, 1))
            if ran<0.2:
                turtle.dot(15, "orange")
                charging_station.append(turtle.position())
            if c==20:
                turtle.left(angle)
                c=0
        angle = -angle

    turtle.forward(cell_size)
    turtle.right(angle)

charging_station.append((0,0))
#print(charging_station)

currentX= -GRID_SIZE/2
currentY = GRID_SIZE/2

#making the turtle move
#new turtle turtle
turtle.color("blue")
turtle.width(5)
turtle.speed(2)
turtle.penup()
turtle.goto(currentX, currentY)
turtle.pendown()

while(turtle.position()!=(0,0)):

    
    #testing.py creates array for distances 
    arr = charging_station
    
    arrY = [y for x, y in arr]
    arrX = [x for x, y in arr]
    new_arrX = []
    new_arrY = []
    distances= []
    length = len(arrX)
    for i in range(length):
        if (arrX[i]>=currentX) and (arrY[i]<=currentY):
            new_arrX.append(arrX[i])
            new_arrY.append(arrY[i])
            

    newLength =len(new_arrX)
    #print (arrY)
    for j in range(newLength):
        d = (((currentX-new_arrX[j])**2)+((currentY-new_arrY[j])**2))**0.5 
        distances.append(d)

    #print(distances)
    newDistances=[]

    for k in distances:
        if k<=250:
            newDistances.append(k)
    print (newDistances)        
    maxi = max(newDistances)
    print (newDistances)
    print (maxi)


    #creating dictionary to match distances to x,y coordinates
    dictX = dict(map(lambda i,j: (i,j) , newDistances,new_arrX))
    dictY = dict(map(lambda i,j: (i,j) , newDistances,new_arrY))
    #print (dictX)
    #print(dictY)

    print(dictX[maxi], dictY[maxi])

   
    #start at 
    
    turtle.setheading(turtle.towards(dictX[maxi],dictY[maxi] ))
    turtle.forward(maxi)  
    
    currentX = dictX[maxi]
    currentY = dictY[maxi]
    newDistances = distances






screen.exitonclick()



