//// SPDX-License-Identifier: MIT
//
pragma solidity ^0.8.11;

import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
//
contract BackerToken is ERC1155 {

    // dynamic
    enum BackingType {
        SMALL,
        MIDDLE,
        LARGE
    }
    string base_ipfs_uri = "https://ipfs.io/ipfs/Qmb8UbwYBk8ZY1UfNK3SrfXX6Ezkw2gPyqnGnehcuQBMCi/";
    mapping (uint256 => string) private _uris; //token id to uri

    constructor() public ERC1155("https://ipfs.io/ipfs/QmZ5RnZdHqha4P4FubWaxZSz9yjz8LH3cKaRrCk7xDEAEa/{id}.json") {

    }
    // content creator only
    function startProject(uint256 smallAmount, uint256 mediumAmount, uint256 largeAmount) public
    {
        // TODO decrease uint size
        _mint(msg.sender,uint256(BackingType.SMALL),smallAmount,"");
        _mint(msg.sender,uint256(BackingType.MIDDLE),mediumAmount,"");
        _mint(msg.sender,uint256(BackingType.LARGE),largeAmount,"");

        // mint all tokens that we need to mint for given creator
        // set data from given tokens
    }
    // buy tokens for given creator
    function uri(uint256 tokenId) override public view returns (string memory) {
        return(
            string(abi.encodePacked(base_ipfs_uri,
            Strings.toString(tokenId),
            ".json")));
    }

    // TODO ownable
    function setTokenUri(uint256 tokenId, string memory uri) public {
        require(bytes(_uris[tokenId]).length == 0, "Cannot set uri twice");
        _uris[tokenId] = uri;
    }
}