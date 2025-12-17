from tests import worst_case
import os

os.makedirs("data", exist_ok=True)
os.makedirs("reports", exist_ok=True)

worst_case()