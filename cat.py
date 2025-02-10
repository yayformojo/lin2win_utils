import argparse
import sys
import os

# Sample for teaching
# Can make executable with pyinstaller or re-write in C or Go
# TODO add binary file check, if binary run "strings" linux equivalent
# TODO add command line args

parser = argparse.ArgumentParser(description='Reads file and prints the contents')
parser.add_argument('file', type=str, help='The file to read')
args = parser.parse_args()
file = args.file

def lencheck(file):
    return os.path.getsize(file) <= 10000000

if lencheck(file):
    with open(file, 'r') as f:
        print(f.read())
else:
    proceed = input('File exceeds 10MB....continue? [Y n]')
    if proceed.lower() == 'n':
        sys.exit()
    else:
        with open(file, 'r') as f:
            print(f.read())