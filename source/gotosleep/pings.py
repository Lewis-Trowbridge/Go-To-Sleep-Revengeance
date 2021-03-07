import datetime


def is_bedtime(ntpoffset, utc_offset, dst_offset, bedtime_offset):
    time_in_timezone = (
            datetime.datetime.now() + ntpoffset + datetime.timedelta(seconds=utc_offset) +
            datetime.timedelta(seconds=dst_offset))
    bedtime_float = bedtime_offset / 3600
    bedtime_hours = int(bedtime_float)
    bedtime_minutes = round((bedtime_float - bedtime_hours) * 60)
    if time_in_timezone.hour == bedtime_hours and time_in_timezone.minute == bedtime_minutes:
        return True
    else:
        return False
