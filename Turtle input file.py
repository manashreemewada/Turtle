import turtle
#imports turtle in python enviornment

s=turtle.getscreen()
#gives the screen for the turtle

tur = turtle.Turtle()
#we have saved the turtle in an object named tur

turtle_file = list(open('turtle.txt').read().rstrip())
#this command will open the file, read it and strip each letter giving back the list form

for t in range(len(turtle_file)):
# this loop will continue untill the last letter in the text file
    
    if turtle_file[t]=='F':
        tur.forward(90)
        #turtle will move forward
        
    elif turtle_file[t]=='L':
        tur.left(90)
        # turtle will move left
        
    elif turtle_file[t]=='R':
        tur.right(90)
        # turtle will move right
        
    else :
        break
        #this will break the loop and turtle will come to an end.
