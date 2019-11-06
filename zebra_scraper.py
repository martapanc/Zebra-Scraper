#!/usr/bin/python3

import requests
import configparser

def main():
	config = configparser.RawConfigParser()
	config.read('config.properties')

	LIVE_BALANCE_URL = config.get('Api', 'api.url');

	headers = {
	    "user-agent": "Mozilla/5.0", 
	    "authorization": config.get('Api', 'api.auth')
	}
	return requests.get(LIVE_BALANCE_URL, headers = headers).json()

if __name__ == '__main__':
    print(main())