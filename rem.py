#!/usr/bin/env python3
import os, glob, sys, re

def changeDir():
  try:
    os.chdir('treatedFiles')
  except:
    os.mkdir('treatedFiles')
    os.chdir('treatedFiles')

def go(path):
  changeDir()
  for currentFile in glob.glob(os.path.join(path, '*')):
    newFile = currentFile[-12:]
    with open(currentFile, 'r') as f, open(newFile, 'w') as output:
      print('Treating file: ', f.name)
      for line in f:
        rasc = re.search(r'\b^rascunho\b', line)
        if (rasc == None):
          newLine = re.sub('\"', '', line)
          output.write(newLine)
        else:
          print('Found a -rascunho-')
    f.closed
    
def main():
  path = 'Y:/scripts/test/'
  go(path)
  
if __name__ == "__main__":
  main()
