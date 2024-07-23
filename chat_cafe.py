import os
os.system("cls")

import webbrowser 

def inicio():
    print("""
Bem vindo(a) ao Café Estação, sua a Beanie, sua assitente virtual e estou aqui para te ajudar, o que necessita?
1- Nosso menu
2- Nosso horário de funcionamento
3- Nossas localizações
4- Nossos serviços
5- Falar com atendente
""")
    opcao=input()
    if opcao == '1':
        menu()
    elif opcao == '2':
        horario()
    elif opcao == '3':
        localizacao()
    elif opcao == '4':
        servicos()
    elif opcao == '5':
        atendente()
    else:
        print("""
Desculpe, não temos essa opção. O que deseja?
1- Tentar novamente
2- Sair
""")
        escolha=input()
        if escolha == '1':
            inicio()
        elif escolha == '2':
           print("Fim de atendimento, obrigado por visitar o Café Estação, volte sempre! :D")
    
        
       
def menu():
    print("""
Menu do Café Estações

Bebidas Quentes

Expresso - R$ 5,00
Café puro e intenso.

Cappuccino - R$ 7,50
Café expresso com leite vaporizado e espuma de leite.

Latte - R$ 8,00
Expresso com uma generosa quantidade de leite vaporizado.

Mocha - R$ 9,00
Expresso com chocolate quente e leite vaporizado.

Chá Verde - R$ 6,00
Infusão de folhas de chá verde.

Chocolate Quente - R$ 7,00
Delicioso chocolate derretido com leite quente.

Bebidas Geladas

Iced Coffee - R$ 6,00
Café gelado com gelo.
Frappuccino - R$ 10,00
Café batido com gelo, leite e chantilly.
Iced Latte - R$ 8,50
Expresso com leite gelado e gelo.
Smoothie de Frutas Vermelhas - R$ 9,00
Mistura refrescante de morango, amora e framboesa.
Chá Gelado de Limão - R$ 6,00
Chá preto gelado com limão.
Milkshake de Chocolate - R$ 10,00
Sorvete de chocolate batido com leite.

Doces

Bolo de Cenoura com Cobertura de Chocolate - R$ 7,00
Brownie de Chocolate - R$ 6,50
Torta de Limão - R$ 8,00
Croissant de Amêndoas - R$ 5,00
Muffin de Blueberry - R$ 5,50
Pão de Mel - R$ 4,00

Salgados

Coxinha - R$ 6,00
Empada de Frango - R$ 5,50
Quiche de Alho-Poró - R$ 7,00
Sanduíche de Peru com Queijo - R$ 8,50
Pão de Queijo - R$ 3,50
Tostado de Presunto e Queijo - R$ 9,00
""")
    
    
def horario():
    print("""
Horário de Funcionamento do Café Estação

Segunda a Sexta:
08:00 - 20:00

Sábado e Feriados:
09:00 - 18:00

Domingo:
10:00 - 16:00

""")

def localizacao():
    print("""
Café Estação
Rua das Flores, 123
Bairro Jardim das Estações
Cidade Encantada, EC 45678-000
          
""")


def servicos():
    print("""
No Café Estação, estamos comprometidos em proporcionar a melhor experiência para nossos clientes, com uma variedade de serviços pensados especialmente para você. Confira o que oferecemos:

Espaço para Festas e Eventos
Procurando um local aconchegante para celebrar uma ocasião especial? Nosso café oferece um espaço exclusivo para festas e eventos, perfeito para aniversários, reuniões corporativas, encontros de amigos e muito mais. Entre em contato conosco para saber mais sobre pacotes e reservas.

Reservas Antecipadas
Garanta seu lugar no Café Estação fazendo uma reserva antecipada. Seja para um encontro casual ou uma reunião importante, estamos aqui para tornar sua visita ainda mais agradável. Ligue para nós ou faça sua reserva online pelo nosso site.

Serviço de Catering
Leve o sabor do Café Estação para o seu evento! Oferecemos serviços de catering com uma seleção de bebidas, doces e salgados para surpreender seus convidados. Personalize o cardápio conforme suas necessidades e deixe o resto por nossa conta.

Wi-Fi Gratuito
Precisa trabalhar ou estudar? Aproveite nosso Wi-Fi gratuito enquanto saboreia nossas deliciosas opções de café e lanches. Um ambiente tranquilo e confortável para você se concentrar nas suas atividades.

Programas de Fidelidade
Queremos recompensar nossos clientes fiéis! Participe do nosso programa de fidelidade e ganhe pontos a cada compra, que podem ser trocados por descontos e brindes exclusivos.

Atendimento Personalizado
Nossa equipe está sempre pronta para atender você com um sorriso e oferecer o melhor serviço. Seja uma recomendação de café ou uma sugestão de combinação de sabores, estamos aqui para ajudar.

Venda de Produtos Artesanais
Além de nossas deliciosas bebidas e lanches, oferecemos uma seleção de produtos artesanais para você levar para casa. Desde grãos de café selecionados até doces caseiros, temos opções que vão encantar seu paladar.
""")
    
    

def atendente():
    print(""" Você já está sendo direcionado(a)
""")
    webbrowser.open("https://www.google.com")  #canal simbólico 

inicio()
