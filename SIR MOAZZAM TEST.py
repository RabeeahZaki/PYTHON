#TO PRINT ALL ODD NO IN A LIST
odd_no=[]
while True:
    i=int(input("enter no:"))
    if (i%2 == 0):
     print(i," is not odd")
    else:
     odd_no.append(i)
    print("ODD_NO",odd_no)
    i+=1
#TO FIND SUM OF LIST ELEMENTS
Sum=0
odd_no=[]
while True:
    i=int(input("enter no:"))
    if (i%2 == 0):
     print(i," is not odd")
    else:
     odd_no.append(i)
    print("ODD_NO",odd_no)
    Sum+=i
    print("SUM",Sum)
    i+=1
#TO REVERSE  A LIST IN TWO WAYS
a=[1,2,3,4,5,6,7,8,9]
print("TO REVERSE  A LIST IN TWO WAYS")
print("1st METHOD")
for a in range(9,0,-1):
 print(a)
print("2nd method")
i=9
while i>=1:
    print(i)
    i-=1
#to find the top two maximum numbers in a list
a = [1,2,3,4,6,7,99,88,999]
print("to find the top two maximum numbers in a list")
a.sort(reverse = True)
print(a[0],a[1])
# #to sort characters in descending order
a = [1,2,3,4,6,7,99,88,999]
print("to sort characters in descending order")
a.sort(reverse = True)
print(a[:])
#to find the second highest number in an integer list
a = [1,2,3,4,6,7,99,88,999]
print("to find the second highest number in an integer list")
a.sort(reverse = True)
print(a[1])
#to remove repeated characters from a string.
string="geeksforgeeks"
p=""
for i in string:
	if i not in p:
		p=p+i
print(p)
k=list("geeksforgeeks")
print(k)
#to check if a given character is a vowel or consonant.
string=input("Enter charcter:")
if(string=='a' or string=='e' or string=='i' or string=='o'or string=='u'):
    print(string)
else:
    print(string,"is a consonant")
Python Program to calculate factorial.
a=int(input("enter no:"))
fact=1
for i in range(1,a+1):
     fact*=i
print("the factorial of",a,"is",fact)
#Python Program to merge two lists
list_1=[1,2,3,4,5]
list_2=[6,7,8,9,10]
for i in list_2:
    list_1.append(i)
# print(list_1)
