# DEEPReditor-CMG
DEEPReditor-CMG: A deep learning-based predictive RNA editor for crop mitochondria Genome. 

## 1. Samples Extraction
[GenomicFiles](https://github.com/Qinsidong/DEEPReditor-CMG/tree/main/GenomicFiles) $\rightarrow$ [Positive&NegativeSamples](https://github.com/Qinsidong/DEEPReditor-CMG/tree/main/Positive&NegativeSamples) $\rightarrow$ [Train&Test](https://github.com/Qinsidong/DEEPReditor-CMG/tree/main/Train&Test)<br>
GenomicFiles: Samples genome files and NCBI annotation files.<br>
Positive&NegativeSamples: Positive and negative sample files of 501bp.<br>
Train&Test: Randomly divide the training sets and test sets file 5 times.<br>
![image](https://user-images.githubusercontent.com/73972671/217203098-82994219-0107-4ff9-8b6e-56d017122914.png)


### 1.1. [ExtractSamples.py](https://github.com/Qinsidong/DEEPReditor-CMG/blob/main/ExtractSamples.py)
Notes: Extraction of positive and negative samples.<br>
Data: DEEPReditor-CMG/GenomicFiles <br>
```python
ExtractSamples(filenameGB,filenameFasta,numPos,numNeg)
```
filenameGB: GenBank file of genome, such as 'sequence.gb'.<br> 
filenameFasta: FASTA file of genome, such as 'sequence.fasta'.<br> 
numPos: Save the file name suffix of the positive sample, such as 'numPos+posSample.csv'.<br> 
numNeg: Save the file name suffix of the negative sample, such as 'numNeg+negSample.csv'.<br> 
### 1.2. [TrainTestPartition.py](https://github.com/Qinsidong/DEEPReditor-CMG/blob/main/TrainTestPartition.py)
Notes: Dividing the training sets and test sets.<br>
Data: DEEPReditor-CMG/Positive&NegativeSamples <br>
```python
TrainTest(posfile,negfile,n,random_state)
```
posfile: A positive sample file.<br>
negfile: A negfile sample file.<br>
n: Number of the result document.<br>
random_state: A random number of positive integers.<br>



