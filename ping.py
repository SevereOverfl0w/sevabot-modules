#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ping a MC server!
"""
import os
import sys
import json
import urllib
url = 'https://theminecraftapi.com/v1/?server=%s&action=info&apiKey=KEY'
threshold = 10

def grab_server_data(server):
    request = urllib.urlopen(url % server)
    payload = json.loads(request.read())
    if 'status' in payload:
        online_players=payload['players']['online']
        max_players=payload['players']['max']
        server_motd=payload['motd']
        minecraft_version=payload['version']
        print('The server %s is up with %d/%d' % (server, online_players, max_players))
        print("The server's MOTD is: %s" % (server_motd,) )
        print("The server is running Minecraft version: %s" % (minecraft_version,))
    else:
        print('Are you sure %s is a server?' % (server))
if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("You must enter a server IP")
    else:
        host = sys.argv[1]
    grab_server_data(host) 
            
