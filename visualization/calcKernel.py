from zss import simple_distance, Node
import os
import re
import itertools
import networkx as nx
import numpy as np
import string
import matplotlib.pyplot as plt
import tree as tr 
import tree_kernels as tk
import math
leaf_nodes=["Tf","Idf","Tfidf","First","Last","NumberF","NumberS","NumberT","Length","Rare","Title", "Noun","Adv","Verb","Adj"]
nonleaf_nodes=["Plus","Minus","Times","Div","Log","Inv","TimTen","DivTen"]
twochild_nodes=["Plus","Minus","Times","Div"]
class cKernel():
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
                n = tr.TreeNode(node,[])
                if len(stk) > 0 :
                    par=stk.pop()
                    assert(len(leaf_stks)>0)
                    if par in twochild_nodes and len(leaf_stks[-1])>0: #n is right child
                        lc=leaf_stks[-1].pop()
                        p = tr.TreeNode(par,[lc,n])
                        assert(len(leaf_stks[-1])==0)
                        leaf_stks.pop()
                        leaf_stks[-1].append(p)
                    elif par in twochild_nodes : # n is left child
                        stk.append(par)
                        leaf_stks[-1].append(n)
                    else: # n is single child
                        p = tr.TreeNode(par,[n])
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
                    p = tr.TreeNode(par,[lc,rc])
                    assert(len(leaf_stks[-1])==0)
                    leaf_stks.pop()
                    leaf_stks[-1].append(p)
                elif par not in twochild_nodes and par in nonleaf_nodes and len(leaf_stks[-1])==1:
                    p = tr.TreeNode(par,[leaf_stks[-1].pop()])
                    assert(len(leaf_stks[-1])==0)
                    leaf_stks.pop()
                    leaf_stks[-1].append(p)
                else:
                    stk.append(par)
                    break
        assert(len(stk)==0)
        assert(len(leaf_stks)==1)
        assert(len(leaf_stks[0])==1)
        return tr.Tree(leaf_stks[0][0]) ## target=??
    def calc_average_dist(self,l,r):
        #最初の10個はlifehacker
        distances=[]
        trkn=tk.KernelST(10.0) ## l=??
        for t1,t2 in list(itertools.combinations(self.trees[l:r], 2)):
            trkn.kernel(t1,t2)
        return sum(distances)/len(distances) if len(distances)>0 else 0
    def calc_matrix(self):
        matrix=[]
        trkn=tk.KernelST(1.0)
        for i in range(len(self.trees)):
            matrix.append([])
            for j in range(len(self.trees)):
                coskernel=trkn.kernel(self.trees[i],self.trees[j])/math.sqrt( trkn.kernel(self.trees[i],self.trees[i]) )/ math.sqrt( trkn.kernel(self.trees[j],self.trees[j]))
                matrix[i].append(coskernel)
        print(matrix)
        return matrix
    def visualize_matrix(self):
        plt.figure(figsize=(15,15))
        matrix=self.calc_matrix()
        A = np.array(matrix)
        print(A)
        G = nx.from_numpy_matrix(A)
        pos = nx.spring_layout(G,iterations=5000)#エッジの重さが大きいほど近くなる
        node_color = ["red" for i in range(10)] + ["blue" for i in range(10)]
        label = [str(i) for i in range(1,21)]
        nx.draw_networkx(G,pos=pos,node_color=node_color,width=0.1)
        plt.axis("off")
        plt.savefig("kernel.png")


krnl=cKernel(os.getcwd()+"/data/")
krnl.visualize_matrix()