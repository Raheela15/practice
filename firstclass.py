a = ["alina",0.45,9]
a[3] = 3
print(a)
# b = ["ali"]
# # # print(a)
# # a[1] = "ali"
# # print(a)

# #print(0 == -0)
# # a.insert(1,4) agr add krna ho ksis b indexinfg k baad 
# a.extend(b) #merge krna ho do varibale ko
# # print(a)
# a.remove(0.45)
# # a.pop() is mein hhamesha indexing k thorugh hum remove krta hain,agr khali choor diya 
# # to wo ultimately end 
# ala ko rmeove kr dega
# a.clear()
# # print(a)

#N E X T C L A S S

# E = [1,2,3,4,5,6,7,8,9]
# print(E[::-1]) #slicing mein format[start:stop:end]

# k = {        #DICTIONARY MEIN SPACING KA CONCEPT NAHI HAI
# "Name" : ["shayan",0.95,23],
# 88 : [99,22]
# }
# k[88] = 33  #agr hum dictionary mein kisi ak list mein change kran to us k liiya update hoga
# print(k) 

# D = {"username": "raheel_123" ,"email" : "ali@gmail.com" }
# D["address"] = "malir cantt karachi"
# print(D)
# print(D.get("DOB" , "YOU ARE AGED GO AND REBORN AGAIN BRUHHHHHH"))
# DOB KA KOI VARIABLE STORE nhi hai to .get 
# sa wo error nahi dega lakin agr .get nahi lagaya to error ata hai terminal mein 


#j = {"pak","ind","africa"} #sets mein order nahi hota just repitation ko ak bar kr dega 
# j[1] # sets mein indexing nahi hoti


# p = {1,3,4,5,5,7,8,8,9,} #sets bn gaya 
# print(p)

# value = {1,2,3,4,5}
# a,b,c,d,e = value
# value.update([10,12])
# value.remove(5)
# value.difference_update([3,4])
# # value.discard(8)
# a,*b = value #koi b variable k saat star lga den to wo aagay k sara data le lega or
# agr mein is k saat ak or varible daal don to wo star wala variable ki aakhri value 
# lega like yaha agr *b ki value hai 3,4,5 agr b k baaad ak or variable de don c to 
# ab c=5 and b become b=3,4 agr ak or variable d dala to b=3,c=4,d=5 
# print(b)
# print(value)


# # 3 r d c l a s s

# # inner working in python+
# a = 23
# b = 23
# c = {1,2,3}
# d = { 
#       "name" : "ali" ,
#        44 : [3,5] ,
#     w"name2" : "Shayan"     
# }
# e = { 
#       "name" : "ali" ,
#        44 : [3,5] ,
#        "name2" : "Shayan"     
# }
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))
# print(id(e))


# conditional statments

# z = int(input("Enter marks: "))  
# if z>80 :
#     print("4")
# else :
#     print("average")


# def pinki(NAME, AGE=22):
#     print(f"my name is {NAME} AND MY AGE IS {AGE}")

# pinki("alena")
# pinki("Shayan", 20)
# pinki("Raheela", 23)
# pinki("ali",9)  
# pinki("aleezay", 23) 

# a = 20            

# def data(): 
#     b = 2 # ghr ka pani
#     c = 5
#     print(b)
#     print(c)
    
# print(a)
# print(a)
# data()

#f u n c t i o n (d e f)

# NAME = "Raheela" 
# def class_1st_test(NAME, AGE, CITY="KARACHI", COUNTRY="PAKISTAN") :
#     print(f"my name is {NAME} and age is {AGE}.i live in {CITY} and my hometown is in {COUNTRY}")
# class_1st_test("aleena", 9)   

# use of r e t u r n 

# NAME = "Raheela" 
# def class_1st_test(NAME, AGE, CITY="KARACHI", COUNTRY="PAKISTAN") :
#     print(f"my name is {NAME} and age is {AGE}.i live in {CITY} and my hometown is in {COUNTRY}")
# class_1st_test("aleena",9)
# class_1st_test("ali",10) 



#s c o o p 

#def fun lganay sa phala global hota hai or colin k baaat jo b likhtay hein wo local hoga

# NAME = "Raheela" 
# def class_1st_test(NAME, AGE, CITY="KARACHI", COUNTRY="PAKISTAN") :
#     print(f"my name is {NAME} and age is {AGE}.i live in {CITY} and my hometown is in {COUNTRY}")
# class_1st_test("aleena", 9)

#l o o p
# a = "hello"
# b = ["hello","ali"]
# f = ["hello","ali","aleena"]
# for i in a:
#     print(i)
#     print(b)
#     print(f)

# # for c in range(2,22,4):
# #     print(c)

# # w h i l e loop
# d = 3
# while d < 20 :
#     d = d + 1
#     print(d)
    
# print("stop it bruh")






 
 
# R   E   V   I   S   I   O   N

# email_id_1 = input("my email:")
# passward_1= input("my passward: ")
# if (email_id_1=="raheela6123@gamil.com" and passward_1=="pinki"):
#     print("correct user")
# else:
#     print("incorrect")

# fruits = {"Apple", "Mango"}
# print(len(fruits))

# set_A = {1, 2, 3, 4}
# # set_B = {3, 4, 5, 6}
# # set_A | (set_B)

# # d = { 
# #        "name" : "ali" ,
# #         44 : [3,5] ,
# #       "name2" : "Shayan"     
# # }
# # print(d["name"])
# # print(d.get("name3","user not found"))





# # uni_portal_id = "raheela123"
# # farig_insaan = ""
# # while uni_portal_id != farig_insaan:
# #     farig_insaan=input("enter trial passward:")
# #     print("beta demaag lga")
# # print("us k id sa tumha kiya ajeeb ")    





# email = "raheela123"
# password ="user@gmail.com"
# user_email =""
# user_pass =""
# while email != user_email and password != user_pass:
#     user_email = input("Enter your email:")
#     user_pass = input("Enter password:")
#     print("Invalid email")

# print("valid email")    


# A =1,2
# print(type(A))


# c l  a  s s

# class Car:
#     def subcar(self,Brand,Model):
#         self.Brand = Brand #local
#         self.Model = Model#local
# newCar = Car()
# newCar.subCar("Tesla", 2027)
# print(newCar.Brand)


# class Car:
#     def __init__(self,Brand,Model):
#         self.Brand = Brand #local
#         self.Model = Model#local

# newCar = Car("Tesla", 2027)
# print(newCar.Brand)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  nnnn













  

