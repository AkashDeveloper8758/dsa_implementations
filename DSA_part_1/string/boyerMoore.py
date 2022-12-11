def badCharHeuristic(string, size):
    NO_OF_CHARS = 256
    # Initialize all occurrence as -1
    badChar = [-1]*NO_OF_CHARS
 
    # Fill the actual value of last occurrence
    for i in range(size):
        badChar[ord(string[i])] = i
 
    # return initialized list
    return badChar

def boyerMoorePatternSearching(txt,pat):
    m = len(pat)
    n = len(txt)
    badChar = badCharHeuristic(pat,m)
    # shift (s)
    s = 0
    while s <= n-m+1:
        # start searhing from the last
        j =m-1
        while j>=0 and pat[j]==txt[j+s]:
            j-=1
        if j <0:
            print('pattern occured at {}'.format(s))
            '''   
                Shift the pattern so that the next character in text
                      aligns with the last occurrence of it in pattern.
                The condition s+m < n is necessary for the case when
                   pattern occurs at the end of text
               '''
            # increment by s+m or by 1
            s+= m-badChar[ord(txt[s+m])]  if s+m <n else 1

        else:
            s+= max(1,j- badChar[ord(txt[s+j])])

boyerMoorePatternSearching('akashmauryaisgoodmanoftheuniverse','isgood')
        
