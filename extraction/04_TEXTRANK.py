import config as cfg
from EvaluateExtraction import EvaluateExtraction
import spacy
import pytextrank
class TEXTRANK(EvaluateExtraction):
    def __init__(self,opt):
        super(TEXTRANK,self).__init__(opt,"TEXTRANK")
    def extract_keyword(self):
        self.read_files()
        answers=[]
        nlp=spacy.load("en_core_web_sm")
        nlp.add_pipe("textrank")
        for sentence in self.test_sentences:
            doc=nlp(sentence)
            answer=[]
            for phrase in doc._.phrases:
                answer.append(phrase.text)
            answers.append(answer)
        return answers

tr=TEXTRANK(cfg)
#tr.extract_keyword()
tr.run_evaluation()