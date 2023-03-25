# NLP traning CLI application

## Description

This application is used for analyzing raw text, preprocess it using tokenization, stemming, lemmatization, rules matcher and sentiment analyst to get infromation about each sentence of finance news article.
It characterize each sentence by 5 sentiments: 'negative', 'positive', 'uncertainty', 'litigious','constraining' and giving numerical representation of each of them, summing in 1.

## Usage

Paste article in text variable in app.py and start app.py script

### Installing

In order to use this application you will need to make sure that the following
dependencies are installed on your system:
  - spacy
  - pandas
  - nltk

### Folder structure

Here's a folder structure for a the application:

```
NLPScripts/       # Root directory.
|- data/          # Folder used to store data files, such as tsv, csv ... 
|- app.py         # entry point of application
|- rulers.py      # rulers module
|- sentiments.py  # module with sentiments parser
|- stocksParse.py # module for named entity recognition 
```
## Output


### Text input example
<img title="Text example" alt="Text example" src="/images/boo.svg">

### Output example
<img title="Output example" alt="Output example" src="/images/boo.svg">
