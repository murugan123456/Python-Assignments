a = "murugan mmk"
print(a.upper()) #to uppercase all the letters
print(a.lower()) #to lowercase all the letters
print(a.capitalize()) #to capitalize first letter or the parragraph
print(a.title()) #to capitalize the first letter of all words
print(a.count("u")) #show the count of a specific letter
print(a.endswith("mmk")) #check the para end with the specific word or letter
print(a.find("m")) #show the index of a specific letter
print(a.replace("m","n")) #replace the any letter to anothe letter
m="smiley king 1234"
print("is upper = " ,m.isupper()) #check all are capital letters
print("is lower = " ,m.islower()) #check all are small lettters
print("is alpha numeric ",m.isalnum()) #check all are numbers
print("is alpha : ",m.isalpha()) #check all are num and letter
b = "he\nis\ngood" 
print(b) #print actual string 
print(b.splitlines()) #split the all lines and store it as array
print(b.splitlines(True)) #split all the words inclue \n
print(b.split(" ")) #split the word using space when space occue in line it split it next word
c="     murugan      "
print(len(c)) #count the length of para cout the space also
print(len(c.strip())) #count the length of para without count the space 