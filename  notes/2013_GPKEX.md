# Gpkex: Genetically programmed keyphrase extraction from croatian texts.
This article is only in Japanese.
## 引用
Marko Bekavac and Jan Snajder. Gpkex: Genetically programmed keyphrase extraction from croatian texts.
In Proceedings of the 4th Biennial International Workshop on Balto-Slavic Natural Language Processing, pp. 43–47, 2013.

[implementation](https://github.com/TakeLab/gpkex)
## 和訳
### 概要
おそらく、GPをkeyphrase extractionに適用した ~~最初の~~ (本人談。実際には一応後述する論文があった（ちょっとずれてるけど）)、そして数少ない論文である。
これとCategory-based Extracting Keyword Method Selection with Genetic
Programming(2002)ぐらいしか見つからなかった。

### introduction
keyphrase assignment...predefined taxonomyからキーフレーズを選ぶ v.s. keyphrase extraction...documentから選ぶ
taxonomyがnot availableか大きすぎる時にはextractionが有効

抽象的な構文木として表されるキーフレーズスコア測定器を進化させる。
ブラックボックスな機械学習に比べてinterpretabilityが高いことが利点として挙げられ、キーフレーズの使い方に関する洞察が得られるだろう。さらに、GPはシンプルなスコア測定器を生成でき、複雑な機械学習と比べて効率的な代替案を提供することができる。
本論文ではクロアチア語のニュース記事のテキストにキーフレーズが付属したデータセット上でその効力を試し、これまでの教師あり・教師なしのアプローチと同等の性能を発揮することがわかった。

## related work
キーフレーズの抽出は候補の抽出と候補のスコアリングというステップがある。
教師付きのアプローチとしては決定木モデル・ベイズ分類法・SVMなどがあり、教師なしのアプローチとしてはクラスタリング・グラフベースの方法・言語モデリングなどが存在する。

本論文ではキーフレーズの抽出をclassification task(binary relevance judgement)として考えているが、GPKEXは連続値のscoring measuresを生成し、ランク付によってキーフレーズは評価される。
## GPKEX
keyphrase canditate extractionとgenetic programming of keyphrase scoring measures(KSMs)のフェーズがある。
### keyphrase canditate extraction
以下の条件を満たすキーフレーズ候補を抽出
- 文の境界を超えていない
- 事前に定義されたPOS(品詞)パターンのどれかにマッチする（section 4で説明）
候補が抽出されたら、それぞれに以下の11個の特徴が割り当てられる。
- 頻度に基づく情報 (tf,idf,tf-idf)
- 位置に基づく情報 (最初の出現位置、最後の出現位置、タイトルへの出現、文章の前1/3,中1/3,後ろ1/3への出現数)
- キーフレーズの表面形式(その長さ、含まれる識別用の単語の数　注:「識別用の単語」とはtf-idfが高い単語上位10単語のこと)
### GP for KSMs
syntax treeで表されるKSMを作る。inner nodesとしてはbinary(+,-,x,/)とunary operators(logA,Ax10,A/10,1/A)を用いる。ランダムに最初のKSMを生成し、fitnessにより進化させる。
#### fitness function
出来上がったKSMをgold-standard keyphrases(それをkeyphraseとして抽出したannotatorの人数とかで決まるランクのことらしい。のちに解説。)と比べる。
いくつかのfitness functionを用いた。simple function(Precision at n や　Mean Reciprocal Rank)では良い結果とならなかったので、独自のfitnessを定義した。これにより、同じ数の正しいkeyphraseを抜き出せたとしても、よりrankの高いkeyphraseを抜き出せた方がfitnessが高くなる。
#### persimony pressure
GPでは、overfittingしないようにparsimony pressureというものがよく用いられる。complexなexpressionsは正規化項によってペナルティが与えられる。
さらに、木の深さは最大17までとした（一般的に用いられている値らしい）
#### Crossover and mutation
crossoverのために選ばれた木について、ランダムに選ばれたノードをrootとするsubtreeを交換する（両方の親の部分木を持つ子孫が選ばれる）。elite strategyを採用してbest-fitted individualを次の世代に残す。
また、mutationとして、ランダムに選ばれたノードから生えている部分木をランダムに成長させた。5%の確率で各KSM木が突然変異し、inner nodeは10%の確率で突然変異する。

populationは500、generationは50で実験を行った。

## Evaluation
### Dataset and Preprocessing
クロアチア語のニュースのデータセットを用いた。
keyphrase candidateとしてN, AN, NN, NSN, V, U (N – noun, A – adjective, S– preposition, V – verb, U – unknown).のみを用いた。training setに存在する全てのキーフレーズのパターンをカバーするには（おそらく品詞のパターンのことを指している）200以上のパターンが必要となるが、キーフレーズの70%を占める6つのパターンのみを候補として用いることとした（候補数は80%削減できた。）また、3語以下のキーフレーズのみを抽出することでキーフレーズの93%をカバーすることができた。
### Evaluation methodology
rank-based evaluation measureを採用した。提案手法がranked list of keyphrasesを生み出すので、それをgold-standard keyphrase ranking(annotatorsの判断を集約して作った、あるkeyphraseをkeyphraseとして選んだannotatorが多ければ多いほどランクが高くなる)と比べる。単語の形態的変異は考慮するがpartial matchは考慮しない。

ranked list of extracted keyphrasesを評価するにはgeneralized average precision(GAP)を用いた。precision(全ての正しいkeyphraseが間違ったkeyphraseより前にrankedされていること)とquality of ranking(より関連のあるkeyphraseが他のkeyphraseより前にrankedされていること)の両方を考慮する。また、rank-based IR measures(Precision and Recall at Rank 10)も採用。

注:Precision@kとは…検索結果のk番目まで見た時のprecision。[参考](https://www.szdrblog.info/entry/2018/12/06/010959)

GPのrandomnessを考慮して、30runsの平均を算出。unpaired t-test(対応のないt検定)でtf-idfによるextractionに比べて優位性を確認する。

### test configurations
parsimony pressureがないA、α=1000のB、α=100のC、そしてAと同じだが全てのPOS patternをkeyphraseとして用いたD

## results
ABCD全てでbaseline(tf-idf)を上回った。DはABCにoutperformedされたのでPOSタグの限定はbeneficialだった。persimony pressureはP@10とR@10においては効果がなかった（が、木が単純化される効果はあった。）