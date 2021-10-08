# GP_keyword
Genetic Programming for keyword abstraction

## dataset
`dataset/*.txt` is a collection of sentences, and `dataset/*_keywords.txt` is the collection of keywords.

prese run `dataset/scraper.py` and scrape by youself from these sites:
http://lifehacker.com/
https://gizmodo.com/

### statistics
#### lifehacker
```
#sentences in ./dataset/lifehacker
mean length:    9.441084788029926
max length:     19 (i'm melinda wenner moyer, author of 'how to raise kids who aren't assholes', and this is how i work)
min length:     2 (rip moviepass)
#keywords in ./dataset/lifehacker
mean    1.5635910224438903
max:    7
min:    1
```

## files
```
KeyGAN_keyword
├dataset
│   ├scraper.py...python code for scraping
│   └separatetestdata.py...python coder for separate dataset
├extraction
│   ├01_LA.py...keyword extraction by linguisitic approach
│   ├02_TFIDF...keyword extraction by TF-IDF
│   ├03_RAKE...keyword extraction by RAKE
│   ├04_TEXTRANK...keyword extraction by TextRank
│   ├05_YAKE...keyword extraction by YAKE
│   ├06_GP...keyword extraction by Genetic Programming
│   ├EvaluateExtraction.py...evaluation of keyword extraction
│   └config.py...config for extraction
├.gitignore
└README.md...this file
```

## usage
```
python -m spacy download en_core_web_sm #for TEXTRANK
```

## results
### extraction
![](./extraction/results.png)
