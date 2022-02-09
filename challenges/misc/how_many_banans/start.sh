#!/bin/bash

#while [ true ]; do
su -l $USER -c "socat -dd TCP4-LISTEN:9000,fork,reuseaddr EXEC:'/usr/bin/python3 /run.py',pty,stderr"
#done;
