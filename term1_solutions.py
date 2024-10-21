# session1:
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
#     n=1
#     try:
#         for j in i:
#             if j==i[c]:
#                 print(f"{i} = {j}")
#             c+=1
#             if j!=i[c]:
#                 n+=1
#                 if n == len(i)-1:
#                     print(f"{i} = None")
#     except:
#         pass

"""
a = ["soroosh" , "mohammad" , "shadi" , "matim" , "alii"]

for i in a:
    n = 1
    for c in range(1, len(i)-1):
        if i[c] == i[c+1]:
            print(f"{i} = {i[c]}")
        if i[c] != i[c+1]:
            n+=1
            if n == len(i)-1:
                print(f"{i} = None")
"""
# .....................

# برنامه بنویسید که از کاربر  عدد چند رقمی بگیرد و دو برابر عکس آن را چاپ کند
"""
while True:
    number = input("please enter a number with at least 3 digits: ")
    if number.isdigit() and len(number) > 2:
        reversed_number = ""
        c = 1
        for i in number:
            reversed_number += number[-c]
            c += 1
        result = int(reversed_number) * 2
        print(result)
        break
    else:
        print("Invalid number, try again!")    
"""
# ..............
# primary number : 
# 2 3 5 7 11 13 17 , ....
"""
number1 = int(input("please enter a number : "))
c=0
for i in range(2 , number1):
    if number1%i==0:
        c+=1
        break
if c==0:
    print(f"{number1} is primary number")
else:
    print(f"{number1} is not primary number")
"""
# ............
# homework (moshakhas kardan esmhay moshtarak)
"""
mylist1 = ["amin", "reza" , "matin" , "sara" , "ali" , "vahid", "mohamad" , "hasan"]
mylist2 =["vahid" , "sara" , "hasan" , "mehdi"]

mylist3 = []
for i in mylist1:
    for j in mylist2:
        if i == j:
            mylist3.append(i)

result = "\n".join(mylist3)
print(f"Common names:\n{result}")
"""
# ..........
# homework (Factorial)
"""
result = 1
while True:
    a = input("Enter a number:")
    if a.isdigit():
        for i in range(1 , int(a)+1):
            result *= i
        break
    else:
        print("Invalid number, try again!")

print(result)
"""
# ..............
# Find the biggest number in a list
"""
numbers = input("Please enter a few numbers seprated by a space:").strip().split() 
max_num = int(numbers[0])
for item in numbers:
    if int(item) > max_num:
          max_num = int(item)

print(max_num)
"""
# .............
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
"""
rows = int(input("Enter a number: "))

for i in range(1, rows+2):
    for j in range(1, i+1):
        if j == 1 or j == i:
            print("x", end="")
        elif i == rows+1:
             print("x" * (rows))
             break
        else:
            print("o", end="")
    print("")
"""
# ...........
# homework:
""" 
شما میخواین به برادرزادتون کمک کنین که الفبا رو یاد بگیره. برای همین یه برنامه باید بسازین که یه حرف بگیره و تمام حروف رو با توجه به حرف قبلی به ترتیب نشون بده. با این حال احتمال بهم زدن برنامه به وسیله بچه زیاد هست.
 
اولین قدم باید برنامه ای بنویسین که بچه با زدن تصادفی دکمه ها و وارد کردن حروف بی معنی نتونه  برنامه رو به هم بریزه. تا زمانی که کاربر هیچ حرفی وارد نکنه برنامه ازش درخواست میکنه که یک حرف وارد کنه.

در ادامه برنامه باید تمام حروف قبل از حرف شما رو نشان بده. برای نمایش حروف هر حرف باید حرف به صورت بزرگ و جدا شده از دیگری به وسیله ویرگول باشد. بعد از نمایش 5 حرف به خط بعدی میره. حروفی که وارد میکنیم میتونه  کوچیک یا بزرگ باشه. 

"""
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while True:
    
    letter = input("Enter an letter from English alphabet: ").lower()
    if letter not in alphabet: 
        print("Invalid letter, try again!")
        continue

    letter_index = alphabet.index(letter)
    result = ",".join(alphabet[:letter_index])
    c=0
    for i in result:
        if c % 10 == 0:
            print("")
        c+=1
        print(i.upper(), end="")
    
    break
"""
# ...........
# homework:
# برنامه‌ای بنویسید که یک دیکشنری را دریافت کند و ولیوهایی که بیشتر از یک بار تکرار شدن را داخل دیکشنری دیگر نشان بدهد
# a = {"name1": "matin", "name2": "shamim", "name3": "arash", "name4": "matin" , "name5":"shamim"}
# {'matin': 2, 'shamim': 2}
"""
names = []
result = {}
for i in a:
    names.append(a[i])
print(names)

for j in names:
    counter = names.count(j)
    if counter > 1:
        result[j] = counter

print(result)
"""
# ...........
# homework:

#      *
#      *
# ***********
#  *********
#   *******
#    *****
#     ***
#      * 
"""
a = int(input("Enter a number: ")) #5
b=a+1
for j in range(2):
        print(a*" ", end="*")
        print("")
for i in range(a+1):
    print(i*" ", end=((2*b)-1)*"*")
    b-=1
    print("")
"""
# ...........
# homework: 
# Car that can be switched on/off (OOP)
"""
class Car():

    count = 0

    def __init__(self, make: str, type: str, max_speed: int) -> None:
        self.make = make
        self.type = type
        self.max_speed = max_speed
    
    def __str__(self) -> str:
        return f"{self.make} is a {self.type} car and has a maximum speed of {self.max_speed} km/h"

    def switch_on(self) -> str:
        self.count+=1
        if self.count > 1:
            return "Engine is on, it is not an elevator, stop pressing that button!"
        return "Engine on"
    
    def switch_off(self) -> str:
        return "Engine off" 

car1 = Car("Ford", "sedan", 250)
print(car1)
print(car1.switch_on())
print(car1.switch_on())
print(car1.switch_off())
"""
# ...........
# Session 4
# homework: add loaning system and any other feature of my choice]
"""
import random

class Bank:

    interest_rate = 1

    def __init__(self , account_number , balance):
        self.account_number = account_number
        self.balance = balance
        self.transaction = 0
        self.trasnactions_holder = {}

    def __str__(self):
        return f"your balance is ${self.balance}"
    
    def deposit(self , money1):
        self.balance += money1
        self.transaction+=1
        self.trasnactions_holder[self.transaction] = {
            "type": "deposit",
            "amount": money1,
            # Time to be added later
        }

        return f"${money1} was deposited to your account and your balance is ${self.balance}"
    
    def whithdraw(self , money2):
        if self.balance>money2+20:
            self.balance-=money2
            self.transaction+=1
            self.trasnactions_holder[self.transaction] = {
            "type": "withdraw",
            "amount": money2,
            # Time to be added later
        }
            return f"${money2} was withdrawn from your account and your balance is ${self.balance}"
        else:
            return ("Insufficient funds!")
    
    def lottery(self):
        gifts = ["206" , "" , "100$"  , "iphone-15" , "" ,"" , "" , "candy" ]
        giftscore = int(self.transaction/3)+1
        for _ in range(giftscore):
            mygift = random.choice(gifts)
            if mygift:
                print("Congratulations! your gift is " + mygift)
                break
        if not mygift:    
            print("Sorry, you didn't win anything, go and pray more!")     

    def loan(self): 
        loan_term = {
            "short": (10, 12),
            "medium": (20, 24),
            "long": (30, 36),
        }
        if self.balance <= 1000:
            return "You can't take a loan!"
        elif self.balance > 1000:
            user_loan_term = input("Please choose your preferred loan term short/medium/long:").lower()
            loan_amount = (self.balance * (loan_term[user_loan_term][0])/100) 
            self.deposit(loan_amount)
            loan_installment = round(loan_amount / loan_term[user_loan_term][1], 2) 
            return (f"Your requested loan amount of {loan_amount} is granted on a {user_loan_term} term agreement.\n"
                    f"Your loan duration is {loan_term[user_loan_term][1]} and your loan installment is ${loan_installment} per month.")

    def interest_calculation(self):
        # needs to be added overtime ----> Time
        interest_amount = self.balance * (self.interest_rate/100)
        self.deposit(interest_amount)
        return f"Your monthly interest rate is {self.interest_rate}% which will be added to your balance on monthly basis."  

    def transaction_history(self):
        history = []
        for trans_id, details in self.trasnactions_holder.items():
            history.append(f"Trnsaction ID: {trans_id} - Type: {details["type"]}, Amount: {details["amount"]}")
        
        return "\n".join(history)
    
account1 = Bank("145612531" , 2000)
print(account1.deposit(200))
print(account1.whithdraw(100))
account1.lottery()
print(account1.loan())
print(account1.interest_calculation())
print(account1.transaction_history())
print(account1)
"""
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
"""
class Zoo:
    def __init__(self , zoo_name  ,zoo_territory=100):
        self.zoo_name = zoo_name
        self.zoo_territory = zoo_territory
        self.animals = {}

    def place_animal(self, animal):
        if self.zoo_territory < animal.animal_territory:
            self.zoo_territory = 0 
            print(f"no territory for {animal.animal_name} in {self.zoo_name}")
        else:
            self.animals[animal.animal_name] = animal.animal_territory
            self.zoo_territory -= animal.animal_territory
            print(f"{animal.animal_name} is placed in {self.zoo_name}") 
        
    def sell(self):
        if self.animals == {}:
            print("no animals to sell")
        else:
            biggest_territory = max(self.animals.values())
            largest_animal = [key for key, val in self.animals.items() if val == biggest_territory]
            largest_animal = "".join(largest_animal)
            animal = Animal(largest_animal, biggest_territory)
            self.zoo_territory += biggest_territory
            return animal

class Animal:
    def __init__(self , animal_name  ,animal_territory=20):
        self.animal_name = animal_name
        self.animal_territory = animal_territory

budapest_zoo = Zoo('Budapest Zoo') # Created with 100 territory
berlin_zoo = Zoo('Berlin Zoo', 200) # Created with 200 territory
elephant = Animal('elephant', 50) # Created with 50 territory
giraffe = Animal('giraffe', 40) # Created with 40 territory
zebra = Animal('zebra') # Created with 20 territory

budapest_zoo.sell() # Should print: no animals to sell
budapest_zoo.place_animal(elephant) # Should print: elephant is placed in Budapest Zoo
budapest_zoo.place_animal(giraffe) # Should print: giraffe is placed in Budapest Zoo
budapest_zoo.place_animal(zebra) # Should print: no territory for zebra in Budapest Zoo
berlin_zoo.place_animal(budapest_zoo.sell()) # Should print: elephant is placed in Berlin Zoo
budapest_zoo.place_animal(zebra) # Should print: zebra is placed in Budapest Zoo
"""
# .............
# Shooting game
# The method for selecting a weapon chooses a weapon based on the input so that it can be used later.

# If a weapon with the given name does not exist, an exception should be thrown. This method should be case-sensitive; for example, we don't have a weapon named "submachine gun."

# The method for selecting bullets adds bullets of the given size and quantity to the weapon.
# If any of the following occurs, an exception should be thrown:
# No weapon has been selected.
# The bullet does not match the weapon.
# The quantity is negative. 
# There is no bullet with the given size.

# The method for shooting at a target takes the target’s coordinates, the distance to it, and the coordinates of the point where the weapon is aimed as input, and returns the amount of damage dealt to the target using the formula described below.

# The target is a square with a side length of 10. 
# The coordinates of the bottom-left corner of the square are provided as input. 

# To calculate the output, we proceed as follows:
# If the weapon's range is less than the distance, return 0.
# Otherwise, return the product of the weapon’s power and the bullet’s damage.
# If no weapon has been selected or there are no bullets, an exception should be thrown.
"""
weapons_data = {
    "Submachine Gun": {
        "range": 100,
        "power": 10,
        "bullet_size": 0.5
    },
    "Assault Rifle": {
        "range": 200,
        "power": 20,
        "bullet_size": 1
    },
    "Pistol": {
        "range": 80,
        "power": 8,
        "bullet_size": 0.5
    },
    "Shotgun": {
        "range": 50,
        "power": 40,
        "bullet_size": 4
    },
    "Sniper Rifle": {
        "range": 1000,
        "power": 30,
        "bullet_size": 3
    }
}

bullets_data = {
    "A": {
        "size": 0.5,
        "damage": 1
    },
    "B": {
        "size": 1,
        "damage": 1.5
    },
    "C": {
        "size": 3,
        "damage": 3
    },
    "D": {
        "size": 4,
        "damage": 2
    }
}

class Shooter:

    def __init__(self) -> None:
        self.selected_gun = None
        self.selcted_bullet = None

    def set_gun_by_name(self, name: str) -> None:

        if name not in weapons_data:
            raise KeyError("This weapon doesn't exist.")
        self.selected_gun = weapons_data[name]

    def add_bullet_of_given_size_to_gun(self, size: float, count: int) -> None:

        if self.selected_gun == None:
            raise KeyError("No Weapon has been selected.")

        if size != self.selected_gun["bullet_size"]:
            raise KeyError("Bullet size doesn't match the gun.")
        
        if count < 0:
            raise KeyError("Not enough bullets.")
        
        bullet = "".join([key for key, val in bullets_data.items() if val["size"] == size])
        self.selcted_bullet = bullets_data[bullet]
    
    def shoot_to_target(self, target_x: int,  target_y: int,  target_distance: int,  aim_x: int,  aim_y: int) -> float:

        if self.selected_gun["range"] < target_distance:
            return 0
        
        result = int(self.selected_gun["power"]) * int(self.selcted_bullet["damage"])
        return result



shooter = Shooter()
shooter.set_gun_by_name('Submachine Gun')
shooter.add_bullet_of_given_size_to_gun(0.5, 1)
result = shooter.shoot_to_target(1, 1, 20, 5, 4)
print(result) # result should be 10
"""
# Session 7
# homework
"""
mylist1 = [("amin", "football"), ("reza", "basketball"), ("matin", "ski"), ("sara", "football"), ("ali", "koshti")]
mylist2 = [("mehdi", "football"), ("lili", "karate"), ("vahid", "handball"), ("mohamad", "ski")]
mylist3 = [("asal", "baseball"), ("maryam", "karate"), ("vahid", "box"), ("korosh", "ski")]

# over 2 persons - which sports
# output = {('amin', 'sara', 'mehdi'): 'football', ('matin', 'mohamad', 'korosh'): 'ski', ('lili', 'maryam'): 'karate'}

#[('amin', 'football'), ('reza', 'basketball'), ('matin', 'ski'), ('sara', 'football'), ('ali', 'koshti'), 
# ('mehdi', 'football'), ('lili', 'karate'), ('vahid', 'handball'), 
# ('mohamad', 'ski'), ('asal', 'baseball'), ('maryam', 'karate'), ('vahid', 'box'), ('korosh', 'ski')]


result1 = {}
result2 = {}
final_result = {} 

my_list = mylist1 + mylist2 + mylist3
for name, sport in my_list:
    if sport not in result1:
        result1[sport] = []
    result1[sport].append(name)

for key, val in result1.items():
    result1[key] = tuple(val)

for key, val in result1.items():
    result2[val] = key

for key, val in result2.items():
    if len(key) >= 2:
        final_result[key] = val

print(final_result)
"""
# .....................
# Session 8
# https://quera.org/problemset/33036
"""
class Security:
    def secure(self, info):
        inf = info.split(", ")
        result = []

        for i in inf: 
            if self.is_social_account_info(i):
                result.append(i)

        encrypted_result = []
        for item in result:
            division = item.split("/")
            encrypted_username = self.encrypt(division[1])
            encrypted_account = division[0] + "/" + encrypted_username
            encrypted_result.append(encrypted_account)
    
        for i, element in enumerate(inf):
            if self.is_social_account_info(element):
                inf[i] = encrypted_result.pop(0)
                
        return " ".join(inf)
        
    def is_social_account_info(self, param):
        try:
            if param[0].isupper():
                domain = param.split(".")[1]
                account = param.split("/")[1]
                for i in domain:
                    if i.islower() or i.isnumeric():
                        continue
                    else:
                        return False
                for j in account:
                    if j.isalnum() or j=="_":
                        continue
                    else:
                        return False

                return True
            
            else:
                return False
        except:
            pass

    def encrypt(self, s):
        # if not sorted, the encryption code changes every time code is run
        s = "".join(sorted(s))
        
        b = set(s)

        segments = {}
        result = []

        for i in b:
            for j in s:
                if i == j:
                    break
            segments[i] = s.count(i)

        for key, val in segments.items():
            result.append(key * val)

        result = [key * val for key,val in segments.items()]

        result_sorted = sorted(result, key=lambda x: s.index(x))
        
        code = []
        for i in result_sorted:
            chunk_code = ""
            num = ord(i[0])
            num = abs(num - 96)
            for j in range(1, len(i)+1):
                chunk_code = chunk_code + str(num * j)
            code.append(chunk_code)

        code = "".join(code)

        return code

account1 = Security()
print(account1.encrypt('abcccdd'))
print(account1.secure('FirstName:Ali, LastName:Alavi, BirthDate:1990/02/02, Gender:male, Instagram:www.instagram.com/aalavi, Degree:Master, Twitter:www.twiter.com/alaviii, imdb:www.imdb.com/alavi'))
# Output: 'FirstName:Ali, LastName:Alavi, BirthDate:1990/02/02 Gender:male Instagram:www.instagram.com/12121229 Degree:Master Twitter:www.twiter.com/11212291827 imdb:www.imdb.com/alavi'
"""
# Write a Python program to sort a given list of lists by length and value using lambda.
"""
a = [[2], [1, 3], [0], [0, 7], [9, 11], [13, 15, 17]]
# Sort the list of lists by length and value: [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]
b = sorted(a, key=lambda x: (len(x), max(x)))
print(b)
"""
# ........
"""
# Write a Python program to remove None values from a given list using the lambda function.
a = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
# Remove None value from the said list: [12, 0, 23, -55, 234, 89, 0, 6, -12]
c = []
b = list(filter(lambda x: c.append(x) if x != None else None, a))
print(c)
"""
# ...........
"""
# Write a Python program to remove specific words from a given list using lambda.
# Remove words:
# ['orange', 'black']
# After removing the specified words from the said list:
# ['red', 'green', 'blue', 'white']

a = ['orange', 'red', 'green', 'blue', 'white', 'black']

b = list(filter(lambda x: x if x != "orange" and x != "black" else None, a))

print(b)
"""
# .................
# https://quera.org/problemset/87184

"""
# my way with different naming conventions, transfered based on the exercises file
class Account:
    # def __init__(self, username, password, user_id, phone, email):
    #     self.username = username
    #     self.password = password
    #     self.user_id = user_id
    #     self.phone = phone
    #     self.email = email

    # def username_check(self, username):
    #     username_div = re.split(r"(_)", username)
    #     if username.count("_") != 1 or not username_div[0].isalpha() or not username_div[2].isalpha(): 
    #         raise ValueError("Invalid username!")
    #     else:
    #         return username
                
    # def password_check(self, password):
    #         upper_check = any(i.isupper() for i in password)
    #         lower_check = any(i.islower() for i in password)
    #         num_check = any(i.isnumeric() for i in password) 
    #         if len(password) > 7 and upper_check and lower_check and num_check:
    #              return password
    #         else:
    #              raise ValueError("Invalid password!")

    # def user_id_check(self, user_id):
        
    #     result = 0
    #     control_digit = 0

    #     if not user_id.isnumeric():
    #          return False
        
    #     for i in range(2, len(user_id)+1):
    #          result += (int(user_id[i-1]) * i)

    #     if result % 11 <= 2:
    #         control_digit = result % 11
    #     else: 
    #         control_digit = abs((result % 11) - 11) 
    
    #     if str(control_digit) == user_id[0]:
    #         return user_id
    #     else:
    #         raise ValueError("Invalid User_ID") 
    
    # def phone_check(self, phone):
    #     if phone.startswith("0"):
    #         phone = phone
    #     else:
    #         phone = "0" + phone.replace("+98", "")

    #     if len(phone) != 11 or phone[1] != "9":
    #         raise ValueError("Invalid phone number!")
    #     else:
    #         return phone
        
    # def email_check(self, email):
    #     email_splt = re.split(r"[@.]", email)
    #     print(email_splt)
    #     if (email_splt[0].isalnum() or "_" in email_splt[0] or "-" in email_splt[0]) and (email_splt[1].isalnum() or "_" in email_splt[1] or "-" in email_splt[1]) and (email_splt[2].isalpha() and 1 < len(email_splt[2]) < 6):
    #          return email
    #     else:
    #         raise ValueError("Invalid email!")

    # def email_check(self, email): # ChatGPT
    #     email_splt = re.split(r"[@.]", email)
        
    #     # Check first part
    #     if not re.match(r"^[a-zA-Z0-9_.-]+$", email_splt[0]):
    #         raise ValueError("Invalid email!")
        
    #     # Check second part
    #     if not re.match(r"^[a-zA-Z0-9_.-]+$", email_splt[1]):
    #         raise ValueError("Invalid email!")
        
    #     # Check third part
    #     if not (email_splt[2].isalpha() and 2 <= len(email_splt[2]) <= 5):
    #         raise ValueError("Invalid email!")
        
        # return email
            
    def verify_change_password(self):
        pass
"""
"""
import re
import hashlib

class Account:
    def __init__(self, username, password, user_id, phone, email):
        self.username = username
        self.password = password
        self.user_id = user_id
        self.phone = phone
        self.email = email

    def set_new_password(self, new_password):
        return self.password_validation(new_password)

    def username_validation(self, username):
        username_div = re.split(r"(_)", username)
        if username.count("_") != 1 or not username_div[0].isalpha() or not username_div[2].isalpha(): 
            raise ValueError("Invalid username!")
        else:
            return username

    def password_validation(self, password):
        upper_check = any(i.isupper() for i in password)
        lower_check = any(i.islower() for i in password)
        num_check = any(i.isnumeric() for i in password) 
        if len(password) > 7 and upper_check and lower_check and num_check:
            password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
            return password_hash
        else:
                raise ValueError("Invalid password!")

    def id_validation(self, id):
        result = 0
        control_digit = 0

        if not id.isnumeric():
             return False
        
        for i in range(2, len(id)+1):
             result += (int(id[i-1]) * i)

        if result % 11 <= 2:
            control_digit = result % 11
        else: 
            control_digit = abs((result % 11) - 11) 
    
        if str(control_digit) == id[0]:
            return id
        else:
            raise ValueError("Invalid User_ID") 

    def phone_validation(self, phone):
        if phone.startswith("0"):
            phone = phone
        else:
            phone = "0" + phone.replace("+98", "")

        if len(phone) != 11 or phone[1] != "9":
            raise ValueError("Invalid phone number!")
        else:
            return phone

    def email_validation(self, email): # ChatGPT
        email_splt = re.split(r"[@.]", email) 
        
        # Check first part
        if not re.match(r"^[a-zA-Z0-9_.-]+$", email_splt[0]):
            raise ValueError("Invalid email!")
        
        # Check second part
        if not re.match(r"^[a-zA-Z0-9_.-]+$", email_splt[1]):
            raise ValueError("Invalid email!")
        
        # Check third part
        if not (email_splt[2].isalpha() and 2 <= len(email_splt[2]) <= 5):
            raise ValueError("Invalid email!")
        
        return email

    def __repr__(self):
        return self.username

    def __str__(self):
        return self.username
"""
# ...............................................................................
# ...............................................................................
# ...............................................................................
"""
class Site:
    def __init__(self, url):
        self.url = url
        self.register_users = []
        self.active_users = []

    def show_users(self):
        return "Registered users:" + "\n" + "\n".join(self.register_users)

    def register(self, user):
        if user in self.register_users:
            raise Exception("User already registered!")
        else:
            self.register_users.append(user)
            return "Registeration successful."

    def login(self, **kwargs):
        username = input("Please enter your username:")
        email = input("Please enter your email:")
        password = input("Please enter your password:")
        
        login_id = kwargs.get("username")
        pass_id = kwargs.get("password")

        for user in self.register_users:
            if login_id == user:
                return "Login successful"
            else:
                return "User doesn't exist!"

    def logout(self, user):
        pass

    def __repr__(self):
        return "Site url:%s\nregister_users:%s\nactive_users:%s" % (self.url, self.register_users, self.active_users)

    def __str__(self):
        return self.url
"""
# ...............................................................................
# ...............................................................................
# ...............................................................................
"""
def show_welcome(func):
    def wrapper(user):
        message = func(user)
        
        user_split = user.replace("_", " ").split()
        user_break = []

        for i in user_split:
            user_break.append(i.capitalize())

        user_break = " ".join(user_break)

        if len(user_break) > 15:
            user_div = user_break[:15]
            user_break = user_div + "..."
            return f"{message} {user_break}"
        else:
            return f"{message} {user_split[0]} {user_split[1]}"
            
    return wrapper

def verify_change_password(func):
    def wrapper(user, old_pass, new_pass):
        if old_pass == new_pass:
            return "This password has been used before."
        else:
            return f"{func(user, old_pass, new_pass)}"
    return wrapper

@show_welcome
def welcome(user):
    return (f"Welcome to our site")

@verify_change_password
def change_password(user, old_pass, new_pass):
    return ("your password is changed successfully.")


account1 = Account("salib_alibabaeei", "Aab123123", "4848484200", "09121212121", "salib@alibabaeei.com")
account2 = Account("john_doe", "Gfh123123", "4848484200", "09124569856", "john@email.com")
print(account1.username_validation(account1.username))
print(account1.password_validation((account1.password)))
print(account1.id_validation(account1.user_id))
print(account1.phone_validation(account1.phone))
print(account1.email_validation(account1.email))
print(welcome(account1.username_validation(account1.username)))
print(account1.set_new_password("CcDd123123"))
print(change_password(account1.username, account1.password, "CcDd123123"))

site1 = Site("url")
print(site1.register(account1.username))
print(site1.register(account2.username))
print(site1.show_users())
print("................")
print(site1.login())
"""
# ..............................
# homework:
# practice : ezafe kardan bitcoin hay zir 1 dollar :

# cryptocurrency price:

import requests

# a = str( input("what cryptocurrency whould you like to have the information for? "))

# response = requests.get(f"https://api.coincap.io/v2/assets/{a}")

response = requests.get(f"https://api.coincap.io/v2/assets")

data = response.json()

for item in data['data']:
    if float(item['priceUsd']) < 1:
        print(f"{item['id']} = ${item['priceUsd']}")

# print("cryptocurrency:", response.json()["data"]["name"])
# print("symbol:", response.json()["data"]["symbol"])
# print("rank:", response.json()["data"]["rank"])
# print("price USD:" , response.json()["data"]["priceUsd"])
