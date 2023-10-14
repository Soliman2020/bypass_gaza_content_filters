import pandas as pd

# Sample data
data = {'column_A': ['Hello', 'مرحبا', 'Python', 'برمجة', "مصر"]}

# Create a DataFrame
df = pd.DataFrame(data)

# Function to replace the middle letter
def replace_middle_letter(word):
    equivalent_letters = {'ا': 'a', 
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


    # if len(word) < 3:
    #     return word  # If the word has less than 3 characters, return the original word

    middle_index = len(word) // 2
    before_middle = word[:middle_index]
    after_middle = word[middle_index + 1:]

    if word[middle_index] in equivalent_letters:
        middle_letter = equivalent_letters[word[middle_index]]
    else:
        middle_letter = word[middle_index]

    return before_middle +middle_letter+after_middle

# Replace middle letter in column_A with Arabic equivalents
df['column_A'] = df['column_A'].apply(lambda word: replace_middle_letter(word))
 
# df['column_A'] = df['column_A'].apply(lambda x: x[::-1])


print(df)
