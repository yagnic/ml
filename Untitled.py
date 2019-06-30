
# coding: utf-8

# In[ ]:

games=""
try:
    games=int(input("enter a number of games"))
except:
    print("please enter a integer")
import random
    
for game in range(0,games):
    pick=random.randint(1,25)
    guess=None
    attempts=0
    
    if(pick!=guess):
        try:
            guess=int(input("please enter your number"))
        except:
            print("please enter a valid integer")
    if(guess!=pick):
        attempts+=1
        if(guess>pick):
            print("bro too high")
        else:
            print("dude very low")
    else:
        print("right and you took %s attempts dude",attempts)

    
    


# In[ ]:




# In[ ]:



