def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r " % (arg1, arg2))


def print_two_again(arg1, arg2):
    print("arg1: %r , arg2: %r" % (arg1, arg2))

def print_one(arg1):
    print("arg1: %r" % arg1)

def print_none():
    print("I got nothin.")

def print_sum(arg1,arg2,arg3):
    sum=arg1+arg2+arg3
    
    print(print_sum(4,5,6))

num=[2,3,4]
sum= sum(num)
print(sum)
num=[2,6,8,10,3,7,9]
num = num % 2
if num > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")


print_two("Zed","Shaw")
print_two_again("Zed", "Show")
print_one("First")
print_none()
start, end = 4, 25
  
# iterating each number in list 
for num in range(start, end + 1): 
      
    # checking condition 
    if num % 2 == 0: 
        print(num, end = " ") 
start,end = 4,19

for num in range(start, end+1):
    if num %2 !=0:
        print(num, end="")

start, end = -4 , 19
for num in range(start, end +1):
    if num <=0:
      print(num, end = " ")

start,end = -4,19
for num in range(start ,end+1):
    if num < 0:
        print(num, end="")

list1 =[10,21,4,45,66,93]
for num in list1:
    if num % 2==0:
        print(num)

list1 = [10,21,4,45,66,93]

num=0

while(num<len(list1)):                         var list1 =[10,21,4,45,66,93]
  if num%2 ==0:
        print(list1[num])
        num+=1                                              var num=0
                                                for(var i=0; i<length.num;i--S){
                                                 if(num[i] % 2 ==0){
                                                  console.log(list1.num[i])
                                                 }
     
list1 = [10,21,4,45,66,93]
for num in list1:
    if num%2 != 0:
        print(num, end="")

list1 =[10,21,4,45,66,93]
num=0
while(num<len(list1)):
    if num % 2!=0:
        print(list1[num], end="")
        num +=1

l=10
u=20

for num in range(l, u + 1):
    print(num)

list1=[11,-21,0,45,66,-93]
for num in list1:
    if num >=0:
        print(num)

list1=[-10,21,-4,-45,-66,93]
num=0
while(num<len(list1)):
    if list1[num]>=0:
        print(list1[num])
        num+=1

list1=[11,-21,0,45,66,-93]
for num in list1:
    if num >0:
        print(num)
list1 = [11,-21,0,45,66,-93]
num=0
while(num<len(list1)):
    if list1[num]<0:
        print(list1[num])
        num+=1
def factorial(number):
    fact = 1
    if number == 0 or number ==1:
        return fact 
    for i in range(2, number +1):
        fact *=i
    return fact


def find_strong_numbers(num_list):
    result = []

    for num in num_list:
        sum=0
        temp = num

    while num != 0:
        r = num % 10
        sum +=factorial(r) 
        num // = 10
    if sum == temp:

       result.append(temp)
    return result



var numbers = [10,20,30,40]
var sum = 0;

for(var i =0; i<numbers.length; i++){
    sum+=numbers[i];
}
console.log(sum)
start=11
end =25

for val in range(start,end+1):
    if val>1:
        for n in range(2, val):
            if (val % n) ==0:
                break
        else:
            print(val)
from itertools import cycle

list =  [90, 99,192,0,43,5]
n= 9
k= 5
for index, *ans in zip(range(n), *[cycle(list)]*k):
    print(ans)

list =['Geeks','for','geeks','is','portal']
n=4
k=6
for index, *ans in zip(range(n),*[cycle(list)]*k):
    print(ans)

def reverse(s):
    str = ""
    for i in s:
      str = i+str
    return str  
s="dad"
# print("The reversed string(using loops) is:", end="")
print(reverse(s))
for elem in reversed('dad'):
    print(elem, end ="")

list1=[3,4,5]
sum=sum(list1)
print(sum)



for elem in reversed('dad'):

    print(elem)  
list1=[2,3,-4,6,5,-9]


for num in list1:
    if num % 2!=0:
        print(num,end="")


for num in list1:
    if num % 2==0:
        print(num)
start,end = 1,13
for num in range(start,end):
    if num % 2!=0:
        print(num, end ="")

for elem in reversed('dad'):
    print(elem,end="")
list1 = [3,-4,-6,5,9,2]
for num in list1:
    if num<0:
        print(num)

for elem in reversed("you are a boss"):
   print(elem,end="")




    if(elem==elem):
      print("The %s is a palindrome", elem)
    else:
      print("Not a palindrome")
    



start,end = 100,200

for elem in range(start,end):
    if elem%5==0:
        print(elem)

for elem in reversed('ludwe is a star'):
    print(elem,end="")

string ='dad'
if string == string
print('This string is palindrome')
else:
    print('This is not a palindrome')

elem = 0
name = "You are a boss"

for elem in name:
    if elem=='a':
        elem+=1
        print(elem)


start,end = 100,200
for elem in range(start,end):
    if elem%5==0:
        print(elem)
string = "Nonzulu Kala"[::-1]
print(string)

numbers=[-3,5,4,2,5,8,9]
for num in numbers:
    if num%2!=0:
        print(num)

elem =input("Enter string:")
if elem ==elem[::-1]:
    print("Its palindrome")
else:
        print("Not a palindrome")


n=int(input("Enter number of rows"))
for i in range(n,0,-1):
    print((n-1)*''+i*'*')


power=1
while(power<6):
    print(power)
    power+=1  

i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1

i=0
while i<6:
    i+=1
    if i ==3:
        continue
    print(i)

i=1
while i<6:
    print(i)
    i+=1
else:
        print("i is no longer less than 6")

i=1
while i<6:
    
    print(i)
i+=1

thislist=["apple","banana","cherry"]
thislist.insert(1,"orange")
print(thislist)

thislist=["apple","banana","cherry"]
thislist.remove("banana")
print(thislist)

thislist=["apple","banana","cherry"]
del thislist[0]
print(thislist)


        