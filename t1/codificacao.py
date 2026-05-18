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

# TODO: implementar 2B1Q, Código Miller (Delay Modulation), e MLT-3