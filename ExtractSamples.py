#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time :2021.9.28
# Update :2022.3.2
# Author :QinSidong
# Notes: ExtractSamples(filenameGB,filenameFasta,numPos,numNeg)
# filenameGB:GenBank file of genome, such as 'sequence.gb'.
# filenameFasta:FASTA file of genome, such as 'sequence.fasta'
# numPos:Save the file name suffix of the positive sample, such as 'numPos+posSample.csv'.
# numNeg:Save the file name suffix of the negative sample, such as 'numPos+negSample.csv'.


from random import sample
import re

def DNA_complement2(sequence):  #碱基互补配对
    trantab = str.maketrans('ACGTNacgt', 'TGCANtgca')     # trantab = str.maketrans(intab, outtab)   # 制作翻译表
    string = sequence.translate(trantab)     # str.translate(trantab)  # 转换字符
    return string

def ExtractMisc_feature(filenameGB,seq):     #提取有效的misc_featureID
    with open(filenameGB,'r') as f: #gb文件
        dataInput = f.readlines()
    f.close()

    #提取编辑位点ID
    misc_feature=[]
                
    for i in range(len(dataInput)):
        if dataInput[i].startswith('     misc_feature') == True :
            if str(dataInput[i].rsplit()[1]).isdigit() == True :
                misc_feature.append(dataInput[i].rsplit()[1])
            else: 
                if str(dataInput[i].rsplit()[1]).find('(') > 0:
                    if (re.findall(r'[(](.*?)[)]', dataInput[i]))[0].isdigit() == True:
                        misc_feature=misc_feature+(re.findall(r'[(](.*?)[)]', dataInput[i]))
        misc_feature = list(map(int, misc_feature))
       
    #对misc_featureID再一次检查，排除序列A中G编辑位点，和序列B中C编辑位点
    Cid=[]
    Gid=[]
    for i in range(len(misc_feature)):
        if seq[misc_feature[i]-1]=='C':
            if 250 <misc_feature[i]< len(seq)-250: #排除空白行
                Cid=Cid + [misc_feature[i]]
        if seq[misc_feature[i]-1]=='G':
            if 250 <misc_feature[i]< len(seq)-250:
                Gid=Gid + [misc_feature[i]]
    return Cid,Gid

def ExtractSeq(filenameFasta):          #提取序列数据
    with open(filenameFasta,'r') as x: #fasta文件
        dataInput = x.readlines()
        x.close()
    sequence = dataInput[1:]

    i=0
    seq0=str()                            #整理序列数据，转为List
    while i < len(sequence):
        seq0=seq0+str(sequence[i][0:-1])
        i=i+1
    seq=list(seq0)

    return seq

def ExtractPosNeg(Cid,Gid,seq,numPos,numNeg):

    #提取正样本
    result = open(f'{numPos}PosSample.csv', 'w', encoding='gbk') #保存正样本
    for i in range(len(Cid)):
        newC = list(seq[Cid[i]-1-250:Cid[i]+251-1])
        for i in range(0, len(newC)-1):
            result.write(str(newC[i]))
            result.write(',')  
        result.write(str(newC[-1]))
        result.write(',')
        result.write('1')
        result.write("\n")

    for i in range(len(Gid)):
        newG = list(seq[Gid[i]-1-250:Gid[i]+251-1])
        for i in range(0, len(newG)-1):
            result.write(str(DNA_complement2(newG[i])))
            result.write(',')  
        result.write(str(DNA_complement2(newG[-1])))
        result.write(',')
        result.write('1')
        result.write("\n")
    result.close()

    print(f"Positive sample extraction succeeded, see '{numPos}PosSample.csv'.")

    #提取负样本
    #负样本提取，A链和b链分别排除编辑位点后，随机取与正样本等量的非编辑位点的序列。
    allC=[i for i , x in enumerate(seq) if x == 'C' ]  #找到所有的‘C’位点
    trueCNew = [x  for x in Cid] #补齐250
    newC=[i for i in allC if i not in trueCNew] #排除是编辑位点的‘C’
    newCid=[]
    for i in range(len(newC)):
        if 250< int(newC[i]) <len(seq)-250 :
            newCid = newCid +[newC[i]]
    negativeCid = newCid    #随机提取非编辑位点‘’

    allG=[i for i , x in enumerate(seq) if x == 'G' ]  #找到所有的‘G’位点
    trueGNew = [x  for x in Gid] #补齐250
    newG=[i for i in allG if i not in trueGNew] #排除是编辑位点的‘G’
    newGid=[]
    for i in range(len(newG)):
        if 250< int(newG[i]) <len(seq)-250 :
            newGid = newGid +[newG[i]]
    negativeGid = newGid     #随机提取非编辑位点‘’

    result2 = open(f'{numNeg}NegSample.csv', 'w', encoding='gbk') #保存负样本
    for i in range(len(negativeCid)):
        negCFeature = list(seq[negativeCid[i]-250:negativeCid[i]+251])
        for j in range(0, len(negCFeature)-1):
            result2.write(str(negCFeature[j]))
            result2.write(',')  
        result2.write(str(negCFeature[-1]))
        result2.write(',')
        result2.write('0')
        result2.write("\n") 

    for i in range(len(negativeGid)):
        negGFeature = list(seq[negativeGid[i]-250:negativeGid[i]+251])
        for j in range(0, len(negGFeature)-1):
            result2.write(str(DNA_complement2(negGFeature[j])))#互补
            result2.write(',')  
        result2.write(str(DNA_complement2(negGFeature[-1])))#互补
        result2.write(',')
        result2.write('0')
        result2.write("\n") 

    result2.close()
    print(f"Negative sample extraction succeeded, see '{numNeg}NegSample.csv'.")


if __name__ == "__main__":
    def Extract(filenameGB,filenameFasta,numPos,numNeg):
        seq = ExtractSeq(filenameFasta)
        Cid,Gid=ExtractMisc_feature(filenameGB,seq)
        ExtractPosNeg(Cid,Gid,seq,numPos,numNeg)

       