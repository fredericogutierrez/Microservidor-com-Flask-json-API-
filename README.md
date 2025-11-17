# Microservidor-com-Flask-json-API-
API em python utilizando Flask e json. 

# -----------------------------------------------
# API de manipulação de arquivos .txt usando Flask
# Funcionalidades:
#   - Criar arquivo (POST)
#   - Ler arquivo (GET)
#   - Editar arquivo (PUT)
#   - Deletar arquivo (DELETE)
# -----------------------------------------------


TESTES VIA POWERSHELL


CRIAR
curl -Method POST http://127.0.0.1:5000/files `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{"filename":"teste_powershell.txt","content":"Primeira linha do arquivo\n"}'

GET

curl -Method GET http://127.0.0.1:5000/files/teste_powershell.txt


PUT

curl -Method PUT http://127.0.0.1:5000/files/teste_powershell.txt `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{"content":"Segunda linha adicionada via PowerShell\n"}'


DELETE

curl -Method DELETE http://127.0.0.1:5000/files/teste_powershell.txt


TESTE VIA CMD

CRIAR
curl -X POST http://127.0.0.1:5000/files ^
  -H "Content-Type: application/json" ^
  -d "{\"filename\":\"teste.txt\",\"content\":\"Primeira linha do arquivo\n\"}"

GET

curl http://127.0.0.1:5000/files/teste.txt


PUT

curl -X PUT http://127.0.0.1:5000/files/teste.txt ^
  -H "Content-Type: application/json" ^
  -d "{\"content\":\"Segunda linha adicionada\n\"}"


DELETE

del teste.txt
