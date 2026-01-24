
import poskaship_pb2
import grpc
import client

def descriptor_description(obj):
    for service_name, service in obj.services_by_name.items():
        print(f"Service: {service_name}")
        for method in service.methods:
            print(f"  Method: {method.name}")

def inspect(obj: object, exclude: list[str] = ["__builtins__", "_globals"]):
    print(f"--- Inspecting {obj} ---")
    for name in dir(obj):
        if name in exclude:
            continue
        attribute = getattr(obj, name)
        print(f"{name}: {attribute} ({type(attribute)})")
        # If it's a ServiceDescriptor, print its methods
        if name == "DESCRIPTOR":
            descriptor_description(attribute)



inspect(poskaship_pb2)
