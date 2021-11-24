"""
Project 3 - TEXT ANALYSIS
TOPIC:
Complete the class 'analysedText' with the following methods -

Constructor -   Takes argument 'text',makes it lower case and removes all punctuation.
                Assume only the following punctuation is used - period (.), exclamation mark (!), comma (,) and question mark (?).
                Store the argument in "fmtText"
freqAll - returns a dictionary of all unique words in the text along with the number of their occurences.
freqOf - returns the frequency of the word passed in argument.
"""
"""
PART 1: TESTING
"""
text2 = 'Chi Chi is my name'
print(text2.split())
word_list = text2.split()
#Count the occurencies of the word
for word in word_list:
    word_list.count(word)
    print(word_list.count(word))
#Create dictionary
dict2 = {}
"""#Turn word list into set to avoid DUPLICATE -> NOT NECCESSARY because DICT support UNIQUE KEY
word_list2 = set(word_list)"""
#Assign value to key : value
for word in word_list:
    dict2[word] = word_list.count(word)

print(dict2)

def freword(word):
    if word in dict2:
        print(dict2[word])
    else:
        print('Not included')
freword('Chi')
"""
PART 2: APPLY
"""
#dict2[text.split()] =
class analysedText(object):
    #Constructor
    def __init__(self, text):
        fmtText = text.replace('.', '').replace('!', '').replace(',', '').replace('?','')
        fmtText = fmtText.lower()
        self.fmtText = fmtText

    #Methods
    def freAll(self): #dictionary
        #Split word in the fmtText
        list_of_word = self.fmtText.split()
        #Create a new dictionary
        word_dict = {}
        #Turn into set to remove duplicate
        for word in list_of_word:
            word_dict[word] = list_of_word.count(word)
        return word_dict
    def freqOf(self, word):
        freqDict = self.freAll()
        if word in freqDict:
            return freqDict[word]
        else:
            return 0
        pass
print(analysedText(text2).freAll())

print(analysedText(text2).freqOf('chi'))






