from statistics import mean
import os
import nltk
import copy
class EvaluateExtraction:
    def __init__(self,opt,name):
        self.name=name
        self.opt=opt
    def run_evaluation(self):
        # extract keyword and score by precision,recall,F1
        answers=self.extract_keyword()
        #print(answers)
        precision_list=[]
        recall_list=[]
        F1_list=[]
        for i,true_keywords in enumerate(self.test_keywords):
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
    def read_text_file(self,folder_name):
        sentences=[]
        files_paths=os.listdir(folder_name)
        files_paths.sort()
        for file_path in files_paths:
            if file_path[-4:]==".txt":
                file_handle=open(folder_name+file_path,"r",encoding="utf8", errors='ignore')
                sentence=file_handle.read().strip()
                if self.opt.is_already_tokenized:
                    sentences.append(sentence)
                else :
                    tokenized_d=nltk.word_tokenize(sentence.lower())
                    sentence_tokenized=' '.join(tokenized_d)
                    sentences.append(sentence_tokenized)
        return sentences
    def read_key_file(self,folder_name):
        keywords_list=[]
        files_paths=os.listdir(folder_name)
        files_paths.sort()
        for file_path in files_paths:
            if file_path[-4:]==".txt":
                file_handle=open(folder_name+file_path,"r",encoding="utf8", errors='ignore')
                keywords=file_handle.read().splitlines()
                keywords_list.append(keywords)
        return keywords_list
    def read_files(self):
        self.train_sentences=copy.deepcopy(self.read_text_file(self.opt.train_file_pass))
        self.test_sentences=copy.deepcopy(self.read_text_file(self.opt.test_file_pass))
        self.train_keywords=copy.deepcopy(self.read_key_file(self.opt.train_key_file_pass))
        self.test_keywords=copy.deepcopy(self.read_key_file(self.opt.test_key_file_pass))
    def extract_keyword(self):
        answers=[]
        # change here
        return answers