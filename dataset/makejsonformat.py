import random
import os
import json
import copy
class MakeJsonformat:
    def __init__(self,dataset):
        self.dataset=dataset
        self.train_file_pass = dataset+"_train_text/"
        self.test_file_pass = dataset+"_test_text/"
        self.train_key_file_pass = dataset+"_train_keywords/"
        self.test_key_file_pass =dataset+"_test_keywords/"
        self.read_files()
        self.output_test_file_pass = dataset+"_test.json"
        self.output_train_file_pass = dataset+"_train.json"
        self.output_valid_file_pass = dataset+"_valid.json"
    def read_text_file(self,folder_name):
        sentences=[]
        files_paths=os.listdir(folder_name)
        files_paths.sort()
        for file_path in files_paths:
            if file_path[-4:]==".txt":
                file_handle=open(folder_name+file_path,"r",encoding="utf8", errors='ignore')
                sentence=file_handle.read().strip()
                sentences.append(sentence)
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
        self.train_sentences=copy.deepcopy(self.read_text_file(self.train_file_pass))
        self.test_sentences=copy.deepcopy(self.read_text_file(self.test_file_pass))
        self.train_keywords=copy.deepcopy(self.read_key_file(self.train_key_file_pass))
        self.test_keywords=copy.deepcopy(self.read_key_file(self.test_key_file_pass))
    def run(self):
        ### kp20k_train.json,kp20k_valid.json,kp20k_test.json
        ### {"title":"","abstract":"here it comes sentence","keywords":"keyword1;keyword2;keyword3"}
        ## train
        f=open(self.output_train_file_pass,"w",encoding="utf8")
        for i in range(len(self.train_sentences)):
            dic={}
            dic["title"]=""
            dic["abstract"]=self.train_sentences[i]
            dic["keywords"]=";".join(self.train_keywords[i])
            f.write(json.dumps(dic)+"\n")
        f.close()
        ## valid
        f=open(self.output_valid_file_pass,"w",encoding="utf8")
        for i in range(len(self.train_sentences)):
            dic={}
            dic["title"]=""
            dic["abstract"]=self.train_sentences[i]
            dic["keywords"]=";".join(self.train_keywords[i])
            f.write(json.dumps(dic)+"\n")
        f.close()
        ## test
        f=open(self.output_test_file_pass,"w",encoding="utf8")
        for i in range(len(self.test_sentences)):
            dic={}
            dic["title"]=""
            dic["abstract"]=self.test_sentences[i]
            dic["keywords"]=";".join(self.test_keywords[i])
            f.write(json.dumps(dic)+"\n")
        f.close()

mjf=MakeJsonformat(os.getcwd()+"/lifehacker")
mjf.run()
mjf=MakeJsonformat(os.getcwd()+"/gizmodo")
mjf.run()
mjf=MakeJsonformat(os.getcwd()+"/semeval")
mjf.run()
