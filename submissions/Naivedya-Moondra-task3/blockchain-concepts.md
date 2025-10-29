**Local vs Real Blockchain:**

**What are 3 differences between Hardhat local network and Ethereum mainnet?:**

* Hardhat local network is used for local development and testing whereas Ethereum mainnet is a real public network for live deployments.  
* In a local blockchain, fake ETH (Ether) is used whereas in the Ethereum mainnet, real ETH is used to pay gas fees.  
* Local blockchains are also very fast, whereas Ethereum mainnet is slower due to real mining and validation time.

**Why do we develop locally first?:**

* To test and debug smart contracts before sending them to the Ethereum mainnet and spending real ETH.  
* To simulate blockchain behaviour (transactions, gas etc) immediately.

**What would change if you deployed this same contract to real Ethereum?:**

* You would need real ETH in your wallet to pay the gas fees.  
* The deployment will be public, and permanent on the blockchain.  
* You cannot easily modify the contract once it is deployed.


**Smart Contract Basics:**

**In your own words, what is a smart contract?:**

* A smart contract is a piece of code that is stored on the blockchain and runs when certain conditions are met.   
* It is like a digital agreement and does not  need a middleman (for example \- a court of law).  
* The code is written in an if-then-else format, which run when their condition is met.

**Once deployed, can you edit the contract code? Why or why not?:**

* Once deployed, you cannot edit the contract code due to the immutability of any data on the blockchain.  
* This is what makes smart contracts trustworthy and reliable. It guarantees that the agreement that was made between the two parties is fulfilled. There is no scope of fraud from either party, the code that is written must be followed.

**If you restart your Hardhat node, what happens to your deployed contract?:**

* Once you restart the hardhat node, it will disappear.  
* This is because Hardhat local blockchain is stored in memory.   
* This means that restarting your Hardhat node will wipe all previous blocks, accounts and contracts.

**How is a smart contract different from a regular program/website?:**

* The main difference is that a smart contract runs on a blockchain whereas a regular program/website runs on centralized servers.  
* This makes smart contracts immutable, whereas in regular programs/websites, code can be changed at any time.  
* A smart contract is verified by multiple network nodes, whereas regular programs/websites are controlled by a single owner.  
* A smart contract executes automatically when its conditions are satisfied, whereas regular programs/websites execute their code only when triggered by the server.

**Blockchain & Our VPN Project:**

**Why would a VPN project use blockchain?:**

* The issue with a conventional VPN (Virtual Private Network)  is that even though our ISP cannot see what our internet activity is, the VPN servers can still track our DNS requests.  
* This means that the organization providing the VPN services can actually see our internet traffic and can sell it to others with harmful intentions.  
* Therefore, conventional VPNs are based on trust, that is, you trust the VPN provider more than your ISP.  
* This is where blockchains are helpful. They shift the conventional VPN infrastructure from a single company to a peer-to-peer network of independent nodes. This architecture is called a dVPN (Decentralized VPN).  
* This peer-to-peer network ensures not all your network data is at one company’s servers, thus protecting your data better. We can say that in such a VPN trust is distributed (among the many nodes).

**What advantages does blockchain provide over a central database?:**

* Transparency: Everyone has a copy of the records, thus anyone can verify the records.  
* Security: Data cannot be changed easily.  
* No single point of failure: Even if one node goes down, the other nodes will still have the list of transactions and thus the network stays up.

**Disadvantages or challenges:**

* It requires gas fees for every transaction.  
* It is way slower than a centralized database.  
* Once it is deployed, it is really hard to update.  
* The setup is not very beginner friendly, there is a steep learning curve.

**Two examples of what our VPN project might store on blockchain:**

* Node registration information: When a user joins the VPN network.  
* Payment records: How much data a user has consumed and how much ETH they owe or how much they have earned.

**Key Terms:**

* **Blockchain:** It is basically a distributed ledger containing some sort of information (may be transactions) across several computers. One of its properties is that data on a blockchain is immutable, that is, it cannot be modified once it is put on the blockchain.  
* **Smart Contract:** It is some code written on the blockchain (for example, Solidity code) that runs automatically once its given set of conditions are satisfied, without the need of a middleman.  
* **Gas:** It refers to the fees paid in ETH (ether) to execute transactions or run smart contracts on the blockchain.  
* **Wallet Address:** A unique and public address or identifier used to send and receive cryptocurrency. Kind of like a phone number, but instead of sending crypto we are sending a phone call.  
* **Private Key:** A secret key that proves ownership of a crypto wallet. Kind of like a password, but much stronger.  
* **Transaction:** Record of an action (such as spending ETH) on the blockchain is called a transaction.  
* **Deployment:** The process of uploading and activating a smart contract on a blockchain network is called deployment. It can happen on a local network or on the mainnet.

