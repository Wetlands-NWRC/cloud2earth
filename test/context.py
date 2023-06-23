import os
import sys

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
os.chdir(CURRENT_DIR)

sys.path.insert(0, "../..")

import src
