import random

class SeparateData:
    def __init__(self,filename):
        self.filename=filename
        self.readfile = open(self.filename+".txt","r")
        self.readkeyfile = open(self.filename+"_keywords.txt","r")
        self.alldata=self.readfile.readlines()
        self.allkeydata=self.readkeyfile.readlines()
        self.readfile.close()
        self.readkeyfile.close()
    def run(self,testsize):
        testsize=min(testsize,len(self.alldata))
        train_file=open(self.filename+".txt","w")
        train_key_file=open(self.filename+"_keywords.txt","w")
        test_file=open(self.filename+"_test.txt","w")
        test_key_file=open(self.filename+"_test_keywords.txt","w")

        number_list=list(range(len(self.alldata)))
        random.shuffle(number_list)
        for num in number_list[:testsize]:
            test_file.write(self.alldata[num])
            test_key_file.write(self.allkeydata[num])
        for num in number_list[testsize:]:
            train_file.write(self.alldata[num])
            train_key_file.write(self.allkeydata[num])


sep=SeparateData("lifehacker")
sep.run(5000)
