class Receita ():
    def __init__(self, tipo, cor, quantidade, kg, gosto, nome):
        self.tipo = tipo
        self.cor = cor
        self.quantidade = quantidade
        self. kg = kg
        self.gosto = gosto
        self. nome = nome

    def get_all(self): 

        print ("Esse alimento é um {}, é {} a sua cor, tem {} de quantidade, tem {} kg, tem gosto {}, tem nome {}.".format (self.tipo, self.cor, self.quantidade, self.kg, self.gosto, self.nome))

macarrao = Receita ("Spagetti", "Amarela", "2 pacotes", 2, "bom", "kenned")
bolo = Receita ("bolinho", "marrom", "1 pacote", 2, "ótimo", "boludo")

macarrao.get_all()
bolo.get_all()




