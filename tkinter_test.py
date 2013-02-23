#!/usr/bin/python
#Filename=tkinter_test.py

from Tkinter import *

class msgBox:
  def __init__(self,parent):
		parent.geometry("220x130")
		self.parent=parent
		self.frame1=Frame(parent)
		self.frame1["height"]=200
		self.frame1["width"]=200
		self.frame1.pack()
		#button1:
		self.btn1=Button(self.frame1)
		self.btn1.configure(text="exit!!!")
		self.btn1.bind("<Button-1>",self.act1)
		#button2:
		self.btn2=Button(self.frame1)
		self.btn2.configure(text='show info')
		self.btn2.bind("<Button-1>",self.act2)
		
		
		
		#labels:
		self.msg=Label(self.frame1,text='Welcome to the "msgbox"!!!\nclick exit to exit :D')
		self.msg2=Label(self.frame1)

		
		
		self.msg.pack()
		self.btn2.pack()
		self.msg2.pack()
		self.btn1.pack(side=BOTTOM)
		
	def act1(self,event):
		self.parent.destroy()
		
	def act2(self,event):
		if self.msg2["text"]=='':
			self.msg2["text"]='this simple program is \none of my first "Tkinter" programs.'
			self.btn2["text"]='Hide info'
		else:
			self.msg2["text"]=''
			self.btn2["text"]='show info'
		
#main:
root=Tk()
msgBox1=msgBox(root)
root.mainloop()
