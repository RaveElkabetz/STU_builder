import sys
oo = (sys.maxsize * 2 + 1) / 2

class Node():
    def __init__(self, _start, _end, _tree_reference):
        self.start = _start
        self.end = _end
        self.link = 0
        self.next = {}
        self.Tree_ref = _tree_reference

    def edge_length(self):
        return min(self.end, self.Tree_ref.get_position()+1) - self.start

    def set_link(self, _node_int):
        self.link = _node_int



