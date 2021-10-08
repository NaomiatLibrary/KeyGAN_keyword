import config as cfg
from EvaluateExtraction import EvaluateExtraction
import yake
class YAKE(EvaluateExtraction):
    def __init__(self,opt):
        super(YAKE,self).__init__(opt,"YAKE")
    def extract_keyword(self):
        test_file=open(self.opt.test_file_pass,"r")
        sentences=[lines.strip() for lines in test_file.readlines()]
        answers=[]
        kw_extractor=yake.KeywordExtractor()
        for sentence in sentences:
            keywords=kw_extractor.extract_keywords(sentence)
            answers.append([key for key,score in keywords])
        return answers


yk=YAKE(cfg)
#yk.extract_keyword()
yk.run_evaluation()