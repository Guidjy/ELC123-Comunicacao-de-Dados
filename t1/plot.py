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