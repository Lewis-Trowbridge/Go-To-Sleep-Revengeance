import argparse
import unittest
import contextlib
from io import StringIO
import source.gotosleep.setup as setup
import os

test_bot_token = "bottokenx"
test_maps_token = "mapstokeny"
test_db_path = "test_db.db"
test_log_path = "log-folder"
test_support_server = "invitelink"

class TestArgParser(unittest.TestCase):
    
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)

    def setUp(self) -> None:
        self.argparser = setup.init_argparse()
        open(test_db_path, "w").close()

    def test_help(self):
        with self.assertRaises(SystemExit):
            help_args = ["-h"]
            with contextlib.redirect_stdout(StringIO()) as f:
                self.argparser.parse_args(help_args)
    
    def test_all_args(self):
        all_args = [test_bot_token, test_maps_token, test_db_path, "--log-dir", test_log_path, "--support-server", test_support_server]
        result = self.argparser.parse_args(all_args)
        self.assertEqual(all_args[0], result.bot_token)
        self.assertEqual(all_args[1], result.maps_token)
        self.assertEqual(all_args[2], str(result.db_path))
        self.assertEqual(all_args[4], str(result.log_dir))
        self.assertEqual(all_args[6], result.support_server)

    def test_nonexistent_db_path(self):
        false_db_path = "./notarealdb.db"
        with self.assertRaises(FileNotFoundError):
            all_args = [test_bot_token, test_maps_token, false_db_path, "--log-dir", test_log_path]
            self.argparser.parse_args(all_args)
    
    def test_not_db_file(self):
        not_a_db_file_path = "README.md"
        with self.assertRaises(SystemExit):
            all_args = [test_bot_token, test_maps_token, not_a_db_file_path, "--log-dir", test_log_path]
            self.argparser.parse_args(all_args)
        
    def test_default_log_dir(self):
        default_log_path = "logs"
        all_args = [test_bot_token, test_maps_token, test_db_path]
        results = self.argparser.parse_args(all_args)
        self.assertEqual(default_log_path, results.log_dir)
    
    def test_default_support_server(self):
        default_support_server = ""
        all_args = [test_bot_token, test_maps_token, test_db_path]
        results = self.argparser.parse_args(all_args)
        self.assertEqual(default_support_server, results.support_server)


    def tearDown(self) -> None:
        os.remove(test_db_path)

if __name__ == '__main__':
    unittest.main()