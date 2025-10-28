**DHCP:**

* It stands for Dynamic Host Configuration Protocol.   
* When a new client boots up, it does not have its own IP address. This protocol helps every device on the network to get its own IP address.  
* To join the network, the newly booted client broadcasts a DHCP DISCOVER to find a DHCP server.   
* The server responds with a DHCP OFFER, suggesting an IP address to the client.  
* The client replies with a DHCP REQUEST, requesting that server for that particular IP.  
* The server confirms this by sending a DHCP ACK, officially leasing out that IP.  
* This process gives each client a unique IP automatically, eliminating the need for manual network configuration.   
* In the simulation, clientA and clientB each go through this handshake and receive IPs like 192.168.1.2 and 192.168.1.3. 

**DNS:**

* DNS stands for Domain Name System.  
* Once the clients have their IPs, they register their names in the DNS Server.  
* It maps domain names to their corresponding IP addresses.  
* When one client wants to communicate with the other, it sends out a DNS Query. The DNS Server returns the IP address associated with the requested domain.

**Ping:**

* This is also called the ICMP Echo test. ICMP stands for Internet Control Message Protocol.  
* After learning the IP of the destination, a client can test the connectivity by sending a ping to it.  
* Ping uses the ICMP protocol to send an Echo Request and wait for an Echo Reply.  
* If the client receives an Echo Reply, it means that the connection is properly established. It also measures the latency.  
* In this simulation, the ICMP messages (“PING” and “PONG”) are symbolic.