**1\. Your Contract Code:**  
```
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
    function setGreeting(string memory \_greeting) public {  
        greeting=\_greeting;  
    }

    //Getting the current greeting  
    function getGreeting() public view returns (string memory) {  
        return greeting;  
    }

    //Set the VPN Node Count  
    function setNodeCount(uint256 \_count) public {  
        nodeCount=\_count;  
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
```

**2\. Solidity Basics**

**What is a constructor and when does it run?**

* A constructor is a special function that runs only once when the contract is first deployed to the blockchain.  
* It is used to initialize values, just like class constructors in any programming language.  
* You do not have to call it, it executes automatically when the contract is deployed.  
* The constructor in the code of HelloVPN.sol initialises the value of the deployer’s address to the variable deployer.

**Explain these keywords in your own words:**

* public: It means that anyone can access or call the function or variable, regardless of them being inside or outside the contract.  
* private: It means that the only way to access it is through public getter functions. The function or variable is only accessible within this contract and other contracts or users cannot directly use them.  
* view: A view function only reads data from the blockchain, it does not modify it. It does not use gas if it is called externally, meaning that it doesn’t cost any money to call.  
* memory: This means that the data is stored temporarily till the function it is declared in is running. It is used mainly for function inputs.

**What is msg.sender and what information does it give you?:**

* msg.sender is a global variable in Solidity that gives the address of the person who called the function.   
* Since in my code, I have put deployer=msg.sender in my constructor, it stores my address in the deployer variable.  
* If another user calls msg.sender in another function, it will return the address of the other user.

**Why do we declare variable types like string and uint256?**

* We have to declare variable types in Solidity since it is a statically typed language.   
* This helps the compiler know how much memory to reserve, prevent type errors and optimize gas usage.  
* In my code, I have declared deployer as address type, greeting as string type and nodeCount as uint256 (unsigned integer).

**3\. Understanding State:**

**What is a "state variable" in a smart contract?:**

* It is a variable that stores data on the blockchain permanently.  
* This means that it remembers its value even after the function stops running.  
* It is used to describe the current state of the contract.  
* When you update a state variable, that change is written to the blockchain and becomes part of the network’s permanent history  
* In my code, the variables greeting, nodeCount and deployer are the state variables.

**Where are state variables stored?:**

* State variables are stored in a special area of the blockchain called the contract storage (or persistent storage).  
* Each smart contract has its own storage space, linked to its own blockchain address.  
* This storage is replicated across all nodes on the Ethereum network, meaning every node on the network keeps a copy of your contract’s data.

**What happens to state variables when you restart your computer?:**

* They stay exactly the same, since the values are stored on the blockchain, not on the local device.  
* Restarting the computer or switching devices does not affect blockchain data.

