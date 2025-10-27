**Protocol Distribution:** 
 
Most of the internet packets in the network are IPv4 based, around 95.3%.

**Transmission Control Protocol (TCP)**:   
These packets are under the IPv4 based packets. 47.9% of the packets are TCP. It operates on the Transport Layer of the OSI model. It creates a connection between client and server using a three way handshake which ensures both client and server are receiving the data sent on the network. I have explained this handshake in detail later in this file. TCP ensures data is delivered in order, without loss or duplication. Packets that are lost are retransmitted.

**User Datagram Protocol:**  
These packets are also under the IPv4 based packets. 46.7% of the packets are UDP. It is used when speed is more important than reliability. Unlike TCP, it is connectionless, that is, there is no three way handshake in UDP. Instead, the data is sent directly to the destination. There are no acknowledgements or retransmissions, and thus, packets may be lost, making it unreliable. Its main use-case comes where we need more speed, since no connection needs to be established. These use-cases include video games, streaming etc.

**QUIC IETF:**  
These packets are under UDP in IPv4 based packets. They account for 44.2% of the network packets. It stands for Quick UDP Internet Connection (QUIC). The IETF stands for Internet Engineering Task Force. QUIC is a relatively recent transport protocol developed by Google and later standardized by IETF, the same organisation that defines TCP and HTTP standards. It’s designed to make web communication faster, more secure, and more efficient than traditional TCP \+ TLS. QUIC replaces both TCP and TLS layers and combines them into a single protocol over UDP. This ensures that encrypted communication starts immediately. 

**Transport Layer Security (TLS):**  
These packets are under TCP in IPv4 based packets. They account for 19.8% of the network packets. This is a security protocol used to encrypt and authenticate communication over networks. TLS is the successor to SSL (Secure Sockets Layer). TLS works between application and transport layer. It runs on top of TCP, so once the TCP connection is established, the TLS protocols act. It starts by sending a Client Hello (contains supported TLS versions, supported encryption methods). The server then sends a Server Hello (Chosen TLS version and encryption method along with the server’s TLS certificate). The client then checks if the certificate is valid. After this, both sides exchange cryptographic keys to create a shared secret. Once both sides confirm they are ready, all data is encrypted. Both use the shared secret to encrypt and decrypt data. Note that HTTPS \- HTTP over TLS.

**Address Resolution Protocol (ARP):**  
These packets come under IPv4 based packets. They account for 4.4% of the network packets. This protocol is used to map an IP address to a MAC address in a local network. RP essentially maintains a table of key–value pairs, where: the key is the IP address and the value is the MAC address.

**DNS Query Analysis:**

**DNS Query 1:**

* **Domain being queried:** shiningclearshinytreasure.neverssl.com  
* **DNS Server IP:** 49.205.72.130  
* **Response IP address:** 34.223.124.45  
* **Response Time:** 0.003897 seconds

**DNS Query 2:**

* **Domain being queried:** i.ytimg.com  
* **DNS Server IP:** 49.205.72.130  
* **Response IP address:** 74.125.200.119 (If you open the packet details you can see the final IP it returns)  
* **Response Time:** 0.004146 seconds

**DNS Query 3:**

* **Domain being queried:** fonts.googleapis.com  
* **DNS Server IP:** 49.205.72.130  
* **Response IP address:** 172.217.24.138  
* **Response Time:** 0.004778 seconds

**TCP Three-Way Handshake:**

* **SYN:** Stands for Synchronize. It is the first step in establishing a TCP connection. When you want to start a conversation with a server, your computer sends a packet with the SYN flag set to 1\.  
* **SYN-ACK:** Once the server receives the SYN from the client, it sends its own SYN, along with an ACK (Acknowledgment) for the SYN sent to it.   
* **ACK:** Once the client receives the SYN-ACK, it sends ACK to the server for the SYN sent to the client.  
* All the three processes mentioned above are what constitute the TCP three-way handshake.  
* It is required to establish a reliable connection between the client and the server.

**HTTP vs HTTPS in Packet:**

* Yes, I can see the actual HTTP requests/responses.  
* We cannot read the encrypted data on the HTTPS requests/responses.  
* This difference occurs due to the extra security provided by TLS or SSL. Anyone tapping into the network cannot read the HTTPS requests unless they have the decryption key, which is only possessed by the server.  
* If you see the bottom section of the http-plaintext.png file, you can clearly see the HTML data sent.   
* But if you see the bottom section of the https-encrypted.png file, you can see the “Encrypted Application Data”, which shows some sort of unreadable hexadecimal code.  
* This occurs due to the additional security of TLS which is applied to HTTPS requests, not HTTP requests.

