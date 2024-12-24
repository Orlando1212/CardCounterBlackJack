import tkinter as tk
from tkinter import messagebox

# Definir o valor das cartas no sistema Hi-Lo
valores_cartas = {
    '2': +1, '3': +1, '4': +1, '5': +1, '6': +1,
    '7': 0, '8': 0, '9': 0,
    '10': -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1
}

# Deck inicial (8 baralhos padrão de 52 cartas)
deck_inicial = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 32

# Contagem de cartas restantes por tipo
contagem_cartas = {carta: 32 for carta in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']}

# Função para calcular a contagem usando o método Hi-Lo
def atualizar_contagem(carta, contagem):
    return contagem + valores_cartas.get(carta, 0)

# Função para calcular a contagem real (ajustada para múltiplos baralhos)
def calcular_contagem_real(contagem, baralhos_restantes):
    if baralhos_restantes > 0:
        return contagem / baralhos_restantes
    return 0

# Função para mostrar o sinal de cor
def sinal_de_cor(contagem):
    if contagem < 4:
        return "Vermelho (ruim)", "red"
    elif 4 <= contagem <= 11:
        return "Amarelo (médio)", "yellow"
    elif 11 <= contagem <= 16:
        return "Azul claro (bom)", "light blue"
    else:
        return "Azul (excelente)", "blue"

# Função para atualizar a interface
def atualizar_interface(carta):
    global contagem, total_cartas, baralhos_restantes, deck, contagem_cartas

    # Verificar se a carta ainda está no deck (para evitar clicar em cartas repetidas)
    if carta in deck and contagem_cartas[carta] > 0:
        # Atualizar a contagem
        contagem = atualizar_contagem(carta, contagem)
        deck.remove(carta)  # Remover a carta do deck
        contagem_cartas[carta] -= 1  # Atualizar a contagem de cartas por tipo
        total_cartas -= 1  # Atualizar o total de cartas no deck

        # Atualizar o número de baralhos restantes
        baralhos_restantes = total_cartas / 52

        # Atualizar as informações da interface
        lbl_contagem_atual.config(text=f"Contagem Atual: {contagem}")
        contagem_real = calcular_contagem_real(contagem, baralhos_restantes)
        lbl_contagem_real.config(text=f"Contagem Real: {contagem_real:.2f}")
        sinal, cor = sinal_de_cor(contagem)
        lbl_sinal.config(text=f"Sinal de cor: {sinal}", bg=cor)
        lbl_cartas_restantes.config(text=f"Cartas restantes: {total_cartas}")

        # Atualizar a contagem em cada botão
        for carta_botao, lbl in labels_cartas.items():
            lbl.config(text=f"{carta_botao}\n{contagem_cartas[carta_botao]}")

        # Se todas as cartas forem baixadas, exibe uma mensagem de fim
        if total_cartas == 0:
            messagebox.showinfo("Fim do Jogo", "Você removeu todas as cartas do deck!")
    else:
        messagebox.showwarning("Carta já removida", "Esta carta já foi removida do deck ou está esgotada.")

# Função para criar os botões para as cartas
def criar_botoes():
    cartas_lado_esquerdo = ['A']
    cartas_superior = ['2', '3', '4', '5', '6', '7']
    cartas_inferior = ['8', '9', '10', 'J', 'Q', 'K']

    # Botão para o Ás (lado esquerdo)
    for carta in cartas_lado_esquerdo:
        lbl = tk.Label(frame_botoes, text=f"{carta}\n{contagem_cartas[carta]}", font=('Arial', 12), width=4, height=2, relief='solid')
        lbl.grid(row=1, column=0, padx=5, pady=5)
        labels_cartas[carta] = lbl
        btn = tk.Button(frame_botoes, text=carta, command=lambda c=carta: atualizar_interface(c), font=('Arial', 14), width=4, height=2)
        btn.grid(row=1, column=1, padx=5, pady=5)

    # Botões para as cartas superiores
    for idx, carta in enumerate(cartas_superior):
        lbl = tk.Label(frame_botoes, text=f"{carta}\n{contagem_cartas[carta]}", font=('Arial', 12), width=4, height=2, relief='solid')
        lbl.grid(row=0, column=idx + 1, padx=5, pady=5)
        labels_cartas[carta] = lbl
        btn = tk.Button(frame_botoes, text=carta, command=lambda c=carta: atualizar_interface(c), font=('Arial', 14), width=4, height=2)
        btn.grid(row=0, column=idx + 1, padx=5, pady=5)

    # Botões para as cartas inferiores
    for idx, carta in enumerate(cartas_inferior):
        lbl = tk.Label(frame_botoes, text=f"{carta}\n{contagem_cartas[carta]}", font=('Arial', 12), width=4, height=2, relief='solid')
        lbl.grid(row=2, column=idx + 1, padx=5, pady=5)
        labels_cartas[carta] = lbl
        btn = tk.Button(frame_botoes, text=carta, command=lambda c=carta: atualizar_interface(c), font=('Arial', 14), width=4, height=2)
        btn.grid(row=2, column=idx + 1, padx=5, pady=5)

# Função principal para configurar a janela
def criar_janela():
    global root, lbl_contagem_atual, lbl_contagem_real, lbl_sinal, lbl_cartas_restantes, frame_botoes, labels_cartas
    root = tk.Tk()
    root.title("Contagem de Cartas Hi-Lo")
    root.geometry("800x500")  # Definir tamanho da janela

    # Informações principais
    lbl_contagem_atual = tk.Label(root, text="Contagem Atual: 0", font=('Arial', 16))
    lbl_contagem_atual.pack(pady=5)

    lbl_contagem_real = tk.Label(root, text="Contagem Real: 0.00", font=('Arial', 16))
    lbl_contagem_real.pack(pady=5)

    lbl_sinal = tk.Label(root, text="Sinal de cor: Amarelo (médio)", font=('Arial', 16), width=25, height=2, relief='solid', bg='yellow')
    lbl_sinal.pack(pady=10)

    lbl_cartas_restantes = tk.Label(root, text="Cartas restantes: 416", font=('Arial', 16))
    lbl_cartas_restantes.pack(pady=5)

    # Frame para os botões das cartas
    frame_botoes = tk.Frame(root)
    frame_botoes.pack(pady=20)

    # Criar os botões para as cartas
    labels_cartas = {}
    criar_botoes()

    root.mainloop()

# Variáveis globais
contagem = 0  # Contagem inicial
deck = deck_inicial.copy()  # Copiar o deck inicial
total_cartas = len(deck)  # Total de cartas no deck
baralhos_restantes = 8  # Número de baralhos restantes

# Rodar a interface gráfica
criar_janela()
