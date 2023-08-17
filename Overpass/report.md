# Overpass

**Target IP:** `10.10.17.200` <br>
From `nmap` results we have to open ports:<br>
`22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)`<br>
`80/tcp open  http    Golang net/http server (Go-IPFS json-rpc or InfluxDB API)`<br>
Let's look at the http server.
![http server](https://i.ibb.co/1vqCb4N/2.png)