folder = "ttHDaniel"
inFile = open(folder+"/datasetList.txt")
datasets = []
for dataset in inFile:
    dataset = dataset.replace("\n","")
    if "/" in dataset:
        datasets.append(dataset)

import os
filesPerDict = {}
for dataset in datasets:
    command = 'das_client --limit=0 --query "file dataset=%s instance=prod/phys03"'%dataset
    print command
    files = os.popen(command).read()
    files = files.split('\n')
    files = [file_ for file_ in files if ".root" in file_]
    filesPerDict[dataset] = files



counter = 0
for dataset in datasets:
    fileName = dataset
    cut = -1
    for i in range(len(fileName)):
        if fileName[i] is "-":
            cut = i
    fileName = fileName[0:cut]
    fileName = fileName.replace("/","_")[1:]
    address = folder+"/"+fileName+".txt"
    outFile = open(address,"w")
    outFile.write("[%s]\n"%fileName)
    for file_ in filesPerDict[dataset]:
        outFile.write(file_ + " = "+str(counter)+"\n")
        counter+=1



