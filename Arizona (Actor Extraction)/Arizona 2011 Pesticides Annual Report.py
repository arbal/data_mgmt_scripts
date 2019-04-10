# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:19:02 2019

@author: ALarger

2011 Pesticides Annual Report (A.R.S 49-303.C)
Extract chemicals and CAS from tables 2-7
"""

import camelot
import pandas as pd

chemName = []
casN = []

tables = camelot.read_pdf(r'L:\Lab\HEM\ALarger\Actor Automated Extraction\Arizona\2011 Pesticides Annual Report (A.R.S 49-303.C)\document_320440.pdf',pages='6-29', flavor='lattice')
i=0 
for table in tables:
    df = tables[i].df
    df = df.drop(df.index[0])
    df = df.drop(df.index[0])
    if i <= 0:
        chemName.extend(df.loc[:,1])
        casN.extend(['']*len(df))
    elif i <= 4:
        chemName.extend(df.loc[:,2])
        casN.extend(df.loc[:,1])
    elif i <= 17:
        chemName.extend(df.loc[:,5])
        casN.extend(df.loc[:,4])
    elif i <= 18:
        chemName.extend(df.loc[:,0])
        casN.extend(['']*len(df))
    else:
        chemName.extend(df.loc[:,5])
        casN.extend(['']*len(df))
    i+=1

tables2 = (camelot.read_pdf(r'L:\Lab\HEM\ALarger\Actor Automated Extraction\Arizona\2011 Pesticides Annual Report (A.R.S 49-303.C)\document_320440.pdf',pages='30-37', flavor='stream'))
k=0
for table in tables2:
    df = tables2[k].df
    df = df.drop(df.index[0])
    df = df.drop(df.index[0])
    df = df.drop(df.index[0])
    chemName.extend(df.loc[:,6])
    casN.extend(['']*len(df))
    k+=1

chemList = [] #list of chem names with cas numbers (so duplicates without cas can be deleted)
j = len(chemName) - 1
while j >= 0: #go through list backwards, so it doesnt mess up the index if a row is deleted
    if ',' in chemName[j] or '\n' in chemName[j]:
        chemName[j] = chemName[j].replace(',','_')
        chemName[j] = chemName[j].replace('\n',' ')
    if chemName[j] == '':
        del chemName[j]
        del casN[j]
    if '*' in chemName[j]:
        chemName[j] = chemName[j].split('*')[0]
    if chemName[j] == 'salt':
        chemName[j-1] = chemName[j-1] + ' salt'
        del chemName[j]
        del casN[j]
    if chemName[j] == '1_2_3-':
        chemName[j+1] = '1_2_3-' + chemName[j+1] 
        del chemName[j]
        del casN[j]
    chemName[j] = chemName[j].lower()
    chemName[j] = chemName[j].strip()
    if chemName[j] not in chemList and casN[j] != '':
        chemList.append(chemName[j])
    j-=1
        
k = len(chemName) - 1
while k >= 0:
    if chemName[k] in chemList and casN[k] == '':
        del chemName[k]
        del casN[k]
    k-=1

nIngredients = len(chemName)
prodID = [320440]*nIngredients
templateName = ['Arizona_PestUse_2010.pdf']*nIngredients
msdsDate = [2011]*nIngredients
recUse = ['Pesticides: Active Ingredients']*nIngredients
catCode = ['ACToR_Assays_***']*nIngredients
descrip = ['pesticide active_ingredient']*nIngredients
code = ['Arizona_PestUse_2010_AID_1']*nIngredients
sourceType = ['ACToR Assays and Lists']*nIngredients
  
df = pd.DataFrame({'data_document_id':prodID, 'data_document_filename':templateName, 'doc_date':msdsDate, 'raw_category':recUse, 'raw_cas':casN, 'raw_chem_name':chemName, 'cat_code':catCode, 'description_cpcat': descrip, 'cpcat_code':code, 'cpcat_sourcetype':sourceType})
df=df.drop_duplicates()
df.to_csv(r'L:\Lab\HEM\ALarger\Actor Automated Extraction\Arizona\2011 Pesticides Annual Report (A.R.S 49-303.C)\Arizona 2011 Pesticides Annual Report.csv',index=False, header=True, date_format=None)