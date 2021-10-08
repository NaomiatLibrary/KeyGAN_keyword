from statistics import mean
class EvaluateExtraction:
    def __init__(self,opt,name):
        self.name=name
        self.opt=opt
    def run_evaluation(self):
        # extract keyword and score by precision,recall,F1
        answers=self.extract_keyword()
        #print(answers)
        test_key_file=open(self.opt.test_key_file_pass,"r")
        true_keywords_list=[line.strip().split(',') for line in test_key_file.readlines()]
        precision_list=[]
        recall_list=[]
        F1_list=[]
        for i,true_keywords in enumerate(true_keywords_list):
            #answers[i] matches with true_keywords
            hit=0
            for answer in answers[i][:self.opt.max_key_len]:
                if answer in true_keywords:
                    hit+=1
            p=hit/min(self.opt.max_key_len,len(answers[i])) if min(self.opt.max_key_len,len(answers[i]))>0 else 0
            r=hit/len(true_keywords)
            precision_list.append(p)
            recall_list.append(r)
            F1_list.append(2*p*r/(p+r) if p+r>0 else 0)
        print("### "+self.name+" ###")
        print("PRECISION:\t{}".format(mean(precision_list)))
        print("RECALL:\t{}".format(mean(recall_list)))
        print("F1:\t{}".format(mean(F1_list)))
        print("{},{},{},{}".format(self.name,mean(precision_list),mean(recall_list),mean(F1_list)))
    def extract_keyword(self):
        test_file=open(self.opt.test_file_pass,"r")
        sentences=test_file.readlines()
        answers=[]
        # change here
        return answers