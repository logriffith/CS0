###Assignmnet 1 notes and instructions####
"""
Assignment 1: A siimply hangman game steps
-program displays various stages of hangman game

By: Ram Basnet
1/30/20

"""
print("Hey there what's your name? ")
# TBD- read the name and store into a variable
print('Hey ...') # FIXME
print('The hangman game is under construction, maybe you will get to play it i a few weeks')
print("this is what various stages of hangman game will look like")
print()
print("Stage 0")
print("|-------")
print("|\\       |")
#... fix the rest
#######

"""
Notes from class

a=10
print(float(a))
b='10'
print(a*float(b))

3 in binary is 11.
1(2)^1+2^0=3

round(area, 4) rounds area to 4 decimal points

def getData():
    s1=input("What is the first number")
    s2=input("What is the second number")
    s3=input("What is the thrid number")
    # does it form a triangle
    # if it does return s1,s2,s3

def main():
    s1,s2,s3=getData()
    #find perimeter
    #find area
    #display results

while True:
        main()
        ans=input('Want to test more? [y/n]: ')
        if ans!='y':
            break

## for loops
for val in range of values:
    # loop body

print(list(range(1,11,2)))
2 is th step size
first parameter is the start:1
second parameter is the stop:11
thrid parameter is the step size:2

for i in range(1,11):
    print(i,"Hello World")
    # this will output 1 Hello World

for num in range(20):
    print(num)
output is 
print 0
print 1
.
.
.
print 19

for num in range(20):
    print(num, end=' ')
output is 
0 1 ... 19

for i in range(1,11): #range 1...10
    if i%2==0:
        continue #continue means to go to the next i
    print(i)
output is
1
3
5
7
9
i.e. if i is odd, then the conditional is not met and i is printed

 for i in range(1,11):
     continue
     print(i)
output is nothing

for i in range(10):
    if i==5:   #same output if i>4
        break
    print(i)
print('done')
output is 
0
1
2
3
4
done
## break ends the loop

local variables are only inside functions, otherwise global

for i in range(5):
    print(i)
    if i==2
    break
else:
    print('end!')
output is 
0
1
2
else is part of the for loop like if and elif go together

n=97
for i in range(2,n//2+1):
    if n%i==0:
        print(n, 'is not prime')
        break
else:
    print(n, 'is prime')
output is '107 is prime'

python has only while loops and for loops

i+=1 means i=i+1
"""