import eng_to_ipa as phen

def ipa_helper():
  string = "key win rebate red had about bud bird law cod okay wood boot out why boy man pan be why phone voice thank this written check just yes right finger guest who"
  ipa = phen.convert(string)
  li = ipa.split(" ")
  res = []
  for i in li:
    res += list(i)
  final = list(set(res))
  final.pop(5)
  final.pop(24)
  
  temp = phen.convert("zoo")
  #print(temp)
  final.append(temp[0])
  
  temp = phen.convert("she")
  #print(temp)
  final.append(temp[0])
  
  temp = phen.convert("usual")
  #print(temp)
  final.append(temp[2])
  
  temp = phen.convert("father")
  #print(temp)
  final.append(temp[2])
  
  temp = phen.convert("towel")
  #print(temp)
  final.append(temp[1:3])
  
  temp = phen.convert("why")
  #print(temp)
  final.append(temp[1:])
  
  temp = phen.convert("boy")
  #print(temp)
  final.append(temp[1:])
  
  #print(final)

  return final

dict = {}
ipa_list = ['i', 'r', 'p', 'd', 'l', 'ʧ', 'ɛ', 'h', 'm', 'ə', 'ŋ', 'θ', 'k', 'o', 'ʤ', 'a', 'g', 'æ', 'u', 'f', 'e', 'ð', 'w', 'n', 'b', 'ɔ', 'j', 't', 's', 'ɪ', 'v', 'ʊ', 'z', 'ʃ', 'u', 'ɑ', 'aʊ', 'aɪ', 'ɔɪ']
paragraph = input("Enter the paragraph to process : \n")
converted = phen.convert(paragraph)
print("Choose any 3 symbols from the following list to highlight by using their serial number")
for ind, sym in enumerate(ipa_list):
  print(ind+1,"  :  ", sym)
s1 = input("Symbol 1 : ")
s2 = input("Symbol 2 : ")
s3 = input("Symbol 3 : ")


s1 = ipa_list[int(s1)-1]
s2 = ipa_list[int(s2)-1]
s3 = ipa_list[int(s3)-1]
result = ""

converted = converted.split(" ")
paragraph = paragraph.split(" ")

for ind, c in enumerate(converted):
  if(s1 in c):
    result += "\033[2;31;47m "
    result += paragraph[ind]
    result += " \033[0;0m"
  elif(s2 in c):
    result += "\033[2;33;47m "
    result += paragraph[ind]
    result += " \033[0;0m"
  elif(s2 in c):
    result += "\033[2;34;43m "
    result += paragraph[ind]
    result += " \033[0;0m"
  else:
    result += " " + paragraph[ind]
  
print(result)


  
# a = ord('ɜ')
# print(a)
# print('\033[2;31;43m CHEESY')
