# Simulates a SoFi wallet holding USDC balances
wallet = {
    "address": "sofi_user_001",
    "usdc_balance": 500.00
}

def get_usdc_balance():
    return wallet["usdc_balance"]

def convert_usdc_to_xrp(amount):
    if amount > wallet["usdc_balance"]:
        raise ValueError("Insufficient USDC balance")
    wallet["usdc_balance"] -= amount
    print(f"Converted ${amount} USDC to XRP")
    return amount * 1.8  # mock rate
