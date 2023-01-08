# DEEPReditor-CMG
DEEPReditor-CMG: A deep learning-based predictive RNA editor for crop mitochondria Genome. 

## 1. Samples Extraction
### 1.1. ExtractSamples.py
Notes: Extraction of positive and negative samples.<br>
Data: DEEPReditor-CMG/GenomicFiles <br>
```
ExtractSamples(filenameGB,filenameFasta,numPos,numNeg)
```
filenameGB: GenBank file of genome, such as 'sequence.gb'.<br> 
filenameFasta: FASTA file of genome, such as 'sequence.fasta'.<br> 
numPos: Save the file name suffix of the positive sample, such as 'numPos+posSample.csv'.<br> 
numNeg: Save the file name suffix of the negative sample, such as 'numNeg+negSample.csv'.<br> 
