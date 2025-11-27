from tests import run_tests
from generate_data import generate_data
import os

os.makedirs("data", exist_ok=True)
os.makedirs("reports", exist_ok=True)
os.makedirs("charts", exist_ok=True)


run_tests()
