#!/usr/bin/env python

#  (C) 2013 Jim Buffenbarger
#  All rights reserved.

from pl_evalexception import EvalException

class Node(object):
    pos = 0

    def __str__(self):
        result = ""
        result += str(self.__class__.__name__)
        result += " ( "
        fields = self.__dict__
        for field in fields:
            result += "  "
            result += str(field)
            result += str(": ")
            result += str(fields[field])
        result += str(" ) ")
        return result

    def eval(self, env):
        raise EvalException(self.pos, "cannot eval() node!")

class NodeAssn(Node):
   
    def __init__(self, id, expr):
        super(NodeAssn, self).__init__()
        self.id = id
        self.expr = expr

    

class NodeBlock(Node):

    def __init__(self, stmt, block):
        super(NodeBlock, self).__init__()
        self.stmt = stmt
        self.block = block

class NodeStmt(Node):
    

    def __init__(self, assn):
        super(NodeStmt, self).__init__()
        self.assn = assn


