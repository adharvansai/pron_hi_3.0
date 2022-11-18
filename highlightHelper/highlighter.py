import os

try:
  import eng_to_ipa
except ImportError:
  os.system('python -m pip install eng_to_ipa')

import eng_to_ipa as phen
from collections import defaultdict

# Returns indexes of words that need to be highlighted in a dictionary where key is the ipa
# and value is a list of indices
def highlight_text(text,targets):
    target_dict = defaultdict(list)
    split_converted_text = []
    missing = []
    for txt in text:
        phon_rep = phen.convert(txt)
        if '*' in phon_rep:
            missing.append(txt)
        else:
            split_converted_text.append(phon_rep)
            

    # Writing in file to keep tack of missing words in dict
    f = open("analytics/Missing Words", "a+")
    for word in missing:
        f.writelines(word + '\n')
    f.close()

    for t in targets:
        for ind, word in enumerate(split_converted_text):
            if(t in word):
                target_dict[t].append(ind)

    return target_dict
