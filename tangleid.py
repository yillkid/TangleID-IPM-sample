import requests

def new_claim(node_url, message):
    r = requests.post(node_url, json = message)

    return r.text

def get_claim_info(node_url, txn_hash):
    r = requests.post(node_url, json = txn_hash)

    return r.text

def get_all_claims_in_channel(node_url, message):
    r = requests.post(node_url, json = message)

    return r.text
