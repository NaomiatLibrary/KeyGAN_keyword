from statistics import mean
import numpy as np
class Statistics:
    def __init__(self,filename):
        self.filename=filename
        self.train_file=open(filename+".txt","r")
        self.train_key_file=open(filename+"_keywords.txt","r")
        self.test_file=open(filename+"_test.txt","r")
        self.test_key_file=open(filename+"_test_keywords.txt","r")
    def printstat(self):
        train_lines=[line.strip() for line in self.train_file.readlines()]
        train_keywords=[line.strip().split(",") for line in self.train_key_file.readlines()]
        test_lines=[line.strip() for line in self.test_file.readlines()]
        test_keywords=[line.strip().split(",") for line in self.test_key_file.readlines()]

        train_lines_word_count = [len(line.split(" "))for line in train_lines]
        test_lines_word_count = [len(line.split(" "))for line in test_lines]
        train_test_lines_word_count = train_lines_word_count+test_lines_word_count
        train_test_lines=train_lines+test_lines
        train_key_word_count = [len(keys)for keys in train_keywords]
        test_key_word_count =  [len(keys)for keys in test_keywords]
        train_test_key_word_count = train_key_word_count+test_key_word_count
        print("#sentences in {}".format(self.filename))
        print("number of sentences:\t{}(test data:\t{})".format(len(train_test_lines_word_count),len(test_lines)))
        print("mean length:\t{}".format(mean(train_test_lines_word_count)))
        print("max length:\t{} ({})".format(max(train_test_lines_word_count),train_test_lines[np.argmax(train_test_lines_word_count)]))
        print("min length:\t{} ({})".format(min(train_test_lines_word_count),train_test_lines[np.argmin(train_test_lines_word_count)]))
        print("#keywords in {}".format(self.filename))
        print("mean:\t{}".format(mean(train_test_key_word_count)))
        print("max:\t{}".format(max(train_test_key_word_count)))
        print("min:\t{}".format(min(train_test_key_word_count)))

stat=Statistics("lifehacker")
stat.printstat()
stat=Statistics("lifehacker_all")
stat.printstat()
stat=Statistics("gizmodo")
stat.printstat()
stat=Statistics("gizmodo_all")
stat.printstat()