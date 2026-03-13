''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created: TODO
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
# Initiate the flask app : TODO
app = Flask("Sentiment Analyzer")


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # TODO
    text_to_analyze = request.args.get("text_to_analyze")
    res = sentiment_analyzer(text_to_analyze)
    if res['label'] is None:
        return "Invalid input ! Please provide a valid text to analyze."
    label = res['label']
    score = res['score']
    return f"The given text has been identified as {label} with a score of {score}."


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    # TODO
    return render_template("index.html")


if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''  # TODO
    app.run(host="0.0.0.0", port=5000)

'''

With the completion of this project, you have:

Created an AI based sentiment analysis application using Watson NLP embedded libraries.

Formatted the output received from the Watson NLP library function to extract relevant information from it.

Packaged the application and made it importable to any python code for usage.

Ran unit tests on the application and checked the validity of its outputs for different inputs.

Deployed the application using Flask framework.

Incorporated error handling capability in the application, such that a response code of 500 receives an appropriate response from the application.

Ran static code analysis on the code files to confirm their adherence to the PEP8 guidelines.

'''
