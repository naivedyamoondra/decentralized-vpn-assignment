**Part-A:**  
I will be using Firefox’s devtools for this part.

1. **HTTP vs HTTPS comparison:**  
* The HTTP and HTTPS request headers are structurally the same. The only difference is that HTTPS requests get encrypted when it reaches the Transport Layer (called TLS or Transport Layer Security) whereas HTTP is sent directly to the TCP, without any encryption.   
* We can see the actual data in HTTP requests because it is not encrypted. Anyone monitoring the network can receive the data packets and see the data with no need to decrypt it. This does not happen with HTTPS because anyone intercepting the data would need the decryption key to read the encrypted packets transmitted over the network.  
* HTTP and HTTPS function similarly at the Application Layer. However, before HTTPS data is sent over the Transport Layer, it passes through the TLS (Transport Layer Security) protocol — formerly known as SSL (Secure Sockets Layer) — which encrypts the data. TLS sits between the Application and Transport Layers in the network stack, where it prevents eavesdropping through encryption and ensures authenticity using digital certificates.  
    
2. **Request Analysis, 3\. Performance Insights:**  
* [http://neverssl.com](http://neverssl.com)  
  * Requests: 2  
  * Resources loaded: HTML and images  
  * Load time: 925 ms  
* [https://youtube.com](https://youtube.com)  
  * Initial requests: 20 (increases dynamically as you scroll)  
  * Resources loaded: HTML, CSS, JavaScript, images (thumbnails), XHR requests  
  * Initial load time: 5.70 seconds  
  * Note: Load time is not static — scrolling and dynamic content (videos, thumbnails, recommendations) will increase total requests and load time.  
* [https://github.com](https://github.com)  
  * Initial requests: 205 (also increases dynamically with scrolling and interactions)  
  * Resources loaded: HTML, CSS, JavaScript, images, media, fonts, XHR requests  
  * Load time: 15.77 seconds  
  * Note: Load time varies as dynamic data, fonts, and API calls continue loading in the background.

* The longest request in [neverssl.com](http://neverssl.com) was loading the favicon of the site, which took longer than the other request due to its larger size.  
* The longest requests observed on analysing YouTube and GitHub were those returning HTTP status codes 403 (Forbidden) and 204 (No Content). Status 403 refers to when the request was valid, but the server rejects it due to various reasons such as bot protection, permissions etc. Status 204 happens when the request is valid, but there is no content for the server to send back.This shows that long request times do not always indicate large file sizes, but can also result from server response delays or denied access.Even though they do not return visible content, they still undergo DNS resolution, TCP/TLS handshake, and server-side processing, which contributes to their longer duration.

* DNS Lookup: Refers to the time taken to resolve domain name, i.e, the time taken for the DNS request to get an answer. In the case I have taken, the DNS lookup is 70ms (DNS Resolution).  
* Connection Time: It is the time taken to establish a TCP (and optionally TLS) connection. It includes the time taken to establish the TCP handshake (SYN, SYN-ACK, ACK) and the TLS handshake. Note that the Connection Time for HTTP packets is lesser than the Connection Time for HTTPS packets because HTTP doesn’t have to establish the TLS connection. In the case I have taken, the Connection Time is 39+76=115ms (Connecting \+TLS Setup).  
* Waiting (TTFB-Time To First Byte): It is the time measured from when the browser sends its first request to when it receives the first byte of the response-after the connection is established. Note that some sources include DNS lookup and connection time in the TTFB, but browser DevTools measure TTFB only after the connection is established. In the example I have taken, the Waiting or the TTFB is 61ms.