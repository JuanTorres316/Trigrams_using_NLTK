# -*- coding: utf-8 -*-

#code sample to make a new list from and existing list

#first list
import re
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



#you can loop to add the items from one list to another, or do list comprehension
newNumber = []
for number in numbers:
    newNumber.append(number)
   
#these 3 lines of code are the same as the following lines of code
    
newNumbers = [number for numbers in numbers]

#you can also do conditional statements after the list comprehension

newNumbers = [number for numbers in numbers if number <=5]

#you can also make a list from two lists, the following will list all items not contained in another list

numbers2 = [1, 3, 5, 7, 9]

newNumbers = (number for number in numbers if number not in numbers2)

print(newNumbers)

sentence = "I was born in 1988"

"""will return an re.Match Object with the span and the whole sentence, the 
. will match all, and the * will allegedly match anything that is more than one span"""

re.match(r".*", sentence)

re.sub(r"\d","",sentence)


#testing out sub function

sentence2 = "I love Avengers avengers"

print(re.sub(r"avengers","The", sentence2,1, flags=re.I))