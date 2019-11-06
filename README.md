# Zebra Scraper

### Requisites
- Python 3
- pip

### Dependencies
- ConfigParser
- requests
- selenium
- [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

### Setup
- Rename `config.properties.local` to `config.properties`
- Replace your ZebraPower credentials in file (the email address needs double quotes, e.g. "example@mail.com", the other field don't)
- The api url and token can be found by logging into your account, then right click and choose "Inspect", go to "Network" tab, refresh the page and find the request named `liveBalances`. Under the "Headers" tab, the URL is the value of `Request URL` (e.g. `https://www.zebrapower.co.uk/api/Accounts/12345/liveBalances`) and the auth token is the value of `Authorization` (e.g. `Bearer 54tBoPtBNlwSrCYuFFjO...`)
- Download the Chromedriver executable above and place its absolute path in the config.properties file as well

config.properties should look like:

```
[Login]
site.username="example@mail.com"
site.password=Pa5sW0rD

[Api]
api.url=https://www.zebrapower.co.uk/api/Accounts/12345/liveBalances
api.auth=Bearer 54tBoPtBNlwSrCYuFFjO...

[Chromedriver]
chromedriver.path=/Users/pancaldim/PersonalProjects/ZebraScraper/chromedriver
```