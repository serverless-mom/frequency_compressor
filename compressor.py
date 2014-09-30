#new file name for the compressed file
compressFileName = "CompressDick.txt"
#compression target
textFileName = "MobyDickshort.txt"
#don't modify unless you're copying the formatting exactly with a new frequency table
dictFileName = "top1000.txt"
textFile = open (textFileName,"r")
top10 = open (dictFileName,"r")
compressResult = open (compressFileName,"w")
textLines = []
terms = []

#cut for final version, this tests the decompression
decompressFileName = "deCompressDick.txt"
decompressResult = open (decompressFileName,"w")

def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

def arrayMaker(source, dest):
    for line in source:
        dest.append (line.rstrip()),
arrayMaker(textFile, textLines)
arrayMaker(top10, terms)

#Dictionary to undo compression
revDictionary = dict(e.split(' ') for e in terms)
#Compression Dictionary
myDictionary = {v: k for k, v in revDictionary.items()}

#create compress file
for line in textLines:
    compressLine = (replace_all(line, myDictionary))
    compressResult.write(compressLine)
    #testing decompression
    decompressLine = (replace_all(line, revDictionary))
    decompressResult.write(decompressLine)