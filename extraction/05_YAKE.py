import config as cfg
from EvaluateExtraction import EvaluateExtraction
import yake
class YAKE(EvaluateExtraction):
    def __init__(self,opt):
        super(YAKE,self).__init__(opt,"YAKE")
    def extract_keyword(self):
        self.read_files()
        answers=[]
        kw_extractor=yake.KeywordExtractor()
        for sentence in self.test_sentences:
            keywords=kw_extractor.extract_keywords(sentence)
            answers.append([key for key,score in keywords])
        return answers


yk=YAKE(cfg)
#yk.extract_keyword()
yk.run_evaluation()