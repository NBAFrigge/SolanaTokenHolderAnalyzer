import requests
import os
from dotenv import load_dotenv

load_dotenv()

RPCURL = os.getenv("RpcUrl")


def getTokenLargest(address):
    data = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getTokenLargestAccounts",
        "params": [
            address,
        ],
    }

    response = requests.post(RPCURL, json=data).json()
    if "error" in response:
        print(response["error"])
        return []
    return response["result"]['value']

def CheckAccount(address):
    data = {
        'jsonrpc': '2.0',
        'id': 1,
        'method': 'getAccountInfo',
        'params': [
            address,
            {
                'encoding': 'jsonParsed'
            }
        ],
    }
    response = requests.post(RPCURL, json=data).json()
    return response["result"]['value']

def WalletStats(address):
    response = requests.get(f"https://gmgn.ai/defi/quotation/v1/smartmoney/sol/walletNew/{address}?period=7d")
    return response.json()

if __name__ == "__main__":
    while True:
        address = input("Token Address: ")
        if len(address) == 44:
            break
        else:
            print("Invalid address")
    
    wallets = getTokenLargest(address)
    if len(wallets) == 0:
        print("Address not found")

    print(f"Analyzing {len(wallets)} wallets")
    print("============================================================")
    for w in wallets:
        wallet_info = CheckAccount(w['address'])['data']['parsed']['info']
        Ws = WalletStats(wallet_info['owner'])['data']
        if Ws['pnl'] == 0:
            continue
        print(f"Address: {wallet_info['owner']}")
        print(f"SOL balace: {Ws['sol_balance']}")
        print(f"pnl: {round(Ws['total_profit_pnl']*100, 2)}%")
        print(f"7d pnl: {round(Ws['pnl_7d']*100, 2)}%")
        if Ws['winrate'] == None:
            print(f"win rate: N/A")
        else:
            print(f"win rate: {round(Ws['winrate']*100, 2)}%")
        print(f"buy count: {Ws['buy']}")
        print(f"sell count: {Ws['sell']}")
        print(f"============================================================")




            
        
    
