proteinDict = {'AUG' : "Methionine", 

        

          

               'UUU' : "Phenylalanine", 

        

          

               'UUC' : "Phenylalanine",

        

          

               'UUA' : "Leucine", 'UUG' : "Leucine",

        

          

               'UCU' : "Serine", 'UCC' : "Serine", 'UCA' : "Serine", 'UCG'	: "Serine",

        

          

               'UAU' : "Tyrosine", 'UAC' : "Tyrosine",

        

          

               'UGU' : "Cysteine", 'UGC' : "Cysteine",

        

          

               'UGG' : "Tryptophan",

        

          

               'UAA' : "STOP", 'UAG' : "STOP", 'UGA' : "STOP"}

        

          


        

          


        

          

def proteins(strand):

        

          

    codonList = [strand[k:k+3] for k in range(0, len(strand), 3)] 

        

          

    proteinList = [proteinDict[codon] for codon in codonList]

        

          

    if 'STOP' in proteinList:

        

          

        proteinList = proteinList[:proteinList.index("STOP")]

        

          

    return proteinList