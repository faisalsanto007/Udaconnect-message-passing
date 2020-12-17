# -*- coding: utf-8 -*-

import time
from concurrent import futures

import grpc
import person_pb2_grpc
import person_pb2 


class PersonServicer(person_pb2_grpc.PersonServiceServicer):
    
    def storePerson (self, request, context):

      request_value = {
          "first_name": request.first_name,
          "last_name": request.last_name,
          "id": int(request.id),
          "company": request.company,
      }
      print(request_value)

      return person_pb2.PersonMessage(**request_value)

        
# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
person_pb2_grpc.add_PersonServiceServicer_to_server(PersonServicer(), server)

print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)