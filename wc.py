# wc.exe for Windows
import sys
import os

def count_cwl(filearg):
    if not os.path.isfile(filearg):
        print(f'The file {filearg} can\'t be found')
    
    with open(filearg, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        chars = sum(len(line) for line in lines)
        
    print(f'Output (chars, words, lines): {chars}, {num_words}, {num_lines}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Requires a filename argument after the wc command')
    else: 
        count_cwl(sys.argv[1])
        
# TODO add command line switches


