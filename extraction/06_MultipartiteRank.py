import config as cfg
from EvaluateExtraction import EvaluateExtraction
import pke
import string
from nltk.corpus import stopwords
class MultipartiteRank(EvaluateExtraction):
    def __init__(self,opt):
        super(MultipartiteRank,self).__init__(opt,"MultipartiteRank")
    def extract_keyword(self):
        self.read_files()
        answers=[]
        for sentence in self.test_sentences:
            extractor = pke.unsupervised.MultipartiteRank()
            extractor.load_document(sentence,language="en",normalization='stemming')
            pos = {'NOUN', 'PROPN', 'ADJ'}
            stoplist = list(string.punctuation)
            stoplist += ['-lrb-', '-rrb-', '-lcb-', '-rcb-', '-lsb-', '-rsb-']
            stoplist += stopwords.words('english')
            extractor.candidate_selection(pos=pos,stoplist=stoplist)
            extractor.candidate_weighting(alpha=1.1,
                              threshold=0.74,
                              method='average')
            keyphrases=extractor.get_n_best(n=5)
            answers.append([key for key,score in keyphrases])
        return answers


mk=MultipartiteRank(cfg)
mk.run_evaluation()