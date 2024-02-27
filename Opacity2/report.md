# Opacity2

Nmap found a couple of open ports<br>
```
22/tcp   open     ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp   open     http        Apache httpd 2.4.41 ((Ubuntu))
139/tcp  open     netbios-ssn Samba smbd 4.6.2
445/tcp  open     netbios-ssn Samba smbd 4.6.2
3546/tcp filtered unknown
```

This is what we got when we got to the port 80<br>
![port 80](./imgs/port80.png)<br>

I checked out the `smb` thing and it looks like we do not have any access.<br>
![smb](./imgs/smb.png)<br>
Most likely it wants us to do web exploitation.<br>
Using `ffuf` I found a page called cloud on the server.<br>
![cloud](./imgs/cloud.png)<br>
I played with it for a couple of minutes trying uploading different things and putting different payloads. I set up an nc listener and my main goal was to upload a reverse-shell to the server. Soon I realized that I can upload whatever I want to the server as soon as I put `>.png` at the end of the link. So I set `python http server` got a simple reverse-shell, uploaded it to the server and accessed in http://opacity2.thm/cloud/images/shell.php and got a reverse-shell.

```
741852963        (dataset) # keepass

sysadmin:Cl0udP4ss40p4city#8700
```
