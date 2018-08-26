
# coding: utf-8

# In[91]:

#Q2a - This function clean data to remove all punctuations

def clean_data(tw):
    
    tw = tw.lower()
    
    #The following is the list of punctuation that each character from the tweet will loop through to delete them from the punctuation
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    
    #Loop to remove punctuation and then return the tweet without punctuations
    for char in tw:
        if char not in punctuation:
            no_punct = no_punct + char
    tw_no_punct = no_punct
    return tw_no_punct


# In[92]:

#Q2b - This function removes stop words from the stop words file

def remove_stop_words(tw):
    #Convert stop words into array to be used to compare with words in the tweet later in the function
    stop_words = []
    stopwords_file = open("stop_words.txt",'r')
    for line in stopwords_file:
        line = line.strip()
        stop_words.append(line)
        
    #Call clean data function to remove punctuations and split the sentence into each words
    tw = clean_data(tw)
    tw = tw.split()
    
    #Loop to remove the stop words from the tweet
    for i in tw[:]:
        for j in stop_words[:]:
            if i == j:
                tw.remove(i)
            
    #return tweet_words without the stop words   
    return ' '.join(tw)


# In[93]:

# Q2c This function is used to tokenizing unigrams

def tokenize_unigram(tw):
    
    #Call function to remove stop words & also remove punctuation
    tw = remove_stop_words(tw)
    #Convert tweets into array
    tw = tw.split()
    
    return tw


# In[94]:

# Q3 This function creates a bag of words in the form of a Python Dictionary

def bag_of_words(tw):
    
    #Call fucntion to tokenize words after removing stop words & punctuation
    tw = tokenize_unigram(tw)
    
    #This loop will develop a dictionary for bag of words in the tweet
    wordlist = tw
    wordfreq = []
    pairs = {}
    k = 0
    for i in wordlist:
        #The following equation will calculate the frequency of words in a tweet and return the disctionary back
        wordfreq.append(wordlist.count(i)) 
        pairs[i]=pairs.get(i,0)+1
    return pairs


# In[95]:

# Q4 This function determines the political party (liberal, conservative, NDP or Others) for a tweet

def party(tw):
    
    #Call the function to tokenize unigrams after removing stop words & also remove punctuation
    tw = tokenize_unigram(tw)
    
    #The common hashtags and key words were taken from following links which describes the most commonly Twitter hashtags used during the last Canadian Elections: http://politwitter.ca/page/canadian-politics-hash-tags, http://www.cbc.ca/news/politics/economy-debate-google-twitter-searches-1.3233292, http://www.cbc.ca/news/politics/your-federal-election-hashtag-guide-1.1083016. In addition the names and slogans - English and French from the political parties were included in this list. 
    
    #Common Liberal Party words and hashtags
    liberal = ['justin','trudeau','justintrudeau', 'teamtrudeau', 'lpc', 'ptlib', 'cdnleft', 'realchange', 'real change' 'changer ensemble', 'liberal']

    #Common Conservative words and hashtags
    conservative = ['cpc','conservative','tory','pmharper', 'pttory','harper','roft', 'stephen','stephenharper','protect our economy','proven leadership for a safer canada','stronger economy', 'un leadership qui a fait ses preuves pour une économie plus forte']
    
    #Common NDP words and hashtags
    NDP = ['ndp', 'mulcair', 'tommulcair', 'tommulcairplq', 'tom mulcair','ready for change','read4change','readyforchange','ensemble pour le changement']
    
    #Common Other Party words and hashtags
    Others = ['gpc','bq','emayln','ptgreen','ptbloq','votegreen','elizabeth','may','elizabethmay','gilles','duceppe', 'bloc québécois','green party','strength in democracy','a canada that works together','empowering our regions uniting our strengths','des gains pour le quebec','on a tout a gagner','prendre lavenir en main','allier les forces de nos regions','Moen']
   
    #Loop to check if the word matches any liberal keywords
    count_lib = 0
    for i in liberal:
        for j in tw:
            if i in j:
                count_lib = count_lib+1
                
        
    #Loop to check if the word matches any Conservative keywords
    count_cons = 0
    for k in conservative:
        for l in tw:
            if k in l:
                count_cons = count_cons+1
                
    #Loop to check if the word matches any NDP keywords
    count_NDP = 0
    for m in NDP:
        for n in tw:
            if m in n:
                count_NDP = count_NDP+1
              
    #Loop to check if the word matches any Other party keywords
    count_others = 0
    for o in Others:
        for p in tw:
            if o in p:
                count_others = count_others+1
    
    #If else statements to determine which political party the tweet is about. When there are keywords and hashtags in a tweet that belong to multiple parties, then the political party with the largest number of keywords in the tweet is picked and the name of the political party is returned
    if count_lib > count_cons and count_lib > count_NDP and count_lib > count_others:
        return "Liberal"
    elif count_cons > count_lib and count_cons > count_NDP and count_cons > count_others:
        return "Conservative"
    elif count_NDP > count_lib and count_NDP > count_cons and count_NDP > count_others:
        return "NDP"
    else:
        return "Others"


# In[96]:

# Q5 This function calculates the tweet score between 0 to 1 


def tweet_score(tw):
    
    #Call Bag of Words function to get the dictionary of the words in the tweet. This function also calls all the other functions to tokenize words after removing stop words & punctuation
    tw = bag_of_words(tw)
    
    #Get and convert corpus text into a dictionary to compare the words in tweet to words in corpus text
    corpus_words = []
    corpus_dict = {}
    corpus_file = open("corpus.txt",'r').read() 
    for item in corpus_file.split('\n'):
        k,v = item.split('\t')
        corpus_dict[k] = int(v)
    
    #Find total number of bag of words in a tweet
    total_words = sum(tw.itervalues())
    
    #The following loops checks if the words in tweet are in the corpus or not 
    #initializing new dictionaries to store values for tweet scores
    new_score = {}
    new_score_1 = {}

    for i in tw: 
        for k in corpus_dict:
            #If the words in tweet are in the corpus then the value of the new dictionary is updated to a total score which is equal to the value of bag of words dictionary, ie. the number of words in the tweet and multipled by value of the corpus dictionary which gives the sentimental score
            if i == k:
                score1 = tw[i]
                score2 = corpus_dict[k]
                total_score = score1 * score2
                new_score_1[i]= total_score
    
    #If the words in tweet were not in the corpus then the value a tweet score dictionary for that word is added as 0                
    for i in tw:
        for j in new_score_1:
            if i == j:
                next 
            else:
                new_score[i] = 0
    
    #This dictionary for tweet score is updated by merging the values from the above two loops
    new_score.update(new_score_1)
    
    #Add up all the new scores to get a total score for the tweet
    final_scores = sum(new_score.itervalues())
    
    #Calculate a tweet score between the range of 0 and 1. 
    #If total score for tweet calcluated above is less than 0, then the value is divided by the total number of words in the tweet. In order too convert the number between 0 to 1, the number is further divided by 2 and multiplies by -1 to make the number positive. The number is rounded down to 2 decimals
    if final_scores < 0: 
        tweet_score_bigrange = (float(final_scores)/(total_words))
        tweet_score = round(((tweet_score_bigrange)/2),2)
        tweet_score= (-1)*(tweet_score)
        #print tweet_score_bigrange
        return tweet_score
    
    #If total score for tweet calcluated above is greater than 0, then the value is divided by the total number of words in the tweet. In order too convert the number between 0 to 1, the number is further divided by 2 and then added to 0.5. The number is rounded down to 2 decimals
    elif final_scores > 0:
        tweet_score_bigrange = (float(final_scores)/(total_words))
        tweet_score = 0.5 +((tweet_score_bigrange)/2)
        tweet_score= round(tweet_score,2)
        #print tweet_score_bigrange
        return tweet_score
    
    #If total score doesn't fit any other scenarios, then the tweet score is -1
    else:
        tweet_score = -1
        return tweet_score 
    


# In[97]:

# Q5 This function converts the tweet score to a binary value as either 0 or 1

def tweet_classifier(tw):
    
    #Call Tweet_score function to calulate the tweet score between 0 and 1  
    tw = tweet_score(tw)
    
    #The following loops determine that if the tweet score from previous function is between 0 to 0.5 it is negative, between 0.5 and 1 is positive. 0.5 and any other value is classified as -1 and the classified values are returned  
    tweet_score_array = []
    
    tweet_score_array.append(tw)
    for i in tweet_score_array:
        if i >= 0 and i < 0.5:
            tweet_classifier = 0
            return tweet_classifier
        elif i > 0.5 and i <=1:
            tweet_classifier = 1
            return tweet_classifier
        else:
            tweet_classifier = -1
            return tweet_classifier
       

