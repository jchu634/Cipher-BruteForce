from pycipher import ColTrans
from multiprocessing import Pool, cpu_count,freeze_support
from itertools import permutations
from functools import partial
from tqdm import tqdm
if __name__ == '__main__':
    import sys
    sys.path.append("..") # Adds higher directory to python modules path.
    def importWords(filename):
        with open(filename, 'r') as file:
            line = file.readline()
            while line:
                line = line[:-1].upper()
                globals.dic.append(line)
                line = file.readline()
            return globals.dic
    from timeit import default_timer as timer

import globals
from Validation.score import scoreViaDict
    
def columnarSingleThreaded(cipherText:str,maxKeyLength:int=9):    
    perms = ['']
    for i in range(1, maxKeyLength+1):
        if globals.verbose:
            print('Key Length n = %d' % i)
        perms = [''.join(p) for p in permutations(perms[0]+str(i))]        
        bruteForceDecipher(cipherText, perms)


def columnarMultiThreaded(cipherText:str,maxKeyLength:int=9):
    perms = ['']
    for i in tqdm(range(1, maxKeyLength+1),ascii=globals.asciiFallback,desc='BruteForce Progress'):
        perms = [''.join(p) for p in permutations(perms[0]+str(i))]        
        with Pool(cpu_count()) as p:
            """
            NOTE:   Uses a singleThread get a list from a function
                    instead of a multiThreaded to make a list from several functions returning a single item
            Seems to be faster with a single-thread

            NOTE: Scoring is done multi-threaded, 
            however during testing, single-threading was faster until n=9 where multi-threading was overwhelmingly faster
            """
            globals.ranked += p.map(partial(partial(scoreViaDict,dic=globals.dic),knownWords = globals.known),bruteForceDecipherList(cipherText,perms))


def bruteForceDecipher(cipherText, perms):
    for key in perms:
        plainText = ColTrans(key).decipher(cipherText)
        globals.ranked.append(scoreViaDict(plainText))

def unsortind(word): #From PyCipher for bruteForceDecipherString
    t1 = [(word[i],i) for i in range(len(word))]
    return [q[1] for q in sorted(t1)]    

def bruteForceDecipherString(cipherText,key) -> str:
    ret = ['_']*len(cipherText)
    L,M = len(cipherText),len(key)
    ind = unsortind(key)
    upto = 0
    for i in range(len(key)):
        thiscollen = (int)(L/M)
        if ind[i]< L%M: thiscollen += 1
        ret[ind[i]::M] = cipherText[upto:upto+thiscollen]
        upto += thiscollen
    return ''.join(ret)

def bruteForceDecipherList(cipherText, perms) -> list:
    returnList = []
    for key in perms:
        returnList.append(ColTrans(key).decipher(cipherText))
    return returnList


if __name__ == '__main__':
    freeze_support()
