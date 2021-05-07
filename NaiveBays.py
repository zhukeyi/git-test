# -*- coding: utf-8 -*-
#计算各个属性各个值的嫡
import numpy as np
import pandas as pd
def loaddata():
	#f=open('E:/dataset.csv',encoding='utf-8')
	dataset = pd.read_csv('E:/buycomputer.csv',encoding='utf-8')
	return dataset

#dataset = pd.read_csv('E:/buycomputer.csv',encoding='utf-8')
#dataset=loaddata()





def naivebays(dataset):
	Nb=dict()
	label=dataset.iloc[:,-1]
	Pall=label.value_counts()/label.count()
	labels=label.unique()
	features=dataset.columns
	for lab in labels:
		Nb[lab]=dict()
		ds=dataset[dataset.iloc[:,-1]==lab]
		for feat in features:
			Nb[lab][feat]=ds[feat].value_counts()/ds[feat].count()
	return Pall,Nb
		
	
def predict(Pall,Nb,data):
	
	