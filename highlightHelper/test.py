import eng_to_ipa as phen
from configDict import IPA_DICT
#print(IPA_DICT)
txt = "awe cot hot"
print((phen.convert(txt)))
# f = open("/Users/adharvan/Desktop/Work/pron_hi_2.0/highlightHelper/ipa.txt", "r+")
# ipa = f.readlines()
# unq = []
# for line in ipa:
#     line = line.strip()
#     ph = line.split(".")
#     for p in ph:
#         if not p in unq:
#             unq.append(p)
# print(unq)


