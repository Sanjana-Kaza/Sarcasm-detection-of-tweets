import nltk
from nltk.tokenize import word_tokenize
from textblob import TextBlob
import pandas as pd
from nltk import pos_tag
from collections import Counter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from cleaning import emoji
from cleaning import cleaning
emojis = emoji()

def store_features():
    X_train, Y_train = cleaning()
         
    ### getting the occurence of capitalized letters ###    
    def capital(sent):
              count = sum(1 for elem in sent if elem.isupper())
              return count

    capital_val = []
    for i in range(len(X_train)):
      capital_val.append(capital(X_train[i]))
    
    df = pd.DataFrame(capital_val , columns=['capitalizations'])
    df.to_csv('features.csv', index=False)
    
    ### getting the POS tags ###
    
    def pos(sent):
            NN = 0 
            VB =0
            RB=0
            JJ=0
            UH = 0
            tokens = word_tokenize(sent)
            tags = pos_tag(tokens)
            counts = Counter(tag for word,tag in tags)

            for i in counts.keys():
                if "VB" in i:
                    VB = VB + counts[i]

                if "NN" in i:
                    NN = NN + counts[i]
                if "RB" in i:
                    RB = RB + counts[i]
                if "UH" in i:
                    UH = UH + counts[i]
                if "JJ" in i:
                    JJ = JJ + counts[i]

            return VB, NN, RB, UH, JJ

    POS_VB = []
    POS_NN = []
    POS_RB = []
    POS_UH = []
    POS_JJ = []
    for i in range(len(X_train)):
      POS_VB.append(pos(X_train[i])[0])
      POS_NN.append(pos(X_train[i])[1])
      POS_RB.append(pos(X_train[i])[2])
      POS_UH.append(pos(X_train[i])[3])
      POS_JJ.append(pos(X_train[i])[4])
    
    df = pd.read_csv("features.csv")
    df["POS_VB"] = POS_VB
    df["POS_NN"] = POS_NN
    df["POS_RB"] = POS_RB
    df["POS_UH"] = POS_UH
    df["POS_JJ"] = POS_JJ
    df.to_csv("features.csv", index=False)
        
 
    ### getting the occurences of exclamation points ###
    
    def exclamations(sent):
           count = 0
           for i in range(len(sent)):
               if sent[i] == '!': 
                    count = count + 1
           return count

    excl_val = []
    for i in range(len(X_train)):
      excl_val.append(exclamations(X_train[i]))
    df = pd.read_csv("features.csv")
    df["exclamations"] = excl_val
    df.to_csv("features.csv", index=False)
    
    ### getting the occurences of 2 consecutive question marks ###

    def questionmarks2(sent):
           count = 0
           for i in range(len(sent)):
             if i != len(sent)-1:
                if sent[i] == '?' and sent[i+1] == '?': 
                    count = 1
           return count

    ques_val = []

    for i in range(len(X_train)):
      ques_val.append(questionmarks2(X_train[i]))
    df = pd.read_csv("features.csv")
    df["questionmarks"] = ques_val
    df.to_csv("features.csv", index=False)
  
    ### getting the emoticons scores ###
    
    def emoji(sent):
        emoji_score = 0
        for i in sent:
           if i in emojis:
              emoji_score = emoji_score + emojis[i]
        return emoji_score

    emoji_val = []
    for i in range(len(X_train)):
      emoji_val.append(emoji(X_train[i]))

    df = pd.read_csv("features.csv")
    df["emoji_scores"] = emoji_val
    df.to_csv("features.csv", index=False)
    
    ### getting the contrast in a tweet ###
    
    def contrast(sent):
        tokens = word_tokenize(sent)
        mid = int(len(tokens)/2)
        first_half = tokens[0:mid]
        second_half = tokens[mid:]
        first_half = str(first_half)
        second_half = str(second_half)
        blob1 = TextBlob(first_half)
        blob2 = TextBlob(second_half)
        return abs(blob1.sentiment.polarity - blob2.sentiment.polarity)

    contrast_val = []
    for i in range(len(X_train)):
      contrast_val.append(contrast(X_train[i]))
    
    df = pd.read_csv("features.csv")
    df["contrast"] = contrast_val
    df.to_csv('features.csv', index=False)

    
    ### getting the sentiment of a tweet ###
    
    def sentiment(sent):
            tokens = word_tokenize(sent)
            blob = TextBlob(str(tokens))

            return blob.sentiment.polarity

    sent_val = []
    for i in range(len(X_train)):
      sent_val.append(sentiment(X_train[i]))
    df = pd.read_csv("features.csv")
    df["sentiment"] = sent_val
    df.to_csv("features.csv", index=False)
    
    
    ### getting the setiment and polarity score using VADER module ###
    
    def vader(sent):
        analyzer = SentimentIntensityAnalyzer()
        vs = analyzer.polarity_scores(sent)
        diff = abs(vs['pos'] - vs['neg'])
        return vs['compound'], diff

    
    
    compound = []
    contrast = []
    for i in range(len(X_train)):

       result = vader(X_train[i])
       compound.append(result[0])
       contrast.append(result[1])

    df = pd.read_csv("features.csv")
    df["vader_sentiment"] = compound
    df["vader_contrast"] = contrast
    df.to_csv("features.csv", index=False)
    
    ### getting the subjectivity score ###

    def subj(sent):
        vs = TextBlob(sent).subjectivity
        return vs
   
    
    subj_val = []

    for i in range(len(X_train)):
       subj_val.append(subj(X_train[i]))

    df = pd.read_csv("features.csv")
    df["sujectivity"] = subj_val
    df.to_csv("features.csv", index=False)









