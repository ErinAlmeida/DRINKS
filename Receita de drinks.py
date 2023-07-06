import tkinter as tk
from tkinter import ttk


drinks = {
        1:"Gin Tônica",
        2:"Altos Margarita",
        3:"Aperol Spritz",
        4:"Piña Colada",
        5:"Piña Bourbon",
        6:"Fantasy Ice",
        7:"Mojito",
        8:"Caipirinha",
        9:"Caipirosca",
        10:"Negroni",
        11:"French",
        12:"Lemon Smash",
        13:"Moscow Mule",
        14:"Aperol Sour",
        15:"Whisky Sour",
        16:"Garibaldi",
        17:"Sex on the beach",
        18:"Daiquiri",
        19:"Tequila Sunrise",
        20:"Clericot",
        21:"Drink da patroa",
        22:"Apple gin",
        23:"Sour Singer",
        24:"Soda italiana",
        25:"Coquetel de frutas",
        26:"Cosmopolitan",
        27:"Drink baianinha"  
        }
def exibir_opcoes():
    window = tk.Tk()
    window.title("Zezin's Gastro Pub")

    # Criar tabela
    table = ttk.Treeview(window, columns=("Drink"), height=25)
    table.heading("#0", text="ID")
    table.column("#0", width=40, anchor="center")
    table.heading("Drink", text="Drink", anchor="w")
    largura_maxima = max(len(drink) for drink in drinks.values())
    table.column("Drink", width=largura_maxima * 30)
 
    for numero, drink in drinks.items():
        table.insert("", "end", text=str(numero), values=(drink))
 
    table.pack()

    window.mainloop()
    
def obter_receita(numero):
    return drinks.get(numero)

def main():
    exibir_opcoes()

def receita(nome, forma, ingredientes, passos):
    print("Receita: " + nome)
    print("Forma: " + forma)
    print("Ingredientes:")
    for ingrediente in ingredientes:
        print("- " + ingrediente)
    print("Modo de preparo:")
    for i, passo in enumerate(passos):
        print(str(i + 1) + ". " + passo)
    print("Saúde!")
main()
# Receita 1: Gin Tônica
nome1 = "Gin Tônica\n"
forma1 = "MONTADO\n"
ingredientes1 = ["Gin", "Sumo de limão", "Água tônica\n"]   
passos1 = ["70ml de gin", "20ml de sumo de limão", "Completar com água tônica\n"]

# Receita 2: Altos Margarita
nome2 = "Altos Margarita\n"
forma2 = "BATIDO E COADO\n"
ingredientes2 = ["Tequila", "Sumo de limão", "Cointreau\n"]
passos2 = ["50ml de tequila", "20ml de limão", "30ml de cointreau\n"]

# Receita 3: Aperol Spritz
nome3 = "Aperol Spritz\n"
forma3 = "MONTADO\n"
ingredientes3 = ["Aperol", "Espumante", "Água com gás", "Laranja bahia\n"]
passos3 = ["70ml de aperol", "200ml de espumante", "Completar com água com gás", "Uma fatia, dentro, de laranja bahia\n"]

# Receita 4: Piña Colada
nome4 = "Piña Colada\n"
forma4 = "BATIDO\n"
ingredientes4 = ["Compota de abacaxi", "Rum", "Leite de coco", "Leite condensado\n"]
passos4 = ["5 a 6 pedaços de abacaxi", "70ml de rum", "40ml de leite de coco", "30ml de leite condensado\n"]

# Receita 5: Piña Bourbon
nome5 = "Piña Bourbon\n"
forma5 = "BATIDO\n"
ingredientes5 = ["Whisky Bourbon","Limão siciliano\n"]
passos5 = ["50ml de whisky bourbon", "20ml de limão siciliano\n"]

# Receita 6: Fantasy Ice
nome6 = "Fantasy Ice\n"
forma6 = "MONTADO\n"
ingredientes6 = ["Morango", "Grenadine", "Gordon's", "Ice smirnoff ou kisla\n"]
passos6 = ["5 morangos macerados", "10ml de grenadine", "70ml de gordon's", "ice de sua escolha\n"]

# Receita 7: Mojito
nome7 = "Mojito\n"
forma7 = "MONTADO\n"
ingredientes7 = ["Limão", "Xarope de açúcar", "Hortelã", "Água com gás\n"]
passos7 = ["6 pedaços de limão", "30ml de xarope simples", "10 folhas de hortelã", "Completar com água com gás\n"]

# Receita 8: Caipirinha
nome8 = "Caipirinha\n"
forma8 = "BATIDO\n"
ingredientes8 = ["Limão", "Cachaça", "Xarope simples\n"]
passos8 = ["6 a 8 pedaços de limão", "70ml de cachaça", "40ml de xarope simples\n"]

# Receita 9: Caipirosca
nome9 = "Caipirosca\n"
forma9 = "BATIDO\n"
ingredientes9 = ["Limão", "Vodka", "Xarope Simples\n"]
passos9 = ["6 a 8 pedaços de limão", "70ml de vodka", "40ml de xarope simples\n"]

# Receita 10: Negroni
nome10 = "Negroni\n"
forma10 = "Mexido\n"
ingredientes10 = ["Vermut", "Campari", "Gin\n"]
passos10 = ["30ml de vermut", "30ml de campari", "30ml de gin\n"]

# Receita 11: French
nome11 = "French\n"
forma11 = "Montado\n"
ingredientes11 = ["Gin", "Limão siciliano", "Espumante", "Cereja\n"]
passos11 = ["20ml de gin","15ml de limão siciliano","Completar com espumante","Finalizar com cereja\n"]

# Receita 12: Lemon Smash
nome12 = "Lemon Smash\n"
forma12 = "BATIDO\n"
ingredientes12 = ["Redução de maracujá", "Limão siciliano", "Vodka", "Xarope simples", "Capim cidreira\n"]
passos12 = ["Capim cidreira macerado com um pouco de gelo", "100ml de redução de maracujá", "40ml de limão siciliano", "120ml de vodka", "50ml de xarope simples\n"]

# Receita 13: Moscow Mule
nome13 = "Moscow Mule\n"
forma13 = "Montado\n"
ingredientes13 = ["Limão", "Xarope simples", "Vodka", "Espuma de gengibre\n"]
passos13 = ["30ml de sumo de limão", "35ml de xarope simples", "70ml de vodka", "Espuma por cima\n"]

# Receita 14: Aperol Sour
nome14 = "Aperol Sour\n"
forma14 = "BATIDO\n"
ingredientes14 = ["Aperol", "Gin", "Sumo de laranja", "Xarope simples", "Uma clara de ovo\n"]
passos14 = ["30ml de aperol","30ml de gin", "20ml de sumo de laranja","20ml de xarope simples", "Uma clara de ovo inteira\n"]

# Solicita ao usuário o número da receita desejada
n_receita = int(input("Digite o número da receita que você deseja visualizar: "))


# Exibe apenas a receita selecionada
if n_receita == 1:
    receita(nome1, forma1, ingredientes1, passos1)
elif n_receita == 2:
    receita(nome2, forma2, ingredientes2, passos2)
elif n_receita == 3:
    receita(nome3, forma3, ingredientes3, passos3)
elif n_receita == 4:
    receita(nome4, forma4, ingredientes4, passos4)
elif n_receita == 5:
    receita(nome5, forma5, ingredientes5, passos5)
elif n_receita == 6:
    receita(nome6, forma6, ingredientes6, passos6)
elif n_receita == 7:
    receita(nome7, forma7, ingredientes7, passos7)
elif n_receita == 8:
    receita(nome8, forma8, ingredientes8, passos8)
elif n_receita == 9:
    receita(nome9, forma9, ingredientes9, passos9)
elif n_receita == 10:
    receita(nome10, forma10, ingredientes10, passos10)
elif n_receita == 11:
    receita(nome11, forma11, ingredientes11, passos11)
elif n_receita == 12:
    receita(nome12, forma12, ingredientes12, passos12)
elif n_receita == 13:
    receita(nome13, forma13, ingredientes13, passos13)
elif n_receita == 14:
    receita(nome14, forma14, ingredientes14, passos14)
else:
    print("Número de receita inválido!")