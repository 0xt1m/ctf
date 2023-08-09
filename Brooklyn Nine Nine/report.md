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
<p>Don't forget about the apache server. So if we go there it looks like this: <img src="https://i.ibb.co/dp91ZpN/4.png" alt="4" border="0"> And we can see that there is a comment about stenography. We can download the image and look what we can do with it <img src="brooklyn99.jpg" alt=""></p>
<p>I tried to use steghide to extract the contents of the image, but it wants a password.</p>
<p>I used <b>stegcracker</b> to crack the password and it turned out that the password was admin. Let's look at the contents. <img src="https://i.ibb.co/PQqQSfT/5.png" alt="5" border="0"></p>
<p>We have something that looks like a password.</p>
<code>Holts Password:
fluffydog12@ninenine

Enjoy!!</code>
<p>Let's check where we can login with the password.</p>

<p>
	<b>Known users:</b>
	<ul>
		<li>amy</li>
		<li>jack</li>
	</ul>
	And we can suppose that trere is a user <b>holt</b>
</p>
<p>Here we go. We can make ssh connection to the use holt with the password that we have got before. And now we have got the first flag.</p>

# Privilege Escalation
<p>Besides the file <b>user.txt</b> we have the file named <b>nano.save</b></p>
<p>Using <code>sudo -l</code> We found that we can use nano as sudo without password.</p>
<p>Having the possibility to use nano with sudo privileges open a lot of ways for us to get the root privileges. I am going to change the <code>/etc/passwd</code> file. I will add a new root user there with my own password.</p>
<b>WVLY0mgH0RtUI = mrcake</b>
<p>I am going to use the hash there.</p>
<p>I added the following line to the <code>/etc/passwd</code> using <code>sudo nano</code>: <br><code>root2:WVLY0mgH0RtUI:0:0:root:/root:/bin/bash</code><br>And now we can loging as <code>root2</code> with password <code>mrcake</code>using <code>su root2</code></p>
<p>Now we just have to go to the root directory and read the file root.txt</p>