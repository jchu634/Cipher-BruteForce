import globals
from shutil import get_terminal_size
def scoreViaDict(plainText:str,dic=globals.dic): #Scores Based on a dictionary
    score = 0 
    wordFound = []
    for word in dic:
        _cnt = plainText.count(word)
        if _cnt > 0:
            score += _cnt
            wordFound.append(word.lower())
    return [score, plainText, ','.join(wordFound)]

def outputToConsole(noToPrint:int=100):
    global ranked
    if globals.asciiFallback:
        print('-' * get_terminal_size().columns)
    else:
        print(u'\u2500' * get_terminal_size().columns)
    globals.ranked = sorted(globals.ranked, key=lambda item: item[0], reverse=True)
    try:
        for i in range(noToPrint):
            print(globals.ranked[i][1].lower(), 'score=' + str(globals.ranked[i]
                                                    [0]), 'word=' + globals.ranked[i][2], sep=' | ',end=' |\n')
    except IndexError:
        pass