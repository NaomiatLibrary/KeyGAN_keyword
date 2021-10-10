# Ranking Keyphrases from Semantic and Syntactic Features of Textual Terms
This article is only in Japanese.
## 引用
Raquel Silveira, Vasco Furtado, and Vladia Pinheiro.  Ranking keyphrases from semantic and syn-tactic features of textual terms. In2015 Brazilian Conference on Intelligent Systems (BRACIS), pp.134-139. IEEE, 2015.

## 概要
## Introduction
keyphraseをrankingする良い関数を見つけたい。
keyword extractionのためのranking functionを重み付けする。
異なるdomainでは異なるapproachが必要。統計的手法と意味的手法で用いられる属性について重みをつけるためにGPを用いる。

## Related work for keyphrases extraction
### syntactic
TFIDF,KEA(supervised leaning methodsの一つ、TFIDF,単語の出現位置,キーフレーズとして出現した回数を考慮して学習を行う。)など
### semantic
TextRank,Wikify!,Ranking SVMとか

## GP
inner nodeとしては+(sum)のみを用いた。葉は、外部関数を通じて計算されたevidenceの値を受け取る変数(semantic relatedness,first ocurrence,wikipedia's keyphraseness,tfidfといった数値)。

## others
Random ForestsとかLogistic Regiression(こっちは可視化性もある)の方が結果が良かった。
