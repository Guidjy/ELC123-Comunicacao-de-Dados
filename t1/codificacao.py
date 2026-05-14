# TODO: implementar métodos de codificação

def manchester(dado_digital):
    """Codificação de Manchester
    Args:
        dado_digital (int[]): lista que representa o dado digital (ex: [1, 0, 1, 1, 0])
    Returns:
        int[]: lista que representa o dado digital codificado (ex: [1, 0, 0, 1, 1, 0, 1, 0, 0, 1])
    """
    elementos_de_sinal = []
    
    for bit in dado_digital:
        bit_convertido = [0, 1] if bit == 0 else [1, 0]
        elementos_de_sinal.extend(bit_convertido)
        
    return elementos_de_sinal
        