#STACK..............................................
book = ["math", "physics", " chamestry"]


#push 
book.append("Programming essential1")
book.append("Programming essential2")


#pop....
book.pop()
book.pop()
book.pop()
book.pop()
book.pop()


#Condition check...
if not book:
    print("Book Empty")

item = len(book)
print("Book is",book ,"Items", item)



#QUEUE........................................................

from collections import deque

bank = deque(["shamim", "Salam", "Aslam"])

print(bank)

# Use popleft....
bank.popleft()
bank.popleft()
bank.popleft()

print(bank)

if not bank:
    print("No item here!!!!")
