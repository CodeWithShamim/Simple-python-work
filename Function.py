#Introduction of Function......
def add(a,b):
   sum = a+b
   print(sum)

def sub(a,b):
   sum = a+b
   print(sum)


#An.... Function......
def message():
    print("Hello!!")


#Function call......
add(10,20)
sub(30,40)
message()



#Returning value from Function.....
#11
def value(a,b,c):
   sum = a+b+c
   return sum


#variable change....
sum  = value

val = sum(10,20,30)
print("sumation is : ", val)


#22
def large(a, b):
   if a>b:
      return a
   else:
      return b


#Function call......
a = large(160,208)
b = large(1000,20)
print("Largest number is : ", a)
print("Largest number is : ", b)


'''(xargs)x argumments ------------------OR xx arguments(xxargs)--------------------'''

#xargs use single *--------------------------------------------------------------
#11
def student(*details):
   print(details)


#print value(tuple )..................................
student(101, "shamim", 102, "Salam", 103, "Rafik")


#22------
def addition(*number):
   sum = 0
   for num in number:
       sum = sum + num

   print("Total sumation : ", sum)


addition(10, 30)
addition(10, 30, 40, 59, 57, 37, 58, 37)


#xxargs use Double ** ---------------------------------------------------------------
def addition(**number):
   return number

s = addition(name="shaim", id=100, CGPA=4.00)
#print value(Dictionary)
print(s)




