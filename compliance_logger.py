# Logs the transaction details for compliance
import json

def log_transaction(data):
    with open("compliance_log.json", "a") as log_file:
        json.dump(data, log_file)
        log_file.write("\n")
    print("Compliance log updated.")
