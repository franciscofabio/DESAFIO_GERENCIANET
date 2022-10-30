# PROJETO DESAFIO GERENCIANET COM DEPLY EM API FLASK

- #### Arquivos do Projeto
    - ##### Desafio_Gerencianet.ipynb - Notebook python com a linha que faz download do zip pela url https://s3.amazonaws.com/gerencianet-pub-prod-1/printscreen/2021/desafio-tecnico.zip, para o download foi utilizado urllib e request, para descompactação a biblioteca ZipFile, para importação do banco SQLite foi utilizado a bibliote sqlite3 e pandas, na descritiva foi utilizado matplotlib para os graficos, para desenvolvimento do modelo e save para deploy utilizei a pycaret e json para transformar o dataset com levels sem classificação em um json para a API consumir e predizer em cima dos dados do json.
    - ##### my_rf_pycaret_model.pkl - modelo salvo para uso na API.
    - ##### data.json - arquivo json gerado com o dataset de levels não classificados para a API consumir.
    - ##### app.py - Script python com utilização do Flask para criação de uma API que consome um JSON com todos os regidtros cujo não tem classificação em level, segue um exemplo do endpoint da API http://localhost:5000/?account_number=309054, a API pode ser iniciada com o comando no terminal conda -> python app.py em seguida basta abrir a URL e passar o account_number
    - ##### deploy.csv - arquivo resultado do deploy apenas em csv.
    
    
- ### O Modelo e os resultados podem ser melhorados utilizado outras tecnicas como banlanceamento de classes, encode, essemble e outros.