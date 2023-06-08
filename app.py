from flask import Flask
from textblob import TextBlob

app = Flask(__name__)

def analysisSentiment(blobOfText):
    testimonial = TextBlob(blobOfText)
    return testimonial.sentiment

@app.route("/")
def hello_DAPT():  # put application's code here
    return "<p>Hello DAPT615!</p>"

@app.route("/characterize")
def analyzeText():
    text_1 = "I really enjoy writing code in Python."
    resultSentiment = analysisSentiment(text_1)
    resultString = "<h1>Sentiment Analysis</h1></p><p>\"%s\"</p><p>sentiment polarity is %f and subjectivity is %f</p>" % (text_1, resultSentiment.polarity, resultSentiment.subjectivity)
    print(resultString)
    return resultString


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
