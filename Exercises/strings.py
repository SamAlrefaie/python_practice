# 1
# Convert a string to upper case
# Example: upper_case("Hello, World!") -> "HELLO, WORLD!"
def upper_case(str):
  return str.upper()
  
# 2
# Remove all whitespace around a string
# Example: remove_whitespace("  Hello, World!  ") -> "Hello, World!"
def remove_whitespace(str):
  return str.strip()

# 3
# Remove all special characters from a string (advanced: keep whitespace)
# Example: remove_special_characters("@Hello- /Everyone\") -> "HelloEveryone" (advanced: "Hello Everyone")
# Example: remove_special_characters("-Redi School of \Digital @Integration") -> "Redi School of Digital Integration"
# Advanced: Make it robust and get any 
def remove_special_characters(string_to_clean):
  # return "TO-DO: Implement this function"
  return ''.join(filter(str.isalnum, string_to_clean)) 

# Advanced solution options:
# 1. Replace
# string.replace("@", "").replace("-", "").replace("/", "").replace("\", "")
# 2. Regex
# import re‚
# re.sub(r'[^\w\s]', '', string) or re.sub("[@-/\]","",string)
# 3. Punctuation
# import string
# test_string.translate(str.maketrans('', '', string.punctuation))


# 4
# Check if a string belongs to a word (advanced: make case insensitive)
# Example: belongs_to("Hello, World!", "Hello") -> True
def belongs_to(str, word):
  if word in str:
    return True


# 5
# Count the number of occurrences of each character in a string 
# return a dictionairy with key as the character and its value as its frequency in the given string
# Example: count_character_occurrences("Banana") -> {"B": 1, "a": 3, "n": 2}
def count_character_occurrences(str):
  # char_freq = {} or char_freq = dict()
  char_freq = {}
  
  # for i in string:
  #     if i in char_freq:
  #         char_freq[i] += 1
  #     else:
  #         char_freq[i] = 1

  for i in  str:
    count = str.count(i)
    char_freq[i] = count # add / update the count of a character
  
  return char_freq


# --------------------------------------------------
# Do not touch these Lines  
test = upper_case("Hello World")
print(("Passed ✅" if test == "HELLO WORLD" else " Failed ❌") + " Test 1 (upper_case)")

test = remove_whitespace(" Hello World   ")
print(("Passed ✅" if test == "Hello World" else " Failed ❌") + " Test 2 (remove_whitespace)")

test = remove_special_characters("@Hello- /Everyone!")
print(("Passed ✅" if test == "HelloEveryone" else " Failed ❌") + " Test 3 (remove_special_characters)")

test =  belongs_to("Hello, World!", "World")
print(("Passed ✅" if test == True else " Failed ❌") + " Test 4 (belongs_to)")

test = count_character_occurrences("Banana")
print(("Passed ✅" if test == {"B": 1, "a": 3, "n": 2} else " Failed ❌") + " Test 5 (count_character_occurrences)")