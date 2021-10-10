# Category-based Extracting Keyword Method Selection with Genetic Programming
This article is only in Japanese.

## 引用
Ayahiko Niimi, Yasunobu Takuma, and Eiichiro Tazaki. Category-based extracting keyword methodselection with genetic programming. 2002.

## 概要
documentをcategoryにわけ、そのcategoryごとに適したkeyword extraction methodをGでPを用いて組み合わせる。

## Genetic Programming
一般的なGPの説明
## Keyword Extractiong Method
### morphome analysis
形態素解析する。我々のlinguistics Approachと大体一緒。
### frequency analysis
多分TF-IDFと大体一緒。
### Serial Noun Extraction
日本語なので連続した名詞を抜き出そうという話。（"発表""会"ではなく"発表会"）
### N-gram
### Association rule
### Text Structure Analysis
TexとかHTMLとかXMLといったドキュメントではいろいろな情報が使える。

## AUTO-SELECTION OF EXTRACTING KEYWORD METHOD WITH GP
fitness functionはaccuracyとnumber of keywordsとcalculation timeを考慮できるように定めた。fitness valueはaccuracyの合計と定めた。（両者の違いは何？）

terminal nodeはkeyword extraction methodsでfunction nodesはどの文章カテゴリを評価するかという状況判断（？）。
それぞれのkeyword extraction methodのparametersはnodeとして定義される（？）。

## Experiments Results
document categorizationとcorrect keyword extractionは人手。