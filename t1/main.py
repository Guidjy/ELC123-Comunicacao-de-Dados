from fastapi import FastAPI, Request, Body, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import matplotlib.pyplot as plt
from pathlib import Path
from codificacao import *
from plot import *

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")   

@app.post('/plot')
def plot(dado_digital: list[int] = Body(), metodos_de_codificacao: list[str] = Body()):
    """
    **Plota um gráfico de codificação de linha, salva em 'static/plots/'.**
    #### Args:
        - dado_digital (int[]): lista de bits que representam o dado digital (ex: [1, 0, 1, 1, 0])
        - metodos_de_codificacao (str[]): lista com o nome dos métodos de codificação a serem 
        aplicados no dado digital (ex: ['nrz', 'manchester']).
    #### Returns:
        - FileResponse: imagem do gráfico gerado
    """
    # caminho para salvar o gráfico e nome do arquivo
    diretorio = Path("static") / "plots"
    caminho = diretorio / "plot.png"

    # aplica os métodos de codificação no dado_digital
    codigos_de_linha = {}
    for metodo in metodos_de_codificacao:
        metodo = metodo.upper()
        match metodo:
            case "MANCHESTER":
                codigos_de_linha[metodo] = manchester(dado_digital)
            # TODO: implementar resto dos métodos
            case _:
                raise HTTPException(status_code=404, detail=f'método {metodo} não recdonhecido')

    # plota e salva o gráfico (TODO: usar os métodos de codificação e não um gráfico fake)
    plota_grafico(codigos_de_linha["MANCHESTER"], caminho)
    
    return FileResponse(caminho)