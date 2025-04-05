# num = int(input("enter any number:"))
# for i in range(num):
#      for j in range(num):
#       if(i>=j):
#          print("*",end="");
#      else:
#              print("");
         
       
num = int(input("enter any number:"))
for i in range(num):
    for j in range(num):
        if(j>=num-1):
            print("*",end="");
    else:
        print(" ");


   

