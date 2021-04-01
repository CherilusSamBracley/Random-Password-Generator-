#Cherilus Sam Bracley
#cherilussambracley@gmail.com


#Random Password Generator

import random
import time

USER_CHARACTERS = input("Insert your character(s) in the order to have the password...")

#INTERVAL= PROCESS_THREE[0:8]


x= input("Insert the first step for password len (only one number [RECOMANDED (0) THE FIRST ONE])")
y= input("Insert the last step for your password len (only one number) [RECOMANDED (WHAT YOU WANT )]")

a= int(x)
b= int(y)



OPERATION_ONE = USER_CHARACTERS[a:b]



PROCESS_ONE =list(OPERATION_ONE)

PROCESS_TWO =list(str(OPERATION_ONE.__hash__()))

PROCESS_THREE = PROCESS_ONE + PROCESS_TWO 

print("You will have a pasword which will have "+ str (len (PROCESS_THREE)) + " characters")

print("\n _______________WAITING FOR 5 SECONDS___________")

time.sleep(5)




def JoinToString(s):
    str1=" "

    return (str1.join(s))


FINAL_VALUE = JoinToString(PROCESS_THREE)
print(FINAL_VALUE)


"""

PAY ATTENTION TO THAT 


ATTENTION

This is not a secure script that you can use to protect your account
This is just a script that takes a part of the user input and add it to the hash of this user input
According to me the final result is not secure enough for security purpose 
                            @Cherilus Sam Bracley

"""











