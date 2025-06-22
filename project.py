import time
import sys
import re
from collections import Counter
from langdetect import detect, detect_langs
from textblob import TextBlob
import textstat
import language_tool_python

def numerical(text):
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

def sentimental(text):
    blobtext = TextBlob(text)
    polarity = blobtext.sentiment.polarity
    subjectivity = blobtext.sentiment.subjectivity
    if polarity < -0.1:
        polarity_sentiment = "negative"
    elif polarity > 0.1:
        polarity_sentiment = "positive"
    else:
        polarity_sentiment = "neutral"
    ###
    if subjectivity < 0.25:
        subjectivity_sentiment = "very objective"
    elif subjectivity > 0.25 and subjectivity < 0.5:
        subjectivity_sentiment = "relatively objective"
    elif subjectivity > 0.5 and subjectivity < 0.75:
        subjectivity_sentiment = "relatively subjective"
    elif subjectivity > 0.75:
        subjectivity_sentiment = "very subjective"
    return f"The text has a {polarity_sentiment} tone and is {subjectivity_sentiment}."

def reading_ease(text):
    #to determine reading ease I used Flesch-Kincaid readability test
    total_words = len(text.split())
    total_sentences = len(re.split(r'[.!?]', text)) - 1
    total_syllables = textstat.syllable_count(text)
    readability_score = (206.835 - (1.015 * (total_words / total_sentences))) - (84.6 * (total_syllables / total_words))
    if 90 < readability_score < 100:
        return"The text is very easy to read - 5th grade level readability"
    elif 80 < readability_score <= 90:
        return"The text is easy to read - 6th grade level readability"
    elif 70 < readability_score <= 80:
        return"The text is fairly easy to read - 7th grade level readability"
    elif 60 < readability_score <= 70:
        return"The text is plain English - 8th to 9th grade level readability"
    elif 50 < readability_score <= 60:
        return"The text is fairly difficult to read - 10th to 12th grade level readability"
    elif 30 < readability_score <= 50:
        return"The text is difficult to read - College level readability"
    elif 10 < readability_score <= 30:
        return"The text is very difficult to read - Best understood by university graduates"
    elif 0 < readability_score <= 10:
        return"The text is insanely hard to read - Best understood by professionals"
    else:
        return "Error"

def grammar_check(text):
    output = ""
    print("Processing...")
    tool = language_tool_python.LanguageTool("en-US")
    matches = tool.check(text)
    time.sleep(2)
    output += f"{len(matches)} possible mistakes found\n"
    for match in matches:
        output += f"\nIssue: {match.message}\n"
        output += f"Incorrect: {text[match.offset:match.offset+match.errorLength]}\n"
        output += f"Suggestion: {match.replacements}"

    return output

def comprehensive(text):
    return f"{numerical(text)}\n{sentimental(text)}\n{reading_ease(text)}\n{grammar_check(text)}"

def main():
    print("Welcome to TextAnalyzer! ")
    time.sleep(0.5)
    if len(sys.argv) == 1:
        text = input("Please input the whole text you want to be analyzed - ")
    elif len(sys.argv) == 2:
        try:
            with open(sys.argv[1], 'r') as file:
                text = file.read()
        except FileNotFoundError:
            sys.exit("Error. Mentioned file was not found.")
    else:
        sys.exit("Error. Please input maximum 1 file")
    print("Got it!")
    time.sleep(2)
    print("Processing...")
    x = "."
    for i in range(3):
        time.sleep(1)
        print(x)
        x = x + "."
    time.sleep(3)
    functions = {"numerical" : numerical(text), "sentimental" : sentimental(text), "reading_ease" : reading_ease(text), "grammar_check" : grammar_check(text), "comprehensive" : comprehensive(text)}
    mode = input("Choose the analysis mode: \n1) Numerical (numerical) - different statistics about your text \n2) Sentimental (sentimental) - analysis of the sentiment (tone) of your text \n3) Reading ease (reading_ease) - self-explanatory \n4) Grammar check (grammar_check) - checks for grammatical mistakes in your text\n5) Comprehensive (comprehensive) - all modes in one\n").lower()
    try:
        print(functions[mode])
    except KeyError:
        sys.exit("No such mode exists. Please enter existing mode.")

if __name__ == "__main__":
    main()
