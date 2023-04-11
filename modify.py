import sys
import input_validation
import nltk
import random
import requests
from bs4 import BeautifulSoup
from newsapi import NewsApiClient

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
    # Check if user put in their own article
    if len(sys.argv) >= 2:
        input_validation.check_args(sys.argv)
        input_validation.check_file_valid(sys.argv[1])
        sentences = get_sentences(sys.argv[1])
        new_sentences = replace_random_sentence(sentences)
            
        # Print the new sentences
        for sentence in new_sentences:
            print(sentence)
            print() # Add a blank line for readability
    # if user didnt put in their own file, grab one using news api
    else:
        # Initialize the NewsAPI client with your API key
        try:
            newsapi = NewsApiClient(api_key='88d3ee5544a34e0387ae1c54b74ec5f0')

            # Get a list of top headlines
            top_headlines = newsapi.get_top_headlines()

            # Choose a random article from the list
            article = random.choice(top_headlines['articles'])

            # Fetch the full content of the article by parsing the HTML of the article page
            response = requests.get(article['url'])
            if response.status_code == 200: # success
                soup = BeautifulSoup(response.content, 'html.parser')

                # Find the header section of the article and remove it from the HTML content
                header = soup.find('header')
                if header:
                    header.extract()
                # Find the footer section of the article and remove it from the HTML content
                footer = soup.find('footer')
                if footer:
                    footer.extract()

                article_content = soup.get_text()

                # Print the content of the article
                print(article['url'])
                print(article_content)
            else:
                print(f"Error: Failed to retrieve article content. Response status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: Failed to retrieve article content. Exception: {e}")