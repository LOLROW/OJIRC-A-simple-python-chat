OCHAT is a simple chat program me and a friend built because we were bored and are learning computer science / networking / digital forensics / cyber security.
I hope you enjoy.

This chat can send messages over LAN and between networks but for p2p between networks both clients must port-forward protocol ICMP on port 1.

To install dependencies use:
pip3 install -r requirements.txt

Known bugs:

Missing dependencies or problems with scapy do python3 install -r requirements.txt.
Sometimes one or more clients have to doubletap enter to send a message (no fix yet).