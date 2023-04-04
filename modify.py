import sys
import input_validation
import nltk

# Reads the file and splits the result into its respective sentences
def get_sentences(filename:str):
    # Read the file
    infile = open(filename, "r")
    file_contents = infile.read()

    # Split the file into sentences
    nltk.download('punkt')
    return nltk.sent_tokenize(file_contents)

if __name__ == "__main__":
    # Check the validity of arguments
    input_validation.check_args(sys.argv)
    input_validation.check_file_valid(sys.argv[1])

    sentences = get_sentences(sys.argv[1])
