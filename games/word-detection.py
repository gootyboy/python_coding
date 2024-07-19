import nltk

def has_punctuation(user_input):
    if user_input.endswith((".", "!", "?")):
        return True
    else:
        return False
    
def is_question(sentence):
    tokens = nltk.word_tokenize(sentence)
    return '?' in tokens or sentence.lower().startswith(("how", "can", "would", "should", "could"))

while True:    

    sentence = input("type a sentence:")
    punctuation_mark = has_punctuation(sentence)
    if punctuation_mark == True:
        print("sentence is correct.")
    else:
        print("sentence doesn't have a punctuation mark at the end.")
        if is_question(sentence):
            print(f"corrected sentence: {sentence}?")
        else:
            print(f"corrected sentence: {sentence}.")

    print(" ")