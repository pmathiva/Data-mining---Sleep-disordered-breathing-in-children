# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 16:37:55 2017

@author: priya.cse2009
"""

"""
pubmed url
To search pubmed you need to use the eSearch API.
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=%28%22sleep%20apnea%20syndromes%22%5BMeSH%20Terms%5D%20%0D%0AOR%20%28%22sleep%22%5BAll%20Fields%5D%20%0D%0AAND%20%22apnea%22%5BAll%20Fields%5D%20%0D%0AAND%20%22syndromes%22%5BAll%20Fields%5D%29%20%0D%0AOR%20%22sleep%20apnea%20syndromes%22%5BAll%20Fields%5D%20%0D%0AOR%20%28%22sleep%22%5BAll%20Fields%5D%20%0D%0AAND%20%22disordered%22%5BAll%20Fields%5D%20%0D%0AAND%20%22breathing%22%5BAll%20Fields%5D%29%20%0D%0AOR%20%22sleep%20disordered%20breathing%22%5BAll%20Fields%5D%29%20%0D%0AAND%20%28%22child%22%5BMeSH%20Terms%5D%20%0D%0AOR%20%22child%22%5BAll%20Fields%5D%20%0D%0AOR%20%22children%22%5BAll%20Fields%5D%29&retmode=txt&retmax=5

Breaking this down…

http://eutils.ncbi.nlm.nih.gov/entrez/ -->is the entry point for the whole system.
/eutils/esearch.fcgi   -->is the actual function that you will be using…This tells the API that you want to search pubmed.
db=pubmed
term= %28%22sleep%20apnea%20syndromes%22%5BMeSH%20Terms%5D%20%0D%0AOR%20%28%22sleep%22%5BAll%20Fields%5D%20%0D%0AAND%20%22apnea%22%5BAll%20Fields%5D%20%0D%0AAND%20%22syndromes%22%5BAll%20Fields%5D%29%20%0D%0AOR%20%22sleep%20apnea%20syndromes%22%5BAll%20Fields%5D%20%0D%0AOR%20%28%22sleep%22%5BAll%20Fields%5D%20%0D%0AAND%20%22disordered%22%5BAll%20Fields%5D%20%0D%0AAND%20%22breathing%22%5BAll%20Fields%5D%29%20%0D%0AOR%20%22sleep%20disordered%20breathing%22%5BAll%20Fields%5D%29%20%0D%0AAND%20%28%22child%22%5BMeSH%20Terms%5D%20%0D%0AOR%20%22child%22%5BAll%20Fields%5D%20%0D%0AOR%20%22children%22%5BAll%20Fields%5D%29

The simplest way to understand the very advanced search functionality on pubmed is to use the PubMed advanced query builder 
or you can do a simple search, and then pay close attention to the box labeled “search details” on the right sidebar.

("sleep apnea syndromes"[MeSH Terms] 
OR ("sleep"[All Fields] 
AND "apnea"[All Fields] 
AND "syndromes"[All Fields]) 
OR "sleep apnea syndromes"[All Fields] 
OR ("sleep"[All Fields] 
AND "disordered"[All Fields] 
AND "breathing"[All Fields]) 
OR "sleep disordered breathing"[All Fields]) 
AND ("child"[MeSH Terms] 
OR "child"[All Fields] 
OR "children"[All Fields])

PubMed is using MesH terms to map my search to what I “really wanted”.
MesH stands for “Medical Subject Headings” is an ontology built specifically to make this task easier.
Use a handy URL encoder to get the term

retmod=txt  -->Next you want to set the “return mode” so that TXT is returned.

retmax=1000
"""

import requests
import time
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

tree = ET.parse('C:\\Users\\priya.cse2009\\priya\\Analytics in a World of Big Data\\Case1\\pubmed_id.xml')     
root = tree.getroot()
ids = root.findall("./IdList/Id")
filenum = 1

dest = 'C:\\Users\\priya.cse2009\\priya\\Analytics in a World of Big Data\\Case1\\pubmed\\'

for i in ids:
    
    url = 'https://www.ncbi.nlm.nih.gov/pubmed/'+i.text
    print i.text
    print url
    for i in range(5): # try 5 times
	try:
		#use the browser to access the url
		response=requests.get(url,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
		html=response.content # get the html
		break # we got the file, break the loop
	except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
		print 'failed attempt',i
		time.sleep(2) # wait 2 secs
				

    if  html:
        print 'success'
        filename = dest+'f'+str(filenum)+'.txt'
        filenum+=1
        myFile = open(filename, 'w+')
        
        soup = BeautifulSoup(html) # parse the html 
        abstracttext =soup.findAll('abstracttext') # get all the abstracttext
        
        for a in abstracttext:
            text = a.text.encode('ascii','ignore')
            myFile.write(text)
        myFile.close()
    else:continue
        
       