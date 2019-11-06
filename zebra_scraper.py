#!/usr/bin/python3

import requests
import configparser
import json

def main():
	config = configparser.RawConfigParser()
	config.read('config.properties')

	LIVE_BALANCE_URL = config.get('Api', 'api.url');

	headers = {
	    "user-agent": "Mozilla/5.0", 
	    "authorization": config.get('Api', 'api.auth')
	}
	return requests.get(LIVE_BALANCE_URL, headers = headers).json()


def save_results():
	res = main()
	f = open("data/%s.json" % res.get("lastUpdated"),"w+")
	f.write(json.dumps(res, sort_keys=True, indent=4))
	f.close()

if __name__ == '__main__':
    print(main())
    # save_results()