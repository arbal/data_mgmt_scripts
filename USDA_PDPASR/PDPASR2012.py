# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 10:13:42 2019

@author: MHORTON
"""

# %% import packages
import tabula as tb
import pandas as pd

# Set variables
pdfPath = 'pdfs/'
csvPath = 'csvs/'

fullchemicals = []
fullfunctions = []
fullproducts = []
fullpdflist = []

chem = ''
func = ''
prod = ''

# %% Parse PDFs

# Appendix B Distribution of Residues by Pesticide in Fruit and Vegetables
dfB = tb.read_pdf(pdfPath + "document_1374756.pdf", pages = "46", stream = True,  multiple_tables = True, guess = False, area = [74.0, 47.5, 739.0, 563.0])
dfB = pd.concat(dfB)
dfB2 = tb.read_pdf(pdfPath + "document_1374756.pdf", pages = "47-113", stream = True, multiple_tables = True, guess = False, area = [51.0, 47.5, 739.0, 563.0])
dfB2 = pd.concat(dfB2)
dfB = dfB.append(dfB2, sort=False)
del dfB2
dfB = dfB.reset_index(drop=True)
dfB = dfB.loc[:4372]

# Appendix C Distribution of Residues by Pesticide in Wheat
dfC = tb.read_pdf(pdfPath + "document_1374757.pdf", pages = "115", stream = True,  multiple_tables = True, guess = False, area = [74.0, 47.5, 739.0, 563.0])
dfC = pd.concat(dfC)
dfC2 = tb.read_pdf(pdfPath + "document_1374757.pdf", pages = "116", stream = True, multiple_tables = True, guess = False, area = [51.0, 47.5, 739.0, 563.0])
dfC2 = pd.concat(dfC2)
dfC = dfC.append(dfC2, sort=False)
del dfC2
dfC = dfC.reset_index(drop=True)
dfC = dfC.loc[:58]

# Appendix D Distribution of Residues by Pesticide in Butter
dfD = tb.read_pdf(pdfPath + "document_1374758.pdf", pages = "118", stream = True,  multiple_tables = True, guess = False, area = [74.0, 47.5, 739.0, 563.0])
dfD = pd.concat(dfD)
dfD2 = tb.read_pdf(pdfPath + "document_1374758.pdf", pages = "119-121", stream = True, multiple_tables = True, guess = False, area = [51.0, 47.5, 739.0, 563.0])
dfD2 = pd.concat(dfD2)
dfD = dfD.append(dfD2, sort=False)
del dfD2
dfD = dfD.reset_index(drop=True)
dfD = dfD.loc[:173]

# Appendix E Distribution of Residues by Pesticide in Groundwater
dfE = tb.read_pdf(pdfPath + "document_1374759.pdf", pages = "123", stream = True,  multiple_tables = True, guess = False, area = [74.0, 47.5, 739.0, 563.0])
dfE = pd.concat(dfE)
dfE2 = tb.read_pdf(pdfPath + "document_1374759.pdf", pages = "124-141", stream = True, multiple_tables = True, guess = False, area = [51.0, 47.5, 739.0, 563.0])
dfE2 = pd.concat(dfE2)
dfE = dfE.append(dfE2, sort=False)
del dfE2
dfE = dfE.reset_index(drop=True)
dfE = dfE.loc[:828]

# Appendix F Distribution of Residues by Pesticide in Drinking Water
dfF = tb.read_pdf(pdfPath + "document_1374760.pdf", pages = "143", stream = True,  multiple_tables = True, guess = False, area = [74.0, 47.5, 739.0, 563.0])
dfF = pd.concat(dfF)
dfF2 = tb.read_pdf(pdfPath + "document_1374760.pdf", pages = "144-153", stream = True, multiple_tables = True, guess = False, area = [51.0, 47.5, 739.0, 563.0])
dfF2 = pd.concat(dfF2)
dfF = dfF.append(dfF2, sort=False)
del dfF2
dfF = dfF.reset_index(drop=True)
dfF = dfF.loc[:660]

# Appendix G Distribution of Residues for Environmental Contaminants 
dfG = tb.read_pdf(pdfPath + "document_1374761.pdf", pages = "155", stream = True,  multiple_tables = False, guess = False, area = [74.0, 47.5, 739.0, 563.0])
dfG1 = tb.read_pdf(pdfPath + "document_1374761.pdf", pages = "156-160", stream = True,  multiple_tables = False, guess = False, area = [51.0, 47.5, 739.0, 563.0])
dfG = dfG.append(dfG1, sort=False)
del dfG1
dfG = dfG.reset_index(drop=True)
dfG = dfG.loc[:334]

# Appendix I Import Versus Domestic Pesticide Residue Comparisons 
#1 - Cherry Tomatoes 
#2 - Winter Squash
#3 - Plums
#3 - Tangerines
#4 - Snap Peas
dfI1 = tb.read_pdf(pdfPath + "document_1374762.pdf", pages = "166", stream = True,  multiple_tables = True, guess = False, area = [130.0, 47.5, 725.0, 563.0])
dfI1 = pd.concat(dfI1)

dfI2 = tb.read_pdf(pdfPath + "document_1374762.pdf", pages = "167", stream = True,  multiple_tables = True, guess = False, area = [100.0, 47.5, 725.0, 563.0])
dfI2 = pd.concat(dfI2)

dfI3 = tb.read_pdf(pdfPath + "document_1374762.pdf", pages = "168", stream = True,  multiple_tables = True, guess = False, area = [100.0, 47.5, 725.0, 563.0])
dfI3 = pd.concat(dfI3)

dfI4 = tb.read_pdf(pdfPath + "document_1374762.pdf", pages = "169", stream = True,  multiple_tables = True, guess = False, area = [100.0, 47.5, 725.0, 563.0])
dfI4 = pd.concat(dfI4)

# Appendix J Pesticide Residues by Commodity 
dfJ = tb.read_pdf(pdfPath + "document_1374763.pdf", pages = "171", stream = True,  multiple_tables = True, guess = False, area = [94.0, 47.5, 721.0, 586.0])
dfJ = pd.concat(dfJ)
dfJ1 = tb.read_pdf(pdfPath + "document_1374763.pdf", pages = "172-174", stream = True,  multiple_tables = True, guess = False, area = [51.0, 47.5, 737.0, 586.0])
dfJ1 = pd.concat(dfJ1)
dfJ = dfJ.append(dfJ1, sort=False)
del dfJ1
dfJ = dfJ.reset_index(drop=True)
dfJ = dfJ.loc[:169]

# Appendix L Samples Reported to the U.S. Food and Drug Administration as Exceeding the Tolerance or Without Established Tolerance 
dfL1 = tb.read_pdf(pdfPath + "document_1374765.pdf", pages = "179", stream = True,  multiple_tables = True, guess = False, area = [126.0, 35.0, 735.0, 563.0])
dfL1 = pd.concat(dfL1)
dfL2 = tb.read_pdf(pdfPath + "document_1374765.pdf", pages = "180", stream = True,  multiple_tables = True, guess = False, area = [86.0, 35.0, 735.0, 563.0])
dfL2 = pd.concat(dfL2)
dfL1 = dfL1.append(dfL2, sort=False)

dfL2 = tb.read_pdf(pdfPath + "document_1374765.pdf", pages = "181", stream = True,  multiple_tables = True, guess = False, area = [86.0, 35.0, 735.0, 584.0])
dfL2 = pd.concat(dfL2)
dfL2.columns = ['0', '1', '2', '3', '4', '5', '6']
dfL3 = tb.read_pdf(pdfPath + "document_1374765.pdf", pages = "182", stream = True, multiple_tables = False, guess = True, area = [56.0, 35.0, 735.0, 584.0])
dfL3.columns = ['0', '1', '2', '3', '4', '5', '6']
dfL2 = dfL2.append(dfL3, sort=False)
del dfL3
dfL2 = dfL2.reset_index(drop=True)
dfL2 = dfL2.loc[:87]

# %% Parsing data for upload - Appendix B
del chem, func, prod
chemicals = []
functions = []
products = []
pdflist = []


for index, row in dfB.iterrows():
    try:
        #skip lines that don't contain chemicals or products, or where there were no detections
        if pd.isna(row[0]) == True or 'TOTAL' in row[0] or 'Pesticide / Commodity' in row[0] or 'Appendix' in row[0] or row[2] == '0': 
            pass
        #find the chemicals
        elif '(' in row[0] and pd.isna(row[2]) == True :
            chem = row[0].split('(')[0]
            func = row[0].split('(')[1].strip().strip(')')
        elif 'cide' in row[2] :
            chem = row[0].split('(')[0]
            func = row[2].split('(')[1].strip().strip(')')
        elif '(' in row[1] and pd.isna(row[2]) == True:
            chem = row[0]
            func = row[1].split('(')[1].strip().strip(')')
        else:
            prod = row[0].split('(')[0].rstrip(' 0123456789')

            chemicals.append(chem)
            functions.append(func)
            products.append(prod.rstrip(' '))
            pdflist.append('2012 ' + prod.rstrip(' ') + '.pdf')
    except:
        pass

#checking
dfc = pd.DataFrame({'chem':chemicals, 'func':functions, 'prod':products})
dfchems = pd.DataFrame(chemicals)
dfchems = dfchems.drop_duplicates()
dffuncs = pd.DataFrame(functions)
dffuncs = dffuncs.drop_duplicates()
dfprods = pd.DataFrame(products)
dfprods = dfprods.drop_duplicates()

fullchemicals = fullchemicals + chemicals
fullfunctions = fullfunctions + functions
fullproducts = fullproducts + products
fullpdflist = fullpdflist + pdflist

# %% Parsing data for upload - Appendix C
del chem, func, prod
chemicals = []
functions = []
products = []
pdflist = []

prod = 'Wheat'

for index, row in dfC.iterrows():
    try:
        if pd.isna(row[0]) == True or pd.isna(row[3]) == True or 'Pesticide' in row[0] :
            pass

        #get the chemicals
        else: 
            chem = row[0].strip(')')
            chemicals.append(chem)
        
            if row[1] == 'A':
                func = 'acaricide'
            elif row[1] == 'F':
                func = 'fungicide'
            elif row[1] == 'H':
                func = 'herbicide'
            elif row[1] == 'I':
                func = 'insecticide'
            elif row[1] == 'IM':
                func = 'insecticide metabolite'
            elif row[1] == 'N':
                func = 'nitrification inhibitor'
            elif row[1] == 'P':
                func = 'plant growth regulator'
            elif row[1] == 'S':
                func = 'herbicide safener'
            else: func = ''
            
            functions.append(func)
            products.append(prod.rstrip(' '))
            pdflist.append('2012 ' + prod.rstrip(' ') + '.pdf')
            
    except:
        pass

#checking
dfc = pd.DataFrame({'chem':chemicals, 'func':functions, 'prod':products})
dfchems = pd.DataFrame(chemicals)
dfchems = dfchems.drop_duplicates()
dffuncs = pd.DataFrame(functions)
dffuncs = dffuncs.drop_duplicates()
dfprods = pd.DataFrame(products)
dfprods = dfprods.drop_duplicates()

fullchemicals = fullchemicals + chemicals
fullfunctions = fullfunctions + functions
fullproducts = fullproducts + products
fullpdflist = fullpdflist + pdflist

# %% Parsing data for upload - Appendix D
del chem, func, prod
chemicals = []
functions = []
products = []
pdflist = []

prod = 'Butter'


for index, row in dfD.iterrows():
    try:
        if pd.isna(row[0]) == True or pd.isna(row[3]) == True or 'Pesticide' in row[0] :
            pass

        #get the chemicals
        else: 
            chem = row[0]
            chemicals.append(chem)
        
            if row[1] == 'F':
                func = 'fungicide'
            elif row[1] == 'FM':
                func = 'fungicide metabolite'
            elif row[1] == 'H':
                func = 'herbicide'
            elif row[1] == 'I':
                func = 'insecticide'
            elif row[1] == 'IM':
                func = 'insecticide metabolite'
            elif row[1] == 'L':
                func = 'plant activator'
            elif row[1] == 'P':
                func = 'plant growthr regulator'
            elif row[1] == 'R':
                func = 'insect growth regulator'
            elif row[1] == 'S':
                func = 'herbicide safener'
            else: func = ''
        
            functions.append(func)
            products.append(prod.rstrip(' '))
            pdflist.append('2012 ' + prod.rstrip(' ') + '.pdf')
        
    except:
        pass
    
# Fixing a couple of chemicals
chemicals[:] = [chem if 'epimer' not in chem else 'Cyhalothrin, Total (Cyhalothrin-L + R157836 epimer)' for chem in chemicals]

#checking
dfc = pd.DataFrame({'chem':chemicals, 'func':functions, 'prod':products})
dfchems = pd.DataFrame(chemicals)
dfchems = dfchems.drop_duplicates()
dffuncs = pd.DataFrame(functions)
dffuncs = dffuncs.drop_duplicates()
dfprods = pd.DataFrame(products)
dfprods = dfprods.drop_duplicates()

fullchemicals = fullchemicals + chemicals
fullfunctions = fullfunctions + functions
fullproducts = fullproducts + products
fullpdflist = fullpdflist + pdflist

# %% Parsing data for upload - Appendix E
del chem, func, prod

chemicals = []
functions = []
products = []
pdflist = []

prod = 'Groundwater'

for index, row in dfE.iterrows():
    try:
        if pd.isna(row[0]) == True or 'TOTAL' in row[0] or 'NOTES' in row[0] or 'Pesticide' in row[0]: 
            #skip lines that don't contain chemicals, or where there were no detections
            pass
        elif pd.isna(row[1]) == True :
            if '(' in row[0]:
                chem = row[0].rsplit('(',1)[0].strip('* ')
                func = row[0].rsplit('(',1)[1].strip(') ')
            if func == 'F':
                func = 'fungicide'
            elif func == 'FM':
                func = 'fungicide metabolite'
            elif func == 'H':
                func = 'herbicide'
            elif func == 'HM':
                func = 'herbicide metabolite'
            elif func == 'I':
                func = 'insecticide'
            elif func == 'IM':
                func = 'insecticide metabolite'
            else: pass
            
        if pd.isna(row[3]) == False:
            chemicals.append(chem)
            functions.append(func)
            products.append(prod.rstrip(' '))
            pdflist.append('2012 ' + prod.rstrip(' ') + '.pdf')
            
    except:
        pass
    
#checking
dfc = pd.DataFrame({'chem':chemicals, 'func':functions, 'prod':products})
dfchems = pd.DataFrame(sorted(chemicals))
dfchems = dfchems.drop_duplicates()
dffuncs = pd.DataFrame(sorted(functions))
dffuncs = dffuncs.drop_duplicates()
dfprods = pd.DataFrame(sorted(products))
dfprods = dfprods.drop_duplicates()

fullchemicals = fullchemicals + chemicals
fullfunctions = fullfunctions + functions
fullproducts = fullproducts + products
fullpdflist = fullpdflist + pdflist

# %% Parsing data for upload - Appendix F
del chem, func, prod
chemicals = []
functions = []
products = []
pdflist = []

prod = 'Drinking Water'

for index, row in dfF.iterrows():
    try:
        if pd.isna(row[0]) == True or 'TOTAL' in row[0] or 'NOTES' in row[0] or 'Pesticide' in row[0]: 
            #skip lines that don't contain chemicals, or where there were no detections
            pass
        elif pd.isna(row[1]) == True :
            if '(' in row[0]:
                chem = row[0].rsplit('(',1)[0].strip('* ')
                func = row[0].rsplit('(',1)[1].strip(') ')
            if func == 'F':
                func = 'fungicide'
            elif func == 'H':
                func = 'herbicide'
            elif func == 'HM':
                func = 'herbicide metabolite'
            elif func == 'I':
                func = 'insecticide'
            elif func == 'IM':
                func = 'insecticide metabolite'
            elif func == 'P':
                func = 'Plant growth Regulator'
            else: pass
            
        if pd.isna(row[3]) == False:
            chemicals.append(chem)
            functions.append(func)
            products.append(prod.rstrip(' '))
            pdflist.append('2012 ' + prod.rstrip(' ') + '.pdf')
            
    except:
        pass
    
#checking
dfc = pd.DataFrame({'chem':chemicals, 'func':functions, 'prod':products})
dfchems = pd.DataFrame(sorted(chemicals))
dfchems = dfchems.drop_duplicates()
dffuncs = pd.DataFrame(sorted(functions))
dffuncs = dffuncs.drop_duplicates()
dfprods = pd.DataFrame(sorted(products))
dfprods = dfprods.drop_duplicates()

fullchemicals = fullchemicals + chemicals
fullfunctions = fullfunctions + functions
fullproducts = fullproducts + products
fullpdflist = fullpdflist + pdflist

# %% Parsing data for upload - Appendix G
del chem, func, prod
chemicals = []
functions = []
products = []
pdflist = []


for index, row in dfG.iterrows():
    try:
        #skip lines that don't contain chemicals or products, or where there were no detections
        if pd.isna(row[0]) == True or 'TOTAL' in row[0] or 'Pesticide / Commodity' in row[0] or 'Appendix' in row[0] or row[2] == '0': 
            pass
        #find the chemicals
        elif '(' in row[0] and pd.isna(row[2]) == True :
            chem = row[0].split('(')[0]
            func = row[0].split('(')[1].strip().strip(')')
        elif 'cide' in row[2] :
            chem = row[0].split('(')[0]
            func = row[2].split('(')[1].strip().strip(')')
        elif '(' in row[1] and pd.isna(row[2]) == True:
            chem = row[0]
            func = row[1].split('(')[1].strip().strip(')')
        else:
            prod = row[0].split('(')[0].rstrip(' 0123456789')
            
            if ', Total' in chem :
                chem = chem.split(',')[0]
            chemicals.append(chem)
            functions.append(func)
            products.append(prod.rstrip(' '))
            pdflist.append('2012 ' + prod.rstrip(' ') + '.pdf')
            
    except:
        pass

#checking
dfc = pd.DataFrame({'chem':chemicals, 'func':functions, 'prod':products})
dfchems = pd.DataFrame(sorted(chemicals))
dfchems = dfchems.drop_duplicates()
dffuncs = pd.DataFrame(sorted(functions))
dffuncs = dffuncs.drop_duplicates()
dfprods = pd.DataFrame(sorted(products))
dfprods = dfprods.drop_duplicates()

fullchemicals = fullchemicals + chemicals
fullfunctions = fullfunctions + functions
fullproducts = fullproducts + products
fullpdflist = fullpdflist + pdflist

# %% Appendix I Import Versus Domestic Pesticide Residue Comparisons 
#1 - Cherry Tomatoes 

del chem, func, prod
chemicals = []
functions = []
products = []
pdflist = []

prod = 'Cherry Tomatoes'
func = ''

for index, row in dfI1.iterrows():
    try:
        if 'Pesticide' in row[0]  or 'NOTE' in row[0] or pd.isna(row[0]) == True : #skip rows that have "Pesticide" or "NOTE" in first field, or first field is NaN 
            pass

        #get the chemicals
        else: 
            chem = row[0]
            chemicals.append(chem)
            
            functions.append(func)
            products.append(prod.rstrip(' ')) #all entries have >10% sample detections
            pdflist.append('2012 ' + prod.rstrip(' ') + '.pdf')
                
    except:
        pass

#checking
dfc = pd.DataFrame({'chem':chemicals, 'func':functions, 'prod':products})
dfchems = pd.DataFrame(chemicals)
dfchems = dfchems.drop_duplicates()
dffuncs = pd.DataFrame(functions)
dffuncs = dffuncs.drop_duplicates()
dfprods = pd.DataFrame(products)
dfprods = dfprods.drop_duplicates()
 
fullchemicals = fullchemicals + chemicals
fullfunctions = fullfunctions + functions
fullproducts = fullproducts + products
fullpdflist = fullpdflist + pdflist

# %% #2 - Winter Squash
del chem, func, prod
chemicals = []
functions = []
products = []
pdflist = []

prod = 'Winter Squash'
func = ''

for index, row in dfI2.iterrows():
    try:
        if 'Pesticide' in row[0]  or 'NOTE' in row[0] or pd.isna(row[0]) == True : #skip rows that have "Pesticide" or "NOTE" in first field, or first field is NaN 
            pass

        #get the chemicals
        else: 
            chem = row[0]
            chemicals.append(chem)
            
            functions.append(func)
            products.append(prod.rstrip(' ')) #all entries have >10% sample detections
            pdflist.append('2012 ' + prod.rstrip(' ') + '.pdf')
                
    except:
        pass

#checking
dfc = pd.DataFrame({'chem':chemicals, 'func':functions, 'prod':products})
dfchems = pd.DataFrame(chemicals)
dfchems = dfchems.drop_duplicates()
dffuncs = pd.DataFrame(functions)
dffuncs = dffuncs.drop_duplicates()
dfprods = pd.DataFrame(products)
dfprods = dfprods.drop_duplicates()
 
fullchemicals = fullchemicals + chemicals
fullfunctions = fullfunctions + functions
fullproducts = fullproducts + products
fullpdflist = fullpdflist + pdflist

# %% 
#3 - Plums
#3 - Tangerines
del chem, func, prod
chemicals = []
functions = []
products = []
pdflist = []

func = ''

for index, row in dfI3.iterrows():
    try:
        if 'United' in row[2] and pd.isna(row[0]) == False :
            prod = row[0]
            chem = row[1]
            chemicals.append(chem)
            functions.append(func)
            products.append(prod.rstrip(' ')) #all entries have >10% sample detections
            pdflist.append('2012 ' + prod.rstrip(' ') + '.pdf')
        elif 'United' in row[2] and pd.isna(row[0]) == True :
            chem = row[1]
            chemicals.append(chem)
            functions.append(func)
            products.append(prod.rstrip(' ')) #all entries have >10% sample detections
            pdflist.append('2012 ' + prod.rstrip(' ') + '.pdf')
    except:
        pass

#checking
dfc = pd.DataFrame({'chem':chemicals, 'func':functions, 'prod':products})
dfchems = pd.DataFrame(chemicals)
dfchems = dfchems.drop_duplicates()
dffuncs = pd.DataFrame(functions)
dffuncs = dffuncs.drop_duplicates()
dfprods = pd.DataFrame(products)
dfprods = dfprods.drop_duplicates()
 
fullchemicals = fullchemicals + chemicals
fullfunctions = fullfunctions + functions
fullproducts = fullproducts + products
fullpdflist = fullpdflist + pdflist

# %% #4 - Snap Peas
del chem, func, prod
chemicals = []
functions = []
products = []
pdflist = []

prod = 'Snap Peas'
func = ''
for index, row in dfI4.iterrows():
    try:
        if 'United' in row[1] : 
            chem = row[0]
            chemicals.append(chem)
            functions.append(func)
            products.append(prod.rstrip(' ')) #all entries have >10% sample detections
            pdflist.append('2012 ' + prod.rstrip(' ') + '.pdf')
                
    except:
        pass

#checking
dfc = pd.DataFrame({'chem':chemicals, 'func':functions, 'prod':products})
dfchems = pd.DataFrame(chemicals)
dfchems = dfchems.drop_duplicates()
dffuncs = pd.DataFrame(functions)
dffuncs = dffuncs.drop_duplicates()
dfprods = pd.DataFrame(products)
dfprods = dfprods.drop_duplicates()
 
fullchemicals = fullchemicals + chemicals
fullfunctions = fullfunctions + functions
fullproducts = fullproducts + products
fullpdflist = fullpdflist + pdflist

# %% Parsing data for upload - Appendix J
del chem, func, prod
chemicals = []
functions = []
products = []
pdflist = []

for index, row in dfJ.iterrows():
    try:
        if pd.isna(row[0]) == True or 'Pesticide' in row[0] or 'NOTES' in row[0] : 
            #skip lines that don't contain chemicals or products
            pass
        
        elif pd.isna(row[1]) == True  and '(' in row[0] :
            prod = row[0].split('(')[0].strip(' 0123456789')
            
        else :
            chem = row[0].split('(')[0].rstrip(' 0123456789*')
            
            if 'Total' in chem : 
                chem = chem.split(',')[0].rstrip(' Total')
            
            if row[1] == 'A':
                func = 'acaricide'
            elif row[1] == 'F':
                func = 'fungicide'
            elif row[1] == 'FM':
                func = 'fungicide metabolite'
            elif row[1] == 'I':
                func = 'insecticide'
            elif row[1] == 'IM':
                func = 'insecticide metabolite'
            elif row[1] == 'R':
                func = 'insect growth regulator'
            else: func = ''            

            if func != '' :
                products.append(prod.rstrip(' '))
                functions.append(func)
                chemicals.append(chem)
                pdflist.append('2012 ' + prod.rstrip(' ') + '.pdf')   
    
    except: 
        pass

#checking
dfc = pd.DataFrame({'chem':chemicals, 'func':functions, 'prod':products})
dfchems = pd.DataFrame(chemicals)
dfchems = dfchems.drop_duplicates()
dffuncs = pd.DataFrame(functions)
dffuncs = dffuncs.drop_duplicates()
dfprods = pd.DataFrame(products)
dfprods = dfprods.drop_duplicates()
 
fullchemicals = fullchemicals + chemicals
fullfunctions = fullfunctions + functions
fullproducts = fullproducts + products
fullpdflist = fullpdflist + pdflist

# %% Parsing data for upload - Appendix L
del chem, func, prod
chemicals = []
functions = []
products = []
pdflist = []

func = ''

for index, row in dfL1.iterrows():
    try:
        if pd.isna(row[0]) == True or 'Commodity / Pesticide' in row[0] : 
            #skip lines that don't contain chemicals or products
            pass

        #find the products and chemicals
        elif '/' in row[1] :
            prod = row[1].split('/')[0].strip(' 0123456789')
            chem = row[1].split('/')[1].strip(' 0123456789')
        elif '/' in row[0] :
            prod = row[0].split('/')[0].strip(' 0123456789')
            chem = row[0].split('/')[1].strip(' 0123456789')

            #define the functions of the chemicals
        
        else: pass
    
        products.append(prod.rstrip(' '))
        functions.append(func)
        chemicals.append(chem)
        pdflist.append('2012 ' + prod.rstrip(' ') + '.pdf')
        
    except:
        pass

#checking
dfc = pd.DataFrame({'chem':chemicals, 'func':functions, 'prod':products})
dfc = dfc.drop_duplicates()
dfchems = pd.DataFrame(chemicals)
dfchems = dfchems.drop_duplicates()
dffuncs = pd.DataFrame(functions)
dffuncs = dffuncs.drop_duplicates()
dfprods = pd.DataFrame(products)
dfprods = dfprods.drop_duplicates()
 
fullchemicals = fullchemicals + chemicals
fullfunctions = fullfunctions + functions
fullproducts = fullproducts + products
fullpdflist = fullpdflist + pdflist

# %%
del chem, func, prod
chemicals = []
functions = []
products = []
pdflist = []

func = ''

for index, row in dfL2.iterrows():
    try:
        if pd.isna(row[0]) == True or 'Commodity / Pesticide' in row[0] or 'NOTES' in row[0] or 'Permethrin  (parent) 7' in row[0] : 
            #skip lines that don't contain chemicals or products
            pass
        
        elif pd.isna(row[1]) == True  and '(' in row[0] :
            prod = row[0].split('(')[0].strip(' 0123456789')
            
        else :
            chem = row[0].split('(')[0].rstrip(' 0123456789*')
            
            if 'Total' in chem:
                chem = chem.rstrip(' Total')
            
            products.append(prod.rstrip(' '))
            functions.append(func)
            chemicals.append(chem)
            pdflist.append('2012 ' + prod.rstrip(' ') + '.pdf')   
        
    except: 
        pass

#checking
dfc = pd.DataFrame({'chem':chemicals, 'func':functions, 'prod':products})
dfc = dfc.drop_duplicates()
dfchems = pd.DataFrame(chemicals)
dfchems = dfchems.drop_duplicates()
dffuncs = pd.DataFrame(functions)
dffuncs = dffuncs.drop_duplicates()
dfprods = pd.DataFrame(products)
dfprods = dfprods.drop_duplicates()

fullchemicals = fullchemicals + chemicals
fullfunctions = fullfunctions + functions
fullproducts = fullproducts + products
fullpdflist = fullpdflist + pdflist

# %% Verify
oldfullchemicals = fullchemicals
fullchemicals = []

for s in oldfullchemicals:
    if 'Total' in s:
        s = s.rstrip(' Total')
        try:
            s = s.replace(', Total', '')
        except: pass
    elif ' - ' in s:
        s1 = s.split('-')[0].strip(' ')
        s2 = s.split('-')[1].strip(' ')
        s = s1 + ' (' + s2 + ')'
        
    s = s.lower()
    fullchemicals.append(s.rstrip(' '))
    
#checking
dfc = pd.DataFrame({'chem':fullchemicals, 'func':fullfunctions, 'prod':fullproducts})

dfchems = fullchemicals
dfchems = pd.DataFrame(sorted(dfchems))
dfchems = dfchems.drop_duplicates()

dffuncs = fullfunctions
dffuncs = pd.DataFrame(sorted(dffuncs))
dffuncs = dffuncs.drop_duplicates()

dfprods = fullproducts
dfprods = pd.DataFrame(sorted(dfprods))
dfprods = dfprods.drop_duplicates()

# %% fix / in filenames
oldfullpdflist = fullpdflist
fullpdflist = []

for s in oldfullpdflist:
    sn = s.replace('/','-')
    fullpdflist.append(sn)

# %% Registered Records CSV
length = len(fullproducts)

titles = []
for s in fullproducts:
    title = '2012 Pesticide Residues in ' + s.replace('/','-')
    titles.append(title)
document_type = ['FG']*length
url = ['https://www.ams.usda.gov/sites/default/files/media/2012PDPSummary.pdf']*length
organization = ['USDA']*length

dfrr = pd.DataFrame({'filename':fullpdflist, 'title':titles, 'document_type':document_type, 'url':url, 'organization':organization}) 
dfrr=dfrr.drop_duplicates()

#dfrr.to_csv(csvPath + "RR-PDPASR2012.csv",index=False, header=True)

# %% Create PDFs for document matching

#"""
#Created on Thu May 23 09:37:47 2019
#​
#@author: ALarger
#"""
##​
#import os, csv
#from shutil import copyfile
##​
#path = r'C:\Users\mhorton\Documents\extscr\PDPASR\PDPASR2012\pdfs' #Folder doc is in
#os.chdir(path)    
#template = csv.reader(open('usda_pdpasr_2012_registered_documents.csv')) #Register Records template
#i=0
#for row in template:
#    i+=1
#    if i == 1: continue
#    try:
#        oldPath = path + '\\' + 'document_1374756.pdf' #Original doc name
#        newPath = path + '\\matchingdocs\\' + row[1]
#        copyfile(oldPath,newPath)
#    except: print('halp!', row[0])

# %% create the CSV for upload
length = len(fullproducts)
docDate = ['February 2014']*length
rawCat = fullproducts
rawCas = ['']*length
catCode = ['']*length
desc = ['']*length
cpcatCode = ['']*length
cpcatSource = ['']*length
fulldocNumber = ['']*length

#create a dictionary of doc IDs from the RRs
dftemp = pd.read_csv(csvPath + 'usda_pdpasr_2012_registered_documents.csv')
dftemp = dftemp[['DataDocument_id','filename']]
dftemp = dftemp.set_index('filename').T.to_dict('list')

df = pd.DataFrame({'data_document_id':fulldocNumber, 'data_document_filename':fullpdflist, 'doc_date':docDate, 'raw_category':rawCat, 'raw_cas':rawCas, 'raw_chem_name':fullchemicals, 'report_funcuse':fullfunctions, 'cat_code':catCode, 'description_cpcat':desc, 'cpcat_code':cpcatCode, 'cpcat_sourcetype':cpcatSource})
df=df.drop_duplicates()
df['data_document_id'] = df.data_document_filename.replace(dftemp) #get doc IDs from template dictionary
    
#df.to_csv(csvPath + "USDA-PDPASR2012.csv",index=False, header=True)
