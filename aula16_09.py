class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
    
    def mudar_volume(self, botao):
        if botao == "+":
            print("Aumentar o volume")
        elif botao == "-":
            print("Diminuir o volume")
        
controle1 = ControleRemoto("branca", "10cm", "2cm", "3cm")
controle1.mudar_volume("+")

controle2 = ControleRemoto("preto", "15cm", "5cm", "5cm")
controle2.mudar_volume("-")
# print(controle1.cor)
# print(controle1.altura)
# print(controle2.cor)



# Características do controle
#     - Cor
#     - Altura
#     - Profundidade
#     - Largura

# Métodos do controle(o que ele faz!)
#     - Power(Liga/Desliga)
#     - Mexer no Volume
#     - mute
#     - menu