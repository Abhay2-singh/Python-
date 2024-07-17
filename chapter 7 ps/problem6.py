# #write a programme to print the following the pattern for n=3
#   *
#  ***
# *****
n=int(input("enter the number="))
for i in range(1,n+1):
  print(" "*(n-i),end="")
  print("*"*(2*i-1),end="")
  print("")