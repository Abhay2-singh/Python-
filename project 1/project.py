#snake,water,gun game
import random
'''
1 for snake
-1 for water 
0 for gun
'''
print("welcome to snake water game ")
computer=random.choice([-1,0,1])
youstr=(input("enter your choice:" ))
youdict={"s":1,"w":-1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}
you=youdict[youstr]
print(f"you choose {reversedict[you]}\ncomputer choose{reversedict[computer]}")
if(computer==you):
    print("its a draw match")
else:
  if(computer==-1 and you==1):
    print("you are winner")
  elif(computer==-1 and you==0):
    print("you lose!")

  elif(computer==1 and you==-1):
    print("you lose!")
  elif(computer==-1 and you==1):
    print("you are winner")
  elif(computer==1 and you==0):
    print("you are winner!")
  elif(computer==0 and you==-1):
    print("you are winner")
  elif(computer==0 and you==1):
    print("you lose!")
  else:
    print("something is wrong")
  




