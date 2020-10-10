#!/usr/bin/env python
""" generated source for module Scanner """
#  (C) 2013 Jim Buffenbarger
#  All rights reserved.
from pl_syntaxexception import SyntaxException
from pl_token import Token
import sys



class Scanner(object):
    """ generated source for class Scanner """
    program = ""
    whitespace = {' ','\n','\t'}
    digits = set("0123456789")
    letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    legits = set("_").union(digits).union(letters)
    #symbols = set("@[\]^_`!\"#$%&',)(*+-./:;<=>?")
    operators = {}
    keywords = {}
    token = ""
    lexeme = ""


    def __init__(self, program):
        """ generated source for method __init__ """
        self.program = program
        self.pos = 0
        self.token = None

    def done(self):
        """ generated source for method done """
        return self.pos >= len(self.program)

    def many(self, s):
        """ generated source for method many """
        while not self.done() and self.program[self.pos] in s:
            self.pos += 1

    def past(self, c):
        """ generated source for method past """
        while not self.done() and c != self.program[self.pos]:
            self.pos += 1
        if not self.done() and c == self.program[self.pos]:
            self.pos += 1

    def nextNumber(self):
        """ generated source for method nextNumber """
        ### fill in here
        start_pos =self.pos

        self.many(self.legits)
        
        self.token = Token('num', self.program[start_pos:self.pos])

    def nextKwId(self):
        """ generated source for method nextKwId """
        ### fill in here
        ##tracks self.pos right now
        start_pos = self.pos
        ##move self.pos across all reveleant characters
        self.many(self.legits)
        # pullout varaibles using python slicing 
        # creates a new token
        self.token = Token("id", self.program[start_pos:self.pos])
    

    def nextOp(self):
        """ generated source for method nextOp """
        ### fill in here
        start_pos = self.position

        self.many(self.operators)

        self.token = Token("op", self.program[start_pos:self.pos])

    def next(self):
        """ generated source for method next """
        self.many(self.whitespace)
        if self.done():
            return False
        c = self.program[self.pos]
        
        #if c is a kw or id,then call that function
        if c in self.letters:
            self.nextKwId()
        # if c is a digit do something
        elif c in self.digits:
            self.nextNumber()
        # for all other cases 
        else: 
            self.token = Token(c,c)
           ## self.nextOp
            self.pos +=1
       

        return True

    def match(self, t):
        """ generated source for method match """
        if not t == self.curr():
            raise SyntaxException(self.pos, t, self.curr())
        self.next()

    def curr(self):
        """ generated source for method curr """
        if self.token == None:
            raise SyntaxException(self.pos, Token("ANY"), Token("EMPTY"))
        return self.token

    def position(self):
        """ generated source for method pos """
        return self.pos


if __name__ == '__main__':
    scanner = Scanner(sys.argv[1])
    while scanner.next():
        print(scanner.curr())

 