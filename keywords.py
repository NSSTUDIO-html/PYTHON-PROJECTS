import keyword

# List all Python keywords
print("List of Python keywords:")
print(keyword.kwlist)

# Check if a word is a Python keyword
word = "for"
if keyword.iskeyword(word):
    print(f"'{word}' is a Python keyword.")
else:
    print(f"'{word}' is not a Python keyword.")