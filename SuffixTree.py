import sys
from Node import Node

oo = (sys.maxsize * 2 + 1) / 2


class SuffixTree(object):
    def __init__(self, _length):
        # self.nodes = None
        # self.text = None
        self.nodes = []
        self.text = []
        self.position = -1
        self.currentNode = -1
        self.need_suffix_link = 0
        self.reminder = 0

        self.active_length = 0
        self.active_edge = 0
        # self.nodeRef = Node(0, 0, self)

        self.root = self.new_node(-1, -1)
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
        if self.active_length >= self.nodes[_next_int].edge_length():
            self.active_edge += self.nodes[_next_int].edge_length()
            self.active_length -= self.nodes[_next_int].edge_length()
            self.active_node = _next_int
            return True
        return False

    def new_node(self, _start_int, _end_int):
        # if self.currentNode == -1:
        #    self.currentNode += 1
        # temp_current_node = self.currentNode
        self.currentNode += 1
        self.nodes.append(Node(_start_int, _end_int, self))
        # if self.currentNode >= 0:

        return self.currentNode

    def add_char(self, _charecter):
        flag_is_zero = 0
        if self.position == -1:
            self.position += 1
            flag_is_zero = 1
        if flag_is_zero == 0:
            self.position += 1

        self.text.insert(self.position, _charecter)

        self.need_suffix_link = -1
        self.reminder += 1
        while self.reminder > 0:
            if self.active_length == 0:
                self.active_edge = self.position
            if self.get_active_edge_text() not in self.nodes[self.active_node].next:
                leaf = self.new_node(self.position, oo)  # leaf is an integer
                self.nodes[self.active_node].next[self.get_active_edge_text()] = leaf
                self.add_suffix_link(self.active_node)  # rule number 2
            else:
                the_next = self.nodes[self.active_node].next[self.get_active_edge_text()]
                if self.walk_down(the_next):  # observ 2
                    continue
                if self.text[self.nodes[the_next].start + self.active_length] == _charecter:
                    self.active_length += 1
                    self.add_suffix_link(self.active_node)  # observ 3
                    break
                split = self.new_node(self.nodes[the_next].start, self.nodes[the_next].start + self.active_length)
                self.nodes[split].next[self.get_active_edge_text()] = split
                leaf = self.new_node(self.position, oo)
                self.nodes[split].next[_charecter] = leaf
                self.nodes[the_next].start += self.active_length
                self.nodes[split].next[self.text[self.nodes[the_next].start]] = the_next
                self.add_suffix_link(split)  # rule number 2

            self.reminder -= 1

            if self.active_node == self.root and self.active_length > 0:  # this is rule number 1
                self.active_length -= 1
                self.active_edge = self.position - self.reminder + 1
            else:
                if self.nodes[self.active_node].link > 0:
                    self.active_node = self.nodes[self.active_node].link
                else:
                    self.active_node = self.root

    def edge_string(self, _node):
        temp_str = (self.text + '.')[:-1]  # generate a copy of 'text' and not only reference
        start = self.nodes[_node].start
        end = min(self.position + 1,self.nodes[_node].end)
        return temp_str[start:end]

    def print_the_tree(self):
        '''
        print("digraph {");
        print("\trankdir = LR;");
        print("\tedge [arrowsize=0.4,fontsize=10]");
        print("\tnode1 [label=\"\",style=filled,fillcolor=lightgrey,shape=circle,width=.1,height=.1];");
        print("//------leaves------");
        printLeaves(root);
        print("//------internal nodes------");
        printInternalNodes(root);
        print("//------edges------");
        printEdges(root);
        print("//------suffix links------");
        printSLinks(root);
        print("}");'''
        pass

    def print_the_outter_edges(self,_x):
        if len(self.nodes[_x].next) == 0:
            print("\tnode"+x+" [label=\"\",shape=point]")
        else:
            for child in self.nodes[_x].next.values():
                self.print_the_outter_edges(child)
