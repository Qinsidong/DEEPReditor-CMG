# DEEPReditor-CMG
DEEPReditor-CMG: A deep learning-based predictive RNA editor for crop mitochondria Genome. 

## 1. Samples Extraction
[GenomicFiles](https://github.com/Qinsidong/DEEPReditor-CMG/tree/main/GenomicFiles) $\rightarrow$ [Positive&NegativeSamples](https://github.com/Qinsidong/DEEPReditor-CMG/tree/main/Positive&NegativeSamples) $\rightarrow$ [Train&Test](https://github.com/Qinsidong/DEEPReditor-CMG/tree/main/Train&Test)<br>
GenomicFiles: Samples genome files and NCBI annotation files.<br>
Positive&NegativeSamples: Positive and negative sample files of 501bp.<br>
Train&Test: Randomly divide the training sets and test sets file 5 times.<br>
1	Lactuca sativa var. capitata	MZ159954	Gunneridae	Asterales	Asteraceae	Lactuca
2	Arabidopsis thaliana	Y08501	Gunneridae	Brassicales	Brassicaceae	Arabidopsis
3	Arabidopsis thaliana ecotype Col-0	NC_037304	Gunneridae	Brassicales	Brassicaceae	Arabidopsis
4	Brassica napus	NC_008285	Gunneridae	Brassicales	Brassicaceae	Brassica
5	Capsella bursa-pastoris	MN746809	Gunneridae	Brassicales	Brassicaceae	Capsella
6	Raphanus sativus	JQ083668	Gunneridae	Brassicales	Brassicaceae	Raphanus
7	Cucurbita pepo	GQ856148	Gunneridae	Cucurbitales	Cucurbitaceae	Cucurbita
8	Citrullus lanatus	GQ856147	Gunneridae	Cucurbitales	Cucurbitaceae	Citrullus
9	Nelumbo nucifera	NC_030753	Gunneridae	Proteales	Nelumbonaceae	Nelumbo
10	Solanum tuberosum	MN114537	Gunneridae	Solanales	Solanaceae	Solanum
11	Oryza sativa Japonica	BA000029	Liliopsida	Poales	Poaceae	Oryza
12	Triticum aestivum	NC_036024.1	Liliopsida	Poales	Poaceae	Triticum
13	Zea mays	AY506529	Liliopsida	Poales	Poaceae	Zea
![image](https://user-images.githubusercontent.com/73972671/217201161-7e9c54cf-4911-4062-a717-0b0438d354f9.png)


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



