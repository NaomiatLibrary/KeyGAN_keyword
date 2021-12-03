import config as cfg
from EvaluateExtraction import EvaluateExtraction
import nltk
from rake_nltk import Rake
class RAKE(EvaluateExtraction):
    def __init__(self,opt):
        super(RAKE,self).__init__(opt,"RAKE")
    def extract_keyword(self):
        self.read_files()
        answers=[]
        nltk.download('stopwords')
        r=Rake()
        for sentence in self.test_sentences:
            r.extract_keywords_from_text(sentence)
            keyphrases=r.get_ranked_phrases()
            answers.append(keyphrases)
        return answers

ra=RAKE(cfg)
#ra.extract_keyword()
ra.run_evaluation()