import random

class MakeEachFile:
    def __init__(self,filename,dirname):
        self.filename=filename
        self.readfile = open(self.filename+".txt","r")
        self.readkeyfile = open(self.filename+"_keywords.txt","r")
        self.alldata=self.readfile.readlines()
        self.allkeydata=self.readkeyfile.readlines()
        self.readfile.close()
        self.readkeyfile.close()
        self.dirname=dirname+"_text/"
        self.keydirname=dirname+"_keywords/"
    def run(self):
        for i,data in enumerate(self.alldata):
            out_text_file=open(self.dirname+"{:06}.txt".format(i),"w")
            out_key_file=open(self.keydirname+"{:06}.txt".format(i),"w")
            keys=self.allkeydata[i].strip().split(",")
            text=data.strip()
            out_text_file.write(text+'\n')
            out_key_file.write('\n'.join(keys)+'\n')
            



mef=MakeEachFile("lifehacker","lifehacker_train")
mef.run()
mef=MakeEachFile("lifehacker_test","lifehacker_test")
mef.run()
mef=MakeEachFile("gizmodo","gizmodo_train")
mef.run()
mef=MakeEachFile("gizmodo_test","gizmodo_test")
mef.run()
