from Betting import *
from datetime import datetime, timedelta, timezone
import os

def main():
    # Use UTC (Abidjan timezone == UTC) to compute today and the next two days
    today = datetime.now(timezone.utc).date()
    first_day = today.strftime('%Y-%m-%d')
    last_day = (today + timedelta(days=2)).strftime('%Y-%m-%d')
    print('Fetching matches from', first_day, 'to', last_day)
    Db_handler.initialize_dbs()
    print('db initializing finished')
    Db_handler.hire_workers()
    print('hiring process finished')
    # Collect data for the 3-day window: today, tomorrow, day after
    DataCollector().football(first_day, last_day)
    Db_handler.fire_workers()

if __name__ == '__main__':
    main()
