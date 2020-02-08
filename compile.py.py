# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 23:53:40 2020

@author: ABOLI
"""
from pca import PCA
X=[]
X= np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca_model=PCA(2)
pca_model.fit(X)
print(pca_model.variance_ratio)
print(pca_model.transform(X))