from project import numerical
from project import sentimental
from project import reading_ease

def test_numerical():
    assert numerical("Technology has revolutionized the way we live and communicate. From smartphones to smart homes, innovation surrounds us. However, with great convenience comes new challenges. Are we ready to handle the ethical questions and social impacts that emerge with each advancement?") == 'The most likely language of your text is EN\nThe text length - 273 characters\nThe text length without spaces - 234 characters\nThe number of words - 40 words\nThe number of sentences - 4\nThe most common words are: "the" - (2), "we" - (2), "and" - (2), "to" - (2), "with" - (2)\nThe longest word - "revolutionized", The shortest word - "we"'

def test_sentimental():
    assert sentimental("Technology has revolutionized the way we live and communicate. From smartphones to smart homes, innovation surrounds us. However, with great convenience comes new challenges. Are we ready to handle the ethical questions and social impacts that emerge with each advancement?") == "The text has a positive tone and is relatively subjective."

def test_reading_ease():
    assert reading_ease("Technology has revolutionized the way we live and communicate. From smartphones to smart homes, innovation surrounds us. However, with great convenience comes new challenges. Are we ready to handle the ethical questions and social impacts that emerge with each advancement?") == "The text is difficult to read - College level readability"
