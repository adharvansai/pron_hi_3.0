from omapHelper.cmulib import cmu_lib
from syllableHelper.syllabify import get_syllables
from omapHelper.updateRules import getRulesDict
rules = getRulesDict()

def getMapping(word):
    conv = cmu_lib[word.upper()]
    #print(conv)
    sylls = get_syllables(word).split("|")
    #print(sylls)
    excl_list = ['ˈ',',','`']
    orth = []
    for a in conv:
        added= 0
        ref = []
        for i in sylls:
            if i:
                ref.append(i.lower())
        sylls = ref
        if a not in excl_list:
            key = a
            rule_ord = rules[key]
            for i in range(len(sylls)):
                flg = 0
                for comb in rule_ord:
                    if comb in sylls[i]:
                        if i != 0:
                            orth.append((sylls[0],""))
                            sylls[0] = ""

                        idx = sylls[i].find(comb)
                        if idx != 0:
                            let = sylls[0][:idx]
                            orth.append((let, ""))
                        idxend = idx + len(comb)
                        let = sylls[i][idx:idxend]
                        added = 1
                        orth.append((let, key))
                        sylls[i] = sylls[i][idxend:]

                        if not sylls[i]:
                            sylls = sylls[i+1:]
                        flg = 1
                        break
                if flg:
                    break
        if not added:
            orth.append(("",a))
    # print(sylls)
    if sylls:
        silent = "".join(sylls)
        orth.append((silent, ""))
    # print(orth)
    return orth


def getmap(word):
    print(word)
    word = word.lower().strip()
    mapp = getMapping(word)
    res = []
    for let,phn in mapp:
        rep = let + " &ensp; --- &ensp; " + phn
        res.append(rep)
    return res

#print(getMapping("independence"))