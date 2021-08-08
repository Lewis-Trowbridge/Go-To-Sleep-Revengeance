import re

def get_seconds(timestring: str) -> int:
    matcher = re.compile(r'(\d{1,2})\:(\d{2})\s?(AM|PM)?')

    result = matcher.match(timestring)
    if result != None:
        groups = result.groups()
        hours = int(groups[0])
        mins = int(groups[1])
        secs = hours * 3600 + mins * 60
        if groups[2] == "PM":
            secs += 43200
        return secs


    else:
        raise ValueError

