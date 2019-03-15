import asyncio

from lnd_grpc.async_client.async_lnd_grpc import AsyncClient

lncli1 = AsyncClient(lnd_dir='/Users/will/regtest/.lnd/', network='regtest', grpc_host='127.0.0.1',
                     grpc_port='10009',
                     macaroon_path='/Users/will/regtest/.lnd/data/chain/bitcoin/regtest/admin.macaroon')


async def wallet_balance():
    print('Getting Wallet Balance...')
    while True:
        balance = await lncli1.wallet_balance()
        print(balance)
        await asyncio.sleep(5)


async def get_info():
    while True:
        info = await lncli1.get_info()
        print(info)
        await asyncio.sleep(5)


async def run():
    coros = [wallet_balance(), get_info()]
    await asyncio.gather(*coros)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
