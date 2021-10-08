import nltk
import config as cfg
from EvaluateExtraction import EvaluateExtraction

class LinguisticApproach(EvaluateExtraction):
    def __init__(self,opt):
        super(LinguisticApproach,self).__init__(opt,"LA")
    def extract_keyword(self):
        test_file=open(self.opt.test_file_pass,"r")
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        sentences=test_file.readlines()
        answers=[]
        for sentence in sentences:
            text = nltk.word_tokenize(sentence)
            text_tagged=nltk.pos_tag(text)
            keyword_list=[]
            for word in text_tagged:
                if word[1] in ["JJ","JJR","JJS","NN","NNS","NNP","NNPS"]:#adjective or (non pro-)noun
                    keyword_list.append(word[0])
            answers.append(keyword_list)
        return answers

la=LinguisticApproach(cfg)
la.run_evaluation()