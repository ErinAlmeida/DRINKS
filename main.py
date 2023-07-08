from tkinter import *
from tkinter import ttk
drinks =[
    [["Gin Tônica", "MONTADO"], ["Gin", "Sumo de limão", "Água tônica"], ["70ml de gin", "20ml de sumo de limão", "Completar com água tônica"]],
    [["Altos Margarita","BATIDO E COADO"], ["Tequila", "Sumo de limão", "Cointreau"], ["50ml de tequila", "20ml de limão", "30ml de cointreau"]],
    [["Aperol Spritz","MONTADO"], ["Aperol", "Espumante", "Água com gás", "Laranja bahia"], ["70ml de aperol", "200ml de espumante", "Completar com água com gás", "Uma fatia, dentro, de laranja bahia"]],
    [["Piña Colada", "BATIDO"], ["Compota de abacaxi", "Rum", "Leite de coco", "Leite condensado"], ["5 a 6 pedaços de abacaxi", "70ml de rum", "40ml de leite de coco", "30ml de leite condensado"]],
    [["Piña Bourbon","BATIDO"], ["Whisky Bourbon","Limão siciliano"],["50ml de whisky bourbon", "20ml de limão siciliano"]],
    [["Fantasy Ice","MONTADO"], ["Morango", "Grenadine", "Gordon's", "Ice smirnoff ou kisla"], ["5 morangos macerados", "10ml de grenadine", "70ml de gordon's", "ice de sua escolha"]],    
    [["Mojito","MONTADO"], ["Limão", "Xarope de açúcar", "Hortelã", "Água com gás"], ["6 pedaços de limão", "30ml de xarope simples", "10 folhas de hortelã", "Completar com água com gás"]],
    [["Caipirinha","BATIDO"], ["Limão", "Cachaça", "Xarope simples"], ["6 a 8 pedaços de limão", "70ml de cachaça", "40ml de xarope simples"]],
    [["Caipirosca", "BATIDO"], ["Limão", "Vodka", "Xarope Simples"], ["6 a 8 pedaços de limão", "70ml de vodka", "40ml de xarope simples"]],
    [["Negroni","Mexido"], ["Vermut", "Campari", "Gin"], ["30ml de vermut", "30ml de campari", "30ml de gin"]],
    [["French","Montado"], ["Gin", "Limão siciliano", "Espumante", "Cereja"], ["20ml de gin","15ml de limão siciliano","Completar com espumante","Finalizar com cereja"]],
    [["Lemon Smash", "BATIDO"], ["Redução de maracujá", "Limão siciliano", "Vodka", "Xarope simples", "Capim cidreira"], ["Capim cidreira macerado com um pouco de gelo", "100ml de redução de maracujá", "40ml de limão siciliano", "120ml de vodka", "50ml de xarope simples"]],
    [["Moscow Mule", "Montado"], ["Limão", "Xarope simples", "Vodka", "Espuma de gengibre"], ["30ml de sumo de limão", "35ml de xarope simples", "70ml de vodka", "Espuma por cima"]],
    [["Aperol Sour","BATIDO"], ["Aperol", "Gin", "Sumo de laranja", "Xarope simples", "Uma clara de ovo"],["30ml de aperol","30ml de gin", "20ml de sumo de laranja","20ml de xarope simples", "Uma clara de ovo inteira"]]
]
def openReceita(array):
    newWindow = Toplevel(window)
    newWindow.title( array[0][0] + " ------ " + array[0][1])
    newWindow.geometry("300x300")

    Label(newWindow,text = "INGREDIENTES").pack()
    for e in array[1]:
        Label(newWindow,text = e).pack()
    
    Label(newWindow,text = "MODO DE PREPARO").pack()
    for e in array[2]:
        Label(newWindow,text = e).pack()


    button = ttk.Button(
    newWindow,
    text= "Voltar",
    command=lambda: newWindow.quit()
    )
    button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )
 
 
window = Tk()
window.title("Zezin's Gastro Pub")


labels=[] 
for e in drinks:
    
    button = ttk.Button(
        window,
        text= e[0][0] + " ------ " + e[0][1],
        command=lambda: openReceita(e)
    )
    button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )
    

window.mainloop()