from apscheduler.schedulers.blocking import BlockingScheduler
from zebra_scraper import save_results

scheduler = BlockingScheduler()
scheduler.add_job(save_results, 'interval', minutes=10)
scheduler.start()