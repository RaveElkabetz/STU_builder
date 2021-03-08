from SuffixTree import SuffixTree
from PIL import ImageTk,Image
import tkinter as tk
import os

class STU(object):
    def __init__(self):
        self.new_tree_was_built_flag=0
        self.img_label = None
        self.current_str_proccesed = ""
        self.how_many_trees = 0
        self.file1 = None
        self.str_input = ""
        #-----------------------------------------------------
        self.root = tk.Tk()
        self.root.minsize(1000, 800)


        self.header_label = tk.Label(self.root,text="Ukonnens Suffix Tree Builder:")
        self.header_label.config(font=("Raleway",25))
        self.header_label.pack()

        self.string_entered = tk.Entry(self.root, width=30)
        self.string_entered.pack()
        self.show_the_tree_button = tk.Button(self.root, text= "show the tree", command=self.click_and_show)
        button = tk.Button(self.root, text="Build the tree", command=self.click_me)
        button.pack()
        self.current_str_proccesed_label = tk.Label(self.root, text=self.current_str_proccesed)
        self.current_str_proccesed_label.pack()
        the_string_input = tk.Label(self.root)
        the_string_input.pack()

        self.root.mainloop()
        #---------------------------------------------------------------




    def click_and_show(self):
        if self.new_tree_was_built_flag == 0:
            return
        self.img = ImageTk.PhotoImage(Image.open(self.img_path))
        self.img_label = tk.Label(image=self.img)
        self.img_label.pack()
        self.new_tree_was_built_flag = 0

    def click_me(self):
        self.new_tree_was_built_flag = 1
        if self.img_label != None:
            self.img_label.destroy()
        self.how_many_trees += 1
        file_path = "suffix" + str(self.how_many_trees) + ".dot"
        self.file1 = open(file_path, "a+")
        self.str_input = self.string_entered.get()

        self.string_entered.delete(0, 10000000)
        print(self.str_input)
        self.current_str_proccesed_label.config(text=self.str_input,font=("Raleway",18) )
        send_this_str = self.str_input + "$"
        str_length = len(send_this_str)
        self.StRef = SuffixTree(str_length, send_this_str, self.file1)
        for indx in range(str_length):
            self.StRef.add_char(send_this_str[indx])
        i = 0
        for node in self.StRef.nodes:
            i += 1
            if node.node_id in node.childrens.values():
                node.childrens.pop(self.StRef.text[node.start])

        self.StRef.print_the_tree()
        what_to_run = "dot -Tpng -O suffix" + str(self.how_many_trees) + ".dot"
        os.popen(what_to_run)
        self.file1.close()


        self.img_path = "suffix" + str(self.how_many_trees) + ".dot.png"
        self.show_the_tree_button.pack()








