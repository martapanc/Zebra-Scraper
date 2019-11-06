# 🦓 🦓 🦓 Zebra Scraper 🦓 🦓 🦓

### Requisites
- Python 3
- pip

### Dependencies
- configparser
- requests

### Setup
- Rename `config.properties.local` to `config.properties`
- The api url and token can be found by logging into your account, then right click and choose "Inspect", go to "Network" tab, refresh the page and find the request named `liveBalances`. Under the "Headers" tab, the URL is the value of `Request URL` and the auth token is the value of `Authorization`
- Download the Chromedriver executable above and place its absolute path in the config.properties file as well

`config.properties` should look like:

```
[Api]
api.url=https://www.zebrapower.co.uk/api/Accounts/12345/liveBalances
api.auth=Bearer 54tBoPtBNlwSrCYuFFjO...

[Chromedriver]
chromedriver.path=/Users/pancaldim/PersonalProjects/ZebraScraper/chromedriver
```
- Run with
```bash 
python3 zebra_scraper.py
```
