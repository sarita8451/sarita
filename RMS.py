#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:


#Resturant Management System

class RMS: 
    
    def __init__(self,restaurant_name,restaurant_menu):
        
        self.restaurant_name=restaurant_name
        self.total_bill=0
        self.menu=restaurant_menu
        self.user_order=' '
        

    #Welcome user
    def welcome_user(self):
        return(f'Welcome to {self.restaurant_name.title()}!')
    
    #Display Menu    
    def display_menu(self):
        print('*'*30)
        print('Menu:') 
        
        for i in self.menu:
            print (i.title(),self.menu[i])
        print('*'*30)

    #Take Order   
    def take_order(self):
        self.user_order=input('Please place your order here:')

    #Prepare Order  
    def preparing_order(self):
        import time
        print('Preparing your order')
        time.sleep(0.3)
        self.total_bill=self.total_bill+self.menu[self.user_order.lower()]
        user_order_li.append(user_order)
        
    #Serve Order    
    def serve_order(self):
        print('Your order is done!')
       

    #Display Bill 
    def display_bill(self): 


        print('Your total bill:',self.total_bill)

    #Verify Bill
    def verify_bill(self):

        self.user_paid=int(input('Please pay your bill here:'))
        while self.user_paid<self.total_bill:
            self.total_bill=self.total_bill-self.user_paid
            print('Payment failed! please pay remaining:{self.total_bill}')
            self.user_paid=int(input('please pay your bill here:'))

        if self.user_paid>self.total_bill:

            print('here is your change:',self.user_paid-self.total_bill)
        else:
            pass
    #Thank You
    def thank_user(self):
        print(f'Thank you for visiting{self.restaurant_name.title()}!')

    def order_process(self):
        self.take_order()
        if self.user_order.lower() in self.menu:
            self.preparing_order()
            self.serve_order()
            self.ask_user=input('Would you like to order again?')
            while self.ask_user.lower()=='yes':
                self.repeat_order()
                self.ask_user=input('Would you like to order again?')

            self.display_bill()
            self.verify_bill()
            self.thank_user()
        else:
            print('Invalid Order!')
            self.order_process()

    def repeat_order(self):
        self.display_menu()
        self.take_order()
        if self.user_order.lower() in self.menu:
            self.preparing_order()
            self.serve_order()
        else:
            print('Invalid Order!')
            self.repeat_order()

if __name__=='__main__':
    user_input_file=open('user input.txt')
        
    user_input_li=user_input_file.readlines()
        
    rn=user_input_li[0].replace('\n','')
     
    food_items=user_input_li[1].replace('\n','').split(',')
        
    food_prices=[]
    for i in user_input_li[2].split(','):
        food_prices.append(int(i))
            
    rm=dict(zip(food_items,food_prices))
    restaurant=RMS(restaurant_name=rn,restaurant_menu=rm)
        
        
    #importing tkinter library
    import tkinter as tk

    #creating a main window
    window=tk.Tk()

    #change title
    window.title(rn)

    #size
    window.geometry('400x400')

    #Label
    tk.Label(window,text=restaurant.welcome_user(),font=('Helvetica',16)).pack(pady=30)

    #button
    tk.Button(window,text='MENU',command=restaurant.display_menu,width=15).pack(pady=40)
    tk.Button(window,text='START ORDER',command=restaurant.order_process,width=15).pack(pady=50)                                                                        

    window.mainloop()



# In[ ]:





# In[ ]:




