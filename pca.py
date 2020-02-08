# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 23:29:58 2020

@author: ABOLI
"""
import numpy as np
from sklearn.decomposition import PCA as pa
class PCA:
    variance_ratio=1
    X=[]
    n_components1=1
    pca=pa(2)
    def __init__(self,n_components):
       self.n_components1=n_components
       pca = pa(self.n_components1)
    def fit(self,X):
        
        self.pca.fit(X)
        self.variance_ratio=self.pca.explained_variance_ratio_
       
    def transform(self,X):
        return self.pca.transform(X)

    
        