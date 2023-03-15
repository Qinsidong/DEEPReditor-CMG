# DEEPReditor-CMG
DEEPReditor-CMG: A deep learning-based predictive RNA editor for crop mitochondria Genome.<br>
基于深度学习的作物线粒体基因组RNA编辑预测。<br>
Details: The article is in the process of being published. Article Link.<br>
References：<br>
[1] Qin S, Fan Y, Hu S, et al. iPReditor-CMG: Improving a predictive RNA editor for crop mitochondrial genomes using genomic sequence features and an optimal support vector machine. Phytochemistry. 2022;200:113222. doi:10.1016/j.phytochem.2022.113222. [PubMed](https://pubmed.ncbi.nlm.nih.gov/35561852/)
## 1. Samples Extraction
[GenomicFiles](https://github.com/Qinsidong/DEEPReditor-CMG/tree/main/GenomicFiles) $\rightarrow$ [Positive&NegativeSamples](https://github.com/Qinsidong/DEEPReditor-CMG/tree/main/Positive&NegativeSamples) $\rightarrow$ [Train&Test](https://github.com/Qinsidong/DEEPReditor-CMG/tree/main/Train&Test)<br>
GenomicFiles: Samples genome files and NCBI annotation files.<br>
Positive&NegativeSamples: Positive and negative sample files of 501bp.<br>
Train&Test: Randomly divide the training sets and test sets file 5 times.<br>
![image](https://user-images.githubusercontent.com/73972671/217203098-82994219-0107-4ff9-8b6e-56d017122914.png)

### 1.1. [ExtractSamples.py](https://github.com/Qinsidong/DEEPReditor-CMG/blob/main/ExtractSamples.py)
Note: Extraction of positive and negative samples.<br>
Data: DEEPReditor-CMG/GenomicFiles <br>
```python
ExtractSamples(filenameGB,filenameFasta,numPos,numNeg)
```
filenameGB: GenBank file of genome, such as 'sequence.gb'.<br> 
filenameFasta: FASTA file of genome, such as 'sequence.fasta'.<br> 
numPos: Save the file name suffix of the positive sample, such as 'numPos+posSample.csv'.<br> 
numNeg: Save the file name suffix of the negative sample, such as 'numNeg+negSample.csv'.<br> 
### 1.2. [TrainTestPartition.py](https://github.com/Qinsidong/DEEPReditor-CMG/blob/main/TrainTestPartition.py)
Note: Dividing the training sets and test sets.<br>
Data: DEEPReditor-CMG/Positive&NegativeSamples <br>
```python
TrainTest(posfile,negfile,n,random_state)
```
posfile: A positive sample file.<br>
negfile: A negfile sample file.<br>
n: Number of the result document.<br>
random_state: A random number of positive integers.<br>
### 1.3. [SuperSampler.py](https://github.com/Qinsidong/DEEPReditor-CMG/blob/main/SuperSampler.py)
Note: A data enhancement approach for genomic data.<br>
```python
SuperSampler(input,step,output)
```
input: Input data.<br>
step: A positive integer.<br>
output: Output data.<br>

## 2. Model building and hyperparameter optimization
[Hyperparametric_Optimization_Search](https://github.com/Qinsidong/DEEPReditor-CMG/tree/main/Hyperparametric_Optimization_Search)<br>
For more details please check the article.<br>
[DEEPReditor.py](https://github.com/Qinsidong/DEEPReditor-CMG/blob/main/Hyperparametric_Optimization_Search/Final_model_structure/DEEPReditor.py)<br>
Final CNN model structure.<br>
[KerasTunerBPN.py](https://github.com/Qinsidong/DEEPReditor-CMG/blob/main/Hyperparametric_Optimization_Search/Final_model_structure/KerasTunerBPN.py)<br>
Reference model, BPN model structure.<br>


## 3. Applications
### 3.1 [DEEPReditor(Python_scripts_version)](https://github.com/Qinsidong/DEEPReditor-CMG/tree/main/DEEPReditor(Python_scripts_version))
Note: DEEPReditor(Python_scripts_version). To use, download this version to run locally.
#### 3.1.1 [PreCustomData.py](https://github.com/Qinsidong/DEEPReditor-CMG/blob/main/DEEPReditor(Python_scripts_version)/PreCustomData.py)
Note: Suitable for prediction of specified base loci in crop mitochondrial genomes.<br>
[SampleUsage](https://github.com/Qinsidong/DEEPReditor-CMG/tree/main/DEEPReditor(Python_scripts_version)/SampleUsage): Sample usage.
```python
start(['Liliopsida','None','None','None'],'8Neg8Pos.csv',threshold=0.75)
```
['Liliopsida','None','None','None']: Species Category.<br>
Range of sequential selection:<br>
Class = ['Gunneridae','Liliopsida']<br>
Order = ['Cucurbitales','Proteales','Brassicales','Asterales','Solanales','Brassicales','Rhoeadales','Poales']<br>
Family = ['Cucurbitaceae','Nelumbonaceae','Brassicaceae','Asteraceae','Solanaceae','Poaceae']<br>
Genus = ['Cucurbita','Nelumbo','Citrullus','Arabidopsis','Lactuca','Solanum','Capsella','Raphanus','Brassica','Oryza','Triticum','Zea']<br>

['8Neg8Pos.csv'](https://github.com/Qinsidong/DEEPReditor-CMG/blob/main/DEEPReditor(Python_scripts_version)/SampleUsage/8Neg8Pos.csv): Specify sample (example).<br>
threshold: Predicted minimum threshold.The value range is (0,1), the larger the value the stricter the filtering condition and the higher the confidence of the prediction result.<br>
#### 3.1.2 [PreWholeGen.py](https://github.com/Qinsidong/DEEPReditor-CMG/blob/main/DEEPReditor(Python_scripts_version)/PreWholeGen.py)
Note: Suitable for C-to-U editing site prediction for whole crop mitochondrial genomes.
```python
startWholeGen("sequence (0).fasta",['Gunneridae','Cucurbitales','Cucurbitaceae','Cucurbita'],threshold=0.9999)
```
["sequence (0).fasta"](https://github.com/Qinsidong/DEEPReditor-CMG/blob/main/DEEPReditor(Python_scripts_version)/SampleUsage/sequence%20(0).fasta): Genome-wide data (example).<br>
['Gunneridae','Cucurbitales','Cucurbitaceae','Cucurbita']: Species Category.<br>
Range of sequential selection:<br>
Class = ['Gunneridae','Liliopsida']<br>
Order = ['Cucurbitales','Proteales','Brassicales','Asterales','Solanales','Brassicales','Rhoeadales','Poales']<br>
Family = ['Cucurbitaceae','Nelumbonaceae','Brassicaceae','Asteraceae','Solanaceae','Poaceae']<br>
Genus = ['Cucurbita','Nelumbo','Citrullus','Arabidopsis','Lactuca','Solanum','Capsella','Raphanus','Brassica','Oryza','Triticum','Zea']<br>
<br>
threshold: Predicted minimum threshold.The value range is (0.5,1), the larger the value the stricter the filtering condition and the higher the confidence of the prediction result.<br>
[match](https://github.com/Qinsidong/DEEPReditor-CMG/tree/main/DEEPReditor(Python_scripts_version)/match) & [modle](https://github.com/Qinsidong/DEEPReditor-CMG/tree/main/DEEPReditor(Python_scripts_version)/model): Required Folders.
### 3.2 DEEPReditor(Executable_program_version)
