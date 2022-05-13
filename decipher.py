import argparse
from Ciphers.railFence import railFence
from Ciphers.columnar import columnarSingleThreaded,columnarMultiThreaded
from Validation.score import outputToConsole
import globals
from platform import python_implementation
def importWords(filename):
    with open(filename, 'r') as file:
        line = file.readline()
        while line:
            line = line[:-1].upper()
            globals.dic.append(line)
            line = file.readline()
        return globals.dic

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Bruteforce several ciphers"
    )

    parser.add_argument("-r","--rail", help="Bruteforces based on RailFence Cipher",action='store_true',dest='RAILFENCE')
    parser.add_argument("-c","--columnar", help="Bruteforces based on Columnar Transposition Cipher",action='store_true',dest='COLUMNAR')
    parser.add_argument("-a","--all", help="Bruteforces based on All Ciphers (NOTE: May take a longer time)",action='store_true',dest='ALL')
    parser.add_argument("-d","--dict", help="Custom Dictionary location",type=str,dest='DICT')
    parser.add_argument("-k",'--known', nargs='+',help="Known Words",dest='KNOWN')
    parser.add_argument("-singlethread","--st", help="Fallback to single-threaded",action='store_true',dest='SINGLETHREADED')
    parser.add_argument("-file","--f", help="Outputs to a file",action='store_true',dest='FILE')
    parser.add_argument(help="CipherText",type=str.upper,dest='CIPHERTEXT')
    obj = parser.parse_args()
    
    globals.known = obj.KNOWN

    if (obj.DICT):
        dicFilename = obj.DICT
    else:
        dicFilename = 'Dictionaries\\1000TopDict.txt'
    if python_implementation() == 'PyPy':
        globals.asciiFallback = True
    importWords(dicFilename)            #Imports Dictionary
    if obj.FILE:
        globals.toFile = True;

    if obj.SINGLETHREADED:
        if (obj.ALL):
            columnarSingleThreaded(obj.CIPHERTEXT)
            railFence(obj.CIPHERTEXT)                       
            outputToConsole(100)
            pass
        else:
            if (obj.RAILFENCE):
                railFence(obj.CIPHERTEXT)
                outputToConsole(100)
                
            if (obj.COLUMNAR):
                columnarSingleThreaded(obj.CIPHERTEXT)
                outputToConsole(100)
    else:
        if (obj.ALL):               
            columnarSingleThreaded(obj.CIPHERTEXT)
            railFence(obj.CIPHERTEXT)                       
            outputToConsole(100)
        else:
            if (obj.RAILFENCE):
                railFence(obj.CIPHERTEXT)
                outputToConsole(100)
                
            if (obj.COLUMNAR):
                columnarMultiThreaded(obj.CIPHERTEXT)

                outputToConsole(100)
    