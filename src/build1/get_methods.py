"""
Get methods of all the modules.
"""
import pprint

import grpc
import poskaship_pb2
import client
import common

print(f"\n grpc: ")
pprint.pprint(dir(grpc))

print(f"\n poskaship_pb2: ")
pprint.pprint(help(poskaship_pb2))
pprint.pprint(dir(poskaship_pb2))
p = poskaship_pb2.Profile()
help(type(p))

print(f"\n client: ")
pprint.pprint(dir(client))

print(f"\n common: ")
pprint.pprint(dir(common))


print(f"\nDESCRIPTOR")
desc = poskaship_pb2.DESCRIPTOR
pprint.pprint(dir(desc))
for service_name, service in desc.services_by_name.items():
	print(f"Service: {service_name}")
	for method in service.methods:
		print(f"  Method: {method.name}")



poskaship_pb2.Profile(
	username="",
	password="",
	status=0,
)