from tests import run_tests
from generate_data import generate_data
import os

os.makedirs("data", exist_ok=True)
os.makedirs("reports", exist_ok=True)
os.makedirs("charts", exist_ok=True)

TESTS_NUM = 50
GENERATE_DATA = False

if GENERATE_DATA or TESTS_NUM > 500:
    generate_data(TESTS_NUM)

run_tests(TESTS_NUM)
