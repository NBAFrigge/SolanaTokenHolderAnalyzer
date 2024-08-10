# Token Holder Analysis Script

This is a simple Python script that analyzes the top 20 holders of a given Solana token using the `gmgn.ai` API. By providing the mint address of a token, the script retrieves and displays key statistics about the wallets that hold the largest amounts of the token.

## Features

- **Wallet Analysis**: Fetches and analyzes the top 20 wallets holding the specified token, providing details such as SOL balance, profit and loss (PnL), 7-day PnL, win rate, and the number of buy/sell transactions.

## Setup

### Prerequisites

All required Python libraries are listed in the `requirements.txt` file. You can install them using pip:

```bash
pip install -r requirements.txt
```

Create a .env file in the project directory with the following content:

```bash
RpcUrl=<YOUR_SOLANA_RPC_URL>
```

Replace <YOUR_SOLANA_RPC_URL> with the actual RPC URL you want to use.

## Usage
Run the script:

```
python script.py
Enter the mint address of the token when prompted.
The script will analyze the top 20 wallets holding the token and display the results.
```

### Example Output

```
Token Address: <Your_Token_Address>
Analyzing 20 wallets
============================================================
Address: <Wallet_Address_1>
SOL balance: 10.5
PnL: 15.32%
7d PnL: 2.15%
Win rate: 65.00%
Buy count: 12
Sell count: 8
============================================================
```

## License
This project is licensed under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.