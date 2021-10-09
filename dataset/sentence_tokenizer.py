import nltk
class Tokenize:
    def __init__(self,root):
        self.root=root
        self.path=open(root+".txt","r")
        self.path2=open(root+"_all.txt","r")
        self.data=self.path.readlines()
        self.data2=self.path2.readlines()
        self.path.close()
        self.path2.close()
    def run(self):
        path1=open(self.root+".txt","w")
        path2=open(self.root+"_all.txt","w")
        for d in self.data:
            tokenized_d=nltk.word_tokenize(d.lower())
            path1.write(' '.join(tokenized_d)+'\n')
        for d in self.data2:
            tokenized_d=nltk.word_tokenize(d.lower())
            path2.write(' '.join(tokenized_d)+'\n')


tkn=Tokenize("lifehacker")
tkn.run()
tkn=Tokenize("gizmodo")
tkn.run()

