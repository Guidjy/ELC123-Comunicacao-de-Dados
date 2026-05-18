const data = {
    dado_digital: [1, 0, 1, 1, 0],
    metodos_de_codificacao: ["NRZL", "manchester"]
};

async function codificacaoDeLinha(dadoDigital) {
    const response = await fetch("/plot", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    })
    
    if (!response.ok) {
        throw new Error('Resposta não OK');
    }

    // retorna .blob() para poder passar a imagem para uma variável
    return await response.blob();
}

let grafico = await codificacaoDeLinha([1, 0, 1, 1, 0]);
const urlImagem = URL.createObjectURL(grafico);
document.getElementById("resultado-grafico").src = urlImagem;

