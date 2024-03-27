#!/usr/bin/env python3

import sys
import json
import requests
import os
import re


pwd = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
log_file = '/var/ossec/logs/integrations.log'

def get_mac_details(mac_address, api_key):
    API_URL = "https://api.maclookup.app/v2/macs/"
    headers = {'Content-Type': 'application/json'}
    params = {'apiKey': api_key}
    try:
        response = requests.get(f"{API_URL}{mac_address}", headers=headers, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Oops: Something Else", err)

def main():
    try:
        with open(sys.argv[1], 'r') as alert_file:
            alert_json = json.load(alert_file)

        api_key = sys.argv[2]
        alert_level = alert_json.get('rule', {}).get('level')
        ruleid = alert_json.get('rule', {}).get('id')

        if alert_level == 7 and ruleid == "100422":
            mac_address = alert_json.get('data', {}).get('mac_rtr')
            mac_details = get_mac_details(mac_address, api_key)
            if mac_details and mac_details.get('found'):
                print(f"MAC Address: {mac_address} is from {mac_details['company']} located in {mac_details['country']}")
                with open(log_file, 'a') as log:
                    
                    company_name = re.sub(r'\W+', '', mac_details['company'])
                    
                    log.write(f"MAC Address: {mac_address} is from {company_name} located in {mac_details['country']}\n")
                    
            else:
                
                # if None mac do not write to log
                if mac_details is None:
                    return
                
                print(f"UNKNOWN MAC Address: {mac_address} was not found in the database")
                
                with open(log_file, 'a') as log:
                    log.write(f"UNKNOWN MAC Address: {mac_address} was not found in the database\n")
        else:
            print("Alert is not of interest")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
