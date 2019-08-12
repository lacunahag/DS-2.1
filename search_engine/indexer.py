class InvertedIndex(dict):
    def __init__(self, words=None):
        super().__init__() # initialize base class as dict
        if words is not None:
            for index, word in enumerate(words):
                # should this be its own function?
                self.add_index(word, index)
    
    def add_index(self, word, index):
        try: self[word].append(index)
        except KeyError: self[word] = [index]

    def get_index(self, word):
        return self[word]