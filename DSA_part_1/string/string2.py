# aux space used
def reverseWordsInSentences(sentence):
    str_arr = sentence.split(' ')
    str_arr.reverse()
    return ' '.join(str_arr)

# withour aux space: reverse single words then reverse the array
def reverseRange(string:str,s,e):
    subString = string[s:e+1]
    word = list(subString.strip())
    n = len(word)
    for i in range(n//2):
        word[i],word[n-i-1] = word[n-i-1],word[i]
    string = string[:s] + ''.join(word) + string[e+1:]
    return string

# time: O(n) space : O(1)
def reverseWordsInSentencesEff(sentence:str):
    n = len(sentence)
    s = 0
    for i in range(n):
        if sentence[i] == ' ':
            # reverse each sentences after space
            sentence = reverseRange(sentence,s,i-1)
            s = i+1
    # reverse the last remaining word
    sentence = reverseRange(sentence,s,n-1)
    # reverse the whole array
    sentence = reverseRange(sentence,0,n-1)
    return sentence

print('reverse words: ',reverseWordsInSentencesEff('buddy how are you man'))
