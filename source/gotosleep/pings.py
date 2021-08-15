import datetime
import discord


def is_bedtime(ntp_offset: datetime.timedelta, utc_offset: int, dst_offset: int, bedtime_offset:int) -> bool:
    time_in_timezone = (
            datetime.datetime.now() + ntp_offset + datetime.timedelta(seconds=utc_offset) +
            datetime.timedelta(seconds=dst_offset))
    bedtime_timedelta = datetime.timedelta(seconds=bedtime_offset)
    final_time = time_in_timezone - bedtime_timedelta
    if final_time.hour == 0 and final_time.minute == 0:
        return True
    else:
        return False


def is_available(member_to_check: discord.Member, aggressive_pings: bool) -> bool:
    return member_to_check.status == discord.Status.online or aggressive_pings