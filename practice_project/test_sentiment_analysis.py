from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest


class testSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        result1 = sentiment_analyzer("I love this product!")
        result2 = sentiment_analyzer("I hate working with Python")
        result3 = sentiment_analyzer("I am neutral on Python")
        self.assertEqual(result1['label'], "SENT POSITIVE")
        self.assertEqual(result2['label'], "SENT NEGATIVE")
        self.assertEqual(result3['label'], "SENT NEUTRAL")


unittest.main()
