# Go To Sleep - Revengeance
A new bot based off of an old one that is so overcome with in-jokes that it's not worth putting out in the public. Get your friends some semblance of a decent sleep schedule.

## What you'll need if you want to run this yourself:

- The bot token of a Discord developer application with a bot account
- A Google Cloud Services API token with the Maps Geocoding and Time Zone APIs enabled
- A place to host it (I'm currently using a Microsoft Azure VM to varying degrees of success)

Now here's where your options open up a bit. You can either:

### Run it with Docker
For this, you'll need to run:

```sh
docker run lewistrowbridge/go-to-sleep-revengeance
```

### Run it natively
For this, you'll need a bit more setup. You'll need:

- Python 3 - tested on 3.8 - 3.9, but very well may work on higher versions
- These Python libraries:

    - [Discord.py](https://pypi.org/project/discord.py/)
    - [Google Maps Python library](https://pypi.org/project/googlemaps/)
    - [MySQL Connector](https://pypi.org/project/mysql-connector-python/)
    - [ntplib](https://pypi.org/project/ntplib/)
    
- Patience of a saint

### Testing
There are a few more libraries used in testing than those included in the `requirements.txt` for the sake of the Docker image's size - however, if the tests are to be run, these are required.

  - [freezegun](https://pypi.org/project/freezegun/)
  - [coverage](https://pypi.org/project/coverage/)