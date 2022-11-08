#!/usr/bin/python3
#License:
#"Cisco port filter" is a free application what can be used to to filter ports that are down and inactive for 26 weeks
#Copyright (C) 2022 Tom Slenter
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#For more information contact the author:
#Name author: Tom Slenter
#E-mail: info@remotesyslog.com

import paramiko
import time
import os
import argparse
import datetime

#Global information
print("Script is created by T.Slenter")
print("The switches input is as following: hostname or ip,hostname or ip,hostname or ip")
print('Running from directory: ', os.getcwd())
print("Information for non interactive mode:")
print("-n, --host, Enter a hostname or ip, multiple hostname and ips are supported use seperator=,")
print("-u, --username, Add a username")
print("-p, --password, Add a password")

#Set variables to None
host = None
singlecommand = "show int | s proto.*notconnect|proto.*administratively down"
#singlecommand = "ls"
username = None
password = None
lines = None
from_week = 26

#Add arguments for optional use
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--host',  help='Enter a hostname or ip, multiple hostname and ips are supported use seperator=,')
parser.add_argument('-u','--username', help='Add a username')
parser.add_argument('-p', '--password', help='Add a password')
args = parser.parse_args()

#Extract variables from namespace to global
globals().update(vars(args))

#Functions
# Create loop to view output
def outp():
    last_line = ""
    output = ""
    output = "Running on switch: " + host
    output += "\n"
    print("Show output:")
    for line in ssh_stdout:
        if "down" in line or "Description" in line or "Last input never" in line:
                output += line
        for w in range(from_week,52):
                if "Last input " + str(w) + "w" in line:
                    output += line
        for y in range(0,9):
                if "Last input " + str(y) + "y"  in line:
                    output += line
    if output != "":
        with open('output.txt', 'a') as f:
            #print(datetime.datetime.now(), file=f)
            print(output, file=f)
        with open('output.txt', 'r') as f:
            #lines = [line.rstrip('\n') for line in f]
            lines = f.readlines()
            index = len(lines) - 1
            x = list()
            for i in range(0,index):
                if "down" in lines[i] and "down" in lines[i-1]:
                      x.append(lines[i-1])
                if "down" in lines[i] and "Description" in lines[i-1]:
                      x.append(lines[i-1])
                      x.append(lines[i-2])
            for l in x:
                lines.remove(l)
            text = " ".join(lines)
            print(datetime.datetime.now())
            print(text)
            #print(*lines, sep = "\n")
    else:
        print("Nothing here!")
    # Closing file
    f.close()

#Check if interactive mode or arguments are going to be used
if host == None or username == None or password == None:
    print("Interactive mode is loaded!")
    #Ask questions
    host = str(input("Enter switch: "))
    username = str(input("Enter username: "))
    password = str(input("Enter password: "))
else:
    print("Running in non interactive mode!")

if host == "" or username == "" or password == "":
   print ("Not all information given!")
   exit()

#Extract words from list
server_list = list(host.split(','))

#Clear old output files
open('output.txt', 'w').close()

#Loop list with hostnames
for ser in server_list:
    #Initiate connection
    print("Open SSH connection!")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ser, username=username, password=password)

    #Loop down commands or run single command
    if singlecommand != "":
        #Run single command
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(singlecommand)
        print("SSH Connection succeeded!")
        ssh_stdout = ssh_stdout.readlines()
        outp()
    else:
        print("Something went wrong!, no input found ...")

    #Closing down connection
    ssh.close()
    print("Connection closed!")

#Fix "AttributeError: 'NoneType' object has no attribute 'time'"
time.sleep(2.5)
