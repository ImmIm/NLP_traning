import spacy
import pandas as pd
import numpy as np
from rulers import get_patterns
from sentiments import parse_sentiments
from spacy import displacy
import classy_classification
from sentiments import  get_data_filters
import nltk
from nltk.corpus import stopwords

text = '''When there’s a lot of bad news, as there is now about US bank failures, investors often wonder how much of it is reflected in stock prices. It’s tempting to say not much, judging by the fact that headline US market gauges like the S&P 500 Index are roughly flat since reports of bank collapses surfaced two weeks ago.

But it’s never entirely obvious why stock markets move the way they do in the short term. Maybe the market isn’t bothered that a handful of regional banks are going bust. Or maybe it is, and those concerns are counterbalanced by optimism around other problems, such as inflation or post-pandemic hiccups. Who knows?

Fortunately, investors don’t have to be mind readers. When they ask whether bad news is reflected in stock prices, often what they want to know is whether stocks have hit bottom. There’s a more reliable way to answer that question.  

Stocks, of course, are a stake in the earnings, cash flow and assets of businesses, but how much investors pay for that stake can vary considerably. Since 1991, the longest period available for the S&P 500, investors paid as much as 30 times forward earnings — that is, expected earnings for the current fiscal year — at the peak of the dot-com bubble in 1999, nearly a 60% premium over the long-term average P/E ratio of 19. They also paid as little as 11 times during the depths of the 2008 financial crisis, more than a 40% discount over the long-term average.

The wide variation in pricing isn’t unique to the S&P 500. Its high and low P/E ratios approximate those of other markets and groups of stocks. Low P/E ratios tend to bottom in the high single digits or low double digits, and high ratios mostly peak in the upper 20s or low 30s. Similar variations are observable when comparing stock prices with assets, cash flows or other financial metrics, although the scale may be different.

Investors can calculate these ratios going back even further using historical financial results. What they’ll find, not surprisingly, is that the lows typically coincide with bad news, including the Great Depression, both world wars, the 1973 oil embargo and the financial crisis. That doesn’t mean bad news is always reflected in stock prices, but low P/E and other ratios are usually a good indication that markets have digested bad news and are near bottom.     

They also tend to signal higher stock prices. Almost always, changes in ratios are driven by changes in stock prices rather than changes in financial results, meaning that when P/E and other ratios reach historical lows, it’s rising stock prices that give them a lift.

So where are we now? The answer often depends on where you look, which is why investors should look beyond the S&P 500. In the following table, I compile forward P/E ratios for a variety of stock indexes from large and small companies to value and growth stocks from around the world. I also show the historical low P/E ratio for each.  

What jumps out is the divergence within and across markets, despite the fact that many flashpoints, including inflation, post-pandemic effects and the continuing Russia-Ukraine war, have a global reach. For starters, there’s a noticeable rift between US and foreign stocks. US stocks are meaningfully more expensive, and US P/E ratios are well above their historical lows. P/E ratios outside the US, on the other hand, are more subdued and closer to past lows, particularly the value stocks.

There’s also a wide divergence between growth and value stocks, particularly outside the US. On average, P/E ratios for growth stocks are roughly 6 to 7 points higher than for value, but when they retreat to historical lows, the spread is typically closer to 1 or 2 points. So it’s unusual to see P/E ratios for value stocks outside the US near historical lows, while growth stocks in the same markets trade 9 to 12 points higher.

Time will tell which markets or groups of stocks have it right. What’s clear from the numbers, though, is that there’s more bad news priced into some stocks than others. 
'''


stops = set(stopwords.words('english'))

text.replace('’', "'")


nlp = spacy.load('en_core_web_md')

nlp.add_pipe("sentencizer")
ruler = nlp.add_pipe('entity_ruler')
nlp.remove_pipe('ner')
ruler.add_patterns(get_patterns())

# Adding stop words
for w in stops:
    nlp.vocab[w].is_stop = True

doc = nlp(text)


data = get_data_filters()

nlp.add_pipe("text_categorizer", 
    config={
        "data": data,
        "model": "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        "device": "gpu"
    }
)

final_data = []
for sentence in doc.sents:
    doc = nlp(sentence.text)
    final_data.append({"sentence": doc.text, "cats": doc._.cats})


for item in final_data:
     print (item["sentence"].strip())
     print (item["cats"])
     print ()

