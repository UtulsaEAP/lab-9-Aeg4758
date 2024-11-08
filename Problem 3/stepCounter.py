def feet_to_steps(user_feet):
   #write your code here
   steps = int(user_feet/2.5)
   return(steps)

if __name__ == '__main__':
    #take input feet steps here
    #store it into the function
    number_of_feet=float(input())
    number_of_steps=feet_to_steps(number_of_feet)
    print(number_of_steps)
    
    
    #print your steps here
    feet_to_steps(5280)