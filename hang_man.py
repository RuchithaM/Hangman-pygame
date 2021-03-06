# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:43:09 2020

@author: ruchi
"""

import random
import time
from collections import Counter

def seperator():
    print("-----------------------------------------")

def greeting():
    l=list('Welcome to pygame Hang-Man!!')
    print()
    for i in l:
        print(i,end=' ')
        time.sleep(0.25)
    

    
    

def input_user():
    while(True):#no of players
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

#print the user names
def output_username(l):
    seperator()
    for i in l:
        print(i)

#choose word , jumbled it return both jumbled_word and original_word with length of original_word required for printing datshes   
def question(): #generate the jumbled sequence and return the same
    seperator()
    Dictionary=open("Dic.txt","r")
    item=Dictionary.readlines()
    original_word=random.choice(item) #select one word and jumble it
    original_word=original_word.strip('\n') #to remove null characters present in the text file
    
    return(original_word) 

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
        p=str(input("Do you want to continue y/n")).lower()
        if p=='y':
            p=True
        elif p=='n':
            p=False
            print()
            result(player_name,points)
                
            
        
        word=question()
        print(word)
        for i in word: 
             # For printing the empty spaces for letters of the word 
            print('_', end = ' ')         
        print() 
        
        
        
        
        
         # list for storing the letters guessed by the player 
        letterGuessed = ''                 
        chances = 13
        correct = 0
        flag = 0
        try: 
            while (chances != 0) and flag == 0: #flag is updated when the word is correctly guessed  
                print()
                chances -= 1
                try: 
                    try: 
                        guess = str(input('Enter a letter to guess: '))
                        print()
                    except: 
                        print('Enter only a letter!')
                        continue
                except KeyboardInterrupt: #problem with this 
                    chances=0
                    raise SystemExit
                    
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
      
                # Print the word 
                for char in word: 
                    if char in letterGuessed and (Counter(letterGuessed) != Counter(word)): 
                        print(char, end = ' ') 
                        correct += 1
                    # If user has guessed all the letters 
                    elif (Counter(letterGuessed) == Counter(word)): # Once the correct word is guessed fully,  
                                                                    # the game ends, even if chances remain 
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
            if chances <= 0 and (Counter(letterGuessed) != Counter(word)): 
                print() 
                print('You lost! Try again..') 
                print('The word was {}'.format(word))
                points[turn]=points[turn]+0
                print(points[turn])
            
      
        except KeyboardInterrupt:
            raise SystemExit
             
            
            
                
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
    max_p=max(points)
    ind = points.index(max_p)
    print(player_name[ind],'You won the game')
    
    
    
    
    print('Bye! Try again.')
    raise SystemExit

greeting()
player_name=input_user() 
play(player_name)
