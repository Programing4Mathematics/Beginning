
# Python program to ask the user for a range and display all the prime numbers in that interval

# take input from the user
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)

"""
output

Enter lower range: 900
Enter upper range: 950
907
911
919
929
937
941
947

"""
