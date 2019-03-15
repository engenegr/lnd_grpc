from lnd_grpc import lnd_grpc
import grpc

from lnd_grpc import utilities as u
from lnd_grpc.protos import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc


class AsyncClient(lnd_grpc.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def get_info(self):
        response = await self.lightning_stub.GetInfo(ln.GetInfoRequest())
        return response

    async def wallet_balance(self):
        response = await self.lightning_stub.WalletBalance(ln.WalletBalanceRequest())
        return response
