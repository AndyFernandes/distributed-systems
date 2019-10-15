# // método adição de contato
# // retornar lista de contatos

from concurrent import futures
import logging

import grpc

import agenda_pb2
import agenda_pb2_grpc


class Greeter(agenda_pb2_grpc.GreeterServicer):
    agenda = []
    def AddContato(self, request, context):
        self.agenda.append(request)
        return agenda_pb2.Reply(message="Contato adicionado com sucesso!")

    def ListarContatos(self, request, context):
        return agenda_pb2.Lista(lista=self.agenda)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    agenda_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:2000')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
