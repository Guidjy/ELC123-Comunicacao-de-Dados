## Como rodar:

- Crie um ambiente virtual: 
```
python3 -m venv .venv
```
- Ative o ambiente virtual:
    - Linux: 
    ```
    source .venv/bin/activate
    ```
    - Windows(cmd): 
    ```
    .\.venv\Scripts\activate.bat
    ```
- Instale dependências: 
```
pip install requirements.txt
```
- Inicialize o servidor web: 
```
uvicorn main:app
```
    - (Para ver mudanças no código automaticamente): 
    ```
    uvicorn main:app --reload
    ```