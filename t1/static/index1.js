// Lista com todos os métodos disponíveis no trabalho
const TODOS_METODOS = [
    "NRZL", 
    "NRZI",
    "AMI",
    "PSEUDOTERNARIO",
    "MANCHESTER",
    "M. DIFERENCIAL",
    "2B1Q",
    "CÓDIGO MILLER",
    "MLT-3"
];

// Inicializa interface
function inicializarInterface() {
    const container = document.getElementById("container-metodos");
    
    TODOS_METODOS.forEach(metodo => {
        const div = document.createElement("div");
        div.className = "flex items-center space-x-3";
        
        div.innerHTML = `
            <input type="checkbox" value="${metodo}" class="checkbox checkbox-primary metodo-checkbox border-gray-500" />
            <span class="text-gray-300 cursor-pointer select-none">${metodo}</span>
        `;
        
        // Permite clicar no texto para marcar o checkbox
        div.querySelector('span').addEventListener('click', () => {
            const checkbox = div.querySelector('input');
            checkbox.checked = !checkbox.checked;
        });

        container.appendChild(div);
    });
}

// Fetch do gráfico
async function codificacaoDeLinha(payload) {
    const response = await fetch("/plot", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(payload)
    });
    
    if (!response.ok) {
        throw new Error('Erro na resposta do servidor.');
    }

    return await response.blob();
}

// "Gerar Gráfico" callback
document.getElementById("btn-gerar").addEventListener("click", async () => {
    // Captura os bits e valida a entrada (transforma em array de inteiros)
    const textoBits = document.getElementById("input-bits").value.trim();
    const dadoDigital = textoBits.split("").map(Number);

    // Verifica se há algo que não seja 0 ou 1
    if (dadoDigital.some(bit => bit !== 0 && bit !== 1) || dadoDigital.length === 0) {
        alert("Por favor, insira uma sequência válida contendo apenas 0s e 1s.");
        return;
    }

    // Captura os métodos selecionados
    const checkboxes = document.querySelectorAll('.metodo-checkbox:checked');
    const metodosSelecionados = Array.from(checkboxes).map(cb => cb.value);

    if (metodosSelecionados.length === 0) {
        alert("Por favor, selecione pelo menos um método de codificação de linha para visualização.");
        return;
    }

    // Monta o objeto com os dados para o backend
    const dataToSend = {
        dado_digital: dadoDigital,
        metodos_de_codificacao: metodosSelecionados
    };

    // Controle de UI (Loading e Imagem)
    const imgElement = document.getElementById("resultado-grafico");
    const loadingElement = document.getElementById("loading");
    
    imgElement.classList.add("hidden");
    loadingElement.classList.remove("hidden");

    try {
        // Envia a requisição
        const graficoBlob = await codificacaoDeLinha(dataToSend);
        
        // Exibe a imagem
        const urlImagem = URL.createObjectURL(graficoBlob);
        imgElement.src = urlImagem;
        
        loadingElement.classList.add("hidden");
        imgElement.classList.remove("hidden");
        
    } catch (error) {
        console.error(error);
        alert("Ocorreu um erro ao gerar o gráfico. Verifique o console ou a comunicação com o servidor.");
        loadingElement.classList.add("hidden");
    }
});

// "Aleatório" callback
document.getElementById("btn-aleatorio").addEventListener("click", () => {
    let sequenciaAleatoria = "";
    
    // Gera 16 números (0 ou 1) aleatoriamente
    for (let i = 0; i < 16; i++) {
        const bit = Math.floor(Math.random() * 2);
        sequenciaAleatoria += bit;
    }
    
    // Define o valor gerado no campo de texto
    document.getElementById("input-bits").value = sequenciaAleatoria;
});

// Executa a inicialização ao carregar o script
inicializarInterface();