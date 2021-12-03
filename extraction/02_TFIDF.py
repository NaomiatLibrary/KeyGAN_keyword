import config as cfg
from EvaluateExtraction import EvaluateExtraction
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
class TFIDF(EvaluateExtraction):
    def __init__(self,opt):
        super(TFIDF,self).__init__(opt,"TFIDF")
    def extract_keyword(self):
        self.read_files()
        answers=[]
        cv=CountVectorizer(ngram_range=(1,3))
        word_count_vector=cv.fit_transform(self.train_sentences)
        tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
        tfidf_transformer.fit(word_count_vector)
        feature_names=cv.get_feature_names_out()
        for sentence in self.test_sentences:
            tf_idf_vector=tfidf_transformer.transform(cv.transform([sentence]))
            sorted_items=self.sort_coo(tf_idf_vector.tocoo())
            keyphrases=self.extract_topn_from_vector(feature_names,sorted_items)
            answers.append(keyphrases)
        return answers
    def sort_coo(self,coo_matrix):
        tuples=zip(coo_matrix.col, coo_matrix.data)
        return sorted(tuples,key=lambda x:(x[1],x[0]), reverse=True)
    def extract_topn_from_vector(self,feature_names, sorted_items, topn=10):
        sorted_items=sorted_items[:topn]
        feature_vals=[]
        for idx, score in sorted_items:
            feature_vals.append(feature_names[idx])
        return feature_vals

ti=TFIDF(cfg)
#ti.extract_keyword()
ti.run_evaluation()