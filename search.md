# Hostile Secured Session.

This is a CTF.
We have to analyze the code, and find a way to collect a flag from the server.

## Searching the modules.
Using:
	- `help(module)`, 
	- `dir(module)`,
	- `inspect.getmembers()`,
	- `strings <binary>`,
	- Search `DESCRIPTOR`s
	```python
	desc = poskaship_pb2.DESCRIPTOR
	for service_name, service in desc.services_by_name.items():
		print(f"(?) service: {service_name}")
		for method in service.methods:
			print(f"\t- Method: {method.name}")
	```

### Poskahip.
By doing:
```python
import poskaship_pb2
print(f"\n poskaship_pb2: ")
pprint.pprint(help(poskaship_pb2))
```

We find in `DATA`:
```python
ADMIN = 2
GUEST = 0
REGULAR = 1
```

Also, there is:
```python
poskaship_pb2.GetFlagResponse()


poskaship_pb2.Profile(
	username="",
	password="",
	status=0,
)
```

By analyzing services (because method are handled dynamically (with `__getattr__`) (of course)):
```
Service: PoskaShip
  Method: Register
  Method: Login
  Method: GetFlag
  Method: Me
  Method: Sessions

Message: EmptyRequest

Message: EmptyResponse

Message: Exception
  Field: module (Type: 9)
  Field: classname (Type: 9)
  Field: message (Type: 9)

Message: GetFlagResponse
  Field: flag (Type: 9)

Message: Profile
  Field: status (Type: 14)
  Field: username (Type: 9)
  Field: password (Type: 9)

Message: Response
  Field: success (Type: 11)
  Field: exception (Type: 11)

Message: ResponseSuccess
  Field: profile (Type: 11)
  Field: session (Type: 11)
  Field: flag (Type: 9)

Message: Session
  Field: session_id (Type: 9)
  Field: username (Type: 9)   
```

We can Login:
```python
stub.Register(account)
stub.Login(account)
```

With an admin client, we get:
```python
flag = stub.getFlag()
```
