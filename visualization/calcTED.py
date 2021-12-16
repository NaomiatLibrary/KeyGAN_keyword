from zss import simple_distance,distance
import os
import re
import itertools
import networkx as nx
import numpy as np
import string
import matplotlib.pyplot as plt
import copy
leaf_nodes=["Tf","Idf","Tfidf","First","Last","NumberF","NumberS","NumberT","Length","Rare","Title", "Noun","Adv","Verb","Adj"]
nonleaf_nodes=["Plus","Minus","Times","Div","Log","Inv","TimTen","DivTen"]
twochild_nodes=["Plus","Minus","Times","Div"]

class DepthWeightedNode(object):

    def __init__(self, label):
        self.my_label = label
        self.my_children = list()
        self.parent=None
        self.depth=1

    @staticmethod
    def get_children(node):
        return node.my_children

    @staticmethod
    def get_label(node):
        return node.my_label

    @staticmethod
    def add_depth(node):
        if node.parent != None:
            node.depth=node.parent.depth+1
        for c in node.my_children:
            DepthWeightedNode.add_depth(c)
    def addkid(self, node):
        self.my_children.append(node)
        node.parent=self
        DepthWeightedNode.add_depth(node)
        return self
    
    def setparent(self,node):
        self.parent=node
        self.depth=node.depth+1
        return self
    @staticmethod
    def get_depth(node):
        return node.depth

def update_func(node1, node2):
    if DepthWeightedNode.get_label(node1) == DepthWeightedNode.get_label(node2):
        return 0
    return 1#/DepthWeightedNode.get_depth(node1)
def remove_func(node1):
    return 1#/DepthWeightedNode.get_depth(node1)
def insert_func(node1):
    return 1#/DepthWeightedNode.get_depth(node1)

class TED():
    def __init__(self, folder_name):
        # read tree from file
        files_paths=os.listdir(folder_name)
        files_paths.sort()
        self.trees=[]
        for file_path in files_paths:
            if file_path[-4:]==".txt":
                file_handle=open(folder_name+file_path,"r",encoding="utf8", errors='ignore')
                sentence=file_handle.read().strip().split(",")[0][2:-1]
                nodes_list=re.split(' ',sentence.replace("(", "").replace(")", ""))
                root=self.sentencetonode(nodes_list)
                self.trees.append(root)
                file_handle.close()
    def sentencetonode(self,nodes_list):
        stk=[] #stack
        leaf_stks=[[]] 
        for node in nodes_list:
            assert(node in leaf_nodes or node in nonleaf_nodes)
            if node in leaf_nodes:
                n = DepthWeightedNode(node)
                if len(stk) > 0 :
                    par=stk.pop()
                    assert(len(leaf_stks)>0)
                    if par in twochild_nodes and len(leaf_stks[-1])>0: #n is right child
                        lc=leaf_stks[-1].pop()
                        p = DepthWeightedNode(par)
                        p.addkid(lc)
                        p.addkid(n)
                        assert(len(leaf_stks[-1])==0)
                        leaf_stks.pop()
                        leaf_stks[-1].append(p)
                    elif par in twochild_nodes : # n is left child
                        stk.append(par)
                        leaf_stks[-1].append(n)
                    else: # n is single child
                        p = DepthWeightedNode(par)
                        p.addkid(n)
                        assert(len(leaf_stks[-1])==0)
                        leaf_stks.pop()
                        leaf_stks[-1].append(p)
                else : #single node is root
                    leaf_stks.append([n])
            elif node in nonleaf_nodes:
                stk.append(node)
                leaf_stks.append([])
            while(len(stk)>0):
                par=stk.pop()
                assert(len(leaf_stks)>0)
                if par in twochild_nodes and len(leaf_stks[-1])==2:
                    rc=leaf_stks[-1].pop()
                    lc=leaf_stks[-1].pop()
                    p = DepthWeightedNode(par)
                    p.addkid(lc)
                    p.addkid(rc)
                    assert(len(leaf_stks[-1])==0)
                    leaf_stks.pop()
                    leaf_stks[-1].append(p)
                elif par not in twochild_nodes and par in nonleaf_nodes and len(leaf_stks[-1])==1:
                    p = DepthWeightedNode(par)
                    p.addkid(leaf_stks[-1].pop())
                    assert(len(leaf_stks[-1])==0)
                    leaf_stks.pop()
                    leaf_stks[-1].append(p)
                else:
                    stk.append(par)
                    break
        assert(len(stk)==0)
        assert(len(leaf_stks)==1)
        assert(len(leaf_stks[0])==1)
        return leaf_stks[0][0]
    def calc_average_dist(self,l,r):
        #最初の10個はlifehacker
        distances=[]
        for t1,t2 in list(itertools.combinations(self.trees[l:r], 2)):
            distances.append(simple_distance(t1,t2))
        return sum(distances)/len(distances) if len(distances)>0 else 0
    def calc_matrix(self):
        matrix=[]
        for i in range(len(self.trees)):
            matrix.append([])
            for j in range(len(self.trees)):
                A=self.trees[i]
                B=self.trees[j]
                dist=distance(A,B,DepthWeightedNode.get_children,insert_func,remove_func, update_func)
                matrix[i].append(dist)
        return matrix
    def visualize_matrix(self):
        plt.figure(figsize=(15,15))
        matrix=self.calc_matrix()
        print(matrix)
        rematrix=[]
        for i in range(len(matrix)):
            rematrix.append([])
            for j in range(len(matrix)):
                rematrix[i].append(100/matrix[i][j] if matrix[i][j]!=0 else 0)
        A = np.array(rematrix)
        G = nx.from_numpy_matrix(A)
        pos = nx.spring_layout(G)#エッジの重さが大きいほど近くなる
        node_color = ["orange" for i in range(10)] + ["red" for i in range(10)] + ["blue" for i in range(10)]
        nx.draw_networkx(G,pos=pos,node_color=node_color,width=0.01)
        plt.axis("off")
        plt.savefig("out.png")


ted=TED(os.getcwd()+"/data/")
#print(ted.calc_average_dist(0,10))
#print(ted.calc_average_dist(10,20))
#print(ted.calc_average_dist(0,20))
ted.visualize_matrix()