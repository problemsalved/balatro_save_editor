class TokenIterator(object):
    def __init__(self, tokens):
        self.tokens = iter(tokens)

    def until(self, end):
        tokens = [self.__next__()]
        while not tokens[-1] == end:
            tokens.append(self.__next__())
        return tokens

    def __next__(self):
        token = next(self.tokens)
        while token == '':
            token = next(self.tokens)
        return token
