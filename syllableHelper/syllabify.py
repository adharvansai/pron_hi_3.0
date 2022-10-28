from syllableHelper.syllables import SYLLABLES

def get_syllables(word):
    word = word.strip()
    word = word.lower()
    if(SYLLABLES.get(word)):
        return SYLLABLES[word]
    else:
        return "***"

#print(get_syllables("hiatus"))