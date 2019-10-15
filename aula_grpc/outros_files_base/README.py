# Execução da Agenda

1. Gerar os arquivo pb e grpc -> python -m grpc_tools.protoc -I. --python_out=. --grepc_python_out=. agenda.pro
2. Rodar server -> python agenda_server.py
2. Rodar client -> python agenda_client.py
