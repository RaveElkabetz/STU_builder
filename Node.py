import sys

class Node():
    def __init__(self, _start, _end, _tree_reference,_node_id):
        self.start = _start
        self.end = _end
        self.link = 0
        self.childrens = {}
        self.Tree_ref = _tree_reference
        self.node_id = _node_id

    def edge_length(self):
        return min(self.end, self.Tree_ref.get_position()+1) - self.start

    def set_link(self, _node_int):
        self.link = _node_int
