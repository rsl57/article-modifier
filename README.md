# Article Modifier
Slightly alters news articles for the purpose of researching how well AI detection software like GROVER can detect slightly modified articles.

## Setup
Run the following command to install the required dependencies:
```
pip install -r requirements.txt
pip install newsapi-python
pip install requests
pip install beautifulsoup4
pip install nltk
```

## Usage
Use the following format to run the modifier for your own article:
```
python modify.py [input filename]
```
or to have the program generate an article for you
```
python modify.py
```

