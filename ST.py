from SuffixTree import SuffixTree
from graphviz import Digraph
import tkinter as tk

class St(object):
    def __init__(self):
        self.str_input = ""
        #-----------------------------------------------------
        self.root = tk.Tk()
        self.root.minsize(600, 400)
        self.canvas = tk.Canvas(self.root)

        self.header_label = tk.Label(self.root,text="Ukonnens Suffix Tree Builder:")
        self.header_label.config(font=("Raleway",25))
        self.header_label.pack()

        self.string_entered = tk.Entry(self.root, width=30)
        self.string_entered.pack()

        button = tk.Button(self.root, text="Output the tree", command=self.click_me)
        button.pack()

        the_string_input = tk.Label(self.root)
        the_string_input.pack()
        self.canvas.pack()
        self.root.mainloop()
        #---------------------------------------------------------------



        '''here we will init the gui '''


    def click_me(self):
        file1 = open("st.dot", "a+")
        self.str_input = self.string_entered.get()
        self.string_entered.delete(0, 10000000)
        print(self.str_input)
        str_length = len(self.str_input)
        self.StRef = SuffixTree(str_length, self.str_input, file1)
        for indx in range(str_length):
            self.StRef.add_char(self.str_input[indx])
        i = 0
        for node in self.StRef.nodes:
            i += 1
            if node.node_id in node.childrens.values():
                node.childrens.pop(self.StRef.text[node.start])

        self.StRef.print_the_tree()

        file1.close()



