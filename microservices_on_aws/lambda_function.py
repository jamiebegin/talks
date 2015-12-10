import holidays
from datetime import datetime, timedelta, time
from pytz import timezone

BIZ_OPEN = time(9, 0, 0)
BIZ_CLOSE = time(18, 0, 0)
WEEKEND = (5, 6)
TIMEZONE = 'US/Eastern'

def is_rbn_open():
    now_time = datetime.now(timezone(TIMEZONE))
    h = sorted(holidays.US(years=now_time.year).items())
    observed_holidays = [date for date, name in h \
                        if 'Martin Luther' not in name and 'Columbus' not in name]
                        
    # RBN is also closed the day after Thanksgiving
    thanksgiving = [date for date, name in h if name == 'Thanksgiving'][0]
    observed_holidays.append(thanksgiving + timedelta(days=1))
    
    for h in observed_holidays:
        if h == datetime.date(now_time):
            # Today is a holiday
            return False
    
    if now_time.weekday() in WEEKEND:
        # Today is the weekend
        return False
    elif not BIZ_OPEN <= now_time.time() < BIZ_CLOSE:
        # Past business hours
        return False
    else:
        return True
        
def lambda_handler(event, context):
    return {'rbn_open_now': is_rbn_open()}