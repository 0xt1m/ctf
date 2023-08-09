# Brooklyn Nine Nine

<i>Target IP: 10.10.213.175</i>

<i>nmap scan</i><br>
<code>PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.2.38.40
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0             119 May 17  2020 note_to_jake.txt
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 167f2ffe0fba98777d6d3eb62572c6a3 (RSA)
|   256 2e3b61594bc429b5e858396f6fe99bee (ECDSA)
|_  256 ab162e79203c9b0a019c8c4426015804 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel</code>
<p>Generally we have FTP, SSH, Apache</p><br>
<p>Looks like we can connect to ftp with anonymous. and there is a file that we can read.</p>
<img src="https://i.ibb.co/LYfWk62/1.png" alt="1" border="0">
<p>From the note we know that jack's password is weak, but hydra and rockyou can't help us with it. <img src="https://i.ibb.co/wKMZ987/2.png" alt="2" border="0"></p>

