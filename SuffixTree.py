from Node import Node
import sys

infinite = (sys.maxsize * 2 + 1) / 2


class SuffixTree(object):
    def __init__(self, _length, _input_string, _file_ref):
        # self.nodes = None
        # self.text = None
        self.input_string = _input_string
        self.nodes = []
        self.text = []
        self.position = -1
        self.currentNode = -1
        self.need_suffix_link = 0
        self.reminder = 0
        self.file_ref = _file_ref
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

    def get_edge_text_by_node_num(self, _num):
        return self.input_string[self.nodes[_num].start]

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
        self.nodes.append(Node(_start_int, _end_int, self, self.currentNode))
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
        self.reminder += 1  # how many suffixes left to add to the tree
        while self.reminder > 0:
            if self.active_length == 0:
                self.active_edge = self.position
            if self.get_active_edge_text() not in self.nodes[self.active_node].childrens:
                leaf = self.new_node(self.position, infinite)  # leaf is an integer
                self.nodes[self.active_node].childrens[
                    self.get_active_edge_text()] = leaf  # adding a node to the active node(as a child)
                self.add_suffix_link(self.active_node)  # rule number 2
            else:  # in case there is a repeated charecter as an input
                the_next = self.nodes[self.active_node].childrens[self.get_active_edge_text()]
                if self.walk_down(the_next):  # observ 2, 'the_next' node is a leaf
                    continue
                if self.text[self.nodes[the_next].start + self.active_length] == _charecter:
                    self.active_length += 1  # <-- setting where the split will be
                    self.add_suffix_link(self.active_node)  # observ 3
                    break
                '''we got here if we need to split the edge:'''
                split = self.new_node(self.nodes[the_next].start, self.nodes[the_next].start + self.active_length)
                # self.nodes[split].childrens[self.get_active_edge_text()] = split    #consider to add the childs to a node that we save when we find a repitition
                # if self.nodes[split].chidrens[self.get_active_edge_text()] ==
                # ----------------------------------
                self.nodes[self.active_node].childrens.pop(self.get_edge_text_by_node_num(
                    the_next))  # the node that we need to add to the childrens of root is split, and remove: 'the_next' from childs
                self.nodes[self.active_node].childrens.update(
                    {self.text[self.nodes[split].start]: split})  # put [the_next] insted of split : the_next
                # ----------------------------------
                leaf = self.new_node(self.position, infinite)
                self.nodes[split].childrens[_charecter] = leaf
                self.nodes[the_next].start += self.active_length
                self.nodes[split].childrens[self.text[self.nodes[the_next].start]] = the_next
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

    # __________________________________printing methods:______________________________________________

    def edge_string(self, _node):
        # temp_str = (self.text + '.')[:-1]  # generate a copy of 'text' and not only reference
        temp_str = ""
        for char in self.text:
            temp_str += char
        start = self.nodes[_node].start
        end = min(self.position + 1, self.nodes[_node].end)
        return temp_str[start:end]

    def print_the_tree(self):

        self.file_ref.write("digraph {\n")
        self.file_ref.write("\trankdir = LR;\n")
        self.file_ref.write("\tedge [arrowsize=0.6,fontsize=18]\n")
        self.file_ref.write("\tnode0 [label=\"\",style=filled,fillcolor=red,shape=circle,width=.1,height=.1];\n")
        self.file_ref.write("//------leaves------\n")
        self.print_the_outter_nodes(self.root)
        self.file_ref.write("//------internal nodes------\n")
        self.print_internal_nodes(self.root)
        self.file_ref.write("//------edges------\n")
        self.print_the_edges(self.root)
        self.file_ref.write("//------suffix links------\n")
        self.print_links(self.root)
        self.file_ref.write("}")

    def print_the_outter_nodes(self, _root):
        for node in self.nodes:
            if len(node.childrens) == 0:
                self.file_ref.write("\tnode" + str(node.node_id) + " [label=\"\",shape=point]\n")

    def print_internal_nodes(self, _y):
        for node in self.nodes:
            if len(node.childrens) > 0:
                self.file_ref.write("\tnode" + str(
                    node.node_id) + " [label=\"\",style=filled,fillcolor=blue,shape=circle,width=.07,height=.07]\n")

    def print_the_edges(self, _n):
        for node in self.nodes:
            if len(node.childrens) > 0:
                for child in node.childrens.values():
                    self.file_ref.write("\tnode" + str(node.node_id) + " -> node" + str(child) + " [label=\"" +
                                        str(self.edge_string(child)) + "\",weight=25]\n")

    def print_links(self, _l):
        if self.nodes[_l].link > 0:
            self.file_ref.write(
                "\tnode" + str(_l) + " -> node" + str(self.nodes[_l].link) + " [label=\"\",weight=1,style=dotted]\n")
        for child in self.nodes[_l].childrens.values():
            if child == self.nodes[_l].node_id:
                continue
            self.print_links(child)
