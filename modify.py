import sys
import input_validation
import nltk
import random

# Reads the file and splits the result into its respective sentences
def get_sentences(filename:str):
    # Read the file
    infile = open(filename, "r")
    file_contents = infile.read()

    # Split the file into sentences
    nltk.download('punkt')  
    return nltk.sent_tokenize(file_contents)

def replace_random_sentence(sentences):
    # Select a random sentence to replace
    sentence_to_replace = random.choice(sentences)

    # Generate a random sentence to replace it
    new_sentence = "This is a new random sentence."

    # Replace the selected sentence with the new one
    sentences[sentences.index(sentence_to_replace)] = new_sentence

    return sentences

if __name__ == "__main__":
    # Check the validity of arguments
    input_validation.check_args(sys.argv)
    input_validation.check_file_valid(sys.argv[1])

    sentences = get_sentences(sys.argv[1])
    new_sentences = replace_random_sentence(sentences)
    
    # Print the new sentences
    for sentence in new_sentences:
        print(sentence)
        print() # Add a blank line for readability