import nltk
import config as cfg
from EvaluateExtraction import EvaluateExtraction

class LinguisticApproach(EvaluateExtraction):
    def __init__(self,opt):
        super(LinguisticApproach,self).__init__(opt,"LinguisticApproach")
    def extract_keyword(self):
        self.read_files()
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        answers=[]
        for sentence in self.test_sentences:
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