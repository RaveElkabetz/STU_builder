import sys
from Node import Node
oo = (sys.maxsize * 2 + 1) / 2

class SuffixTree(object):
    def __init__(self, _length):
        self.nodes = None
        self.text = None

        self.position = -1
        self.currentNode = 0
        self.need_suffix_link = 0
        self.reminder = 0

        self.active_length = 0
        self.active_edge = 0
        self.nodeRef = Node(0, 0, self)
        self.nodes = [2*_length+2]
        self.text = [_length]
        self.root = self.new_node(-1,-1)
        self.active_node = self.root


    def get_position(self):
        return self.position

    def add_suffix_link(self, _node_int):
        if self.need_suffix_link > 0:
            self.nodes[self.need_suffix_link].set_link(_node_int)
        self.need_suffix_link = _node_int

    def get_active_edge_text(self):
        return self.text[self.active_edge]

    def walk_down(self, _next_int):
        if self.active_length >= self.nodes[_next_int].get_edge_length():
            self.active_edge += self.nodes[_next_int].get_edge_length()
            self.active_length -= self.nodes[_next_int].get_edge_length()
            self.active_node = _next_int
            return True
        return False

    def new_node(self, _start_int, _end_int):
        self.nodes[++self.currentNode] = Node(_start_int,_end_int,self)
        return self.currentNode

    def add_char(self, _charecter):
        self.text[++self.position] = _charecter
        self.need_suffix_link = -1
        self.reminder += 1
        while self.reminder > 0:
            if self.active_length == 0:
                self.active_edge = self.position
            if not self.nodes[self.active_node].next[self.get_active_edge_text()]:
                leaf = self.new_node(self.position, oo)     # leaf is an integer
                self.nodes[self.active_node].next[self.get_active_edge_text()] = leaf
                self.add_suffix_link(self.active_node)      # rule number 2
            else:
                next = self.nodes[self.active_node].next[self.get_active_edge_text()]

