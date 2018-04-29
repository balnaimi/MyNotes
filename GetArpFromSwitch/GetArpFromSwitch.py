#!/usr/bin/python3
import sys, getopt
import base64
import paramiko
import getpass
import ipaddress
import argparse
parser = argparse.ArgumentParser(description="This script will connect to Cisco Switch via SSH, and save the output of \"show arp\" in csv file")
parser.add_argument("username",help="SSH Username")
parser.add_argument("hostname",help="SSH Server or IP address")
parser.add_argument("--port",help="SSH Port, Default 22")
parser.add_argument("--output",help="Output File Name,Default: ArpOutput.csv")
parser.add_argument("--password",help="SSH Password, NOT RECOMMENDED TO USE!") # I don't recommend that you supply this, it will be save in terminal history, 
args=None
if len(sys.argv) < 2: # show help right away if no arguments passed
    parser.print_help()
    sys.exit()
try:  # show help in case these is arguemtn error
    args = parser.parse_args()
except:
    parser.print_help()
    sys.exit()
client = paramiko.SSHClient()
if args.port is None:
    args.port = 22
password = ""
if args.password is None:
    print ("Please type SSH Password")
    password = getpass.getpass('Password:')
else:
    password = args.password
if len(password) == 0:
    sys.exit("No Password Supplied")

# key = paramiko.RSAKey(data=base64.b64decode(b'PUT YOUR BASE64 ENCODED KEY HERE'))
# client.get_host_keys().add(args.hostname,key)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # disable this if you know the key, and you want to add it manually, by uncommenting top two lines and comment out this line
client.connect(args.hostname,port=args.port,username=args.username,password=password)
stdin,stdout,stderr = client.exec_command('show arp')
records = []
for line in stdout:
    r= line.strip('\n').split()
    if len(r) > 3: # first few lines will not be the output of show arp, so we are skipping those lines, and there is an ip check below as well, so it should be ok
        r_ip = r[1]
        try:
            ip = ipaddress.ip_address(r_ip) # to verify this is a valid ip address
            tempstring = ""
            r[3] = r[3].upper().replace(".","-") # make MAC address upper case and replace dots with -, I prefer -, I wrote the code, and this is what I like, so deal with it
            for rr in r:
                tempstring += rr + ","
            tempstring = tempstring[:-1]
            records.append(tempstring)
        except ValueError:
            continue # in error, means the line didn't have an ip address in r[1]

filename = "ArpOutput.csv"
if args.output is not None:
    filename = args.output
with open(filename,mode='w') as f:
    for r in records:
        f.write(str(r) + "\n")
    f.close()
    print ("File: %s\tSaved Successfully"%filename)
client.close()
