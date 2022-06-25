# dictionary for expanding negation words #

appos = {  
"aren't" : "are not",
"can't" : "cannot",
"couldn't" : "could not",
"didn't" : "did not",
"doesn't" : "does not",
"don't" : "do not",
"hadn't" : "had not",
"hasn't" : "has not",
"haven't" : "have not",
"he'd" : "he would",
"he'll" : "he will",
"he's" : "he is",
"i'd" : "I would",
"i'd" : "I had",
"i'll" : "I will",
"i'm" : "I am",
"isn't" : "is not",
"it's" : "it is",
"it'll":"it will",
"i've" : "I have",
"let's" : "let us",
"mightn't" : "might not",
"mustn't" : "must not",
"shan't" : "shall not",
"she'd" : "she would",
"she'll" : "she will",
"she's" : "she is",
"shouldn't" : "should not",
"that's" : "that is",
"there's" : "there is",
"they'd" : "they would",
"they'll" : "they will",
"they're" : "they are",
"they've" : "they have",
"we'd" : "we would",
"we're" : "we are",
"weren't" : "were not",
"we've" : "we have",
"what'll" : "what will",
"what're" : "what are",
"what's" : "what is",
"what've" : "what have",
"where's" : "where is",
"who'd" : "who would",
"who'll" : "who will",
"who're" : "who are",
"who's" : "who is",
"who've" : "who have",
"won't" : "will not",
"wouldn't" : "would not",
"you'd" : "you would",
"you'll" : "you will",
"you're" : "you are",
"you've" : "you have",
"'re": " are",
"wasn't": "was not",
"we'll":" will",
"didn't": "did not"
}

# preproceesing of data #


def cleaning():
    import pandas as pd
    import re
    #import regex
    import emojis
    import emoji
    data = open('dataset.txt', 'r')
    

    line_train = data.readlines()
    


    train = []
    X_train = []
    Y_train = []
    

    for i in line_train:
        line1 = i.strip().split("\t")
        train.append(line1)
    for k in train:
        del k[0] 
    for b in train:
      X_train.append(b[1]) #tweets
      Y_train.append(b[0]) #sarcasm labels
   


   
    for m in range(len(X_train)):

          X_train[m] = re.sub(r"http\S+", "", X_train[m]) # removes links
          X_train[m] = re.sub(r"#", "", X_train[m]) # replaces "#" with space
          X_train[m] = X_train[m].replace('sarcasm', '') #removes the word sarcasm
          X_train[m] = re.sub(r"[@]\w+", '', X_train[m])  # mentions


          for j in X_train[m].split():  # expanding negation words
                if j in appos:
                    X_train[m] = X_train[m].replace(j, appos[j])

          
    return X_train, Y_train


# emoji scoring dictionary for the features part #

def emoji():
    
    emojis={
	'😀' : 3,
	'😃' : 4,
	'😄' : 3,
	'😁' : 4,
	'😆' : 5,
	'😅' : 2,
	'😂' : 5,
	'😊' : 3,
	'☺️' : 3,
	'😇' : 2,
	'🙂' : 1,
	'🙃' : 1,
	'😉' : 2,
	'😌' : 1,
	'😍' : 4,
	'😘' : 3,
	'😋' : 3,
	'😜' : 2,
	'😝' : 3,
	'😛' : 2,
	'😎' : 2,
	'😒' : -2,
	'😞' : -3,
	'😔' : -2,
	'😟' : -3,
	'😕' : -1,
	'🙁' : -2,
	'☹️' : -3,
	'😣' : -4,
	'😖' : -4,
	'😦' : -1,
	'😧' : -2,
	'😰' : -4,
	'😢' : -4,
	'😥' : -3,
	'✌️' : 2,
	'👍' : 2,
	'👎' : -2,
	'❤️' : 5,
	'💕' : 4,
	'❣️' : 4,
	'💔' : -4,
	'😭' : -5,
	'😓' : -4,
	'😪' : -3,
	'😠' : -3,
	'😡' : -5,
	'😣' : -5,
	'😖' : -4,
	'😫' : -4,
	'😩' : -5,
	}
    return emojis

