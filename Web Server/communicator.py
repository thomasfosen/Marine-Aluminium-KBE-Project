import asyncio
import websockets
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', metavar='Command', type=str)
parser.add_argument('-f', metavar='Force', type=float, const=None, default=None)
parser.add_argument('-t', metavar='Torque', type=float, const=None, default = None)

args = parser.parse_args()
cmd = args.c
force = args.f
torque = args.t


print(torque, force, cmd)

"""
async def message():
	async with websockets.connect("ws://localhost:1234") as socket:

		if cmd == 'stop':
			await socket.send(cmd)

		elif cmd == 'load':
			await socket.send(cmd + ' ' + name + ' ' + target)

		elif cmd == 'delete':
			await socket.send(cmd + ' ' + name)

		elif cmd == 'refresh':
			await socket.send(cmd)

		elif cmd == 'optimize':
"""


#asyncio.get_event_loop().run_until_complete(message())


# The process needs to be launched from a seperate process thread. Doing this inside a flask application wasn't as straight forward as initially thought..
# When initation a secondary thread for this server command inside FLASK, NXOpen doesn't run certain codes for an unknown reason
# os.system("start /B start cmd.exe @cmd /k refresh.bat")
