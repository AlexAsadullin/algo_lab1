from tests import run_tests
import os

os.makedirs("data", exist_ok=True)
os.makedirs("reports", exist_ok=True)

run_tests()
