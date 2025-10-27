// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

contract HelloVPN {
    //State Variables
    string private greeting;
    uint256 private nodeCount;
    address private deployer;

    //Constructor used to set the deployer's message
    constructor() {
        deployer=msg.sender;
    }

    //Set a new greeting
    function setGreeting(string memory _greeting) public {
        greeting=_greeting;
    }

    //Getting the current greeting
    function getGreeting() public view returns (string memory) {
        return greeting;
    }

    //Set the VPN Node Count
    function setNodeCount(uint256 _count) public {
        nodeCount=_count;
    }

    //Get the VPN Node Count
    function getNodeCount() public view returns (uint256) {
        return nodeCount;
    }

    //Get the deployer's address
    function getDeployerAddress() public view returns (address) {
        return deployer;
    }
}
