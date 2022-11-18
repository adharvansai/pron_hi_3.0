def updateRulesFile(updatedRules):
    f = open("omapHelper/rules.txt", "w+")
    f.write(updatedRules)
    f.close()
    
def getRules():
    f = open("omapHelper/rules.txt", "r+")
    rules = f.read()
    return rules

def getRulesDict():
    f = open("omapHelper/rules.txt", "r+")
    content = f.read()
    lines = content.split("\n")
    rules = {}
    for l in lines:
        l = l.strip()
        sep = l.split(",")
        k = "".join(list(sep[0])[1:-1])
        rules[k] = []
        for i in sep[1:]:
            if i:
                rules[k].append(i)
    return rules