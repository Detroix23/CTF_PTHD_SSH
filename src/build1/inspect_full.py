"""
Function to analyse the libraries.
"""

def descriptor_description(obj: object) -> None:
    try:
        for service_name, service in obj.services_by_name.items(): # pyright: ignore[reportAttributeAccessIssue]
            print(f"Service: {service_name}")
            for method in service.methods:
                print(f"  Method: {method.name}")
    except:
        print()
        print(f"(!) inspect_full.descriptor_description() Has no `services_by_name`. Inspecting it.")
        inspect(obj)
        print()

def inspect(
    obj: object, 
    exclude: list[str] = ["__builtins__", "_globals"]
) -> None :
    print(f"\n(?) inspect_full.inspect() Inspecting {obj}.")
    for name in dir(obj):
        if name in exclude:
            continue
        attribute = getattr(obj, name)
        print(f"{name}: {attribute} ({type(attribute)})")
        # If it's a ServiceDescriptor, print its methods
        if name == "DESCRIPTOR":
            descriptor_description(attribute)

