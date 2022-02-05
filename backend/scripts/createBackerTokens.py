import requests
from pathlib import Path
from metadata.backerToken_metadata import backer_token_template
from brownie import BackerToken,network
import json
import ipfshttpclient
from scripts.utility import get_account


def main():
    # start_project(10,1000,10000,20)
    print(f"folder URL: ipfs/ipfs/{upload_dir_to_ipfs()}/")

    acc = get_account()
    print("=== deploy contract ===")
    bt = BackerToken.deploy({"from": acc})
    print(bt.balanceOf(acc,0))
    print("=== start project ===")
    tx = bt.startProject(500,200,1)
    tx.wait(1)
    print("=== balance of token 1")
    print(bt.balanceOf(acc,1))
    print(bt.uri(0))
    print(bt.uri(1))
    print(bt.uri(2))

    # # mint_nfts(0,0)
    # upload_dir_to_ipfs()
    # pass
def start_project():
    # uint256 public shareOfRevenue; // not a float
    # address public projectAddress; // the address of the project
    # uint256 public transferFeeToCreator; // the % amount from selling the NFT
    # uint256 public transferFeeToOrg


    pass

def mint_nfts(amount,body):
    # TODO deploy_contract
    # TODO create collectables with linked URI
    body = backer_token_template
    body["percentage"] = 0.01
    body["value"] = 10
    body["transfer_fee_for_creator"] = 20
    body["transfer_fee"] = 0.02
    sizeType_enum = 0
    metadata_file_name = f"./metadata/{network.show_active()}/{sizeType_enum}.json"
    with open(metadata_file_name, "w") as file:
        json.dump(body,file)

    sizeType_enum = 1
    body["value"] = 30
    body["percentage"] = 0.04
    with open(metadata_file_name, "w") as file:
        json.dump(body,file)

    uri = upload_to_ipfs(f"./metadata/boly-fork")
    print(uri)
    # TODO specify group of NFT's
    # all_nfts = []
    # for _ in range(0,amount):
    #     all_nfts.append(1)


    pass

def upload_dir_to_ipfs():
    with ipfshttpclient.connect() as client:
        hash = client.add("./metadata/polygon-fork",recursive=True)
        print(hash)
        print(hash[-1]["Hash"])

def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        binary = fp.read()
        ipfs_url = "http://127.0.0.1:5001"
        end_point = "/api/v0/add"
        response = requests.post(ipfs_url + end_point, files={"file": binary})
        print(response)
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        ipfs_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(ipfs_uri)
        return ipfs_uri
