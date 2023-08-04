from tkinter import *
from tkinter import ttk

# Define constantes para as cores e fontes
BG_COLOR = "#aaa"
HL_COLOR = "#000"
BT_COLOR = {"limpar": "yellow", "buscar": "blue", "novo": "green", "alterar": "yellow", "apagar": "red"}
BT_FONT = ('verdade', 8, 'bold')

# Define uma classe para a aplicação
class Application():
    def __init__(self):
        # Cria a janela principal
        self.janela = Tk()
        self.janela.title("INSTABOT")
        self.janela.configure(background=BG_COLOR)
        self.janela.geometry("500x500")
        self.janela.resizable(False, False)
        
        # Cria os frames e os widgets
        self.tela()
        self.frames()
        self.widgats_frame1()
        self.lista_frame2()
        
        # Inicia o loop principal da janela
        self.janela.mainloop()
    
    def tela(self):
        # Define os títulos dos frames
        self.frame1_title = Label(self.janela, text="Dados do Cliente", bg=BG_COLOR)
        self.frame1_title.place(relx=0.02, rely=0.01)
        
        self.frame2_title = Label(self.janela, text="Lista de Clientes", bg=BG_COLOR)
        self.frame2_title.place(relx=0.02, rely=0.5)

    def frames(self):
        # Cria os frames para os dados e a lista
        self.frames_1 = Frame(self.janela, bd=4, bg=BG_COLOR, 
                              highlightbackground=HL_COLOR, highlightthickness=2)
        self.frames_1.place(relx= 0.02,rely= 0.05, relwidth= 0.96,relheight= 0.4)

        self.frames_2 = Frame(self.janela, bd=4, bg=BG_COLOR, 
                              highlightbackground=HL_COLOR, highlightthickness=2)
        self.frames_2.place(relx= 0.02,rely= 0.54, relwidth= 0.96,relheight= 0.4)
    
    def widgats_frame1(self):
        # Cria os botões para as operações
        self.bt_limpar = Button(self.frames_1, text="Limpar", bd=3, bg=BT_COLOR["limpar"], 
                        font=BT_FONT, command=self.limpar)

        self.bt_limpar.place(relx= 0.2,rely= 0.1, relwidth= 0.13,relheight= 0.15)

        self.bt_buscar = Button(self.frames_1, text="Buscar", bd=3, bg=BT_COLOR["buscar"], fg="#fff", 
                                font=BT_FONT)
        self.bt_buscar.place(relx= 0.35,rely= 0.1, relwidth= 0.13,relheight= 0.15)

        self.bt_novo = Button(self.frames_1, text="Novo", bd=3, bg=BT_COLOR["novo"], fg="#fff", 
                      font=BT_FONT, command=self.novo)
        self.bt_novo.place(relx= 0.55,rely= 0.1, relwidth= 0.13,relheight= 0.15)

        self.bt_alterar = Button(self.frames_1, text="Alterar", bd=3, bg=BT_COLOR["alterar"], 
                                 font=BT_FONT)
        self.bt_alterar.place(relx= 0.68,rely= 0.1, relwidth= 0.15,relheight= 0.15)

        self.bt_apagar = Button(self.frames_1, text="Apagar", bd=3, bg=BT_COLOR["apagar"], fg="#fff", 
                                font=BT_FONT)
        self.bt_apagar.place(relx= 0.84,rely= 0.1, relwidth= 0.15,relheight= 0.15)

        # Cria os labels e os entries para os dados
        # self.lb_codigo = Label(self.frames_1, text="Código", bg="#aaa")
        # self.lb_codigo.place(relx= 0.05,rely= 0.05)
        # self.codigo_entry = Entry(self.frames_1)
        # self.codigo_entry.place(relx= 0.05,rely= 0.17, relwidth= 0.09)

        self.lb_nome = Label(self.frames_1, text="Nome", bg="#aaa")
        self.lb_nome.place(relx= 0.05,rely= 0.35)
        self.nome_entry = Entry(self.frames_1)
        self.nome_entry.place(relx= 0.05,rely= 0.47, relwidth= 0.8)

        self.lb_bio = Label(self.frames_1, text="Bio", bg="#aaa")
        self.lb_bio.place(relx= 0.05,rely= 0.57)
        self.bio_entry = Entry(self.frames_1)
        self.bio_entry.place(relx= 0.05,rely= 0.67, relwidth= 0.8)

    def limpar(self):
    # Apaga os dados dos entries
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.bio_entry.delete(0, END)

    def novo(self):
    # Abre o arquivo em modo de adição
        f = open("dados.txt", "a")
    # Obtém os dados dos entries
        nome = self.nome_entry.get()
        bio = self.bio_entry.get()
    # Cria uma string com os dados e uma quebra de linha
        linha = "\n" +nome + " | " + bio
    # Escreve a string no arquivo
        f.write(linha)
    # Fecha o arquivo
        f.close()

    def lista_frame2(self):
        # Cria a lista de clientes com as colunas
        self.listaCli = ttk.Treeview(self.frames_2, height=3, column=("col1","col2","col3"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Codigo")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Bio")

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=150)
        self.listaCli.column("#3", width=200)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        # Cria a barra de rolagem para a lista
        self.scroolList = Scrollbar(self.frames_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolList.set)
        self.scroolList.place(relx=0.96, rely=0.1, relheight=0.85)

# Cria uma instância da aplicação
Application()
