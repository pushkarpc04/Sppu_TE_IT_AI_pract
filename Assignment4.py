#Write a program for the Information Retrieval System using appropriate NLP tools (such as
#NLTK, Open NLP, …)
#a. Text tokenization
#b. Count word frequency
#c. Remove stop words
#d. POS tagging

import nltk
from nltk import word_tokenize, FreqDist, pos_tag
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

def text_tokenization(text):
    return word_tokenize(text)

def count_word_frequency(tokens):
    return FreqDist(tokens)

def remove_stop_words(tokens):
    stop_words = set(stopwords.words('english'))
    return [word for word in tokens if word.lower() not in stop_words]

def pos_tagging(tokens):
    return pos_tag(tokens)

def get_user_input():
    text = input("Enter a sentence or a paragraph: ")
    operation = input("Select operation:\n1. Tokenization\n2. Word Frequency\n3. Remove Stop Words\n4. POS Tagging\n5. Exit\nEnter your choice: ")
    return text, operation

def main():
    while True:
        text, operation = get_user_input()

        if operation == '1':
            tokens = text_tokenization(text)
            print("Tokens:", tokens)
        elif operation == '2':
            tokens = text_tokenization(text)
            word_frequency = count_word_frequency(tokens)
            print("Word Frequency:", word_frequency)
        elif operation == '3':
            tokens = text_tokenization(text)
            tokens_without_stopwords = remove_stop_words(tokens)
            print("Tokens without Stop Words:", tokens_without_stopwords)
        elif operation == '4':
            tokens = text_tokenization(text)
            pos_tags = pos_tagging(tokens)
            print("POS Tags:", pos_tags)
        elif operation == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
