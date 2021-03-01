from SuffixTree import SuffixTree
from graphviz import Digraph

class St(object):
    def __init__(self):
        str_input = "ravvve"
        str_length = len(str_input)
        '''here we will init the gui '''
        self.StRef = SuffixTree(str_length)
        for indx in range(str_length):
            self.StRef.add_char(str_input[indx])
        #self.StRef.print_the_tree()
        print("hi2")

