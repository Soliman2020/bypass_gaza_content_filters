import pandas as pd
import re
import random


df = pd.read_csv('keywords.csv')
df['column_A'] = df['column_A'].str.strip() # Remove white spaces
df['column_B'] = df['column_A'].apply(lambda word: "ال" + word) # Add "ال" before each word

def replace_middle_letter(word):
    ''' 
        # Function to replace the middle letter
    '''
    mapping = {'ا': 'ⴶ', 
                'ب': 'Ų', 
                'ت': 'Ü',
                'ث' :'Û',
                'ج': "ζ",
                'ح': 'Շ',
                'خ':"ζ'",
                'د': 'כ',
                'ذ': "כ'",
                'ر': 'ノ', 
                'ز': 'ژ',
                'س': 'ω',
                'ش' :'ฬ',
                'ص':'ם',
                'ض':"'ם",
                'ط':'あ',
                'ظ':'お',
                'ع':'દ',
                'غ':"'દ",
                'ف': 'פֿ', 
                'ق': 'פֿ', 
                'ك': 'ـگـ', 
                'ل': 'ł', 
                'م': 'ჲ', 
                'ن': '๒',
                'ه':'θ', 
                'و': 'Ջ',
                'ؤ':"Ѯ",
                'ي':"'Ѧ",
                'ى':"'Ѧ",
                # 'ي': 'អ្', 
                # 'ى': 'អ្',
                'ئ':'ტ', 
                'ء':'ར'}

    if len(word) < 3:
        return word

    middle_index = len(word) // 2
    before_middle = word[:middle_index]
    after_middle = word[middle_index + 1:]

    if word[middle_index] in mapping:
        middle_letter = mapping[word[middle_index]]
    else:
        middle_letter = word[middle_index]
    options = [",", ";", ":", "?"]
    # Randomly select one of the strings
    selected_string1 = random.choice(options)
    selected_string2 = random.choice(options)
    # return  before_middle + selected_string + middle_letter + selected_string + after_middle 
    return before_middle + selected_string1 + ''.join(random.choice([' ', '']) + c for c in middle_letter) + selected_string2 + after_middle

# Replace middle letter in column_A with Arabic equivalents
# df['column_b'] = df['column_A'].apply(lambda word: replace_middle_letter(word))

with open("input.txt", "r", encoding="utf-8") as f:
    input_text = f.read()

words = re.findall(r'\b\w+\b', input_text)

# Apply the function to each word and reconstruct the modified text
# modified_words = [replace_middle_letter(word) if word in df['column_A'].values else word for word in words]
modified_words = [replace_middle_letter(word) if word in df['column_A'].values or word in df['column_B'].values else word for word in words]
modified_text = " ".join(modified_words)

file_path = "output.txt"

# Add RTL markers or use HTML for RTL direction
rtl_text = "\u202E" + modified_text + "\u202C"

# Open the file in write mode and write the string to it
with open(file_path, "w", encoding="utf-8") as file:
    file.write(rtl_text)