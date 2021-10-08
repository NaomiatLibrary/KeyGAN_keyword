import config as cfg
from EvaluateExtraction import EvaluateExtraction
import nltk
from rake_nltk import Rake
class RAKE(EvaluateExtraction):
    def __init__(self,opt):
        super(RAKE,self).__init__(opt,"RAKE")
    def extract_keyword(self):
        test_file=open(self.opt.test_file_pass,"r")
        sentences=[lines.strip() for lines in test_file.readlines()]
        answers=[]
        nltk.download('stopwords')
        r=Rake()
        for sentence in sentences:
            r.extract_keywords_from_text(sentence)
            keyphrases=r.get_ranked_phrases()
            answers.append(keyphrases)
        return answers

ra=RAKE(cfg)
#ra.extract_keyword()
ra.run_evaluation()