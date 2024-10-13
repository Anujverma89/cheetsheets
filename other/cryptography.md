# Information Security 

* **Defination:**   
    Security of information from :  
    * Unauthorized access
    * Misuse 
    * Manipulation 

* **Cryptography :**  
    Cryptography is a methamatical technique mechanism to achieve information security or to protect information.  
    * **Goals of Computer Security**  
        * Confidentiality : We use Cryptography, Access control, masking
        * Data Integirity : We use hashfunctions, checksum , Digital signatures 
        * Authentication : Password, 2FA, MFA, biomatrics 
        * Non Repudiation  : Digital signatures 
        * Access control : 
        * Availability : 
    **How ?** 
    * Authenticate 
    * Validate 
    * Authorize  
    * Hashing 
    * Algorithms 
    * Signatures 

### **MAIN CONTENTS** 
* Cryptography(Encryptoin/Decryption) :
    * Ciphers : (stream & block)
        * Stream cipher : One block is encrypted at a time;
        * Block cipher : one block is encrypted and decrypted at a time;(DES,AES)
        * Substution Techniques cipher : 
            * ceaser cipher
            * Mono aplhabetic cipher
            * Homophonic alphabetic cipher
            * Polygram alphabetic cipher
            * Polyalphabetic ceaser cipher
            * playfair chipher
            * Hill Cipher
        * Transpostion Cipher : 
            * Rail Fence Cipher
            * Simple columnar transpostion technique 
            * Vernam Cipher (one time pad)
        * Book cipher / Running key cipher
        * Steganography 

        * Plain text -> encryption -> Cipher text
        * Cipher text -> decryption -> plain text 

        * Symmetric key cryptography : Same key for encryption & Decryption 
            * stream cipher : RC4, Salsa20, ChaCha20
            * Block cipher : AES, DES, 3DES, Blowfish

        * Assymnetric key cryptography : Different keys for encryption & decryption
            * RSA,DSA,Diffie helman algorithm(Key exchange), ElGamal, ECC(Eleptic curve cryptography) 

* Hashing (cryptographic hash functions)
    * MD5, sha1, sha2(SHA-256, SHA-384, SHA-512), sha3(Keccak), MD6
    * here 224, 256, 382, 512 are bit values.

* Digital Signatures (MAC) : 
    * RSA : 
    * DSA : Digital Signature Algorithm 
    * ECDSA (Elliptic Curve DSA)
    * ElGamal Digital Signature Algorithm


* KDC/CA (Key distributin center/ Certificate authority)





* **Terms Used :**  
  * Cipher text
  * Encryption
  * Decryption 
  * Plain Text 
  * Fiestal 
  * DES(Data Encryption Algorithm)
  * AES(Advanced Encryption Algorithm)
  * Public key cryptography 
  * Diffie Hellman algorithm
  * Symmetric key cryptography 
  * RSA(Rivest, Shamir, and Adleman)
  * ElGamal

* **Security Premitives(Tools for Cryptography)**
    * Encryption techninqiues 
    * Digital Signatures 
    * Hash functions
        * Unkeyed primitives
        * Symmetric key primitives 
        * Public key primitives 


* **Functions** 
    * Image f:x -> Y (with rule)
    * Preimage : if y is the image i.e Y = f(x) then x is preimge of Y such that x belongs to X
    * Image of functino im(f)
    * One to one 
    * Inverse of function


* **Types of Attacks** 
    * Active 
        * DDOS & DOS : Denial of service attack and Distributed Dos.
        * Spoofing : to pretend or immitate as something
        * MITM
        * Ransomware
        * Phishing 
        * SQL Injection 
        * URL interpretation
        * Session hijacking 
        * DNS Spoofing 
        * Brute force attack 
        * Trojan horse 
        * XSS attacks (Cross-Site Scripting)
        * Birthday attack
        * Insider threat 
        * Web attacks (XSS, CSRF)
        * CSRF : Cross site request frogery 
    * Passive 
        * sniffing : To interpret something
        * Eavesdropping attack
   

* We can also enable MFA (Multie Factor Authentication) to stop penetration in a system.
* Least Prevelive 


* Mechanims to ensure Security in the web : 
    * Cryptography (Encryption & decryption)
    * Hashing : Plan text into hased code 
    * MAC : Message authentication code 
    * Key sharing algorithms : Symmetric and Assymetric distribution 
    * Keys : Public & Private keys 
    * AES : Advanced Encryption standard 
    * DES : Data Encryption Standard  

* IPsec is used in IP layer for secure transmission.(Transport Mode, Tunnel Mode) 
* TLS, SSL is used in transport layer for security 
* PGP, HTTPS, S/MIME, SSH are application layer secure protocol 
* MACsec (media acccess control security ) is used in mac layer
    

* AES & DES
```
    AES : 
        Block size : 128 bits
        Key size : 128, 192, 256 
        rounds : 10, 12, 14
        Used in : IPsec, SSL, TLS etc
    DES : 
        BLock size : 64 bits(56 bits key, 8 bits parity)
        Key length : 64 bits
        Rounds : 16
        Valnuerable to brute force attack 
        Advanced version of DES : , 3DES, AES.
    3DES : 
        Block size : 64 bits 
        Key size : 2 keys 56 bits = 112 bits or 3 Keys 56 bits = 168 bits
        In 2 key 3DES : 2 distinct keys k1 is used in step 1st and 3rd for encryption and k2 is used in step second for decryption.
        In 3 key 3DES : all three keys are distinct.

    RSA : 
        248 bit key size 
        Assymetric key algorithm
```


* Cipher texts are generated from plain test using Encryption algorithms.


* TLS : 
```
    Uses AES for Symmetric encryption
    ECDHE for key exchange with forward secrecy 
    SHA-256 for hashing.
```

### Key Exchange Algorithms
* RSA (Rivest-Shamir-Adleman):
* Diffie-Hellman (DH):
    * Ephemeral Diffie-Hellman (DHE):
    * Elliptic-Curve Diffie-Hellman (ECDH):
    * Elliptic-Curve Diffie-Hellman Ephemeral (ECDHE):

### Symmetric Encryption Algorithms
* AES 
* 3DES 
* ChaCha20-Poly1305

### Hashing Algorithms
* md5
* SHA-1 
* SHA-2


### Digital Signature Algorithms
* RSA : 
* DSA : Digital Signature Algorithm 
* ECDSA (Elliptic Curve DSA)



### Kerberos 
```
    Name after three headed hades guard or hell guard know as cerberos or Kerberos 
    Authentication protocol on the internet : 
    AAA : Authentication , Authorization, Accounting. 

    Three main components  :
        Client
        Server 
        KDC 

```


### Security Models : 
* No security 
* Host security 
* Security through Obsecurity 
* Network Security 


### Virus : 
    * Viruses try to harm computer by replicating themself or attching themselves to a file. 
    types: 
        * Parastic : attaches itself with other programme 
        * Polymorphic : Can change its architecture and difficult to identity
        * Stealth : Intelligence virus difficult to detect.
        * Boot sector : stays in MBR sector of computer
        * Meta Morphic : It keeps rewriting itself along with chaning its signature.
        * Memory Resident Virus : attaches itself to ram 

### Worm : 
    * Worm tries to make system unusable by replicating itself again and again thus consuming all the avialable resources.