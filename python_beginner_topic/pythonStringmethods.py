# Exercise 1: Text Formatter 

'''
name=str(input("Enter your name: "))
print(f"Uppercase {name.upper()}")
print(f"Lowercase {name.lower()}")
print(f"Tittle Case {name.title()}")
'''

# Exercise 2: Word Counter

'''
sentence=str(input("Enter a sentence: "))
count=sentence.lower().count("python")
print(f"The word 'python' appears {count} times.")
'''

# Exercise 3: Word Replacer

''''
sentece=str(input("Enter a sentence: ")).lower().replace("python","AI")
print("Word to replace: Python")
print("Replace with: AI")
print(f"Updated sentence: {sentece}")
'''

 # Exercise 4: Sentence Analyzer

'''
sentece=str(input("Enter a sentence: "))
word=sentece.split()
print(f"Words: {word}")
print(f"Word count: {len(word)}")
joinSentece="-".join(word)
print(f"Joined sentence: {joinSentece}")
print(f"Starts with 'hello'? {joinSentece.lower().startswith("hello")}")
print(f"Ends with 'bye'? {joinSentece.lower().endswith("bye")}")
'''

# Exercise 5: Email Formatter & Validator

email=input("Enter your email: ")
formattedEmail=email.strip().lower()
print(f"Formatted Email: {formattedEmail}")
validemail=formattedEmail.endswith("@gmail.com")

if validemail : 
    print("Valid email ✅")
    emailsplit=formattedEmail.split("@")
    print(f"Username: {emailsplit[0]}")
    print(f"Domain: @{emailsplit[1]}")
else:
    print("Unvalid email")