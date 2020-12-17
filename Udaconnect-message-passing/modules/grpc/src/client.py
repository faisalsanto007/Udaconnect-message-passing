# -*- coding: utf-8 -*-

import grpc
import person_pb2 
import person_pb2_grpc 


print("sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = person_pb2_grpc.PersonServiceStub(channel)

# update this with desired payload
person = person_pb2.PersonMessage(
    first_name = "Faisal",
    last_name="Aziz",
    id = 7,
    company = "Adipster"
)

reponse = stub.storePerson(person)