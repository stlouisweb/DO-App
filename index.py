#!/usr/bin/env python
"""Application for creating and provisioning DigitalOcean instances
By Jeremy Plack, 2015-11-22
"""
import json
import requests
import argparse
parser = argparse.ArgumentParser()

def main():
    return

def droplet_create():
    return

# Returns the list of droplets(instances) on the account.
def list_droplets():
     token = '4e8073041c5811735cf470f95e8778e145eaa4515fe8cdb6ed15315be948ed8e'
     droplets = requests.get('https://api.digitalocean.com/v2/droplets', auth=(token, ''))
     if droplets.status_code == 200:
         droplets = droplets.json()
         print 'DROPLETS:'
         print(droplets['droplets'][0]["name"])
         return droplets
     return droplets.status_code



if __name__ == "__main__":
    print """
    ____  ____     ___    ____  ____
   / __ \/ __ \   /   |  / __ \/ __ \/
  / / / / / / /  / /| | / /_/ / /_/ /
 / /_/ / /_/ /  / ___ |/ ____/ ____/
/_____/\____/  /_/  |_/_/   /_/

    This program provides methods for calling
    the DigitalOcean API to create and destroy droplets.
    Provision Docker containers on Droplets, and
    performing healthcheck and maintenance tasks."""
    ans=True
    while ans:
        print ("""
        1. List Droplets
        2. Create Droplet
        3. Exit/Quit
        """)
        ans=raw_input("What would you like to do? ")
        if ans=="1":
          list_droplets()
        elif ans=="2":
          create_droplet()
        elif ans=="3":
            print("\n Goodbye")
            break
        elif ans !="":
          print("\n Not Valid Choice Try again")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
