Sistema de consumo de API Offline meterologica, cujo a estrutura:

#consumidor_api - consume a api, que já está rodando localmente, acessando os dados e disponibilizando em uma função para a demonstração no frontend

#frontend_01 - Utiliza os dados pegos do cosumidor e apresenta no frontend para o usuário

#.gitignore - Ignora os arquivos que não podem ser versionados

#requirements.txt - Possui as dependências para serem instaladas em um ambiente virtual, após sua ativação e então para baixar  o necessário:

1 - git clone url ...
2 - cd projeto_meteorologico
3 - python -m venv .venv
4 - .\.venv\Scripts\Activate.ps1
5 - pip install -r requirements.txt

OBS: Vale lembrar que para rodar o sistema deve se rodar localmente a API OFFLINE, via uvicorn, para sua consulta.


#README - Usado para especificações do sistema






