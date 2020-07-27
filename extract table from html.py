# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 20:54:39 2020

@author: moise
"""

def originalTable(text):

    listTB = [] #list to hold all the data
    varTD = None   #store data table
    listTR = None  #list to hold each table row.
    boolTB = False #check for table
    boolTR = False #check for table row
    boolTD = False #check for table data

    openTag = text.find("<", 0) #check for opening tag

    while( openTag != -1):
        closeTag = text.find(">", openTag)

        if closeTag == -1:    #end of the tag
            return listTB

        textElement = text[openTag+1:closeTag]
       
        tempList = textElement.split()
        tagName = tempList[0] #pull only the tag element name
        tagName = tagName.lower() # change it to lower case

        if tagName == "table": #check for table tag
            boolTB = True
        if tagName == "/table":     
            boolTB = False
    
        if tagName == "tr": #check for table row tag
            boolTR = True
            listTR = []      #create list of row element

        if tagName == "/tr":
            boolTR = False
            listTB.append(listTR) #append all the data in the row list
            listTR = None
   
        if tagName== "td":
            boolTD = True
            varTD = ""

        if tagName == "/td":
            boolTD = False
            if varTD != None and listTR != None:
                listTR.append( varTD.strip() )
            varTD = None

        openTag = text.find("<", closeTag+1)

        if boolTB and boolTR and boolTD:
            varTD = varTD + text[closeTag+1:openTag] + " "

    return(listTB)

def sortedTable(dataTable):
    
    myList = dataTable.copy()
   
    del myList[0] #delete first index which is empty
    
    #siz = len(myList)
    #del myList[siz-1]
    print(siz)
    
    #create new list to append the only county, republican, democrat
    newList = []
    for items in myList:
      newList.append([])
      for item in items[0:3]:
          newList[-1].append(item)
    
    newList = [[x.replace(',','') for x in l] for l in newList]      
    newList.sort(key = lambda x: int(x[2]))# sorted by democrat
    return newList     


f = open("FloridaVoters.html", "r")
text = f.read()
originalData = originalTable(text)
sortedData= sortedTable(originalData)
