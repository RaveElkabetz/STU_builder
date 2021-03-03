from SuffixTree import SuffixTree
from graphviz import Digraph

class St(object):
    def __init__(self):
        str_input = "abcabxabcd"
        str_length = len(str_input)
        '''here we will init the gui '''
        self.StRef = SuffixTree(str_length,str_input)
        for indx in range(str_length):
            self.StRef.add_char(str_input[indx])
        i = 0
        for node in self.StRef.nodes:
            i+=1
            if node.node_id in node.childrens.values():
                node.childrens.pop(self.StRef.text[node.start])
        print("hi2")
        self.StRef.print_the_tree()


