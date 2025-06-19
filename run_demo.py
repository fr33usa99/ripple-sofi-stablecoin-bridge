from usdc_mock import get_usdc_balance, convert_usdc_to_xrp
from xrp_bridge import send_xrp
from dex_swap_mock import swap_xrp_to_eurc
from compliance_logger import log_transaction

def main():
    print("=== Ripple–SoFi Stablecoin Bridge Demo ===")

    usdc_amount = 100
    print(f"SoFi Wallet USDC Balance: ${get_usdc_balance()}")

    xrp = convert_usdc_to_xrp(usdc_amount)
    tx = send_xrp("recipient_eurc_wallet", xrp)
    eurc = swap_xrp_to_eurc(xrp)

    log_transaction({
        "from": "sofi_user_001",
        "to": tx["destination"],
        "usdc_sent": usdc_amount,
        "xrp_sent": xrp,
        "eurc_received": eurc,
        "tx_id": tx["tx_id"]
    })

    print(f"Bridge complete: Received {eurc:.2f} EURC.")

if __name__ == "__main__":
    main()
