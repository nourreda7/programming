x,y,z=1,2.8,2j
print(type(x))
print(type(y))
print(type(z))
a=float(x)
b=int(y)
c=complex(x)
# boolean
print(bool(False))#false
print(bool(None))#false
print(bool(0))#false
print(bool(""))#false
print(bool(()))#false
print(bool([]))#false
print(bool({}))#false
# String
String1 = 'Welcome to the python World'
print(String1) 
print("................") 
String1 = "I'm a Python developer"
print(String1) 
#  slicing in string
a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H", "J"))
print(a.split(",")) 
# comparision between floating & integers Divison
print(5/5)#1.0
print(10/2) #5.0
print(-10/2) #-5.0
print(20.0/2)#10.0

print(5//5)#-->1
print(10//2) #-->5
print(-10//2) #-->-5
print(20.0//2)#-->10a = 13
# Comparision operators
a=13
b = 33
print(a > b) #False
print(a < b)#True
print(a == b)#False
print(a != b)#True
print(a >= b)#False
print(a <= b) #True
# Python program to illustrate short hand
i = 10
if i < 15: print("i is less than 15")

X= 10
print(True) if X< 15 else print(False)

a, b = 10, 20
min = a if a < b else b
print(min) #10
# Example: Python while Loop
#  (Calculate the sum of numbers until user enters 0)
 
num=int(input("Enter a Number: "))
sum=0 
while (num!=0) :
     sum+=num
     num=int(input("Enter a Number: "))
     if num==0 :
         break
print(f'sum is equal : {sum}')        
#                                                             (Lists & Tuples)

list1 = ["apple","banana","cherry"]
print(list1[0], " ",list1[1]," ",list1[-1])  # "cherry"

# slicing
list1 = [10,20,30,40,50,60,70,80,90,100]
print(list1 [::])
print(list1 [2:])
print(list1 [:7])
print(list1 [2:7])
print(list1 [2:7:2])
print(list1 [-6:-2])
print(list1 [-6:-2:2])
print(list1 [-6:-2:-2])
print(list1 [-6:])

list1 = [1,2,3,4,5,6]
list1[1:3] = [10,20]
print(list1)  # [1, 10, 20, 4, 5, 6]
list1[1:3] = [100]
print(list1)   # [1, 100, 4, 5, 6]

# Add list Items
list1 = [1,2,3,4,5,6]
list1.insert(1 , 100)
print(list1)  # [1,100,2,3,4,5,6]

list2 = [4,5,6]
list1.extend(list2)
print(list1)

list1 = [1,2,3]
list2 = [4,5,6]
list1.append(list2)
print(list1)

#  Remove list items
list1 = [1, 2, 3 ,2 , 4 ]
list1.remove(2)
print(list1)  # [1,3,2,4]

list1 = [1, 5, 3 ,2 , 4 ]
list1.pop() # Remove the last item but if you give it a number in the list will delete the number after the number given
print(list1)  # [1,2,3,2]

list1 = [1,2,3]
list1.clear() # Remove all items in the list
print(list1) #[]

# sort the list
list1 =[2,5,3,4]
list1.sort()
print(list1)  # [2, 3, 4, 5]
x = ("apple","banana","cherry")
y=list(x)
y[1] ="kiwi"
x =tuple(y)
print(x) #('apple', 'kiwi', 'cherry')

tuple1 = (10,20,30,40,50,60,70,80,90,100)
print(tuple1 [::])
print(tuple1 [2:])
print(tuple1 [:7])
print(tuple1 [2:7])
print(tuple1 [2:7:2])
print(tuple1 [-6:-2])
print(tuple1 [-6:-2:2])
print(tuple1 [-6:-2:-2])
print(tuple1 [-6:])
#(Sets) 
set_={1,2,3,4,5,1} #Arrange the numbers from smallest to highest & Remove the Duplicated items 
print(set_)
print(len(set_))
# Add Items
set_.add(9)
print(set_)
set2={6,7,8,5}
set_.update(set2)
print(set_)
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
thisset.discard("apple")
print(thisset)

length = 4.2
height = 3.5
area = length * height
prim = 2 * (length + height) 
print (area, prim)
for i	in range(1, 10, 2):
 print(i)  # 1 3 5 7 9
def f1():
 global x  
 x = x + 1  
 return x
def f2():
 return x+1  
def f3():
 x = 5  
 return x+1

x = 0 
print (f1)
print (f2)
print (f3)
Mylist = [5, 2.3, "hello"]
print  (Mylist[0])
print	(Mylist[2])

print	(Mylist[-1])
print	(Mylist[-3])
Mylist1 = [5, 2.3, "hello"]
print (Mylist1)
Mylist1[0] = -2  
print (Mylist1)
Mylist1[2] = -1 
print (Mylist1)
d = {1:"one" , 2: " two" , 3: "three" }
for key, value in d.items():
 print (key, value)


