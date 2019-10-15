from __future__ import print_function
import logging

import grpc

import agenda_pb2
import agenda_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:2000') as channel:
        stub = agenda_pb2_grpc.GreeterStub(channel)
        # contato = agenda_pb2.Contato(nome='Edsu', telefone='88981033010', idade=21)
        # contato2 = agenda_pb2.Contato(nome='Jeova', telefone='88981033010', idade=21)
        # contato3 = agenda_pb2.Contato(nome='Jesus', telefone='88981033010', idade=21)
        # response = stub.AddContato(contato)
        response = stub.ListarContatos(agenda_pb2.Lista())
        print(response)
    # print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
