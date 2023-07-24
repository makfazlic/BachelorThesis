import numpy as np
import pandas as pd
import os
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--language', type=str, default='None')
args = parser.parse_args()

language = args.language.lower()
print("[Start] Running the script, preparing to procees the {} directory".format(language))

files_in_dir = []

try:
    files_in_dir = os.listdir(language)
except:
    print("No such directory: {}".format(language))
    exit(1)

train, valid, test = "", "", ""

for file in files_in_dir:
    if 'train' in file and '.jsonl' in file:
        train = file
    elif 'valid' in file and '.jsonl' in file:
        valid = file
    elif 'test' in file and '.jsonl' in file:
        test = file

train_file = open(language + "/" + train, "r")
train_data = train_file.readlines()

lengths = []

for line in train_data:
    line = json.loads(line)
    lengths.append(len(line["code_tokens"]))

lengths = np.array(lengths)
Q1 = np.percentile(lengths, 25)
med = np.median(lengths)
Q3 = np.percentile(lengths, 75)
print(f"1st quartile {Q1}")
print(f"Median {med}")
print(f"3rd quartile {Q3}")


low = np.where(lengths <= Q1)
low_medium = np.where((Q1 < lengths) & (lengths <= med))
medium_high = np.where((med < lengths) & (lengths <= Q3))
high = np.where(Q3 < lengths)

classes = {
    "Class" : ["low", "low_medium", "medium_high", "high"],
    "Size of the class (instances)" : [len(lengths[low]), len(lengths[low_medium]), len(lengths[medium_high]), len(lengths[high])],
    "Mean length of the class" : [np.mean(lengths[low]), np.mean(lengths[low_medium]), np.mean(lengths[medium_high]), np.mean(lengths[high])],
    "Percentage of the class" : [str(round(100*len(lengths[low])/len(lengths),2))+ "%" , str(round(100*len(lengths[low_medium])/len(lengths),2))+ "%" , str(round(100*len(lengths[medium_high])/len(lengths),2))+ "%" , str(round(100*len(lengths[high])/len(lengths),2))+ "%" ]
}

classes = pd.DataFrame(classes).reset_index(drop=True)
print(classes)

train_low, train_low_medium, train_medium_high, train_high = [], [], [], []

for line in train_data:
    line = json.loads(line)
    if len(line["code_tokens"]) <= Q1:
        train_low.append(line)
    if len(line["code_tokens"]) <= med:
        train_low_medium.append(line)
    if len(line["code_tokens"]) <= Q3:
        train_medium_high.append(line)
    train_high.append(line)

with open(language + "/train_cl_1.jsonl", "w") as f:
    for line in train_low:
        f.write(json.dumps(line))
        f.write("\n")

with open(language + "/train_cl_2.jsonl", "w") as f:
    for line in train_low_medium:
        f.write(json.dumps(line))
        f.write("\n")

with open(language + "/train_cl_3.jsonl", "w") as f:
    for line in train_medium_high:
        f.write(json.dumps(line))
        f.write("\n")


with open(language + "/train_cl_4.jsonl", "w") as f:
    for line in train_high:
        f.write(json.dumps(line))
        f.write("\n")

print("[Done] The data has been split into 4 classes. The files are stored in the {} directory".format(language))
# Print nuber of lines in each file
final_classes = {
    "File" : ["train_cl_1.jsonl", "train_cl_2.jsonl", "train_cl_3.jsonl", "train_cl_4.jsonl"],
    "Number of lines" : [len(train_low), len(train_low_medium), len(train_medium_high), len(train_high)],
    "Percentage of the class" : [str(round(100*(len(train_low)/len(train_data)),2))+ "%" , str(round(100*(len(train_low_medium)/len(train_data)),2))+ "%" , str(round(100*(len(train_medium_high)/len(train_data)),2))+ "%" , str(round(100*(len(train_high)/len(train_data)),2))+ "%" ]
}
final_classes = pd.DataFrame(final_classes).reset_index(drop=True)
print(final_classes)


