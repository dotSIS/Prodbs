from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_scores(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    overallSentiment = ""
    if sentiment_dict['compound'] >= 0.05 :
        overallSentiment =("Positive")
 
    elif sentiment_dict['compound'] <= - 0.05 :
        overallSentiment = ("Negative")
 
    else :
        overallSentiment =("Neutral")
    return {
        'negative':sentiment_dict['neg']*100,
        'neutral':sentiment_dict['neu']*100,
        'positive':sentiment_dict['pos']*100,
        'overall':overallSentiment,
    }