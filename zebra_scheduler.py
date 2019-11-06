
from zebra_scraper import save_results
from datetime import datetime
import time

print("Started on %s" % datetime.now())

starttime = time.time()

while True:
	save_results()
	time.sleep(60.0 - ((time.time() - starttime) % 60.0))
