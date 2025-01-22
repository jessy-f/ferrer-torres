sentence = "Python is fun and Python is easy to learn!"

new_sentence = ""

for letter in sentence:
    if letter in "aeiou":  
       new_sentence += letter.upper()
    elif letter in "AEIOU": 
       new_sentence += letter
    else:
       new_sentence += letter  
print(new_sentence)
