import matplotlib.pyplot as plt

def plota_grafico(dado_digital, caminho):
    """
    Feito pelo gemini -> mudar depois para plotar vários sinais
    """
    # 1. Create the step plot
    # where='post' means the signal stays at its current value until the NEXT point
    plt.step(range(len(dado_digital)), dado_digital, where='post', color='blue', linewidth=2)

    # 2. Format the Y-axis to look like a logic analyzer
    plt.ylim(-0.2, 1.2)  # Add padding above 1 and below 0 so the line doesn't touch the edges
    plt.yticks([0, 1])   # Force the y-axis to ONLY show 0 and 1

    # 3. Add a grid to easily read the "clock cycles"
    plt.grid(True, axis='x', linestyle='--', alpha=0.7)

    # 4. Add labels
    plt.ylabel('Logic Level')
    plt.xlabel('Time Step / Clock Cycle')
    plt.title('Digital Signal Plot')

    # Save the plot
    plt.savefig(caminho)
    plt.close()
    
    
import matplotlib.pyplot as plt
import numpy as np

def plot_codificacoes(dicionario_sinais, caminho, num_bits=None):
    """
    Plota os gráficos dos sinais de codificação de linha em subplots empilhados.

    Args:
        dicionario_sinais (dict): Dicionário { 'Nome do Método': [lista_de_sinais] }
        num_bits (int, opcional): Número total de bits da cadeia original. 
                                  Se não informado, infere pelo tamanho do primeiro sinal.
    """
    if num_bits is None:
        # Pega o tamanho do primeiro sinal como referência de tempo
        num_bits = len(list(dicionario_sinais.values())[0])

    n_plots = len(dicionario_sinais)
    
    # Cria os subplots empilhados compartilhando o eixo X
    fig, axes = plt.subplots(n_plots, 1, figsize=(10, 2.5 * n_plots), sharex=True)
    
    # Se houver apenas 1 método, o matplotlib não retorna um array. Transformamos em lista.
    if n_plots == 1:
        axes = [axes]

    for ax, (nome, sinal) in zip(axes, dicionario_sinais.items()):
        
        # --- ALINHAMENTO DE TEMPO ---
        # Cria um eixo X que vai de 0 até o número de bits.
        # len(sinal) + 1 cria as divisões exatas (ex: 12 partes para Manchester, 6 para NRZ)
        x = np.linspace(0, num_bits, len(sinal) + 1)
        
        # Duplica o último valor do sinal para que a função 'step' desenhe 
        # a linha final até o fim da borda direita.
        y = list(sinal) + [sinal[-1]]
        
        # Plota como onda digital
        ax.step(x, y, where='post', linewidth=2.5, color='#1f77b4')
        
        # --- FORMATAÇÃO DO EIXO Y ---
        # Define as margens Y dinamicamente
        ax.set_ylim(min(sinal) - 0.5, max(sinal) + 0.5)
        
        # Mostra no eixo Y apenas os níveis de tensão exatos que o sinal utiliza
        niveis_tensao = sorted(list(set(sinal)))
        ax.set_yticks(niveis_tensao)
        
        # --- ESTILIZAÇÃO ---
        # Rótulo do eixo Y contendo o nome do método
        ax.set_ylabel(nome, fontsize=12, fontweight='bold', rotation=0, labelpad=60, ha='center')
        
        # Adiciona grade e linha central
        ax.grid(True, which='major', axis='x', linestyle='--', linewidth=1, alpha=0.7)
        ax.grid(True, which='major', axis='y', linestyle=':', linewidth=0.5, alpha=0.5)
        ax.axhline(0, color='black', linewidth=1.2, alpha=0.6) # Linha do 0V

    # Formatação do eixo X comum (fica apenas no último gráfico)
    axes[-1].set_xlabel('Tempo (Duração dos Bits)', fontsize=12, fontweight='bold')
    axes[-1].set_xticks(range(num_bits + 1))
    
    # Título geral e ajuste de margens
    plt.suptitle("Análise de Sinais - Codificação de Linha", fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    
    plt.savefig(caminho)
    plt.close()