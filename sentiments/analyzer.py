import nltk
from nltk.tokenize import TweetTokenizer

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        # TODO
        positive=open(positives,"r")
        negative=open(negatives,"r")
        self.p_words=set()
        self.n_words=set()
        
        for line in positive:
            if line[0]!=';':
                self.p_words.add(line.rstrip("\n"))
        
        for line in negative:
            if line[0]!=';':
                self.n_words.add(line.rstrip("\n"))
    
               

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        # TODO
        tknzr = TweetTokenizer()
        self.s=0
        self.words=tknzr.tokenize(text)
        for word in self.words:
            if word.lower() in self.p_words:
                self.s=self.s+1
            elif word.lower() in self.n_words:
                self.s=self.s-1
        return self.s
