#!/usr/bin/env python3

#Author: Ranmunige Senitha Ransen Rajapaksha"
#Author ID:143264224
#Date Created: 2024/09/22

import sys

if len(sys.argv) ==2:
    timer=int(sys.argv[1])
    
else:
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1
print("blast off!")