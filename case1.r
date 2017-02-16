
install.packages("rJava")
install.packages("openNLP")

#Sys.getenv("R_ARCH") #Check version of R

library(tm)
library(SnowballC)
library(wordcloud)
library(NLP)
library(openNLP)

#Custom function - POS tagging for a corpus
#The tm package provides the ability to do this via the content_transformer function. 
#This function takes a function as input, 
#the input function should specify what transformation needs to be done
# content_transformer(   function(parameters){....}  )
tagPOS <- content_transformer( function(x, ...)
{
  s <- as.String(x)
  word_token_annotator <- Maxent_Word_Token_Annotator()
  a2 <- Annotation(1L, "sentence", 1L, nchar(s))
  a2 <- NLP::annotate(s, word_token_annotator, a2)
  a3 <- annotate(s, Maxent_POS_Tag_Annotator(), a2)
  a3w <- a3[a3$type == "word"]
  POStags <- unlist(lapply(a3w$features, `[[`, "POS"))
  POStagged <- paste(sprintf("%s/%s", s[a3w], POStags), collapse = " ")
  acqTag <- list(POStagged = POStagged, POStags = POStags)
  
  acqTagSplit = strsplit(acqTag$POStagged," ")
  l<-c()
  for (i in 1:length(acqTagSplit[[1]]))
  {
    
    qq <-strsplit(acqTagSplit[[1]][i],'/')
    tag <- qq[[1]][2]
    if (tag == "NN") 
    {
      l<-c(l,qq[[1]][1])
    }
  }
  return (l)
}
)

# Read the text files from local directory
filePath <- "C:\\Users\\priya.cse2009\\priya\\Analytics in a World of Big Data\\Case1\\247_Text_Files_for_Childrens_sleep_study\\247 Text Files for Childrens sleep study"
txt  <- Corpus(DirSource(filePath)) #specifies the exact folder where my text file(s) is for analysis with tm.

# Change to lower case, not necessary here
txt = tm_map(txt, content_transformer(tolower))
# Remove numbers
txt = tm_map(txt, removeNumbers)
# Remove punctuation marks and stopwords
txt = tm_map(txt, removePunctuation)
txt = tm_map(txt, removeWords, c("duh", "whatever", stopwords("english")))
# Remove extra whitespaces
txt =  tm_map(txt, stripWhitespace)
#POS tagging
txt = tm_map(txt,tagPOS)

length(txt[[1]]$content)

# Document-Term Matrix: documents as the rows, terms/words as the columns, frequency of the term in the document as the entries. 
#Notice the dimension of the matrix
dtm <- DocumentTermMatrix(txt)
freq = data.frame(sort(colSums(as.matrix(dtm)), decreasing=TRUE))
inspect(dtm[1:2,1:7])

wordcloud(rownames(freq), freq[,1], scale=c(3,.5),max.words=50, colors=brewer.pal(5, "Dark2"))


------------------
# folder with 1000s of PDFs
dest <- "C:\\Users\\priya.cse2009\\priya\\Analytics in a World of Big Data\\Case1\\PDFs_chest"
# make a vector of PDF file names
myfiles <- list.files(path = dest, pattern = "pdf",  full.names = TRUE)

# convert each PDF file that is named in the vector into a text file 
# text file is created in the same directory as the PDFs
# note that my pdftotext.exe is in a different location to yours
lapply(myfiles, function(i) system(paste('"C:/Program Files/xpdf/bin64/pdftotext.exe"', 
                                         paste0('"', i, '"')), wait = FALSE) )


#----!!!! Delete all the pdf's and leave the text files
filePath <- "C:\\Users\\priya.cse2009\\priya\\Analytics in a World of Big Data\\Case1\\PDFs_chest"
txt  <- Corpus(DirSource(filePath))

# Change to lower case, not necessary here
txt = tm_map(txt, content_transformer(tolower))
# Remove numbers
txt = tm_map(txt, removeNumbers)
# Remove punctuation marks and stopwords
txt = tm_map(txt, removePunctuation)
txt = tm_map(txt, removeWords, c("duh", "whatever", stopwords("english")))
# Remove extra whitespaces
txt =  tm_map(txt, stripWhitespace)
#POS tagging
txt = tm_map(txt,tagPOS)

length(txt[[1]]$content)

# Document-Term Matrix: documents as the rows, terms/words as the columns, frequency of the term in the document as the entries. 
#Notice the dimension of the matrix
dtm <- DocumentTermMatrix(txt)
freq = data.frame(sort(colSums(as.matrix(dtm)), decreasing=TRUE))
#inspect(dtm[1:2,1:7])

wordcloud(rownames(freq), freq[,1], scale=c(2,.5),max.words=100, colors=brewer.pal(5, "Dark2"))



