# Cisco filter for inactive ports
Extracts port information for inactive ports. Currently checks for 26 weeks or older. The script is tested for 4500 and 9400 series switches, it probably runs on other series as well.

This python script makes use of the following library's:

```
paramiko, time, os, argparse, datetime
```

Run the script as following: 

```
python3 free_port_check.py
```

Or 

Run the script with all parameters: 

```
python3 free_port_check.py -n "<cisco_switch>" -u "<username>" -p "<very strong pw>"
python3 free_port_check.py -n "<cisco_switch>,<cisco_switch2>" -u "<username>" -p "<very strong pw>"
```

Script is currently in BETA. Please verify data with the data given via the switch console.

## Example output:

```
root@server:/home/tom# /usr/bin/free_port_check.py
Script is created by T.Slenter
The switches input is as following: hostname or ip,hostname or ip,hostname or ip
Running from directory:  /home/tom
Information for non interactive mode:
-n, --host, Enter a hostname or ip, multiple hostname and ips are supported use seperator=,
-u, --username, Add a username
-p, --password, Add a password
Interactive mode is loaded!
Enter switch: switch1,switch2
Enter username: tom
Enter password: <very_strong_pw>
Open SSH connection!
SSH Connection succeeded!
Show output:
2022-11-11 11:43:16.144506
Running on switch: switch1
 GigabitEthernet1/1 is down, line protocol is down (notconnect)
   Last input 2y51w, output never, output hang never
 GigabitEthernet1/16 is down, line protocol is down (notconnect)
   Last input 26w1d, output never, output hang never
 GigabitEthernet1/18 is down, line protocol is down (notconnect)
   Last input 2y41w, output never, output hang never
 GigabitEthernet1/43 is down, line protocol is down (notconnect)
   Last input 2y1w, output never, output hang never
 GigabitEthernet1/48 is down, line protocol is down (notconnect)
   Last input 1y23w, output never, output hang never

Connection closed!
Open SSH connection!
SSH Connection succeeded!
Show output:
2022-11-11 11:43:17.295553
Running on switch: switch2
 GigabitEthernet1/2 is down, line protocol is down (notconnect)
   Last input 2y30w, output never, output hang never
 GigabitEthernet1/3 is down, line protocol is down (notconnect)
   Last input 2y41w, output never, output hang never
 GigabitEthernet1/4 is down, line protocol is down (notconnect)
   Last input 2y33w, output never, output hang never
 GigabitEthernet1/16 is down, line protocol is down (notconnect)
   Last input 1y23w, output never, output hang never
```
