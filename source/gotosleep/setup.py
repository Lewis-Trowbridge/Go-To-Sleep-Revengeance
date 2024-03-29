import argparse
import pathlib
import os
import sys
import mysql.connector as mysql
from .tracing import setup_tracer

GTS_BOT_TOKEN = "GTS_BOT_TOKEN"
GTS_MAPS_TOKEN = "GTS_MAPS_TOKEN"
GTS_SUPPORT_SERVER = "GTS_SUPPORT_SERVER"
GTS_DB_PATH = "GTS_DB_PATH"
GTS_DB_USER = "GTS_DB_USER"
GTS_DB_PASS = "GTS_DB_PASS"
GTS_DB_DATABASE = "GTS_DB_DATABASE"

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
    parser.add_argument("-b", "--bot-token", help="the bot token supplied from Discord. Overrides GTS_BOT_TOKEN environment variable")
    parser.add_argument("-m", "--maps-token", help="the API token supplied from Google Cloud Services. Overrides GTS_MAPS_TOKEN environment variable")
    parser.add_argument("-d", "--db-path", help="the path to the SQL database to use. Overrides GTS_DB_PATH environment variable", type=db_file)
    parser.add_argument("-l", "--log-dir", help="the directory to store logs in. Defaults to './logs'", type=log_dir, default="logs")
    parser.add_argument("-s", "--support-server", help="the invite link of the support server used with this bot")    
    return parser

def check_env_variable(variable_name: str, default_value = None):
    env_value = os.getenv(variable_name, default_value)
    if env_value == None:
            sys.exit(variable_name + " is blank. Please fill this in to run the bot.")
    return env_value


def handle_args():

    setup_tracer()

    parser = init_argparse()
    args = parser.parse_args()
    
    if args.bot_token == None:
        args.bot_token = check_env_variable(GTS_BOT_TOKEN)
    if args.maps_token == None:
        args.maps_token = check_env_variable(GTS_MAPS_TOKEN)
    if args.support_server == None:
        args.support_server = check_env_variable(GTS_SUPPORT_SERVER, "")
    if args.db_path == None:
        args.db_path = check_env_variable(GTS_DB_PATH)
    args.db_connection = mysql.connect(user=check_env_variable(GTS_DB_USER), passwd=check_env_variable(GTS_DB_PASS), host=args.db_path, db=check_env_variable(GTS_DB_DATABASE), buffered=True)
    return args
