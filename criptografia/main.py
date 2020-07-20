from tkinter import *
from criptografia import *
from time import sleep

COR = "#40E0D0"#"#7FFFD4"# "#008B8B"#"#ADD8E6"#"#696969"

class Screen(object):
    def __init__(self):
        self.i = Tk()
        self.conf_screen()
        self.conf_widgets()
    

    # This method will configure the widgets 
    def conf_widgets(self):
        frame_title = Frame(self.i, pady=0)
        frame_entry = Frame(self.i, bg=COR)
        frame_button = Frame(self.i, pady=5, bg=COR)
        frame_listbox = Frame(self.i)
        title = Label(frame_title, text="BerCrypt", fg="#111111", font=("helvetica", 20, "bold"), bg=COR)
        title.pack()
        frame_title.pack()
        frame_entry.pack()
        #0xac0x30x660x610xfe0x400xb10x6f0x3a0x180xb10x8f0xfd0x430xc40x8b0x980xf10x790x730x2d0xa00x70x8c0xac0x3b0x490xad0x650x370x400x70xaa0xe40x8a0x2f0xd60x710xda0xa90x8c0x9e0xbf0xc10xc00xd00x680x4d0x32
        frame_button.pack()
        label_base = Label(frame_entry, text="Chave:", font=("arial", 15, "bold"), bg=COR)
        self.base = Entry(frame_entry, width=50, font=("helvetica", 15, "bold"))
        label_text = Label(frame_entry, text="Texto:", font=("arial", 15, "bold"), width=10, pady=10, bg=COR)
        self.text = Text(frame_entry, width=50, font=("helvetica", 15, "bold"), height=10)
        encrypt = Button(frame_button, text="Encrypt", font=("helvetica", 15, "bold"), command=self.encryptor)
        decrypt = Button(frame_button, text="Decrypt", font=("arial", 15, "bold"), command=self.decryptor)
        label_base.grid(row=0, column=0)
        self.base.grid(row=0, column=1)
        label_text.grid(row=1, column=0)
        self.text.grid(row=1, column=1, pady=10)
        encrypt.pack(side="left", padx=40)
        decrypt.pack()
        frame_listbox.pack()
        #self.result = Label(self.i, font=("helvetica", 10, "bold"), text="")
        #self.result.pack()
        scroll = Scrollbar(frame_listbox)
        scroll.pack(side="right", fill="y")
        self.result = Listbox(frame_listbox, width=100, yscrollcommand=scroll.set, font=("helvetica", 12, "bold"))
        #for cont in range(100):
            #self.result.insert(END, f"{cont}Sei lá apenas teste")
        self.result.pack()
        self.result["state"] = "disable"
        self.button_copy = Button(self.i, text="Copiar para o campo TEXTO",font=("helvetica", ), command=self.copy)
        self.button_copy.pack(pady=10)
        self.erro = Label(self.i, fg="red", text="ERRO, PARA DECIFRAR UM TEXTO ELE DEVE ESTAR EM HEXADECIMAL", font=("helvetica", 13, "bold"))


    #This method will configure the screen
    def conf_screen(self):
        self.i["bg"] = COR
        self.i.title("Bercrypt")
        self.i.geometry("800x690")
        self.i.resizable(False, False)
    

    def encryptor(self):
        self.result["state"] = "normal"
        self.result.delete(0, END)
        #self.result.insert(END, "a"*80)
        #self.result.delete(self.result.size()-1, END)
        valid = self.checks_entrys()
        try:
            valid[1] = valid[1][:len(valid[1])-1]
        except TypeError:
            valid = False
        if valid:
            self.result["state"] = "normal"
            for buffer in self.count_char(Cript(valid[0], valid[1]).encrypt()):
                self.result.insert(END, buffer)
            self.result["state"] = "disable"
            saida = Cript(valid[0], valid[1])
            saida.encrypt()
            saida.save()#Os bunitim tão tudo virando viadim, os novinhos tão sensacional sarrando ovo com ovo achando legal , a man sei nem o que escreve mais kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk

    def count_char(self, text):
        self.erro.pack_forget()
        replace = []
        pos = 0
        temp = ""
        for l in text:
            temp = temp + l
            pos += 1
            if pos % 80 == 0:
                replace.append(temp)
                temp = ""
            if len(text) == pos:
                replace.append(temp)
        return replace



    def decryptor(self):
        self.erro.pack_forget()
        valid = self.checks_entrys()
        try:
            valid[1] = valid[1][:len(valid[1])-1]
        except TypeError:
            valid = False
        if valid:
            try:
                cont = 0
                for buffer in self.count_char(Cript(valid[0], valid[1]).decrypt()):
                    if cont == 0:
                        self.result["state"] = "normal"
                        self.result.delete(0, END)
                        cont += 1
                    self.result.insert(END, buffer)
                self.result["state"] = "disable"
            except ValueError:
                self.erro.pack()


    def checks_entrys(self):
        if len(self.base.get()) == 0:
            return False
        if len(self.text.get(1.0, END)) == 0:
            return False
        return [self.base.get(), self.text.get(0.0, END)]

    
    def copy(self):
        result_buffers = self.result.get(0, END)
        self.text.delete(1.0, END)
        for buffer in result_buffers:
            self.text.insert(END, buffer) 


    def start(self):
        self.i.mainloop()


if __name__ == "__main__":
    Screen().start()