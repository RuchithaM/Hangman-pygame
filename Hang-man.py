import random
import time
import turtle
from collections import Counter
def seperator():
    print("____________________________________________________________________")
def greeting():
    l=list('Welcome to pygame Hang-Man!!')
    print()
    for i in l:
        print(i,end=' ')
        time.sleep(0.10)
   

    turtle.resetscreen()
    turtle.ht()
    
    turtle.Screen().bgcolor("purple")
    turtle.color("purple")
    turtle.setposition(-20,250)
    
    turtle.color("black")
    style=("Courier",15,"italic")
    turtle.write("Hello folks!.. Welcome back",font=style,align='right')
            
def input_user():
    while(True):
        try:
            n=int(input("Please enter number of players:"))
            print()
            break
        except:
            print()
            print("Characters are not allowed")
            continue
    print()
    player_name=[]

    for i in range(1,n+1):
        print("Please enter player name:")
        x=input()
        print()
        player_name.append(x)
    return(player_name)

def output_username(l):
    seperator()
    for i in l:
        print(i)

def question():
    seperator()
    Dictionary=open("Dic.txt","r")
    item=Dictionary.readlines()
    original_word=random.choice(item)
    original_word=original_word.strip('\n') #to remove null characters present in the text file
    return(original_word) 
def grap(chance):
    draw=turtle.Turtle()
    
    turtle.hideturtle()
    draw.speed(10)
    for chances in range(chance+1):
        if chances==1:
            draw.color("purple")
            draw.setpos(10,-50)
            draw.color("black")
            draw.forward(100)
        elif chances==2:
            draw.left(90)
            draw.color("")
            draw.setpos(110,-50)
            draw.color("black")
            draw.forward(300)
        elif chances==3:
            draw.left(90)
            draw.color("purple")
            draw.setpos(110,250)
            draw.color("black")
            draw.forward(100)
        elif chances==4:
            draw.left(-270)
            draw.color("purple")
            draw.setpos(10,250)
            draw.color("black")
            draw.forward(100)
             
        elif chances==5:
            draw.color("purple")
            draw.setposition(-10,125)
            draw.color("black")
            draw.circle(25)
           
        elif chances==6:
            draw.color("purple")
            draw.setposition(10,100)
            draw.color("black")
            draw.right(60)
            draw.fd(50)
        elif chances==7:
            
            draw.setposition(10,100)
            draw.color("black")
            draw.right(-120)
            draw.fd(50)   
        elif chances==8:
            draw.setposition(10,100)
            draw.color("black")
            draw.left(300)
            draw.fd(50)
        elif chances==9:
            draw.color("purple")
            draw.setposition(10,50)
            draw.color("black")
            draw.left(60)
            draw.fd(50)         
        elif chances==10:        
            draw.setposition(10,50)
            draw.color("black")
            draw.left(-120)
            draw.fd(50)
        elif chances==11:           
            
            draw.color("purple")
            draw.setposition(-10,125)
            draw.color("black")
            draw.right(300)
            
            draw.begin_fill()
            draw.color("red")
            draw.circle(25)
            
            draw.end_fill()
            turtle.hideturtle()           
def result(player_name,points):
    print("Name                              Points")
    seperator()
    print()
    for i in range(len(player_name)):
        x=0
        x=len(player_name[i])
        s=' '*(35-x)
        print(player_name[i],s,points[i])
    print()
    points.sort()
    
    print(player_name[points.index(points[0])])
    print('You won the game')
    print('Bye! Try again.')
    
    turtle.ht()
    turtle.color("purple")
    turtle.setposition(200,-200)
    
    turtle.color("black")
    style=("Courier",15,"italic")
    turtle.write(player_name[0],font=style,align='right')
    turtle.setposition(200,-220)
    turtle.write("You won the game!...",font=style,align='right')
    
    
    raise SystemExit
def play(player_name):
    points=[0]*(len(player_name))
    count=1
    turn=1
    p=True
    while(p):
        turn=count%(len(player_name))  
        count=count+1
        seperator()
        print(player_name[turn-1],"it's your turn")
        print()
        p=str(input("Do you want to continue y/n?")).lower()
        if p=='y':
            p=True
        elif p=='n':
            p=False
            print()
            result(player_name,points)
        word=question()
        #print(word)  print the original word
        for i in word: 
              
            print('_', end = ' ')         
        print() 
       
        letterGuessed = ''                 
        chances = 0
        correct = 0
        flag = 0
        try: 
            while(chances != 11 and flag == 0): #flag is updated when the word is correctly guessed  
                print()
                try: 
                    guess = str(input('Enter a letter to guess: ')).lower()
                    print()
                except: 
                    print('Enter only a letter!')
                    continue
                # Validation of the guess 
                if not guess.isalpha(): 
                    print('Enter only a LETTER') 
                    continue
                elif len(guess) > 1: 
                    print('Enter only a SINGLE letter') 
                    continue
                elif guess in letterGuessed: 
                    print('You have already guessed that letter') 
                    continue
                # If letter is guessed correctly 
                if guess in word: 
                    k = word.count(guess) #k stores the number of times the guessed letter occurs in the word 
                    for _ in range(k):     
                        letterGuessed += guess # The guess letter is added as many times as it occurs 
                else:
                    chances+=1
                    print(chances)
                    grap(chances)
                # Print the word 
                for char in word: 
                    if char in letterGuessed and (Counter(letterGuessed) != Counter(word)): 
                        print(char, end = ' ') 
                        correct += 1
                    # If user has guessed all the letters 
                    elif (Counter(letterGuessed) == Counter(word)): # Once the correct word is guessed fully,                                                                     # the game ends, even if chances remain 
                        print("The word is: ", end=' ') 
                        print(word) 
                        flag = 1
                        print('Congratulations, You got it correct!')
                        points[turn]=points[turn]+1
                        break # To break out of the for loop 
                        break # To break out of the while loop 
                    else: 
                        print('_', end = ' ') 
            # If user has used all of his chances 
            if chances >11 and (Counter(letterGuessed) != Counter(word)): 
                print() 
                print('You lost! Try again..') 
                print('The word was: '.word)            
            turtle.resetscreen()   
        except KeyboardInterrupt:
            raise SystemExit
turtle.resetscreen()
turtle.color("white")
greeting()


player_name=input_user() 
play(player_name)