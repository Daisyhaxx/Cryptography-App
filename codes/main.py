import onetimepad
from tkinter import *

		
root = Tk()
root.title("Python Cryptography App")
root.geometry("700x200")

def encryptMessage():					
	pt = e1.get()

	# * encrypt function
	ct = onetimepad.encrypt(pt, 'random')
	e2.insert(0, ct)



def decryptMessage():					
	ct1 = e3.get()

	# * decrypt function
	pt1 = onetimepad.decrypt(ct1, 'random')
	e4.insert(0, pt1)
	




# * Etkileşim menüleri
label1 = Label(root, text ='Text:')			
label1.grid(row = 10, column = 1)
label2 = Label(root, text ='Encrypted Text: ')
label2.grid(row = 11, column = 1)
l3 = Label(root, text = "Encrypted Text: ")
l3.grid(row = 10, column = 13,)
l4 = Label(root, text = "Text: ")
l4.grid(row = 11, column = 13)





# * bilgi girişleri ve yerleri
e1 = Entry(root)
e1.grid(row = 10, column = 2, pady=20)
e2 = Entry(root)
e2.grid(row = 11, column = 2, pady=20)
e3 = Entry(root)
e3.grid(row = 10, column = 15, pady=20)
e4 = Entry(root)
e4.grid(row = 11, column = 15, pady=20)



# * encrypt button
ent = Button(root, text = "Encrypt", bg ="red", fg ="white", command = encryptMessage)
ent.grid(row = 13, column = 2)




# * decrypt button
b2 = Button(root, text = "Decyrpt", bg ="green", fg ="white", command = decryptMessage)
b2.grid(row = 13, column = 15)


root.mainloop()
