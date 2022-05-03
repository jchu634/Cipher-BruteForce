from Validation.score import scoreViaDict,outputToConsole
from pycipher import Railfence
from tqdm import tqdm
import globals

def railFence(cipherText:str,noToPrint:int=100):
    global ranked
    rails = range(2, 11)

    print("Brute forcing")

    for i in tqdm(rails,ascii=globals.asciiFallback,desc='BruteForce Progress'):
        plaintext = Railfence(i).decipher(cipherText);
        globals.ranked.append(scoreViaDict(plaintext))