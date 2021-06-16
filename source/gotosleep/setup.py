import argparse
import pathlib
import os

def db_file(file_string):
    if os.path.exists(file_string):
        path_object = pathlib.Path(file_string)
        if path_object.is_file() and path_object.suffix == ".db":
            return str(path_object)
        else:
            raise ValueError
    else:
        raise FileNotFoundError

def log_dir(path_string):
    if path_string is None:
        path_string = "./logs"
    path_object = pathlib.Path(path_string)
    if not os.path.exists(str(path_object)):
        os.mkdir(str(path_object))
    if path_object.is_dir():
        return str(path_object)
    else:
        raise ValueError

def init_argparse():
    parser = argparse.ArgumentParser(
        description="A Discord bot designed to give reminders to go to sleep. Get your friends some semblance of a decent sleep schedule!"
    )
    parser.add_argument("bot_token", help="the bot token supplied from Discord.", metavar="bot-token")
    parser.add_argument("maps_token", help="the API token supplied from Google Cloud Services", metavar="maps-token")
    parser.add_argument("db_path", help="the path to the SQL database to use.", metavar="db-path", type=db_file)
    parser.add_argument("-l", "--log-dir", help="the directory to store logs in. Defaults to './logs'", type=log_dir, default="logs")
    
    return parser

def handle_args():

    parser = init_argparse()
    args = parser.parse_args()
    return args
