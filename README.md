# Article Modifier
Slightly alters news articles for the purpose of researching how well AI detection software like GROVER can detect slightly modified articles.

## Group Members
Derek Avila
Christian Conte
Giselle Fratianni
Ryan Larsen
Cleo Mikeska

## Detailed Description
GROVER, a fake news article generator and detector, has been used to detect falsely generated articles many times before. However in their paper about GROVER (found here), the creators mentioned that GROVER had only been used up to that point to test articles that had been fully generated by AI, not articles that had been slightly modified. This program is designed to put fake sentences into real news articles. There are 2 ways to operate the program:

1. Input a text file containing the body of an article for the program to modify, or
2. Don't input a file for the program to search for a random article online and modify that. (Side note: this method is still a little buggy. If the program finds a news article with an odd formatting, it will sometimes crash before creating the modified article. If this happens, simply run the program again.)

In doing this, we can feed a number of slightly modified articles to GROVER's detection mode to test how well it can detect articles that are only modified and not completely AI generated.

## Setup
Run the following command to install the required dependencies:
```
pip install -r requirements.txt
```

## Usage
Use the following format to run the modifier for your own article:
```
python modify.py [input filename]
```
or to have the program generate an article for you (again, this can sometimes crash, so it may need to be run a couple of times before it works properly):
```
python modify.py
```

## Tests
We included a test file for this project. to run the tests, use the command:
```
python testfile.py
```