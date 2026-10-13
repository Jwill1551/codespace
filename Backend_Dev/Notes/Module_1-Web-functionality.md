# Module 1 - How the web Actually Works
---
## The Request Lifecycle
Its important to understand how something works, beyond just the code written for it.

The following entails the request lifecycle:
* DNS
* TCP + TLS
* HTTP request
* Server
* Handler 
* HTTP response

### DNS 
**The Domain Name System (DNS)** is the phonebook of the internet. DNS translates domain names to IP addresses so browsers can load internet resources. 

Each device connected to the internet has a unique IP address wihch other machines use to find the device.

For example, "www.example.com" would converted into a more understandable IP address like "192.168.1.1".

### TCP + TLS
**TCP (Transmission Control Protocol)** is a protocol that allows devices to commnuicate reliably over a network. It ensures that data reaches the destination correctly and in the right order, even if parts of the network are slow or unreliable.
* It works at the Transport Layer (Layer 4) of the OSI model.
* TCP establishes a logical connection between the sender and receiver before data transmission begins. 
* Detects errors using checksums and restransmits lost or corrupted packets to maintain data integrity. 
* It controls the data transmission rate to avoid overwhelming the reeiver and adapts to network congestion for efficient communication.
* Note: TCP is connection-orientated, meaning a connection must be established before any data is sent.

**Transport Layer Security (TLS)** is a cryptogrpahic protocol designed to provide security at the transport layer. It was derived from a security protocol called **Secure Socket Layer (SSL)**. TLS ensures that no third party can eavesdrop on or tamper with any message transmitted between a client and a server.
* Note: Since TLS/SSL operates beneath the application layer, most of its processes are completely invisible to the client.

#### Handshake Protocol
SSL/TLS works through a process called a handshake, which stablishes a secure and encrypted connection between a client and a severs over TCP. 
* Phase 1: Establish Connection
    * First the client initaites the connection by sending supported SSL/TLS version, list of cipher suites and compression methods. And then the Server checks the highest compatible SSL/TLS version and selects a suitable cipher suite and compression method from the client's list.
* Phase 2: Server Authentication
    * Sever sends certificate Server request client's certificate Server Key Exchange.
* Phase 3: Client Authentication
    * Client sends certificate Client Key Exchange.
* Phase 4: Handshake Ends
    * Change Cipher Spec Handshake Finished.

## HTTP request

## Server

## Handler

## HTTP Response