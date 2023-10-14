import pandas as pd
import re

df = pd.read_csv('keywords.csv')

def replace_middle_letter(word):
    ''' 
        # Function to replace the middle letter
    '''
    mapping = {'ا': 'a', 
                'ب': 'b', 
                'ت': 't',
                'ث' :'th',
                'ج': 'g',
                'ح': 'h',
                'خ':'kh',
                'د': 'd',
                'ذ': 'z',
                'ر': 'r', 
                'ز': 'z',
                'س': 's',
                'ش' :'sh',
                'ص':'s',
                'ض':'d',
                'ط':'t',
                'ظ':'z',
                'ع':'a',
                'غ':'gh',
                'ف': 'f', 
                'ق': 'q', 
                'ك': 'k', 
                'ل': 'l', 
                'م': 'm', 
                'ن': 'n',
                'ه':'h', 
                'و': 'o',
                'ي': 'e', 
                'ى': 'e',
                'ئ':'e', 
                'a': 'ا', 
                'b': 'ب',
                'c':'س',
                'd': 'د', 
                'e': 'ي', 
                'f': 'ف', 
                'g': 'ج', 
                'h': 'ح',
                'i': 'ي', 
                'j': 'ج', 
                'k': 'ك', 
                'l': 'ل', 
                'm': 'م', 
                'n': 'ن', 
                'o': 'و', 
                'p': 'ب',
                'q': 'ق', 
                'r': 'ر', 
                's': 'س', 
                't': 'ت', 
                'u': 'و', 
                'v': 'ف', 
                'w': 'و', 
                'x': 'ك',
                'y': 'ي', 
                'z': 'ز'}

    if len(word) < 3:
        return word

    middle_index = len(word) // 2
    before_middle = word[:middle_index]
    after_middle = word[middle_index + 1:]

    if word[middle_index] in mapping:
        middle_letter = mapping[word[middle_index]]
    else:
        middle_letter = word[middle_index]

    return  before_middle + "" + middle_letter + '.' + after_middle 

# Replace middle letter in column_A with Arabic equivalents
# df['column_b'] = df['column_A'].apply(lambda word: replace_middle_letter(word))

with open("input.txt", "r", encoding="utf-8") as f:
    input_text = f.read()

words = re.findall(r'\b\w+\b', input_text)

# Apply the function to each word and reconstruct the modified text
modified_words = [replace_middle_letter(word) if word in df['column_A'].values else word for word in words]
modified_text = " ".join(modified_words)

file_path = "output.txt"
# Open the file in write mode and write the string to it
with open(file_path, "w", encoding="utf-8") as file:
    file.write(modified_text)