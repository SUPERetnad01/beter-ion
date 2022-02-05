from brownie import SimpleToken
from scripts.utility import get_account

sample_URI_example =  "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"

def main():
    deploy_and_create()

def deploy_and_create():
    print("=== get account ===")
    account = get_account()
    print("=== deploy contract ===")
    simple_collectable = SimpleToken.deploy({"from": account})
    print("=== create collectible ===")
    tx = simple_collectable.createCollectible(sample_URI_example, {"from": account})
    print("=== increase token id ===")
    token_id = simple_collectable.tokenCounter()
    tx.wait(1)
    print(token_id)