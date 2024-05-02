import random
import os

def substitute_ambiguous(base):
    if base == 'R':
        return random.choice(['A', 'G'])
    elif base == 'Y':
        return random.choice(['C', 'T'])
    elif base == 'S':
        return random.choice(['G', 'C'])
    elif base == 'W':
        return random.choice(['A', 'T'])
    elif base == 'K':
        return random.choice(['G', 'T'])
    elif base == 'M':
        return random.choice(['A', 'C'])
    elif base == 'B':
        return random.choice(['C', 'G', 'T'])
    elif base == 'D':
        return random.choice(['A', 'G', 'T'])
    elif base == 'H':
        return random.choice(['A', 'C', 'T'])
    elif base == 'V':
        return random.choice(['A', 'C', 'G'])
    elif base == 'N':
        return random.choice(['A', 'C', 'G', 'T'])
    else:
        return base

def modify_fasta(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.startswith('>'):
                outfile.write(line)
            else:
                modified_line = ''.join([substitute_ambiguous(base) for base in line.strip()])
                outfile.write(modified_line + '\n')

loc = "../Fasta Data/"
destLoc = "./"
# For each file in the loc, modify the data and save it in the destLoc

for file in os.listdir(loc):
    if file.endswith(".fasta"):
        modify_fasta(loc+file, destLoc+"modified_"+file)

# Python code snippet that reads a FASTA file, performs random substitutions for ambiguous characters, and writes the modified sequences to a new FASTA file

# This code defines two functions:

# - `substitute_ambiguous(base)`: performs the random substitution for a single ambiguous character
# - `modify_fasta(input_file, output_file)`: reads the input FASTA file, modifies the sequences, and writes the output to a new FASTA file

# The `modify_fasta` function uses a context manager to handle file input/output. It iterates over each line in the input file, checks if the line is a header (starting with '>'), and writes it as-is to the output file. If the line is a sequence, it applies the `substitute_ambiguous` function to each base and writes the modified sequence to the output file.

# Note that this code assumes that the input FASTA file contains only uppercase letters (A, C, G, T, and ambiguous characters). If your file contains lowercase letters or other characters, you may need to modify the code accordingly.