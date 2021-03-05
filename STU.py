from SuffixTree import SuffixTree
from PIL import ImageTk,Image
import tkinter as tk
import subprocess
import os

class STU(object):
    def __init__(self):
        self.current_str_proccesed = ""
        self.how_many_trees = 0
        self.file1 = None
        self.str_input = ""
        #-----------------------------------------------------
        self.root = tk.Tk()
        self.root.minsize(1000, 800)
        self.canvas = tk.Canvas(self.root, width=500, height=300)

        self.header_label = tk.Label(self.root,text="Ukonnens Suffix Tree Builder:")
        self.header_label.config(font=("Raleway",25))
        self.header_label.pack()

        self.string_entered = tk.Entry(self.root, width=30)
        self.string_entered.pack()

        button = tk.Button(self.root, text="Build the tree", command=self.click_me)
        button.pack()
        self.current_str_proccesed_label = tk.Label(self.root, text=self.current_str_proccesed)
        self.current_str_proccesed_label.pack()
        the_string_input = tk.Label(self.root)
        the_string_input.pack()

        self.root.mainloop()
        #---------------------------------------------------------------







    def click_me(self):
        self.how_many_trees += 1
        file_path = "suffix" + str(self.how_many_trees) + ".dot"
        self.file1 = open(file_path, "a+")
        self.str_input = self.string_entered.get()

        self.string_entered.delete(0, 10000000)
        print(self.str_input)
        self.current_str_proccesed_label.config(text=self.str_input,font=("Raleway",18) )
        str_length = len(self.str_input)
        send_this_str =self.str_input + "$"
        self.StRef = SuffixTree(str_length, send_this_str, self.file1)
        for indx in range(str_length):
            self.StRef.add_char(self.str_input[indx])
        i = 0
        for node in self.StRef.nodes:
            i += 1
            if node.node_id in node.childrens.values():
                node.childrens.pop(self.StRef.text[node.start])

        self.StRef.print_the_tree()
        what_to_run = "dot -Tpng -O suffix" + str(self.how_many_trees) + ".dot"
        os.popen(what_to_run)
        self.file1.close()

        self.canvas.pack()

        imp_path = "suffix" + str(self.how_many_trees) + ".dot.png"
        img = ImageTk.PhotoImage(Image.open("suffix1.dot.2.png"))
        my_label = tk.Label(image=img)
        my_label.pack()








