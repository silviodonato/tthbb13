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
    outFile = open(folder+"/"+dataset.replace("/","_")[1:]+".txt","w")
    for file_ in filesPerDict[dataset]:
        outFile.write(file_ + " = "+str(counter))
        counter+=1



