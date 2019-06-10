'''
Created on Mar 21, 2016

@author: Bill Begueradj
'''
import tkinter
from tkinter import ttk


class Gui(tkinter.Frame):
    '''
    classdocs
    '''  
    def __init__(self, parent):
        '''
        Constructor
        '''
        tkinter.Frame.__init__(self, parent)
        self.parent=parent
        self.setInterface()

    def setInterface(self):
        """Draw a user interface allowing the user to type
        items and insert them into the treeview
        """
        self.parent.title("구글 플레이 스토어 카테고리별 랭킹")       
        # self.parent.grid_rowconfigure(0,weight=1)
        # self.parent.grid_columnconfigure(0,weight=1)
        self.parent.config(background="lavender")

        #Set combobox
        value=['HEALTH_AND_FITNESS','PRODUCTIVITY','WEATHER','VIDEO_PLAYERS','TRAVEL_AND_LOCAL','BUSINESS','PHOTOGRAPHY','DATING','FOOD_AND_DRINK','HOUSE_AND_HOME','EVENTS','PARENTING','TOOLS','MAPS_AND_NAVIGATION','COMMUNICATION','SPORTS','ART_AND_DESIGN','AUTO_AND_VEHICLES','LIBRARIES_AND_DEMO','SHOPPING','MEDICAL','SOCIAL','FINANCE','BEAUTY','COMICS','EDUCATION','NEWS_AND_MAGAZINES','PERSONALIZATION','LIFESTYLE','FAMILY','ENTERTAINMENT','GAME','BOOKS_AND_REFERENCE']
        self.combo = ttk.Combobox(self.parent, width=20,  values=value)
        # self.combo.grid(row=0, column=1)
        self.combo.pack()

        self.action=ttk.Button(self.parent, text="검색")
        self.action2=ttk.Button(self.parent, text="초기화")

        # Define the different GUI widgets
        # self.dose_label = tkinter.Label(self.parent, text = "Dose:")
        # self.dose_entry = tkinter.Entry(self.parent)
        # self.dose_label.grid(row = 0, column = 0, sticky = tkinter.W)
        # self.dose_entry.grid(row = 0, column = 1)

        # self.modified_label = tkinter.Label(self.parent, text = "Date Modified:")
        # self.modified_entry = tkinter.Entry(self.parent)
        # self.modified_label.grid(row = 1, column = 0, sticky = tkinter.W)
        # self.modified_entry.grid(row = 1, column = 1)

        self.submit_button = tkinter.Button(self.parent, text = "검색")
        # self.submit_button.grid(row = 0, column = 2, sticky='w')
        self.submit_button.pack()

        self.exit_button = tkinter.Button(self.parent, text = "초기화")
        # self.exit_button.grid(row = 0, column = 3, sticky='w')
        self.exit_button.pack()

        #         self.action=ttk.Button(self.win, text="검색", command=self.clickMe)
#         self.action2=ttk.Button(self.win, text="초기화", command=self.removeMe)

        # Set the treeview
        self.tree = ttk.Treeview( self.parent, columns=('App', 'Category','Rating', 'Installs'))
        self.tree.heading('#0', text='App')
        self.tree.heading('#1', text='Category')
        self.tree.heading('#2', text='Rating')
        self.tree.heading('#3', text='Installs')
        self.tree.heading('#4', text='Score')
 
        # self.tree.column('#1', stretch=tkinter.YES)
        # self.tree.column('#2', stretch=tkinter.YES)
        # self.tree.column('#0', stretch=tkinter.YES)
        # self.tree.grid(row=1, column=2)
        self.tree.pack()

        # self.treeview = self.tree
        # Initialize the counter
        self.i = 0

    def clickMe(self):
        pass
        # self.removeMe()
        # self.label=tkinter.Label(self.window,text=category_dict[self.combo.get()].head())
        # self.label.pack()

    def removeMe(self):
        pass
        # self.label.forget()
    # def insert_data(self):
    #     """
    #     Insertion method.
    #     """
    #     self.treeview.insert('', 'end', text="Item_"+str(self.i), values=(self.dose_entry.get()+" mg", self.modified_entry.get()))
    #     # Increment counter
    #     self.i = self.i + 1         

def main():
    root=tkinter.Tk()
    d=Gui(root)
    root.mainloop()

if __name__=="__main__":
    main()
