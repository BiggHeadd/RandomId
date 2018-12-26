#-*- coding: utf-8 -*-
# Edited by bighead 18-12-26

import random
from util import save

#loading the names from corpus
with open("Chinese_Names_Corpus（120W）.txt", 'r', encoding='utf-8')as f:
    data = f.read().splitlines()
name_numbers = len(data) 

#getting input
print("please type how many students do you want to generate")
student_number = int(input())
print("please type the id")
student_id = input()

#generate numbers
students = list()
for i in range(1, student_number+1):
    id_tmp = student_id + str(i).zfill(2)
    random_name = random.randint(0, name_numbers)
    random_score = random.randint(50, 100)
    str_tmp = id_tmp + "\t" + data[random_name] + "\t" + str(random_score)
    students.append(str_tmp)

save(student_id, students)
