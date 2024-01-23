#!/usr/bin/env python
# coding: utf-8

# In[42]:


def classes_welcoming_bot():
    #NetTech Welcoming Bot
    #Welcome user
    print('Welcome to NetTech!')
    #ask user its name
    username=input('Enter your name here:')
    #greet user
    print('Hello',username)

    #ask user its phone number
    user_ph_no=input('please enter your phone number here')
    #display user phone number
    print('phone number',user_ph_no)

    #ask user its email id
    user_email_id=input('please enter your email id here')
    #display user email id 
    print('email id:',user_email_id)

    #ask user its preferred course
    user_pref_cou=input('please enter your preferred course here')
    #display users preferred course
    print('preferred course:',user_pref_cou)

    #ask user its preferred location
    user_location=input(' enter your preferred location ')
    if user_location.lower()=='thane':

        print('yes we have classes at thane')
    else:
        print('sorry we only have classes at thane')

def Recomandation_chai_bot():
    #Mumbai's Recomandation chai Bot
    #user Welcome
    print('Welcome to the city of Garma Garm chai | Amchi Mumbai')
    #ask user its name
    user_name=input('please enter your name here:')
    #greet user
    print('Hello',user_name.title())
    #ask user its budget for chai
    user_budget=int(input('please enter your budget for chai here:'))
    #500--> Taj Hotel
    if user_budget>=500:
        print('Go to Taj Hotel')
    #100-500-->Starbucks
    elif user_budget>=100 and user_budget<500:
        print('Go to Starbucks')
    #50-100--> Udipi Hotel
    elif user_budget>=50 and user_budget<100:
        print('Go to Udipi Hotel!')
    #20-50--> Omkar's Cafe
    elif user_budget>=20 and user_budget<50:
        print("Go to Omkar's Cafe!")
    #5-20--> Tapri
    elif user_budget>=5 and user_budget<20:
        print('Go to Tapri | Better than Taj Hotel!') 
    #5< Go back simon!
    else:
        print('Go back Simon!')




def Recomanadation_airport_bot():
    #THANE TO AIRPORT BOT
    #WELCOME USER
    print('Welcome to Travel Recommadation Bot(Mumbai Airport)')
    #ask user its name
    user_name=input('Please enter your name here:')
    #greet user
    print('Hello',user_name.title())
    #ask user its budget
    budget=int(input('Please enter your budget here:'))
    #500> Go by ola 
    if budget>=500:
        print ('Go by ola')
    #100-500--->Go by auto
    elif budget>=100 and budget<500:
        print('Go by auto')
    #50-100--->Go by bus
    elif budget>=50 and budget<100:
        print('Go by bus')
    # 10-50--->Go by train
    elif budget>=10 and budget<50:
        print('Go by train')
    #10< sorry there is no other facility
    else:
        print('sorry there is no other facility')

def India_gk_quiz():
    #NetTech Welcoming Bot
    #Welcome user
    print('Welcome to India GK Quiz')
    user_location=input('what is the national animal of India')

    if user_location.lower()=='tiger':
        print('yes you are correct')
    else:
        print('sorry your answer is incorrect')

def head_tails():
    #Heads & Tails Game
    #user welcme
    print('Welcome to Heads & Tails Game!')
    #ask user heads or tails
    user_choice=input('Please choose heads or tails:')
    #display user choice
    print('you chose:',user_choice.title())
    #coin toss
    import random
    if (random.choice('ht'))=='h':
        coin_toss='Heads'
    else:
        coin_toss='Tails'
    #display coin result
    print('Coin Result:',coin_toss)
    #if user choice is equal to coin toss-->you win!
    if user_choice.lower()==coin_toss.lower():
        print('you win!')
    #else-->you lose!
    else:
        print('you lose!')

def dice_game():
    #Welcme to Dice game
    #user welcome
    print('Welcome to the Dice Game!')
    #ask user to role dice (1-6)
    user_roll=int(input('please enter the number between 2,12:'))
    if user_roll>=2 and user_roll<=12:
        #display user roll
        print('you have choose:',user_roll)
        #Dice rolled
        import random
        dice_rolled=random.randrange(2,13)
        #display result
        print('dice result:',dice_rolled)
        if user_roll==dice_rolled:
            print('you win!')
        else:
            print('you lose!')
    else:
            print('invalid lose!')

def Cube_table():
    #cube table
    #welcome bot
    print('Welcome to the world of Cube!')
    #take 1 number as input from user
    num=int(input('Please enter a number here:'))
    #display cube table
    for i in range (1,num+1):
        print('Cube of',i,'=',i**3)

def Multiplication_table():
    #multiplication table
    #welcome bot
    print('Welcome to the world of Multiplication!')
    #take 1 number as input from user
    num=int(input('Please enter a number here:'))
    #display multiplication table
    for i in range(1,11):
        print(num,'x',i,'=',num*i)


def factorial_table():
    #Factorial table
    #welcome bot
    print('Welcome to the world of Factorial!')
    #take 1 number as input from user
    n=int(input('Please enter a number here:'))
    factorial=1
    if n>=1:
    #display the factorials
        for i in range (1,n+1):
            factorial=factorial*i
        print('factorial of the given number is:',factorial)


def fibonacci_table():
    #fibonacci table
    #welcome bot
    print('Welcome to the world of Fibonacci!')
    #take 1 number as input from user
    num=int(input('Please enter a number here:'))
    n1=0
    n2=1
    #disply the fibonacci sequnce
    for i in range(num):
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3


def password_generator():
    #password generator
    #welcome bot
    print('Welcome to the world of password generator!')
    #ask user to number
    user_number=int(input('enter a number of characters here'))
    #define variables
    import random
    characters='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*<>?/'
    password=''
    #create a loop
    for i in range(user_number):
        password=password+(random.choice(characters))
       #print the password
    print('the password is here:',password)




def countdown():
    from countdown import countdown
    #creat a countdown of 1 minute and 10
    countdown(mins=1, secs=10)
    #create a countdown of 1 minute
    countdown(1)
    #create a countdown of 10 seconds
    countdown(mins=0,secs=10)

def mind_game():
    #mind game

    #welcome user
    import time
    print('welcome to the mind guessing game AI!')
    time.sleep(3)

    #ask user to guess a number
    print(random.randrange)
    print('guess a number from 1-5000')
    time.sleep(3)

    #ask user to double the number
    print('ok now double whichever number you hava guessed')
    time.sleep(3)

    import random
    num=0

    for i in range(4):
       # aks user to add 50 in it
       temp_num=random.randrange(1,100)
       num=num+temp_num
       print('alright! now add',temp_num,'in it!')
       time.sleep(3)

    #ask user to divided the number by 2
    print('okay now divided the number by 2')
    time.sleep(3)

    #ask user to minus the original guess number
    print('finally minus the number which you guessed earliar')
    time.sleep(3)

    #given answer
    print('answer is finding....')
    time.sleep(3)
    print('yes! found it')
    print('Your answer is', num/2)


#importing tkinter library
import tkinter as tk

#creating a main window
window=tk.Tk()

#change title
window.title('Sarita yadav')

#size
window.geometry('730x500')

#Label
tk.Label(window,text='Python Projects',font=('Helvetica',21)).place(x=150,y=30)
tk.Label(window,text='Made by: Sarita Yadav',font=('Helvetica',16,'bold')).place(x=220,y=100)


#button
tk.Button(window,text='Multiplication Table',command=Multiplication_table).place(x=50,y=150,width=200,height=25)
tk.Button(window,text='Classes Welcoming Bot',command=classes_welcoming_bot).place(x=270,y=150,width=200,height=25)
tk.Button(window,text='Recomandation chai Bot',command=Recomandation_chai_bot).place(x=490,y=150,width=200,height=25)
tk.Button(window,text='Recomanadation Airport Bot',command=Recomanadation_airport_bot).place(x=50,y=200,width=200,height=25)
tk.Button(window,text='India Gk Quiz',command=India_gk_quiz).place(x=270,y=200,width=200,height=25)
tk.Button(window,text='Head Tails',command=head_tails).place(x=490,y=200,width=200,height=25)
tk.Button(window,text='Dice Game',command=dice_game).place(x=50,y=250,width=200,height=25)
tk.Button(window,text='Cube Table',command=Cube_table).place(x=270,y=250,width=200,height=25)
tk.Button(window,text='Factorial Table',command=factorial_table).place(x=490,y=250,width=200,height=25)
tk.Button(window,text='Fibonacci Table',command=fibonacci_table).place(x=50,y=300,width=200,height=25)
tk.Button(window,text='Password Generator',command=password_generator).place(x=270,y=300,width=200,height=25)
tk.Button(window,text='Countdown',command=countdown).place(x=490,y=300,width=200,height=25)
tk.Button(window,text='Mind Game',command=mind_game).place(x=50,y=350,width=200,height=25)


#YOU NOT WRITE THESE THEN UI WILL NOT SEEN

window.mainloop()


# In[ ]:





# In[ ]:




