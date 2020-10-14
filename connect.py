from OJIRC import *

connect("room_name", "your_name", "client2's ipv4")
# Important: If connecting over networks you must use client2's public ip and they must
# portforward icmp port 1. If you want to recieve messages from them you must also
# portforward.

# If connecting over LAN then use client2's ipv4