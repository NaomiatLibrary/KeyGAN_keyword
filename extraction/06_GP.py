import config as cfg
from EvaluateExtraction import EvaluateExtraction

class GeneticProgramming(EvaluateExtraction):
    def __init__(self,opt):
        super(GeneticProgramming,self).__init__(opt,"GeneticProgramming")
    def extract_keyword(self):
        test_file=open(self.opt.test_file_pass,"r")
        sentences=test_file.readlines()
        answers=[]
        self.train_model()
        return answers
    def train_model(self):
        pass
