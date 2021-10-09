#when i make scraping.py, I mistakenly make it that cognite the part of word as "extracted keyword"
#so I modify it
import random

class ModifyData:
    def __init__(self,filename):
        self.filename=filename
        self.readfile = open(self.filename+".txt","r")
        self.readkeyfile = open(self.filename+"_keywords.txt","r")
        self.alldata=self.readfile.readlines()
        self.allkeydata=self.readkeyfile.readlines()
        self.readfile.close()
        self.readkeyfile.close()
    def run(self):
        train_file=open(self.filename+".txt","w")
        train_key_file=open(self.filename+"_keywords.txt","w")

        for i,data in enumerate(self.alldata):
            tokenized_data=data.strip().split(" ")
            true_extracted_keys=[]
            keys=self.allkeydata[i].strip().split(",")
            for len_keyphrase in range(1,len(tokenized_data)+1):
                for first_word_in_keyphrase in range(len(tokenized_data)-len_keyphrase+1):
                    keyphrase_candidate=' '.join(tokenized_data[first_word_in_keyphrase:first_word_in_keyphrase+len_keyphrase])
                    for key in keys:
                        if key == keyphrase_candidate:
                            true_extracted_keys.append(key)
            if len(true_extracted_keys)>0:
                train_file.write(data)
                train_key_file.write(','.join(true_extracted_keys)+'\n')



mod=ModifyData("lifehacker")
mod.run()
mod=ModifyData("gizmodo")
mod.run()
