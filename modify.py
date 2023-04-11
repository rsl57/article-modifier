import sys
import os
import re
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
            
        # Create a new file name with '_modified' added to the original filename
        file_name, file_extension = os.path.splitext(sys.argv[1])
        new_file_name = file_name + '_modified' + file_extension

        # write new text to file
        with open(new_file_name, 'w') as f:
            for sentence in new_sentences:
                f.write(sentence + "\n")
                
        print(f'New sentences written to file {new_file_name}')
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
                # format article name
                article_title = article['title']
                article_title = article_title.replace("/", "")
                article_title = article_title.replace(" ", "_")
                article_title = re.sub('[^0-9a-zA-Z]+', '_', article_title)
                article_file_name = article_title + "_modified" + ".txt"

                # save article to file system
                print(article['url'])
                with open(article_file_name, "w") as outfile:
                    outfile.write(article_content)

                print(f"Article content saved to {article_file_name}")
            else:
                print(f"Error: Failed to retrieve article content. Response status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: Failed to retrieve article content. Exception: {e}")