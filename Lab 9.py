#Problem 1a:
def count_num_words(text_name):    #text_name should be a string like 'random.txt'
    word_list = open(text_name, encoding="latin-1").read().split()
    word_counts = {}
    for i in range(len(word_list)):
        count = word_list.count(word_list[i])
        if word_list[i] not in list(word_counts.keys()):
            word_counts[word_list[i]] = count
    return word_counts
#print (count_num_words('random.txt'))
#Problem 1b:
import statistics
def top10(L):
    ten_largest = []
    for j in range(10):
        largest = max(L)
        ten_largest.append(largest)
        k = len(L) - 1
        while k >= 0:
            if L[k] == largest:
                del L[k]
            k -= 1
    return ten_largest
#temp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
#print (top10(temp))
#Problem 1c:
def top10_freq(freq):
    #sort_dict = sorted(freq, key=freq.get)
    #return sort_dict[len(sort_dict)-10:len(sort_dict)]
    return sorted(freq, key=freq.get)[len(sorted(freq, key=freq.get))-10:len(sorted(freq, key=freq.get))]
'''
word_counts = count_num_words('random book.txt')
print (top10_freq(word_counts))                      
why is this too slow to finish running?? works on smaller files tho
'''
#Problem 2:
#open html file in vscode and also the browser
#Problem 3:
import urllib.request
def num_results(terms):       #term means the search term, which should be a string, assumes one word without spaces  #change it so that u can add more words
    term_list = terms.split(' ')
    new_str = ''
    for e in range(len(term_list)):
        new_str = new_str + term_list[e]
        if e < len(term_list) - 1:
            new_str = new_str + '+'
    f = urllib.request.urlopen('https://ca.search.yahoo.com/search?p=' + new_str + '&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8')
    page = f.read().decode("utf-8")
    f.close()
    all_instances = []
    for a in range(len(page) - 8):
        if page[a:a+7] == 'results' and page[a-1] != '#':
            all_instances.append(page[a-14:a])
    for b in range(len(all_instances)):
        count = 0
        for c in range(len(all_instances[b])):
            if all_instances[b][c].isdigit() == True:
                count += 1
        if count/len(all_instances[b]) > 0.3: 
            num_str = ''
            for d in range(len(all_instances[b])):
                if all_instances[b][d].isdigit() == True:
                    num_str = num_str + all_instances[b][d]
            return int(num_str) 
#print (num_results('cristiano ronaldo')) 
def choose_variant(L): #L should be a list containing 2 strings, like ["five-year anniversary", "fifth anniversary"]
    if num_results(L[0]) > num_results(L[1]):
        return L[0]
    return L[1]
print (choose_variant(["top ranked school uoft", "top ranked school waterloo"]))