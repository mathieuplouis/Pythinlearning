import string
import random
import re

# This is a sample Python script.


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# class Customer:
#     def __init__(self, cust_id, name, age, wallet_balance):
#         self.cust_id=cust_id
#         self.name=name
#         self.age=age
#         self.__wallet_balance=wallet_balance
#
#     def set_wallet_balance(self,amount):
#         if 0 < amount < 1000:
#             self.__wallet_balance = amount
#
#     def get_wallet_balance(self):
#         return self.__wallet_balance
#
#
#     # def update_balance(self, amount):
#     #     if 0 < amount < 1000:
#     #         self.__wallet_balance += amount
#
#     def show_balance(self):
#         print("The balance is :", self.wallet_balance)
#
#
# cust1 = Customer(100,"mathieu",43,1000)
# cust1.set_wallet_balance(120)
# # cust1.show_balance()
# print(cust1.get_wallet_balance())
# """
# Athlete exercise
# """
#
# class Athlete:
#     def __init__(self, name, gender):
#         self.__name = name
#         self.__gender = gender
#
#     def running(self):
#         if (self.__gender == "girl"):
#             print("150mtr running")
#         else:
#             print("200mtr running")
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_gender(self, gender):
#         self.__gender = gender
#
#     def get_name(self):
#         return self.__name
#
#     def get_gender(self):
#         return self.__gender
#
# athlete = Athlete("Maria","girl")
#
# print(athlete.get_name(), athlete.running())

# """
# University admission exercice
# """
#
#
# class Student:
#     def __init__(self, student_id, age, marks):
#         self.__student_id = student_id
#         self.__age = age
#         self.__marks = marks
#
#     def validate_marks(self, marks):
#         if 0 >= marks >= 100:
#             return True
#         else:
#             return False
#
#     def validate_age(self, age):
#         if age > 20:
#             return True
#         else:
#             return False
#
#     def check_qualication(self, age, marks):
#         if self.validate_age(age) and self.validate_marks(marks):
#             if marks > 65:
#                 return True
#             else:
#                 return False
#
#         else:
#             return False
#
#     def set_student_id(self, student_id):
#         self.__student_id = student_id
#
#     def set_age(self, age):
#         self.__age = age
#
#     def set_marks(self, marks):
#         self.__marks = marks
#
#     def get_student_id(self):
#         return self.__student_id
#
#     def get_age(self):
#         return self.__age
#
#     def get_marks(self):
#         return self.__marks
#
# student1 = Student(1001, 42, 90)
#
# print(student1.get_student_id(), student1.get_age(),student1.get_marks())


# class Mobile:
#     __discount = 50
#
#     def __init__(self, price, brand):
#         self.price = price
#         self.brand = brand
#
#     def purchase(self):
#         total = self.price - self.price * Mobile.__discount / 100
#         print(self.brand, "Mobile with price ", self.price, "is available at: ", total)
#
#     @classmethod
#     def enable_discoiunt(cls):
#         cls.set_discount(50)
#
#     @classmethod
#     def disable_discount(cls):
#         cls.set_discount(0)
#
#     @classmethod
#     def get_discount(cls):
#         return cls.__discount
#
#     @classmethod
#     def set_discount(cls, discount):
#         cls.__discount = discount
#
#     @staticmethod
#     def calculate_tax(cust_type):
#         if (cust_type == 'member'):
#             return 10
#         else:
#             return 20
#
#
# print("Tax percent to be paid by members: ", Mobile.calculate_tax('member'))
# print("Tax percent to be paid by non- members: ", Mobile.calculate_tax('non-member'))
#
#
# mobile1 = Mobile(20000, "Apple")
# mobile2 = Mobile(30000, "Apple")
# mobile3 = Mobile(5000, "Samsung")
# Mobile.disable_discount()
# mobile1.purchase()
# Mobile.enable_discoiunt()
# mobile2.purchase()
# Mobile.disable_discount()
# mobile3.purchase()

# class Classroom:
#     classroom_list = ["Science_room", "Math_room", "Algebra_room", "Technology_room"]
#
#     @classmethod
#     def search_classroom(cls, class_room, ):
#         for item in Classroom.classroom_list:
#             if class_room == item:
#                 print("Found")
#                 break
#             else:
#                 print(-1)
#                 break
#
#
# Classroom.search_classroom("Dentist_room")

# class Ticket:
#     counter = 0
#     ticket_id = 0
#
#     # destination = ["Mumbai", "Chennai", "Pune", "Kolkata"]
#
#     def __init__(self, passenger_name, source, destination):
#         self.__passenger_name = passenger_name
#         self.__source = source
#         self.__destination = destination
#
#     def validate_source_destination(self, source, desti):
#         if source == "Delhi" and (
#                 desti in desti == "Mumbai" or desti == "Chennai" or desti == "Pune" or desti == "Kolkata"):
#             return True
#         else:
#             return False
#
#     def get_destination(self):
#         return self.__destination
#
#     def get_source(self):
#         return self.__source
#
#     def get_ticket_id(self):
#         ticket_id = self.get_destination() + self.get_destination()[0] + str(Ticket.counter + 1)
#
#     def generate_ticket(self, source, destination):
#         if not self.validate_source_destination(source, destination):
#             ticket_id = None
#             print("The source or the destination is incorrect")
#         else:
#             self.get_ticket_id()
#             print(self.__passenger_name, self.get_ticket_id(), self.get_source(), self.get_destination())
#
#
# ticket = Ticket("Mathieu Pierre Louis", "Delhi", "Mumbai")
#
# ticket.generate_ticket("Delhi", "Mumbai")
"""
Aggregation -- has a relationship
"""

# class Customer:
#     def __init__(self, name, age, phone_no, address):
#         self.name = name
#         self.age = age
#         self.phone_no = phone_no
#         self.address = address
#
#     def view_details(self):
#         print(self.name, self.age, self.phone_no)
#         print(self.address.get_door_no(), self.address.get_street(), self.address.get_zipcode())
#
#     def update_details(self, add):
#         self.address = add
#
#
# class Address:
#     def __init__(self, door_no, street, area, zipcode):
#         self.__door_no = door_no
#         self.__street = street
#         self.__area = area
#         self.__zipcode = zipcode
#
#     def get_door_no(self):
#         return self.__door_no
#
#     def get_street(self):
#         return self.__street
#
#     def get_area(self):
#         return self.__area
#
#     def get_zipcode(self):
#         return self.__zipcode
#
#     def set_door_no(self, value):
#         self.__door_no = value
#
#     def set_street(self, value):
#         self.__street = value
#
#     def set_area(self, value):
#         self.__area = value
#
#     def set_zipcode(self, value):
#          self.__zipcode = value
#
#     def update_address(self):
#         pass
#
#
# address1 = Address(11, 5777, "5th pl", 32962)
# address2 = Address(12, 5778, "6th pl", 32962)
# customer = Customer("Mathieu", 43, 1234, address1)
# customer.view_details()

""" Weaker relationship -- Aggregation and association"""
# class Customer:
#     def __init__(self, name, age, phone_no):
#         self.name = name
#         self.age = age
#         self.phnone_no = phone_no
#
#     def purchase(self, payment):
#         if payment.type == "card":
#             print("Paying by card")
#         elif payment.type == "e-wallet":
#             print("Paying by e-wallet")
#         else:
#             print("Paying by cash")
#
#
# class Payment:
#     def __init__(self, type):
#         self.type = type
#
#
# payment = Payment("card")
# customer = Customer("Mathieu", 43, 6412330404)
# customer.purchase(payment)


""" Weaker dependency -- A part an object beeing passed as parameter as in the above example, an object can be 
created  locally inside a method This is also a weaker dependency which does not display in the class diagram """

# class Customer:
#     def __init__(self, name, customer_type, bill):
#         self.name = name
#         self.bill = bill
#         self.customer_type = customer_type
#
#     def calculate_bill(self):
#         taxes = Tax(self.customer_type)
#         final_bill = self.bill * taxes.tax_details(self.customer_type)
#         return final_bill
#
#
# class Tax:
#     def __init__(self, customer_type):
#         self.customer_type = customer_type
#
#     def tax_details(self, customer_type):
#         if customer_type == "Student":
#             return 5
#         else:
#             return 10
#
#
# customer = Customer("Dalica", "Student", 100)
# print(customer.calculate_bill())
""" Need to return on this to complete it."""
# class Freight:
#     counter = 198
#     # freight_charge
#     freight_id = 200
#
#     def __init__(self, recipient_customer, from_customer, weight, distance):
#         self.__recipient_customer = recipient_customer
#         self.__from_customer = from_customer
#         self.__weight = weight
#         self.__distance = distance
#


#     def validate_weight(self, weight):
#         return weight % 5 == 0
#
#     def validate_distance(self):
#         return 500 >= self.__distance <= 5000
#
#     def get_freight_charge(self, weight, distance):
#         return self.__weight / self.__distance
#
#
#     def forward_cargo(self, from_customer, recipient_customer):
#
#
#     @classmethod
#     def get_freight_id():
#         freight_id = Freight.freight_id + 2
#         return freight_id
#
#     def get_recipient_customer(self):
#         return self.__recipient_customer
#
#     def get_from_customer(self):
#         return self.__recipient_customer;
#
#     def get_weight(self):
#         return self.__weight
#
#     def get_distance(self):
#         return self.__distance
#
#
# class Customer:
#     def __init__(self, customer_id, customer_name, address):
#         self.__customer_id = customer_id
#         self.__customer_name = customer_name
#         self.__address = address
#
#     def validate_customer_id(self, customer_id):
#         pattern = re.compile("^[1-9]{6}")
#         if pattern.match(customer_id):
#             return True
#         else:
#             return False
#
#     def get_customer_id(self):
#         return self.__customer_id
#
#     def get_customer_name(self):
#         return self.__customer_name
#
#     def get_address(self):
#         return self.get_customer_address()
#
#
# customer = Customer("246813", "Mathieu", "Littleton")
# print(customer)
#
# print(customer.validate_customer_id("246813)"))


"""Coorg Fruit Farm a retails chain want to keep track of customers who buy fruits from them and also the billing process"""


class FruitInfo:
    fruit_name_list = ["Apple", "Guava", "Orange", "Grape", "Sweet Lime"]
    fruit_price_list = [200, 80, 70, 110, 60]

    @staticmethod
    def get_fruit_price(fruit_name):
        fruit_price_dict = dict(zip(FruitInfo.fruit_name_list, FruitInfo.fruit_price_list))
        return fruit_price_dict[fruit_name]

    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.fruit_name_list

    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.fruit_price_list


class Purchase:
    purchase_id = 100

    def __init__(self, customer, fruit_name, quantity):
        self.customer = customer
        self.fruit_name = fruit_name
        self.quantity = quantity

    @staticmethod
    def get_purchase_id():
        purchase_id = "P" + str(Purchase.purchase_id + 1)
        return purchase_id

    def get_customer(self):
        return self.customer

    def get_quantity(self):
        return self.quantity

    @staticmethod
    def calculate_price(fruit_name, quantity):
        price = FruitInfo.get_fruit_price(fruit_name)
        total_price = price * quantity
        if price == max(FruitInfo.get_fruit_price(fruit_name)) and quantity > 1:
            total_price = total_price - (total_price * 2) / 100
        if price == min(FruitInfo.get_fruit_price(fruit_name)) and quantity >= 5:
            total_price = total_price - (total_price * 5) / 100
        if Customer().get_customer_type() == "wholesale":
            total_price = total_price - (total_price * 10) / 100
        Purchase.get_purchase_id()
        return total_price


class Customer:

    def __init__(self, customer_name, customer_type):
        self.customer_name = customer_name
        self.customer_type = customer_type

    def get_customer_name(self):
        return self.customer_name

    def get_customer_type(self):
        return self.customer_type


cust = Customer("Mathieu Pierre Louis", "wholesale")

print(FruitInfo.get_fruit_price("Apple"))
purchase = Purchase(cust, "Apple", 5)
total_price = Purchase.calculate_price("Apple", 5)
print(purchase.get_purchase_id(), cust.get_customer_name(), cust.get_customer_type(), total_price)
