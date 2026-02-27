# 1. Reverse a String
text = input("Enter a string: ")
reversed_text = text[::-1]
print("Reversed string:", reversed_text)

# 2. Check Palindrome String
text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome string")
else:
    print("Not a palindrome")

# 3. Count Vowels in a String
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Number of vowels:", count)

# 4. Count Words in a Sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))