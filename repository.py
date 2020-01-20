import atexit
import sys
import sqlite3

class _repository:
    def __init__(self):
        self.conn = sqlite3.connect('moncafe.db')
