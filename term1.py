# session1:
# https://py.checkio.org/

# برنامه بنویسید که در یک لیست اگر کلمه دو حرف تکراری وجود داشته باشد آن را نمایش دهد و در غیر این صورت  خروجی دهد

# soroosh = o
# matin = None
# mohammad = m
# shadi = None
# matin = None
# alii=i

# a = ["soroosh" , "mohammad" , "shadi" , "matim" , "alii"]

# for i in a:
#     c=1
#     try:
#         for j in i:
#             if j==i[c]:
#                 print(f"{i} = {j}")
#             c+=1
#             else:
#                 # homework
#     except:
#         pass


# .....................

# برنامه بنویسید که از کاربر  عدد چند رقمی بگیرد و دو برابر عکس آن را چاپ کند

# 123 , 321 , 642

# number = input("please enter a number : ")

# # number = number[::-1]
# # print(int(number)*2)

# result = ""
# c=1
# for i in number:
#     result+=number[-c]
#     c+=1
# print(int(result)*2)


# ..............

# primary number : 
# 2 3 5 7 11 13 17 , ....


# number1 = int(input("please enter a number : "))
# c=0
# for i in range(2 , number1):
#     if number1%i==0:
#         c+=1
#         break
# if c==0:
#     print(f"{number1} is primary number")
# else:
#     print(f"{number1} is not primary number")


# ............
# homework
# practice (moshakhas kardan esmhay moshtarak)
# mylist = ["amin", "reza" , "matin" , "sara" , "ali" , "vahid", "mohamad" , "hasan"]
# mylist2 =["vahid" , "sara" , "hasan" , "mehdi"]

# ..........
# homework
# 5! = 5*4*3*2*1
# 6! = 720

# a = int(input(".... : "))
# total = 1
# for i in range(1 , a+1):
#     i*(total+1)


# ..............

# session2:

# reverse factorial :

# 120 = 5!

# number = int(input("please enter a number : "))
# 1:
# result = 1
# i=1
# while True:
#     result*=i
#     i+=1
#     if result==number:
#         print(f"{i-1}!")
#         break


# 2:
# c = 1
# for i in range(1,number):
#     c*=i
#     if c==number:
#         print(f"{i}!")


# ...........
# a= "ihds6fdfhg"
# b="5423415"
# print(a.isalpha())
# print(b.isnumeric())
# print(b.isdigit())



# login signup:

# usernames = {"ali":"dshf98wy98" , "hamid":"fehfyut287223" , "arash":"sdncvmvnmc000"}

# while True:
#     username = input("please enter new username : ")
#     password = input("please enter new password : ")

#     if username in usernames:
#         print("this username exist , try other...")
#         continue

#     if len(password)<7 :
#         print("too short")
#         continue

#     elif password.isnumeric():
#         print("your password must include atleas 1 charachter")
#         continue
#     elif password.isalpha():
#         print("your password must include atleas 1 number")
#         continue

#     else:
#         print("welcome")
#         usernames[username]=password
#         break

# # print(usernames)
# i=0
# while i<4:
#     if i==3:
#         print("you are block...!")
#         break
#     loginuser = input("please enter username : ")
#     loginpass = input("please enter password : ")
#     if loginuser in usernames and loginpass in usernames.values() :
#         print("welcome")
#         break
#     else:
#         print("your password or username wrong try again!!!")
#     i+=1

# ...............

# homework:

# exp: input = 7

# x       
# xx      
# xox     
# xoox    
# xooox   
# xoooox  
# xooooox 
# xxxxxxxx


# ...........

# homework:

""" 
شما میخواین به برادرزادتون کمک کنین که الفبا رو یاد بگیره. برای همین یه برنامه باید بسازین که یه حرف بگیره و تمام حروف رو با توجه به حرف قبلی به ترتیب نشون بده. با این حال احتمال بهم زدن برنامه به وسیله بچه زیاد هست.
 
اولین قدم باید برنامه ای بنویسین که بچه با زدن تصادفی دکمه ها و وارد کردن حروف بی معنی نتونه  برنامه رو به هم بریزه. تا زمانی که کاربر هیچ حرفی وارد نکنه برنامه ازش درخواست میکنه که یک حرف وارد کنه.

در ادامه برنامه باید تمام حروف قبل از حرف شما رو نشان بده. برای نمایش حروف هر حرف باید حرف به صورت بزرگ و جدا شده از دیگری به وسیله ویرگول باشد. بعد از نمایش 5 حرف به خط بعدی میره. حروفی که وارد میکنیم میتونه  کوچیک یا بزرگ باشه. 

"""


# .........
# session 3:
# homework:

# برنامه‌ای بنویسید که یک دیکشنری را دریافت کند و ولیوهایی که بیشتر از یک بار تکرار شدن را داخل دیکشنری دیگر نشان بدهد
# a = {"name1": "matin", "name2": "shamim", "name3": "arash", "name4": "matin" , "name5":"shamim"}
# # {'matin': 2, 'shamim': 2}
# c=0
# values = []
# for i in a:
#     if a[i]== 

# .................

# christmas tree:
# enter a number : 7

#       *      
#      ***     
#     *****    
#    *******   
#   *********  
#  *********** 
# *************
#       *
#       *

# a = int(input(".... : "))
# b=a
# for i in range(a):
#     print(b*" " , end=((2*i)+1)*"*")
#     b-=1
#     print("")     
    
# for j in range(2):
#     print(a*" " , end="*")
#     print("")


# ....................

# homework:

#      *
#      *
# ***********
#  *********
#   *******
#    *****
#     ***
#      *

# ...............

# def new(**kwargs):
#     a = 10
#     print(kwargs)
#     # return name


# new(name = "matin" , family = "kafashian")

# .............

# list1 = [2 , 3 , 5 , 6, 7]



# x= map(lambda i:i*2 ,list1 )
# print(list(x))

# ......


# user = [
#     {"name":"ali" , "lastname":"mosavi", "age" :25 },
#     {"name":"ahamd" , "lastname":"mosavi2", "age" :23 },
#     {"name":"mona" , "lastname":"mosavi3", "age" :44}
# ]

# print(type(user))
# print(user[1])

# peopole = map(lambda a : a['name'] , user)
# print(list(peopole))

# .........


# x = [1 , 3 ,4 ,6 ,7 ,8 ,9]
# select = filter(lambda a: a%2 == 0 , x)
# print(list(select))

# .............


# mylist = ["sara" , "ahmad", "koorosh" , "saieid" , "mohammad reza" , "amin"]
# x = [1 , 3 ,4 ,6 ,7 ,8 ,9]
# max_value=["sara"]
# for i in mylist:
#     if len(i)>len(max_value[0]):
#         max_value[0] = i
# print(max_value)


# print(max(mylist , key=lambda a: len(a)))

# .........
# False None 0 ""

# num= [4 , 0 , 3 , 20 , 5]

# num2 = [0 , 0, 0 ,0]
# print(any(num2))
# print(any(num))
# .......

# function absolut value
# print(abs(-5))

# .....
#function round
# print(round(4.2))
# print(round(4.7))
# print(round(4.5))
# print(round(5.5))

# .......


# function zip :
# a1 = [1 ,3 ,5 ,7 ,8 , 5]
# a2 = [4 ,5 ,6 ,7 , 11]
# print(list(zip(a1 , a2)))

# new1 =[(1, 4), (3, 5), (5, 6), (7, 7), (8, 11)]
# print(list(zip(*new1)))



# ....................


# class My:
#     def __init__(self , name , lastname):
#         self.myname = name
#         self.mylastname = lastname

#     def fullname(self):
#         print(f"hi i am {self.myname} {self.mylastname}")  


# p1 = My("ali" , "alizade")
# p2 = My("reza" , "mosavi")
# # print(p1.myname , p2.mylastname)
# p1.fullname()


# .............
# homework: 

#practice : on off car:


# ...........

# session4:

#practice : on off car:
# class Car():
#     def __init__(self , name):
#         self.carname = name
#         self.status = False
    
#     def start(self):
#         if self.status == False:
#             self.status = True
#             print("start")
#         else:
#             print("your car is on don not press start button")

#     def off(self):
#         if self.status == True:
#             self.status = False
#             print("your car is off")
#         else:
#             print("your car is off please first start")

# c1 = Car("benz")
# # print(c1.carname)
# # c1.start()
# # c1.start()
# c1.off()


# ................

# __str__:

# class Car:
#     def __init__(self , name , price):
#         self.name=name
#         self.price=price
#     def __str__(self):
#            return f"a {self.name}"

# car1 = Car("benz" , 453432)
# print(car1)

# .............................

import random

# mygifts = ["206" , "" , "100$"  , "iphone 15" , "" ,"" , "" , "candy" ]
# print(random.choice(mygifts))



# class Bank:

#     def __init__(self , account_number , balance):
#         self.account_number = account_number
#         self.balance = balance
#         self.transaction = 0

#     def __str__(self):
#         return f"your balance is {self.balance}$"
    
#     def deposit(self , money):
#         self.balance += money
#         self.transaction+=1

#         return f"{money}$ deposit to your account and your balance is {self.balance}$"
    
#     def whithdraw(self , money2):
#         if self.balance>money2+20:
#             self.balance-=money2
#             self.transaction+=1
#             return f"{money2}$ withdraw of your account and your balance is {self.balance}$"

#         else:
#             return ("Insufficient funds.")
    
#     def lottery(self):
#         gifts = ["206" , "" , "100$"  , "iphone 15" , "" ,"" , "" , "candy" ]
#         giftscore = int(self.transaction/3)+1
#         for i in range(giftscore):
#             mygift = random.choice(gifts)
#             if mygift:
#                 print("... your gift is " + mygift)
#                 break
#         if not mygift:    
#             print("bandeye khoda nabordi")      

#     # home : loan  ........ :          

# account1 = Bank("145612531" , 100)
# print(account1.deposit(50))
# print(account1.whithdraw(100))
# account1.lottery()
# # print(account1)


# ....................


# session5:
import random
import string

# a = string.ascii_lowercase
# a = string.ascii_letters
# a = string.digits
# a = string.punctuation
# print(a)
# .......


# class brutForce:
#     def __init__(self , target):
#         self.target = target

#     def choice(self):
#         mychoice_easy =random.choices(string.ascii_lowercase , k=len(self.target)) 
#         letters =random.choices(string.ascii_letters , k=len(self.target))
#         numbers =random.choices(string.digits , k=len(self.target))
#         symbols =random.choices(string.punctuation , k=len(self.target))
#         mychoice_hard = letters+numbers+symbols
#         mychoice_hard = random.choices(mychoice_hard , k=len(self.target))
        
#         mychoice_easy = "".join(mychoice_easy)
#         mychoice_hard = "".join(mychoice_hard)
#         # print(mychoice_hard)
#         return mychoice_easy
#         # return mychoice_hard
    
#     def guess(self , numberofguess):
#         for i in range(numberofguess):
#             myguess = self.choice()
#             print(f"{i} {myguess}")
#             if self.target==myguess:
#                 print(self.target)
#                 print(f"the target is {myguess}")
#                 break
           


# chance1 = brutForce("df")
# # chance1.choice()
# chance1.guess(1000000)
# # print(chance1.target)


# ............


# __getitem__:

# class MyList:
#     def __init__(self, *args):
#         self.elements = list(args)
    
#     def __getitem__(self, index):
#         return self.elements[index]


# my_list = MyList(1, 2, 3, 4, 5)

# print(my_list[0])      
# print(my_list[2])    
# print(my_list[-1])    
# print(my_list[1:4])    

# ...........................

# __setitem__

# class MyList:
#     def __init__(self, *args):
#         self.elements = list(args)

#     def __getitem__(self, index):
#         return self.elements[index]

#     def __setitem__(self, index, value):
#         self.elements[index] = value

#     # def __repr__(self):
#     #     return repr(self.elements)

#     def __str__(self):
#         return str(self.elements)


# my_list = MyList(1, 2, 3, 4, 5)

# # print(my_list)      
# # print(my_list[2])      

# my_list[0] = 10
# print(my_list)      

# my_list[2:4] = [20, 30]
# print(my_list)       


# ......


# class MyDict:
#     def __init__(self):
#         self.data = {}

#     def __getitem__(self, key):
#         return self.data[key]

#     def __setitem__(self, key, value):
#         self.data[key] = value

#     def __repr__(self):
#         return repr(self.data)

#     def __str__(self):
#         return str(self.data)

# my_dict = MyDict()
# # print(my_dict.data)
# my_dict["name"] = "John"
# my_dict["age"] = 30
# # print(my_dict)         
# print(my_dict["name"]) 
# print(my_dict["age"])   

# ...........

# __len__

# class CustomList:
#     def __init__(self, elements):
#         self.elements = elements
    
#     def __len__(self):
#         return len(self.elements)

# my_list = CustomList([1, 2, 3, 4, 5] )
# print(len(my_list))  

# ..........

a = range(4 ,  10)
# print(a)

# ...............


# class Range:
#     def __init__(self , bounds1 , bounds2=None):
#         if bounds2==None:
#             self.lower=0
#             self.upper=bounds1
#         else:
#             self.lower=bounds1
#             self.upper=bounds2
    
#     def __str__(self):
#         return f"range({self.lower} , {self.upper})"
    
#     def __getitem__(self , lookup):
#         # return "hi"
#         # return lookup
#         # return lookup+self.lower
#         if lookup>self.upper - (self.lower+1):
#             raise IndexError("it is bigger than range!!!")
#         else:
#             return lookup+self.lower
#     def __len__(self):
#         return self.upper - self.lower
#     # try without __len__
    

# r1=Range(4 ,10)
# print(r1[8])
# print(r1[1:4])
# print(len(r1))

# ..........................


# decorator:

# def add(x,y):
#     return x+y
# def sub(x,y):
#     return x-y

# def process(func , a, b):
#     print(func(a,b))

# process(add ,10 , 1)
# process(sub ,10 , 1)

# .........................

# def mydecorator(func):
#     def wrapper():
#         print("11111")
#         func()
#         print("22222")
#     return wrapper

# @mydecorator
# def helloworld():
#     print("helloworld")

# @mydecorator
# def salam():
#     print("000000000")

# helloworld()
# salam()

# .................................


# def mydecorator(func):
#     def wrapper(*args,**kwargs):
#         print("11111")
#         func(*args,**kwargs)
#         print("22222")
#     return wrapper

# @mydecorator
# def helloworld():
#     print("helloworld")

# @mydecorator
# def salam(name):
#     print(f"salam {name}")

# @mydecorator
# def add(a,b):
#     print(a+b)    

# # helloworld()
# # salam("matin")
# add(10,5)


# .............
# homework:
# https://quera.org/problemset?tag=74&tag=78&page=1


# ..............

# session6:
# import time
# import datetime
# # date = datetime.datetime.now()
# # print(date)

# import datetime
# def mydecorator(func):
#     def wrapper(*args,**kwargs):
#         date = datetime.datetime.now()
#         a = func(*args,**kwargs)
#         name=func.__name__
#         print(f"the time is {date} ,the function name is {name} , value is {a}")
        
#     return wrapper

# @mydecorator
# def helloworld():
#     # print("helloworld")
#     return "hello world"
# @mydecorator
# def salam(name):
#     print(f"salam {name}")

# @mydecorator
# def add(a,b):
#     # print(a+b)
#     return a+b    

# # helloworld()
# # salam("matin")
# add(10,5)


# ...........................



# ers bari:

# class My:
#     def __init__(self , name , lastname):
#         self.myname = name
#         self.mylastname = lastname


#     def new(self):
#         print("welcome")

# class Student(My):
#     pass

# s1 = Student("sara" , "ahmadi")
# # s1.new()
# print(s1.mylastname , s1.myname)

# ...................


# class My:
#     def __init__(self , name , lastname):
#         self.myname = name
#         self.mylastname = lastname

#     def new(self):
#         print("welcome")

# class Student(My):
#     def __init__(self , name , family , age):
#         self.myage = age
#         self.myname = name
#         self.myfamily = family

# s1 = Student("sara" , "ahmadi" , 34)
# print(s1.myage)
# print(s1.myname)
# print(s1.mylastname)
# print(s1.myfamily)
# s1.new()

# .........


# super():

# class Parent:
#     def __init__(self ,a , b):
#         print("this is parent")
#         self.one = a
#         self.two = b

# class Child(Parent):
#     def __init__(self ,a ,b):
#         print("this is child")
#         # Parent.__init__(self, a ,b)
#         super().__init__(a, b)

# object_child = Child(10 , 20)
# print(object_child.one)


# .........


# class Parent:
#     def __init__(self ,a , b):
#         print("this is parent")
#         self.one = a
#         self.two = b

# class Child(Parent):
#     def __init__(self ,a ,b ,c=3):
#         print("this is child")
#         # Parent.__init__(self)
#         super().__init__(a, b)
#         self.three = c

# object_child = Child(10 , 20)
# print(object_child.one)
# print(object_child.three)


# ...........


# class Parent:
#     def __init__(self, name):
#         self.name = name
#         print("Parent __init__ called")
        
# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#         print("Child __init__ called")

# c = Child("Alice", 10)
# print(c.name)
# print(c.age)


# ....................


# class Rectangle:
#     def __init__(self , length , width) :
#         self.length= length
#         self.width= width

# class Square(Rectangle):
#     def __init__(self , length , width) :
#        super().__init__( length , width)
#     def area(self):
#         return self.length*self.width

# class Cube(Rectangle):
#     def __init__(self , length , width , height) :
#         super().__init__( length , width)
#         self.height= height
    
#     def volume(self):
#         return self.length*self.width*self.height
    

# square = Square(3 ,3)
# cube = Cube(3 ,3 ,4)

# # print(square.area())
# print(cube.volume())

# ............................


# quiz : 
# 1. Explain with your own words what is an object in Object Oriented Programming! Write an example!
# answer :
'''In object-oriented programming, we see and think about everything as objects. That is, instead of considering every work by defining successive variables and defining successive activities, we consider and design objects so that we can define the characteristics, traits and behaviors we want about the process we want. do. These processes can be anything. Then we create as many examples of that object as we need, which can be completely different from each other based on the definitions we had, but within the framework defined for the object. It means that the attributes and behaviors follow the defined class'''

# class Number:
#   def __init__(self,num):
#     self.num = num
#   def add(self,num2):
#     self.num= self.num +num2
#   def show(self):
#     print('number: ', self.num)

# num = Number(10)
# num.add(2)
# num.show()


# ....................

# 2
#  In the following code we have code duplication: we are defining the same fields in both Cat and Dog classes as well.
#  How could we refactor this solution to avoid this code duplication? Write actual code as a solution (not just describe it)!
# Below the class definitions you can find example instantiations.
#  Don’t touch these lines, your solution should be able to work with this usage.

# ```
# class Dog:
#    def __init__(self, name, age, color):
#        self.type = 'dog'
#        self.name = name
#        self.age = age
#        self.color = color

# class Cat:
#    def __init__(self, name, age, color):
#        self.type = 'cat'
#        self.name = name
#        self.age = age
#        self.color = color


# dog = Dog('Furkesz', 5, 'white')
# cat = Cat('Grumpy', 6, 'grey')
# print(dog.name,dog.age,dog.type,dog.color)
# print(cat.name,cat.age,cat.type,cat.color)

# class Animals:
#     def __init__(self , name , age , color):
#         self.name = name
#         self.age = age
#         self.color = color
    

# class Dog(Animals):
#     def __init__(self , name , age , color):
#         super().__init__(name , age , color)
#         self.type = "dog"

# class Cat(Animals):
#     def __init__(self , name , age , color):
#         super().__init__(name , age , color)
#         self.type = "cat"

# dog = Dog('Furkesz', 5, 'white')
# cat = Cat('Grumpy', 6, 'grey')
# print(dog.name,dog.age,dog.type,dog.color)
# print(cat.name,cat.age,cat.type,cat.color)


# ...................

# q3:
# What is the output of the following code? Explain your answer!
# problem

# ```
# class Book:
#    print_number = 1
#    def __init__(self, author, title, price):
#        self.author = author
#        self.title = title
#        self.price = price
#        if Book.print_number <= 1:
#            self.price *= 2
#        Book.print_number += 1
#    def sell(self, money):
#        print(money - self.price if money >= self.price else money)

# class HardCover(Book):
#    def __init__(self, author, title, price, cover_price = 100):
#        super().__init__(author, title, price + cover_price)
#        self.coverPrice = cover_price

# class PaperCover(Book):
#    def __init__(self, author, title, price):
#        super().__init__(author, title, price)
#    def sell(self, money):
#        print(max(money - self.price, 0))


# lotr = HardCover('J.R.R. Tolkien', 'The Lord of the Rings: The Fellowship of the Ring', 1000)
# hp = HardCover('J.K. Rowling', "Harry Potter and the Philosopher's Stone", 1000, 200)
# lp = PaperCover('Antoine de Saint-Exupéry', "The Little Prince", 1000)
# # lotr.sell(1200)
# # hp.sell(1200)
# lp.sell(1200)

# .........................


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def pr2(self , a):
#         print( f"Person(name={self.name} + {a.name} + {a.family})")

# class New:
#     def __init__(self ,name , family):
#         self.name= name
#         self.family = family
       
# p1=Person("hamid" , 22)
# n1=New("amir" , "karimi")

# p1.pr2(n1)


# ........................

# q4:

# We want to register new zoos in the system. Every zoo has a name and the size of its territory.
# The territory of a zoo is by default 100.
# We want to place animals in zoos. 
# Every animal has a name and a territory requirement (the amount of territory the animal needs to live). 
# The territory requirement of an animal is by default 20.

# When a zoo has enough free territory for the animal which we want to place there, then the zoo places the animal.

# We also want to sell animals from a zoo to free up some territory to other animals.
# A zoo always sells the animal which requires the most territory. 
# When a zoo sells an animal, it returns the sold animal and frees up its territory to be able to place new animals.

# Using your solution, the following code should run without errors and print the expected results.

# ```
# budapest_zoo = Zoo('Budapest Zoo') # Created with 100 territory
# berlin_zoo = Zoo('Berlin Zoo', 200) # Created with 200 territory
# elephant = Animal('elephant', 50) # Created with 50 territory
# giraffe = Animal('giraffe', 40) # Created with 40 territory
# zebra = Animal('zebra') # Created with 20 territory

# budapest_zoo.sell() # Should print: no animals to sell
# budapest_zoo.place_animal(elephant) # Should print: elephant is placed in Budapest Zoo
# budapest_zoo.place_animal(giraffe) # Should print: giraffe is placed in Budapest Zoo
# budapest_zoo.place_animal(zebra) # Should print: no territory for zebra in Budapest Zoo
# berlin_zoo.place_animal(budapest_zoo.sell()) # Should print: elephant is placed in Berlin Zoo
# budapest_zoo.place_animal(zebra) # Should print: zebra is placed in Budapest Zoo

# ........

# class Zoo:
#     def __init__(self , zoo_name  ,zoo_territory=100):
#         self.zoo_name = zoo_name
#         self.zoo_territory = zoo_territory
#     def place_animal(self):
#         pass



# class Animal:
#     def __init__(self , Animal_name  ,Animal_territory=20):
#         self.Animal_name = Animal_name
#         self.Animal_territory = Animal_territory


# ..........

# session 7:
# hard practice : 

# mylist1 = [("amin", "football"), ("reza", "basketball"), ("matin", "ski"), ("sara", "football"), ("ali", "koshti")]
# mylist2 = [("mehdi", "football"), ("lili", "karate"), ("vahid", "handball"), ("mohamad", "ski")]
# mylist3 = [("asal", "baseball"), ("maryam", "karate"), ("vahid", "box"), ("korosh", "ski")]



# answer


# combined_list = mylist1 + mylist2 + mylist3

# sport_dict = {}

# for name, sport in combined_list:
#     if sport not in sport_dict:
#         sport_dict[sport] = []  
#     sport_dict[sport].append(name) 


# result_dict = {}

# for sport, names in sport_dict.items():
#     if len(names) >= 2:
#         result_dict[tuple(names)] = sport

# print("Dictionary format:", result_dict)

# ..............

# https://quera.org/problemset/33036

# session 8:
import string
# a= string.punctuation
# print(a)


# matin  . 8023fu9yuf9u4
# a = "dhh@#"
# print(a.isalnum())


# class Security:
#     def secure(self, info):
#         inf = info.split(", ")
#         # print(inf)
#         for i in inf : 
#             if self.is_social_account_info(i):
#                 print(i)


#     def is_social_account_info(self, param):
#         try:
#             if param[0].isupper():
#                 domain = param.split(".")[1]
#                 account = param.split("/")[1]
#                 for i in domain:
#                     if i.islower() or i.isnumeric():
#                         continue
#                     else:
#                         return False
#                 for j in account:
#                     if j.isalnum() or j=="_":
#                         continue
#                     else:
#                         return False

#                 return True
            
#             else:
#                 return False
#         except:
#             pass

#     def encrypt(self, s):
#         pass



# account1 = Security()

# # print(account1.is_social_account_info('Instagram:www.inst@agram.com/java_fan'))
# account1.secure('FirstName:Ali, LastName:Alavi, BirthDate:1990/02/02, Gender:male, Instagram:www.instagram.com/aalavi, Degree:Master, Twitter:www.twiter.com/alaviii, imdb:www.imdb.com/alavi')
# # 'FirstName:Ali, LastName:Alavi, BirthDate:1990/02/02 Gender:male Instagram:www.instagram.com/12121229 Degree:Master Twitter:www.twiter.com/11212291827 imdb:www.imdb.com/alavi'


# ............
# https://quera.org/problemset/87184



# .............
# session 9:

# class Security:
#     def secure(self, info):
#         inf = info.split(", ")
#         result = []

#         for i in inf: 
#             if self.is_social_account_info(i):
#                 result.append(i)

#         encrypted_result = []
#         for item in result:
#             division = item.split("/")
#             encrypted_username = self.encrypt(division[1])
#             encrypted_account = division[0] + "/" + encrypted_username
#             encrypted_result.append(encrypted_account)
    
#         for i, element in enumerate(inf):
#             if self.is_social_account_info(element):
#                 inf[i] = encrypted_result.pop(0)
                
#         return " ".join(inf)
        
#     def is_social_account_info(self, param):
#         try:
#             if param[0].isupper():
#                 domain = param.split(".")[1]
#                 account = param.split("/")[1]
#                 for i in domain:
#                     if i.islower() or i.isnumeric():
#                         continue
#                     else:
#                         return False
#                 for j in account:
#                     if j.isalnum() or j=="_":
#                         continue
#                     else:
#                         return False

#                 return True
            
#             else:
#                 return False
#         except:
#             pass

#     def encrypt(self, s):
#         # if not sorted, the encryption code changes every time code is run
#         s = "".join(sorted(s))
        
#         b = set(s)

#         segments = {}
#         result = []

#         for i in b:
#             for j in s:
#                 if i == j:
#                     break
#             segments[i] = s.count(i)

#         for key, val in segments.items():
#             result.append(key * val)

#         result = [key * val for key,val in segments.items()]

#         result_sorted = sorted(result, key=lambda x: s.index(x))
        
#         code = []
#         for i in result_sorted:
#             chunk_code = ""
#             num = ord(i[0])
#             num = abs(num - 96)
#             for j in range(1, len(i)+1):
#                 chunk_code = chunk_code + str(num * j)
#             code.append(chunk_code)

#         code = "".join(code)

#         return code

# account1 = Security()
# print(account1.encrypt("abcccdd"))
# print(account1.secure('FirstName:Ali, LastName:Alavi, BirthDate:1990/02/02, Gender:male, Instagram:www.instagram.com/aalavi, Degree:Master, Twitter:www.twiter.com/alaviii, imdb:www.imdb.com/alavi'))
# Output: 'FirstName:Ali, LastName:Alavi, BirthDate:1990/02/02 Gender:male Instagram:www.instagram.com/12121229 Degree:Master Twitter:www.twiter.com/11212291827 imdb:www.imdb.com/alavi'

# ............



# ..........

# Write a Python program to sort a given list of lists by length and value using lambda.
# a = [[2], [1, 3], [0], [0, 7], [9, 11], [13, 15, 17]]
# # Sort the list of lists by length and value: [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]
# b = sorted(a, key=lambda x: (len(x), max(x)))
# print(b)

# ........

# Write a Python program to remove None values from a given list using the lambda function.
# a = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
# Remove None value from the said list: [12, 0, 23, -55, 234, 89, 0, 6, -12]
c = []
# b = list(filter(lambda x: c.append(x) if x != None else None , a))
# b = list(filter(lambda x: x!=None, a))
# print(b)
# ...........
# Write a Python program to remove specific words from a given list using lambda.
# Remove words:
c= ['orange', 'black']
# After removing the specified words from the said list:
# ['red', 'green', 'blue', 'white']

# a = ['orange', 'red', 'green', 'blue', 'white', 'black']

# b = list(filter(lambda x: x if x != "orange" and x != "black" else None, a))
# b = list(filter(lambda x: x not in c , a))

# print(b)


# ............

# https://quera.org/problemset/87184

# import re
# import hashlib

# class Account:
#     def __init__(self, username, password, user_id, phone, email):
#         self.username = username
#         self.password = password
#         self.user_id = user_id
#         self.phone = phone
#         self.email = email

#     def username_check(self):
#         username_div = re.split(r"(_)", self.username)
#         if self.username.count("_") != 1 or not username_div[0].isalpha() or not username_div[2].isalpha(): 
#             raise ValueError("Invalid username!")
#         else:
#             return True
                
#     def password_check(self , password):
#             upper_check = any(i.isupper() for i in self.password)
#             lower_check = any(i.islower() for i in self.password)
#             num_check =  any(i.isnumeric() for i in self.password) 
#             if len(self.password) > 7 and upper_check and lower_check and num_check:
#                 password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
                
#                 return password_hash
#             else:
#                  raise ValueError("Invalid password!")

#     def user_id_check(self , userid):
        
#         result = 0
#         control_digit = 0

#         if not self.user_id.isnumeric():
#              return False
        
#         for i in range(2, len(self.user_id)+1):
#              result += (int(self.user_id[i-1]) * i)

#         if result % 11 <= 2:
#             control_digit = result % 11
#         else: 
#             control_digit = abs((result % 11) - 11) 
    
#         if str(control_digit) == self.user_id[0]:
#             return True
#         else:
#             raise ValueError("Invalid User_ID") 
    
#     def phone_check(self):
#         if self.phone.startswith("0"):
#             self.phone = self.phone
#         else:
#             self.phone = "0" + self.phone.replace("+98", "")

#         if len(self.phone) != 11 or self.phone[1] != "9":
#             raise ValueError("Invalid phone number!")
#         else:
#             return True
        
#     def email_check(self ,email): 
#         # First_Part@Second_Part.Third_Part
#         first_part = email.split("@")[0]    
#         Second_Part = email.split("@")[1]
#         Second_Part = email.split(".")[0]
#         return (first_part , Second_Part)


        
#     def show_welcome(self):
#         user_split = self.username.replace("_", " ").split()
#         user = []

#         for i in user_split:
#             user.append(i.capitalize())

#         user = " ".join(user)

#         if len(user) > 15:
#             user_div = user[:15]
#             user = user_div + "..."
            
#         return f"welcome to our site {user}"
    
#     def verify_change_password(self):
#         pass
     
# class Site:
#     def __init__(self, url, register_users, active_users):
#         self.url = url
#         self.register_users = register_users
#         self.active_users = active_users
        
#         # ۷۷۳۱۶۸۹۹۵۱
# account1 = Account("salib_alibabaeei", "Aa123123", "7731689951", "09121212121", "john@email.com")
# # print(account1.username_check())
# # print(account1.password_check(account1.password))
# print(account1.user_id_check(account1.user_id))
# # print(account1.phone_check())
# # print(account1.email_check(account1.email))
# # print(account1.show_welcome())


# ...........

#code ostad : 


# import string
# import hashlib


# class Site:
#     def __init__(self, url_address):
#         self.url=url_address
        
#         self.register_users=[]
#         self.active_users=[]

#     def show_users(self):
#         pass

#     def register(self, user):
#         if user not in self.register_users:
#             self.register_users.append(user)
#             return "register successful"
#         else:
#             raise Exception("user already registered")

#     def login(self, **kwargs):
#         checkus=False
#         checkem=False
#         checkps=False
#         # username=input("please enter your username : ")
#         # email=input("please enter your email : ")
#         # password=input("please enter your password : ")
#         # kwargs["username"]=username
#         # kwargs["email"]=email
#         # kwargs["password"]=password
#         # {"username" : "matin_kafashian"}
#         # print(kwargs)
        
#         for i , j in kwargs.items():
#             for k in self.register_users:
#                 # print(i)
#                 if i=="username":
#                     # print("check")
#                     if j==k.username_validation(k.username):
#                         checkus=True
#                         # return "invalid login"
#                 elif i=="email":
#                     # print(i,j,k.email_validation(k.email))
#                     if j==k.email_validation(k.email):

#                         checkem=True
#                         # return "invalid login"
                   
#                 elif i=="password":
#                     newj=hashlib.sha256(j.encode('utf-8')).hexdigest()
#                     # print(newj,k.password_validation(k.password))
#                     if newj==k.password_validation(k.password):
#                         checkps=True
#                         # return "invalid login"
#                 if checkps and checkem and checkus:
#                     # print("here")
#                     if k in self.active_users:
#                         return "user already logged in"
#                     else:
#                         self.active_users.append(k)
#                         return "login successful"
                    
#         if checkus==False or checkps==False or checkem==False:
#             return "invalid login"
        

#     def logout(self, user):
#         if user in self.active_users:
#             self.active_users.remove(user)
#             return "logout successful"
#         else:
#             return "user is not logged in"

#     def __repr__(self):
#         return "Site url:%s\nregister_users:%s\nactive_users:%s" % (self.url, self.register_users, self.active_users)

#     def __str__(self):
#         return self.url



# class Account:
#     def __init__(self, username, password, user_id, phone, email):
#         self.username=username
#         self.password=password
#         self.user_id=user_id
#         self.phone=phone
#         self.email=email

#     def set_new_password(self, password):
#         has_upper = any(i.isupper() for i in password)
#         has_lower = any(i.islower() for i in password)
#         has_digit = any(i.isdigit() for i in password)
#         if len(password)>=7 and has_digit and has_lower and has_upper:
#             password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
#             return password_hash
#         else:
#             raise Exception("invalid password")

#     def username_validation(self, username):
#         checkuser=username.split("_")
#         for i in checkuser:
#             for j in i:
#                 if j not in string.ascii_letters:
#                       raise Exception("invalid username")

#         if len(checkuser)!=2:
#             raise Exception("invalid username")
#         else:
#             return username

#     def password_validation(self, password):
#         has_upper = any(i.isupper() for i in password)
#         has_lower = any(i.islower() for i in password)
#         has_digit = any(i.isdigit() for i in password)
#         if len(password)>=7 and has_digit and has_lower and has_upper:
#             password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
#             return password_hash
#         else:
#             raise Exception("invalid password")

#     def id_validation(self, id):
#         resultid=0
#         myid=self.user_id
#         myid=myid[::-1]
        
#         for i ,j in enumerate(myid):
#             if i==0:
#                 continue
            
#             resultid+=((i+1)*(int(j)))
#         remind_resultid=int(resultid)%11
       
#         if remind_resultid<=2:
#             if int(self.user_id[-1])==remind_resultid:
#                 return myid
#             else: 
#                 raise Exception("invalid code melli")
#         else:
#             if int(self.user_id[-1])==(11-remind_resultid):
#                 return myid
#             else:
#                 raise Exception("invalid code melli")


#     def phone_validation(self, phone):
#         if len(self.phone)==13 and self.phone[:4]=="+989":
#             newphone="0"+ self.phone[3:]
      
#         else:
#             raise Exception("invalid phone")

#     def email_validation(self, email):
#         if self.email.count("@")==2:
#             raise Exception("invalid phone")
#         myemail=self.email.split("@")
#         myemail2=myemail[1].split(".")
#         myemail2=myemail2[0]
#         checkmail=True
#         for i in myemail[0]:
            
#             if i in string.punctuation:
#                 if i=="-" or i=="_" or i==".":
#                     for j in myemail2:
#                         if j in string.punctuation:
#                             if j=="-" or j=="_" or j==".":
#                                 pass
#                             else:
#                                 raise Exception("invalid phone")
#                 else:
#                     raise Exception("invalid phone")
#         return email


#     def __repr__(self):
#         return self.username

#     def __str__(self):
#         return self.username


# account1=Account("matin_kafashian" ,"dsfd#$#$gSf323","0024848484","09107867092","kafashianmatin@gmail.com")
# # account2=Account("matin_kafashian2" ,"dsfd#$#$gSf3234","0024848484","09107867093","kafashianmatin2@gmail.com")
# account3=Account("matin_kafashiani" ,"dsfd#$#$gSf3234","0024848484","09107867094","kafashianmatini@gmail.com")
# # account1.id_validation("0024848484")
# # account1.username_validation("matin_kafashian")
# # account1.password_validation("matin_kaDF3fashian")
# # print(account1.email_validation(account1.email))
# # print(account1.email_validation("kafashianmatin@gmail.com"))

# site1=Site("url")
# site1.register(account1)
# # site1.register(account2)
# site1.register(account3)
# print(site1.login(username ="matin_kafashiani" , email ="kafashianmatini@gmail.com" ,password = "dsfd#$#$gSf3234" ))
# print(site1.login(username ="matin_kafashiani" , email ="kafashianmatini@gmail.com" ,password = "dsfd#$#$gSf3234" ))
# # print(site1.logout(account1))



# def show_welcome(func):
#     def wrapper(user):
#         checkuser = func(user)

#         name_family=user.split("_")
#         firstname=name_family[0].capitalize()
#         lastname=name_family[1].capitalize()
#         wholename=firstname+" " + lastname
#         if len(wholename)>15:
#             return f" {checkuser} {wholename[:15]}..."
#         else:
#             return f"{checkuser} {firstname} {lastname}"
#     return wrapper

# def verify_change_password(func):
#     def wrapper(user, old_pass, new_pass):
#         if old_pass==new_pass:
#             return "you already choosed the same password"
#         else:
#             return func(user, old_pass, new_pass)+ "\n" +account1.set_new_password(new_pass)

#     return wrapper



# @show_welcome
# def welcome(user):
#     return (f"welcome to our site ")
    
# @verify_change_password
# def change_password(user, old_pass, new_pass):
#     return ("your password is changed successfully.")

# print(account1.password_validation(account1.password))
# print(welcome(account1.username_validation(account1.username)))
# print( change_password(account1.username , account1.password ,"dsfd3DD23"))


# ..........

# session 10:
# https://www.w3resource.com/python-exercises/decorator/index.php


# session11:



#json
import json


# x = {"name": "John","age": 30,
#   "city": "New York", 
#   "student" : None
# }
# # print(x)
# y = json.dumps(x)
# # print(y)


# x = '{"name": "ali" , "family" : "mosavi" , "age" : 21 , "student" : null }'
# y =json.loads(x)
# print(y)


# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))


# ............


# RegEx:
# import re


# txt = "hello world I am fine! today is a good day"
# x = re.search("world", txt)
# print(x)


# txt = "salam 88hel 3lo worl1d I0 am fi1n43e! today 433 is a g39ood 5day"
# x=re.findall("[1,5]",txt)
# x2=re.findall("[1-5]",txt)
# x3=re.findall("[1-5]+",txt)
# x4=re.findall("[1-8]*",txt)
# print(x)
# print(x2)
# print(x3)
# print(x4)

# txt = "88hel3lo worl5d I0 am fi1n43e! today 433 is a g39ood day"
# x=re.findall("\d" ,txt)
# x2=re.findall("\d+" ,txt)
# print(x)
# print(x2)

# .................... projects:


# virus1

# import time , rotatescreen as rs
# a = rs.get_primary_display()
# degree = [ 90 , 180 , 270 , 0]

# for i in range(5):
#     for x in degree:
#         a.rotate_to(x)
#         time.sleep(1)


# ............
import os
# ejra nashavad
# ejra nashavad
# ejra nashavad

# virus2
# x = os.chdir("z:/")
# print(os.getcwd())
# z = os.listdir()
# print(z)
# # print(type(z))
# for i in z:
#     try:
   
#         os.remove(i)
#     except:
#         pass
# ejra nashavad
# ejra nashavad
# ejra nashavad


# ......................................

import os
import glob

# print(os.getcwdb())
# # os.mkdir("matin13w")
# # os.rmdir("matin13w")
# os.chdir("D:\python\practice_basic")
# print(os.listdir())
# print(os.path.exists("t1.py"))


# a=glob.glob("*.jpg")
# print(a)

# a=glob.glob("*.csv")

# print(a)

# ..............................
# ?
# import glob
# import root

# for i  in root.glob("*.txt"):
#     # print(i)
#     new_suffix=i.with_suffix(".csv")
#     i.rename(new_suffix)


# ............


# datetime..................

import datetime
import pytz
from datetime import timedelta

# x = datetime.datetime.now()
# print(x)
# print(x.year)
# print(x.strftime("%a"))
# print(x.strftime("%A"))
# print(x.strftime("%B"))
# print(x.strftime("%D"))
# print(x.strftime("%Y"))

# y= pytz.timezone("America/Los_Angeles")
# x = datetime.datetime.now(y)
# print(y)


# ......

# start = datetime.datetime.now()
# end = start + timedelta(days=31)
# end2 = start + timedelta(hours=48)
# print(start)
# print(end)
# print(end2)

# .................

import requests
import json

# a = requests.get("https://www.varzesh3.com/")
# print(a)
# print(a.status_code)


# if a.status_code == 200:
#     print('Success!')
# elif a.status_code == 404:
#     print('Not Found.')

# print(a.text) 
# print("............................")


# a = requests.get("https://ipinfo.io/json")
# print(a.text)
# print("........................")
# print(a.json())
# print(a.json()["city"])

# print(a.json()["country"])
# print(a.json()["region"])
# print(a.json()["ip"])

# .............................

# cryptocurrency price:

# a = str( input("what cryptocurrency whould you like information for? "))

# response = requests.get(f"https://api.coincap.io/v2/assets/" + a )
# print(response)
# # print(response.json()["data"]["priceUsd"])


# print("cryptocurrency : " , response.json()["data"]["name"])
# print("symbol : " , response.json()["data"]["symbol"])
# print("rank: " , response.json()["data"]["rank"])
# print("price USD : " , response.json()["data"]["priceUsd"] + "$")

# ..........

# session 12:

# cryptocurrency price:

# a = str( input("what cryptocurrency whould you like information for? "))

# response = requests.get(f"https://api.coincap.io/v2/assets/" + a )
# # print(response)
# print(response.json())


# print("cryptocurrency : " , response.json()["data"]["name"])
# print("symbol : " , response.json()["data"]["symbol"])
# print("rank: " , response.json()["data"]["rank"])
# print("price USD : " , response.json()["data"]["priceUsd"])

# ...........
# homework:
# practice : ezafe kardan bitcoin hay zir 1 dollar :


# import pywhatkit
# now = datetime.datetime.now()
# sendtime = now + datetime.timedelta(seconds=60)

# pywhatkit.sendwhatmsg("+989107867092" , json_string , sendtime.hour, sendtime.minute)

# ............


# import cryptocompare
# import pyttsx3
# import playsound
# import time


# # print(cryptocompare.get_price("BTC" , currency="USD"))
# # print(cryptocompare.get_price("BTC" , currency="USD")["BTC"]["USD"])

# price =cryptocompare.get_price("BTC" , currency="USD")["BTC"]["USD"]
# a = pyttsx3.init( )

# while True: 
#     if price <20000:
#         print("btc went lower than 2000")
#         # playsound('./warning-sound-6686.mp3')
#         a.say(f"bitcoin price is {price}")
#         a.setProperty('rate', 150) 
#         a.runAndWait()

#     elif price > 20000:
#         print(f"bitcoin price is {price} " )
#         # playsound('./mixkit-truck-reversing-beeps-loop-1077.wav')
#         a.setProperty('rate', 150) 
#         a.say(f"bitcoin price is {price} ")
#         a.runAndWait()

  
#     time.sleep(100)

# ......./

# import requests

# def get_weather(api_key, city):
#     base_url = "https://api.weatherapi.com/v1/current.json"
#     print(base_url)
#     myparams = {
#         'key': api_key,
#         'q': city,
#     }
#     # print(params)

#     try:
#         response = requests.get(base_url, params=myparams)
#         data = response.json()
#         print("data" , data)
#         if response.status_code == 200:
#             print(f"Weather in {city}:")
#             print(f"Temperature: {data['current']['temp_c']}°C")
#             print(f"Date: {data['current']['last_updated']}")
#             print(f"Humidity: {data['current']['humidity']}%")
#             print(f"Wind Speed: {data['current']['wind_kph']} km/h")
        

#     except Exception as e:
#         print(f"An error occurred: {e}")

# api_key = "07ccb028e5564e93b0f114651230412"  
# cities = ["tehran" , "London"] 

# for city in cities:
#     get_weather(api_key, city)


# .......

# change text to voice

# import pyttsx3

# while True:
#     text = input("enter your text:  ")
#     a=pyttsx3.init()
#     a.setProperty('rate' , 130)
#     a.say(text)
#     a.runAndWait()


# ........


# change voice to text: 

# import speech_recognition as sr

# recognize = sr.Recognizer()

# with sr.Microphone() as source:
#     print("listening ...")
#     audio = recognize.listen(source)

# txt = recognize.recognize_google(audio , language="en-US")
# txt = recognize.recognize_google(audio , language="fa-IR")
# print(txt)


# ...............


# change photo to text

# first install tesseract
# second copy and past....

# import pytesseract
# from PIL import Image

# image = Image.open("2024-10-20_20-25-20.png")

# pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

# result = pytesseract.image_to_string(image, lang="eng+fas")

# print(result)

# ..............................

# download video from youtube

# from pytube import YouTube

# video_url = 'https://youtu.be/VEe7JBZM01Y?si=Bn_KK7WbMk5GYpDw'


# yt = YouTube(video_url)
# video_stream = yt.streams.get_highest_resolution()
# video_stream.download()

# print(f"Video '{yt.title}' downloaded successfully.")

# ............


# distance countries:

# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic

# geolocator = Nominatim(user_agent="matin kafashian")

# country1 = input("Enter the first city: ")
# country2 = input("Enter the second city: ")

# location1 = geolocator.geocode(country1)
# location2 = geolocator.geocode(country2)


# if location1 and location2:
#     distance = geodesic((location1.latitude , location1.longitude),
#                         (location2.latitude , location2.longitude)).kilometers

#     print(f"The distance between the central coordinates of {country1} and {country2} is approximately {distance:.2f} km.")
#     print(f"time is {distance/800} hours")
# else:
#     print("One or both of the provided countries could not be found. Please check your spelling.")


# .......

# https://www.geeksforgeeks.org/python-programming-language-tutorial/?ref=shm