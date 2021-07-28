import tkinter
import os	
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notepad:

	root = Tk()


	Width = 300
	Height = 300
	TextArea = Text(root)
	MenuBar = Menu(root)
	FileMenu = Menu(MenuBar, tearoff=0)
	EditMenu = Menu(MenuBar, tearoff=0)
	
	
	ScrollBar = Scrollbar(TextArea)	
	file = None

	def __init__(self,**kwargs):

		
		try:
				self.root.wm_iconbitmap("Notepad.ico")
		except:
				pass


		try:
			self.Width = kwargs['width']
		except KeyError:
			pass

		try:
			self.Height = kwargs['height']
		except KeyError:
			pass

		self.root.title("Untitled ")

		screenWidth = self.root.winfo_screenwidth()
		screenHeight = self.root.winfo_screenheight()
	

		left = (screenWidth / 2) - (self.Width / 2)
		
		top = (screenHeight / 2) - (self.Height /2)
		
		self.root.geometry('%dx%d+%d+%d' % (self.Width,
											self.Height,
											left, top))

		self.root.grid_rowconfigure(0, weight=1)
		self.root.grid_columnconfigure(0, weight=1)

		self.TextArea.grid(sticky = N + E + S + W)
		
		self.FileMenu.add_command(label="New",
										command=self.newFile)	
		
		self.FileMenu.add_command(label="Open",
										command=self.openFile)
		
		self.FileMenu.add_command(label="Save",
										command=self.saveFile)	
	
		self.FileMenu.add_separator()										
		self.FileMenu.add_command(label="Exit",
										command=self.quitApplication)
		self.MenuBar.add_cascade(label="File",
									menu=self.FileMenu)	
		
		self.EditMenu.add_command(label="Cut",
										command=self.cut)			
	
		self.EditMenu.add_command(label="Copy",
										command=self.copy)		
		
		self.EditMenu.add_command(label="Paste",
										command=self.paste)		
		
		self.MenuBar.add_cascade(label="Edit",
									menu=self.EditMenu)	

		self.root.config(menu=self.MenuBar)

		self.ScrollBar.pack(side=RIGHT,fill=Y)					
			
		self.ScrollBar.config(command=self.TextArea.yview)	
		self.TextArea.config(yscrollcommand=self.ScrollBar.set)
	
		
	def quitApplication(self):
		self.root.destroy()
		

	def openFile(self):
		
		self.file = askopenfilename(defaultextension=".txt",
                                  filetypes=[("All Files","*.*"),
                                      ("Text Documents","*.txt")])

		if self.file == "":
		
			self.file = None
		else:
			
			self.root.title(os.path.basename(self.file) + " - Notepad")
			self.TextArea.delete(1.0,END)

			file = open(self.file,"r")

			self.TextArea.insert(1.0,file.read())

			file.close()

		
	def newFile(self):
		self.root.title("Untitled")
		self.file = None
		self.TextArea.delete(1.0,END)

	def saveFile(self):

		if self.file == None:
			self.file = asksaveasfilename(initialfile='Untitled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files","*.*"),
                                            ("Text Documents","*.txt")])

			if self.file == "":
				self.file = None
			else:
				
				file = open(self.file,"w")
				file.write(self.TextArea.get(1.0,END))
				file.close()
				self.root.title(os.path.basename(self.file) + " - Notepad")
				
			
		else:
			file = open(self.file,"w")
			file.write(self.TextArea.get(1.0,END))
			file.close()

	def cut(self):
		self.TextArea.event_generate("<<Cut>>")

	def copy(self):
		self.TextArea.event_generate("<<Copy>>")

	def paste(self):
		self.TextArea.event_generate("<<Paste>>")

	def run(self):

		self.root.mainloop()



notepad = Notepad(width=600,height=400)
notepad.run()
