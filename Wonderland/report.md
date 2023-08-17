# Wonderland

First of all I added the *wonderland.thm* to `/etc/hosts` and I am going to use it instead of the IP. <br>
Here is what we got from **nmap** scan:
```nmap
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 8eeefb96cead70dd05a93b0db071b863 (RSA)
|   256 7a927944164f204350a9a847e2c2be84 (ECDSA)
|_  256 000b8044e63d4b6947922c55147e2ac9 (ED25519)
80/tcp open  http    Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Follow the white rabbit.
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
Let's look at the http server using web browser.<br>
![The web page](img/1.png)<br>
Let's download the image and look if there is anything interesting.