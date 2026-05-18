def NRZL(dado_digital):
    """bit 0 = tensão alta, bit 1 = tensão alta
    Args:
        dado_digital (int[]): lista que representa o dado digital
    Returns:
        int[]: lista que representa o dado digital codificado
    """
    elementos_de_sinal = []
    
    for bit in dado_digital:
        if bit == 0:
            elementos_de_sinal.append(1)
        else:
            elementos_de_sinal.append(-1)
            
    return elementos_de_sinal

def NRZI(dado_digital):
    """bit 0 = não inverte tansão, bit 1 = inverte tensão
    Args:
        dado_digital (int[]): lista que representa o dado digital
    Returns:
        int[]: lista que representa o dado digital codificado
    """
    elementos_de_sinal = []
    nivel_atual = -1  # supõe que a linha estava em tensão baixa antes de começar
    
    for bit in dado_digital:
        if bit == 1:
            nivel_atual *= -1
        
        elementos_de_sinal.append(nivel_atual)
            
    return elementos_de_sinal

def AMI(dado_digital):
    """bit 0 = tensão zero, bit 1 = alterna tensão
    Args:
        dado_digital (int[]): lista que representa o dado digital
    Returns:
        int[]: lista que representa o dado digital codificado
    """
    elementos_de_sinal = []
    indice_ultimo_1 = None
    
    for i, bit in enumerate(dado_digital):
        if bit == 0:
            elementos_de_sinal.append(0)
        else:
            if indice_ultimo_1 == None:
                elementos_de_sinal.append(1)
            else:
                elementos_de_sinal.append(elementos_de_sinal[indice_ultimo_1] * -1)
            indice_ultimo_1 = i
    
    return elementos_de_sinal

def pseudoternario(dado_digital):
    """oposto do AMI: bit 0 = alterna tensão, bit 1 = tensão zero
    Args:
        dado_digital (int[]): lista que representa o dado digital
    Returns:
        int[]: lista que representa o dado digital codificado
    """
    elementos_de_sinal = []
    indice_ultimo_0 = None
    
    for i, bit in enumerate(dado_digital):
        if bit == 1:
            elementos_de_sinal.append(0)
        else:
            if indice_ultimo_0 == None:
                elementos_de_sinal.append(1)
            else:
                elementos_de_sinal.append(elementos_de_sinal[indice_ultimo_0] * -1)
            indice_ultimo_0 = i
    
    return elementos_de_sinal

def manchester(dado_digital):
    """bit 0 = transição alta para baixa, bit 1 = transição baixa para alta
    Args:
        dado_digital (int[]): lista que representa o dado digital
    Returns:
        int[]: lista que representa o dado digital codificado
    """
    elementos_de_sinal = []
    
    for bit in dado_digital:
        if bit == 0:
            elementos_de_sinal.extend([1, -1])
        else:
            elementos_de_sinal.extend([-1, 1])
        
    return elementos_de_sinal

def manchester_diferencial(dado_digital):
    """bit é dividido em duas partes:
    - meio do bit: sempre ocorre uma transição
    - início do bit: 
        - 0 = inverte em relação a segunda metade do bit anterior 
        - 1 = não inverte, mantem continuidade com a segunda metade do bit anterior
    Args:
        dado_digital (int[]): lista que representa o dado digital
    Returns:
        int[]: lista que representa o dado digital codificado
    """
    elementos_de_sinal = []
    
    ultima_metade = -1 # supõe que a segunda metade do bit anterior estava em tensão baixa
    
    for bit in dado_digital:
        if bit == 0:
            primeira_metade = ultima_metade * -1
        else:
            primeira_metade = ultima_metade

        segunda_metade = primeira_metade * -1
        
        elementos_de_sinal.extend([primeira_metade, segunda_metade])
        ultima_metade = segunda_metade
        
    return elementos_de_sinal

def cod_2B1Q(dado_digital):
    """Transforma 2 bits binários em 1 símbolo quaternário
    Args:
        dado_digital (int[]): lista que representa o dado digital
    Returns:
        int[]: lista que representa o dado digital codificado
    """
    # criamos uma cópia para não alterar o número de bits adicionando 1 no final
    dado_digital_cpy = dado_digital.copy() 

    #Caso tenha um número ímpar de bits preenchemos com 0 no final
    if len(dado_digital_cpy) % 2 != 0:
        dado_digital_cpy.append(0)

    tabela_2b1q = {
        (0, 0): -3,
        (0, 1): -1,
        (1, 0): +3,
        (1, 1): +1
    }
    
    elemento_de_sinal = []

    for i in range(0, len(dado_digital_cpy), 2):
        par = (dado_digital_cpy[i], dado_digital_cpy[i+1])
        nivel = tabela_2b1q[par]
        elemento_de_sinal.append(nivel)
    
    return elemento_de_sinal

def delay_modulation(dado_digital):        
    """Caso o bit for 0, trocamos de nível na borda do bit, 
    caso o bit for 1, trocamos de nível no meio do tempo do bit
    Args:
        dado_digital (int[]): lista que representa o dado digital
    Returns:
        int[]: lista que representa o dado digital codificado
    """
    elemento_de_sinal = [] # Guardará dois valores por bit: [primeira_metade, segunda_metade]
    
    estado_atual = -1  # supõe que a linha estava em tensão baixa antes de começar
    
    for i, bit in enumerate(dado_digital):
        if bit == 1:
            primeira_metade = estado_atual
            segunda_metade = -estado_atual
            
            elemento_de_sinal.extend([primeira_metade, segunda_metade])
            estado_atual = segunda_metade
            
        else:
            if i > 0 and dado_digital[i-1] == 0:
                estado_atual = -estado_atual
                
            primeira_metade = estado_atual
            segunda_metade = estado_atual
            
            elemento_de_sinal.extend([primeira_metade, segunda_metade])
            
    return elemento_de_sinal

def MLT_3(dado_digital):
    """Caso o bit for 0, se mantém no mesmo nível, caso o bit for 1,
    segue para o próximo estado da sequencia cíclica [0V, +V, 0V, -V]
    Args:
        dado_digital (int[]): lista que representa o dado digital
    Returns:
        int[]: lista que representa o dado digital codificado
    """
    ciclo_estados = [0, 1, 0, -1]
    indice_estado = 0 # Começa no primeiro 0 da sequência
    
    elemento_de_sinal = []
    
    for bit in dado_digital:
        if bit == 1:
            indice_estado = (indice_estado + 1) % 4
            
        elemento_de_sinal.append(ciclo_estados[indice_estado])
        
    return elemento_de_sinal