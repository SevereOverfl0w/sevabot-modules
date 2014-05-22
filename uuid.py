#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Grab UUID of a username!
"""
import os
import sys
import json
import urllib

url = 'https://theminecraftapi.com/v1/?user=%s&apiKey=KEY'

def call_uuid_api(name):
    request = urllib.urlopen(url % name)
    payload = json.loads(request.read())
    if 'uuid' in payload:
        uuid = payload['uuid']
        migrated = payload['migrated']
        premium = payload['premium']
        print ('UUID of %s is %s' % (name ,uuid))
        if premium == 'true':
            print('This account is premium!')
            if migrated == 'true':
                print('The user has migrated their account')
            else:
                print('This user has not migrated their account')
        else:
           print('This account is not premium!')     
    else:
        print('Error, %s was not found.' % name)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("You must enter a username")
    else:
        playerName = sys.argv[1]
    call_uuid_api(playerName)  
