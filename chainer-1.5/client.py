import msgpackrpc, sys

client = msgpackrpc.Client(msgpackrpc.Address("localhost", 5000), pack_encoding='utf-8', unpack_encoding='utf-8')
for line in sys.stdin:
  result = client.call('dqn', ' '.join(line))
  print(result)
