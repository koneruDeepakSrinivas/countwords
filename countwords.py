import re
from tkinter import *

placeholder = "Word count of text: "

def change(evt):
	content = field.get('1.0', 'end').strip()
	content = re.sub(r'\s\s+', ' ', content)
	words = content.split(' ')
	wc = len(words)
	if wc == 1 and len(words[0]) == 0:
		wc = 0

	wordcount.set(placeholder + str(wc))

def select_all(widget):
	field.tag_add('sel', '1.0', 'end')
	return 'break'

root = Tk()
root.title('Word Counter')
frm = Frame(root)

frm.grid()

wordcount = StringVar(root, placeholder + '0')
label = Label(frm, textvariable=wordcount)
field = Text(frm)

field.bind("<KeyRelease>", change)
field.bind('<Control-a>', select_all)

label.grid(column=0, row=1)
field.grid(column=0, row=0)

field.focus_set()

root.mainloop()
