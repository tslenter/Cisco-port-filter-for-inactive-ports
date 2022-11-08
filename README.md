# cisco-port-filter-for-inactive-ports
Extracts port information for inactive ports. Currently locked for 26 weeks.

This python script makes use of the following library's:

paramiko, time, os, argparse, datetime

Run the script as following: python3 free_port_check.py

Or 

Run the script with all parameters: python3 free_port_check.py -n <cisco_switch> -u <username> -p <very strong pw>

Script is currently in BETA. Please verify data with the data given via the switch console.
