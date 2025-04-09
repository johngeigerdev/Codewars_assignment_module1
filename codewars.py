##Embarking on Your CodeWars Journey

#Even or Odd
def even_or_odd(number):
    if (number % 2 == 0):
        return "Even"
    else: 
        return "Odd"
    
#Convert a Number to a String
def number_to_string(num):
    # Return a string of the number here!
    return str(num)

#Vowel Count
def get_count(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    
    for letter in sentence:
        if letter in vowels:
            count += 1
            
    return count