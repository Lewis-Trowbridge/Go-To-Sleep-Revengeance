import argparse
import pathlib
import os

def db_file(file_string):
    if os.path.exists(file_string):
        path_object = pathlib.Path(file_string)
        if path_object.is_file() and path_object.suffix == ".db":
            return path_object
        else:
            raise ValueError
    else:
        raise FileNotFoundError

def init_argparse():
    parser = argparse.ArgumentParser(
        description="A Discord bot designed to give reminders to go to sleep. Get your friends some semblance of a decent sleep schedule!"
    )
    parser.add_argument("bot_token", help="the bot token supplied from Discord.", metavar="bot-token")
    parser.add_argument("maps_token", help="the API token supplied from Google Cloud Services", metavar="maps-token")
    parser.add_argument("db_path", help="the path to the SQL database to use.", metavar="db-path", type=db_file)
    parser.add_argument("-l", "--log-dir", help="the directory to store logs in. Defaults to './logs'", type=pathlib.Path)
    
    return parser

def handle_args():

    parser = init_argparse()
    args = parser.parse_args()
    return args