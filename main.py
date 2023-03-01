#Chamando Bibliotecas de interface grafica
from tkinter import *

#Chamando Bibliotecas de interface grafica com elementos tematicos
from tkinter import ttk


# criando minha variavel central de grafica
root = Tk()

class funcao():

    #Função para limpar dados inseridos
    def limpatela(self):
        self.Eb1.delete(0,END)
        self.Eb2.delete(0,END)
        self.Eb3.delete(0,END)
        self.Eb4.delete(0,END)

# criando classe para gerar toda a minha tela
class aplicação(funcao):
    # Valores inicias da minha classe

    def __init__(self):
        self.root = root
        self.Tela()
        self.frametela()
        self.botao()
        self.lista()
        root.mainloop()

    # Função tela
    def Tela(self):

        #titlo da minha janela,largura,fundo,responcividade,largura_maxima e minima
        self.root.title("Aulas Pratica")
        self.root.geometry("700x500")
        self.root.configure(background="#1e3743")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=600)
        self.root.minsize(width=700,height=500)

    #Divisão da minha janela
    def frametela(self):
        self.frame_1 = Frame(self.root, bd=2, bg="lightblue", highlightbackground="green", highlightthickness=2)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame_2 = Frame(self.root, bd=2, bg="#dfe3ee", highlightbackground="green", highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.50, relwidth=0.96, relheight=0.48)

    # função de botões e elementos da minha janela
    def botao(self):
        self.bt1 = ttk.Button(self.frame_1,text="Limpar",command=self.limpatela)
        self.bt1.place(relx=0.19,rely=0.1,relwidth=0.1,relheight=0.1)
        self.bt2 = ttk.Button(self.frame_1,text="Buscar" )
        self.bt2.place(relx=0.31,rely=0.1,relwidth=0.1,relheight=0.1)
        self.bt3 = ttk.Button(self.frame_1,text="Novo" )
        self.bt3.place(relx=0.6,rely=0.1,relwidth=0.1,relheight=0.1)
        self.bt4 = ttk.Button(self.frame_1,text="Alterar" )
        self.bt4.place(relx=0.72,rely=0.1,relwidth=0.1,relheight=0.1)
        self.bt5 = ttk.Button(self.frame_1,text="Apagar" )
        self.bt5.place(relx=0.84,rely=0.1,relwidth=0.1,relheight=0.1)

        self.lb1 = ttk.Label(self.frame_1,text="Código",background="lightblue",font="verdana 11 bold")
        self.lb1.place(relx=0.05, rely=0.1, relwidth=0.09, relheight=0.1)

        self.Eb1 = ttk.Entry(self.frame_1)
        self.Eb1.place(relx=0.05, rely=0.21, relwidth=0.09, relheight=0.1)

        self.lb2 = ttk.Label(self.frame_1,text="Nome",font="verdana 11 bold",background="lightblue")
        self.lb2.place(relx=0.05, rely=0.37, relwidth=0.08, relheight=0.1)

        self.Eb2 = ttk.Entry(self.frame_1)
        self.Eb2.place(relx=0.05, rely=0.47, relwidth=0.6, relheight=0.1)

        self.lb3 = ttk.Label(self.frame_1,text="Telefone",font="verdana 11 bold",background="lightblue")
        self.lb3.place(relx=0.05, rely=0.64, relwidth=0.12, relheight=0.1)

        self.Eb3 = ttk.Entry(self.frame_1)
        self.Eb3.place(relx=0.05, rely=0.74, relwidth=0.4, relheight=0.1)

        #Elemento cidade
        self.lb4 = ttk.Label(self.frame_1,text="Cidade",font="verdana 11 bold",background="lightblue")
        self.lb4.place(relx=0.6, rely=0.64, relwidth=0.09, relheight=0.1)

        #Entrada de valor de cidade
        self.Eb4 = ttk.Entry(self.frame_1)
        self.Eb4.place(relx=0.6, rely=0.74, relwidth=0.3, relheight=0.1)
    def lista(self):

        #Criando minha Lista e adicionando colunas
        self.lista1 = ttk.Treeview(self.frame_2,height=3,columns=("col1","col2","col3","col4"))
        self.lista1.heading("#0",text="#")
        self.lista1.heading("#1",text="Código")
        self.lista1.heading("#2",text="Nome")
        self.lista1.heading("#3",text="Telefone")
        self.lista1.heading("#4",text="Cidade")

        #Tamanho da colunas
        self.lista1.column("#0",width=1)
        self.lista1.column("#1",width=50)
        self.lista1.column("#2",width=200)
        self.lista1.column("#3",width=130)
        self.lista1.column("#4",width=130)
        self.lista1.place(relx=0,rely=0.01, relwidth=0.95, relheight=0.99)

        #Minha barra de rolagem
        self.lista_rola = Scrollbar(self.frame_2,orient="vertical")
        self.lista1.configure(yscroll=self.lista_rola.set)
        self.lista_rola.place(relx=0.95,rely=0.01,relwidth=0.03,relheight=0.99)



aplicação()
