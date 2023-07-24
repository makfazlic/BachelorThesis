import numpy as np
import time
import re
import os
import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

# Condition to kill the process
def no_improvement(bleu_scores):
    s = np.array(bleu_scores)
    s[0] = s[0]+0.01
    if np.argmax(s) == 0:
        return True
    else:
        return False


# Input the PID of a process
PID = int(sys.argv[1])

# Path of th log file
log_file = sys.argv[2]

# Path of the file to write the BLEU scores
bleu_path = sys.argv[3]

# Pattern to search for
pattern = "bleu-4"

bleu_file = open(bleu_path, "a")

while True:
    with open(log_file) as f:
        lines = f.read().splitlines()
        all_bleus = [line for line in lines if pattern in line]
        read_scores = [float(line.split(" ")[-2]) for line in all_bleus]
        print("[Java] This run BLEU scores: ", read_scores)
        bleu_file.write("[Java] This run BLEU scores: " + str(read_scores) + "\n")
        if len(read_scores) >= 5:
            read_scores_5 = read_scores[-5:]
            if no_improvement(read_scores_5):
                break
        f.close()
    time.sleep(60)

# Kill the process
print("Killing the process")
bleu_file.write("Killing the process" + "\n")
os.kill(PID, 9)

bleu_file.close()
    

