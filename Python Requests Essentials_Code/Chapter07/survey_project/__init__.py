import os
import sys


current_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

sys.path.insert(0, parent_dir)
