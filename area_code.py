#!/usr/bin/python

with open("Phonenumber.txt") as num_file:
    data = num_file.read()

numbers = data.split("\n")

num_tokens = []
for num in numbers:
    num_tokens.append(num.split("-"))

for num in num_tokens:
    print(num[0].strip('()')) 

    



