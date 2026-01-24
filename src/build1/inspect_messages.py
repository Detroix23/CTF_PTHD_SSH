
import sys
import os
import poskaship_pb2

# Add current directory to path
sys.path.append(os.getcwd())

print("--- Inspecting Message Types ---")
messages = [
    'EmptyRequest', 'EmptyResponse', 'Exception', 'GetFlagResponse',
    'Profile', 'Response', 'ResponseSuccess', 'Session'
]

for msg_name in messages:
    if hasattr(poskaship_pb2, msg_name):
        msg_class = getattr(poskaship_pb2, msg_name)
        print(f"\nMessage: {msg_name}")
        for field in msg_class.DESCRIPTOR.fields:
            print(f"  Field: {field.name} (Type: {field.type})")
