#TEXT ANALYZER BY MATVEI LOGINOV

#### Video Demo: https://youtu.be/Pt0nPoy0_fM?si=zsPmOVzRYyA6R_0-

#### Description:

**Text analyzer** allows user to _analyze_ text through five unique ways (funstions), these are:

- _Numerical_ (giving a couple of stats about your text)
- _Sentimental_ (analyzing the setniment of your text)
- _Reading ease_ (how easy is it to read your text)
- _Grammar check_ (if you have any major grammatic mistake in your text, it will detect it)
- _Comprehensive_ (all other four combined in a single one)

The project consists of four files:

## README.md

pretty self explanatory

## project.py

The main file, which contains all of the working scripts.

The file begins with all of the imported libraries both internal and external.

### Then it continues with the first function of the file, which is numerical:
'''
output = ""
main_language = detect(text).upper() #detects the language
output += f"The most likely language of your text is {main_language}\n"
detected_langs = detect_langs(text)
if len(detected_langs) > 1:
    output += "A couple of languages were detected: "
    num = 1
    for lang in detected_langs:
        output += f"{num}) {lang[0].upper()} with the probability of {round(lang[1], 2)}, " #lists all detected languages
        num += 1
    output = output[:-2]
    output += "\n"
'''

The code above firstly defines an empty output to then add to it and eventually return it, then it detects the main language, using the imported library **lang_detect**. Then if there is more than 1 language detected in the text, using loop it lists each one of them with the estimated probability (all using **langdetect**)
'''
###
output += f"The text length - {len(text)} characters\n" #normal text length
###
output += f"The text length without spaces - {len(text.replace(" ", ""))} characters\n" #text length without spaces
###
output += f"The number of words - {len(text.split())} words\n" #number of words in the text
###
output += f"The number of sentences - {len(re.split(r'[.!?]', text))-1}\n" #number of sentences in the text
###
words = re.findall(r'\b\w+\b', text.lower())
word_count = Counter(words)
output += "The most common words are: " + ', '.join(f'"{word}" - ({count})' for word, count in word_count.most_common(5)) #lists all the most common words
output += "\n"
###
shortest_word = ""
longest_word = ""
for word in words:
    if len(word) < len(shortest_word) or len(shortest_word) == 0:
        shortest_word = word
    if len(word) > len(longest_word):
        longest_word = word
output += f'The longest word - "{longest_word}", The shortest word - "{shortest_word}"' #prints the longest and shortest word
return output
'''
Then goes the rest of the script, which is mostly lots of small functions:
- the first one counts total length of the text using built-in len() method
- the second one counts every character, which is not a space, just replacing every space with an empty string and counting its length.
- the third one counts words, basically in the same way as the previous one, just counting words now.
- the fourth one counts sentences by separating all the exclamation marks, question marks and dots.
- then goes the function which counts the occurence of each word using Counter() method from the integrated collections library
- then goes the function which calculates the length of each word and then presents the shortest and the longest ones.

### The second major function of project.py is sentimental:

Sentimental uses the imported TextBlob library, which uses machine learning to determine polarity and sentiment of the given text.
The script analyzes the two and then, categorizes it from negative to positive tone and from subjective to objective and then presents it to the user.

### The third major function is reading ease function:

This function once again analyzes the total amount of words, sentences and syllables (using textstat library which does it automatically) and then makes the use of Flesch-Kincaid formula, which mechanically estimates readability of the text based on the parameters and a couple of constants. Later it categorizes these results and presents to the user.

### The fourth major function is grammar check function:

This function uses imported library called language-tool-python and its check() method, which analyzes words in the text for any grammatical mistakes. If any are used, it will print out every single one with a possible explanation.

### The fifth major function is comprehensive function:

This function is pretty straightforward - it combines all the other functions into a single one and presents the result to the user.

### Main function

The function starts with a welcome message and directly prompts the user to enter the text he wants to analyze. The user also has an option to enter the name of the file with the text in the command line.
Then the program prompts the user to choose the mode, which he wants to analyze his text with, which is essentially a choice between previously explained five functions.

## requirements.txt

This file contains five libraries that need to be installed before utilizing project.py.
'''
textblob
langdetect
language-tool-python
textstat
pytest
'''

## test_project.py

test_project.py tests three first functions to ensure they are working properly using pytest library.

THANKS FOR CS50!
