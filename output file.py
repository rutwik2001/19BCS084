n = int(input("enter a n value :")) #n means number of blood banks
blood_bank_name = {}

for i in range(n):
    keys1 = int(input()) #keys1 means index of blood bank name
    values1 = input()  #values1 means name of blood bank
    blood_bank_name[keys1] = values1 
print(blood_bank_name)
areas1 = {}
for i in range(n):
    keys2 = int(input()) #keys2 means index of blood bank name
    values2 = input() # values2 means area of blood bank
    areas1[keys2] = values2
print(areas1)
m = int(input("enter a m value :")) #m means number of blood donation camps
blood_donation_camps = {}
areas2 = {}
for i in range(m):
    keys3= int(input()) #keys3 means index of blood donation camps
    values3 = input() #values3 means name of blood donation camps
    blood_donation_camps[keys3] = values3
    values4 = input() #values4 means area of blood donation camps
    areas2[keys3] = values4
print(blood_donation_camps)
print(areas2)
blood_donor_details = {}
areas3 = {}

y = int(input("enter a y value :")) #y means number of donors

for i in range(y):
    keys4 = input() #keys4 means name of donor
    values5 = input() #values5 means blood group of donor
    blood_donor_details[keys4] = values5
    values6 = input() #values6 means area of donor
    areas3[keys4] = values6
print(blood_donor_details)
print(areas3)

b = int(input("enter a b value :")) #b means number of users

user = {}
user_blood_group = {}
for i in range(b):
    keys5 = int(input()) #keys5 means index of username
    values7 = input() #values7 means name of user
    values8 = input() #values8 means blood group of user
    user[keys5] = values7
    user_blood_group[values7] = values8
print(user)
print(user_blood_group)
c = int(input("enter a c value :")) #c means number of blood camps
check_blood_camps = {}
check_blood_camps_area = {}
for i in range(c):
    keys6 = keys3 #keys6 means index of blood donation camps
    values9 = values3 #values9 means name of blood donation camps
    values10 = values4 #values10 means area of blood donation camps
    check_blood_camps[keys6] = values9
    check_blood_camps_area[keys6] = values10
print(check_blood_camps)
print(check_blood_camps_area)
check_blood_bank = {}
check_blood_bank_area = {}
for i in range(c):
    keys7 =  keys1 #keys7 means index of blood bank name
    values11 = values1 #values11 means name of blood bank
    values12 = values2 #values12 means area of blood bank
    check_blood_bank[keys7] = values11
    check_blood_bank_area[values12] = values12
print(check_blood_bank)
print(check_blood_bank_area)






