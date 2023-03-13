#!/usr/bin/python3
def multiple_returns(sentence):
    tupl = ()
    if len(sentence) == 0:
        tupl = 0, None
    else:
        tupl = len(sentence), sentence[0]
    return tupl
