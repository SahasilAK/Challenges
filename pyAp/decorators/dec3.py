import os
import sys


def bold_tag(func):

    def inner(*args, **kwdargs):
        return '<b>'+func(*args, **kwdargs)+'</b>'

    return inner



def say(msg):
    return msg

'''Check the Tail section for input/output'''

if __name__ == "__main__":
