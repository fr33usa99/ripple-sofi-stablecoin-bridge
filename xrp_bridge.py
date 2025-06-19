# Simulates sending XRP to another wallet (e.g., cross-border)
def send_xrp(destination, amount):
    print(f"Sent {amount:.2f} XRP to {destination}")
    return {"tx_id": "mock_tx_123abc", "destination": destination, "amount": amount}
