# Attacktive Directory
<b>Target IP: <code>10.10.235.52</code></b>

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