import globals
from shutil import get_terminal_size
flag = False
def scoreViaDict(plainText:str,dic=globals.dic): #Scores Based on a dictionary
    if globals.known:
        return scoreViaDictWithKnownWords(plainText)
    
    score = 0 
    wordFound = []
    for word in dic:
        _cnt = plainText.count(word)
        if _cnt > 0:
            score += _cnt
            wordFound.append(word.lower())
    return [score, plainText, ','.join(wordFound)]

def scoreViaDictWithKnownWords(plainText:str,dic=globals.dic,knownWords=globals.known):
    score = 0 
    if globals.known:
        for word in globals.known:
            if(plainText.count(word.upper()) ==0):
                return [0, plainText, '']
    
    wordFound = []
    for word in dic:
        _cnt = plainText.count(word)
        if _cnt > 0:
            score += _cnt
            wordFound.append(word.lower())
    return [score, plainText, ','.join(wordFound)]
    
    
    pass



def outputToConsole(noToPrint:int=100):
    global ranked
    if globals.asciiFallback:
        print('-' * get_terminal_size().columns)
    else:
        print(u'\u2500' * get_terminal_size().columns)
    globals.ranked = sorted(globals.ranked, key=lambda item: item[0], reverse=True)
    try:
        for i in range(noToPrint):
            if (globals.ranked[i][0]==0):
                pass
            else:
                print(globals.ranked[i][1].lower(), 'score=' + str(globals.ranked[i]
                                                    [0]), 'word=' + globals.ranked[i][2], sep=' | ',end=' |\n')
        if globals.toFile:
            f = open("results.txt",'w')
            for strings in globals.ranked:
                if (strings[0]==0):
                    pass
                else:
                    f.write("{},score={},words={}\n".format(strings[1].lower(),strings[0],strings[2]))
            f.close()
    except IndexError:
        pass