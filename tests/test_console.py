#!/usr/bin/python3
"""Testing the console"""

import unittest
import console
from console import HBNBCommand


class test_console(unittest.TestCase):
    """Test console class"""

    def create(self):
        """creates an instance"""
        return HBNBCommand()

    def test_quit(self):
        """Test the quit method
        """
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def test_EOF(self):
        """Test the EQF method
        """
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))
