#Problem 1:
f = open("data2.txt")
text = f.read()
temp = text.split('\n')
for i in range(len(temp)):
    for j in range(len(temp[i]) - 3):
        if temp[i][j:j+3].lower() == 'lol':
            print (temp[i])
#Problem 2:
def dict_to_str(d):
    keys = list(d.keys())
    values = list(d.values())
    temp_1 = ''
    for k in range(len(keys)):
        temp_1 += str(keys[k])
        temp_1 += ', '
        temp_1 += str(values[k])
        if k < len(keys) - 1:
            temp_1 += r'\n'
    return temp_1
#Problem 3:
def dict_to_str_sorted(d):
    keys = list(d.keys())
    keys = sorted(keys)
    values = list(d.values())
    temp_1 = ''
    for k in range(len(keys)):
        temp_1 += str(keys[k])
        temp_1 += ', '
        temp_1 += str(values[k])
        if k < len(keys) - 1:
            temp_1 += r'\n'
    return temp_1
#Problem 4a:
dict_file = open("cmudict-0.7b.txt")
new_text = dict_file.read()
temp_2 = new_text.split('\n')
temp_3 = {}
for a in range(len(temp_2)):
    temp_4 = temp_2[a].split(' ')
    temp_5 = temp_4[1:len(temp_4)]
    temp_3[temp_4[0]] = temp_5
#Problem 4b:
new_dict_file = open("cmudict-0.7b.phones.txt")
new_new_text = new_dict_file.read()
temp_6 = new_new_text.split('\n')
del temp_6[len(temp_6) - 1]
temp_8 = {}
for b in range(len(temp_6)):
    temp_7 = temp_6[b].split('\t')
    temp_8[temp_7[0]] = temp_7[1]
#Problem 4c:
def num_vowels(word, dict1, dict2):
    word = word.upper()
    phones_list = dict1.get(word)
    vowels_count = 0
    if phones_list != None:
        for c in range(len(phones_list)):
            temp_9 = phones_list[c]     
            phones_letters = ''
            for d in range(len(temp_9)):
                if temp_9[d].isalpha() == True: 
                    phones_letters += temp_9[d] 
            if dict2.get(phones_letters) == 'vowel':
                vowels_count += 1
    return vowels_count
#Problem 4d:
#should this just be the same as 4c?
#Problem 5:
def fkrg(text):
    #for now assumes that the text is inputted in one line 
    text_list = text.split(' ')
    word_list = []
    for e in range(len(text_list)):
        word = ''
        for f in range(len(text_list[e])):
            if text_list[e][f].isalpha() == True:
                word += text_list[e][f]
        word_list.append(word)
    sentences = text.split('.')
    total_words = len(text_list)
    total_sentences = len(sentences)
    total_syllables = 0
    for g in range(len(word_list)):
        total_syllables += num_vowels(word_list[g], temp_3, temp_8)
    return ((0.39)*(total_words/total_sentences) + (11.8)*(total_syllables/total_words) - 15.59)
print (fkrg("This is a rather sophisticated text that I shall use to test this function."))
print (fkrg("hi this is just a random text"))