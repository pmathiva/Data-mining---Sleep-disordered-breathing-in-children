# Data-mining: Sleep-disordered-breathing-in-children

Sleep-disordered breathing (SDB) is a common and highly prevalent condition in children, affecting up to 27 percent of children, with a median in the 10 percent to 12 percent range. Rather than being an “all of nothing” condition, SDB is traditionally perceived as encompassing a wide spectrum of clinical severity – ranging from habitual snoring to obstructive sleep apnea syndrome (OSAS).

247 Articles Associated with the Treatment and Outcomes of SDB.

The research team is interested in identifying relevant patterns associated with existing research trends – the objective is to index and mine these documents using singular value decomposition (SVD) with the intent of identifying logical patterns in the text.

* pubmed_extract.py
  This script extracts all the files related to the search keywords.
  In this case, the search keywords are :'Sleep disordered breathing'
  
* case1.r
  This script parses all the downloaded files and the pdf's to make a document term matrix and then a word cloud of the top frequent terms
  
