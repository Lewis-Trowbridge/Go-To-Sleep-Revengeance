import re

def get_seconds(timestring: str) -> int:
    matcher = re.compile(r'(\d{1,2})\:(\d{2})\s?(AM|PM)?')

    result = matcher.match(timestring)
    if result != None:
        groups = result.groups()
        hours = int(groups[0])
        mins = int(groups[1])
        ampm = groups[2]
        if ((ampm is None and hours in range(0, 24)) or (hours in range(0, 12))) and (mins in range(0, 60)):
            secs = hours * 3600 + mins * 60
            if ampm == "PM":
                secs += 43200
            return secs
        else:
            raise ValueError


    else:
        raise ValueError

