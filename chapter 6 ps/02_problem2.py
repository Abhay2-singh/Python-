#write a programme to find out the wherther  a student  has passed or failed it is reqiure the a total 40% and least 33% in each 
mark1=int(input("enter the marks="))
mark2=int(input("enter the marks="))
mark3=int(input("enter the marks="))
total_percenatge=(mark1+mark2+mark3)*100/300
print(total_percenatge)
if(total_percenatge>40 and mark1>33 and mark2>33 and mark3>33):
    print("you are pass",total_percenatge)
else:
    print("you are fail")
    print("try again next year")