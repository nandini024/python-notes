# num=int(input("enter a numebr"))
# if num==0:
#     print("0")
    

# digit_sum=0
# while num>0:
#         last_digit=num%10
#         digit_sum=digit_sum+last_digit
# print(digit_sum)


# num=int(input("enter a value"))
# if num==0:
#     print("enter valid number")
# else:
        
#         f1=0
#         f2=1
#         print(f1)
#         print(f2)
        
#         for i in range(0,num):
#             fib=f1+f2
       
#             f1=f2
#             f2=fib
#             print(fib)


#Write a program that keeps asking the user to enter numbers 
# until they enter a negative number. Use a  while  loop. 
# num=0
# while num>=0:
#     num=int(input("enter the number")) 

# FACTORIAL OF A NUMBER:
# num=int(input("enter the number"))
# if num==0:
#     print("enter the valid number")
# else:
#     fact=1
#     while num>0:
#         fact=fact*num
#         num=num-1
#     print(fact)

# Print all numbers from 1 to 100 that are divisible by 3 and 5 
# using a  for  loop. 
# for i in range(1,101):
#     if i%5==0:
#         print(i,"divisable by 5")
#     elif i%3==0:
#         print(i,"is divisable by 3")



# WHEN GIVEN SINGLE NUMBER IS PRIME OR NOT
# num=10
# for i in range(2,num+1):
#     if num%i==0:
#         print("not prime")
#         break
#     else:
#         print("prime number")

# USING WHILE LOOP:
num=int(input("enter a number"))
if num<=1:
    print(num,"not a prime number")
elif num==2:
    print(num,"prime number")
elif num%2==0:
    print(num,"is not a prime number")

else:
    i=3
    while i*i<=num:
        if num%i==0:
            print("not a prime")
        i=i+1
    print(num,"is a prime number")



    















       
  
    
    
     








