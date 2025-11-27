from algorithms import Solution
from generate_data import pair_odd_odd, pair_even_odd, pair_odd_even, pair_even_even, pair_small_long_big_short, pair_big_long_small_short
import numpy as np
import json
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def run_tests(tests_num: int):
    print("=== Testing pair_odd_odd ===")
    short, long = pair_odd_odd()
    solution = Solution(short, long)

    result1, time1, mem1 = solution.two_pointers()
    print(f"Two pointers - Result: {result1}, Time: {time1}, Memory: {mem1}")

    result2, time2, mem2 = solution.binary_search()
    print(f"Binary search - Result: {result2}, Time: {time2}, Memory: {mem2}")

    result3, time3, mem3 = solution.exponential_search()
    print(f"Exponential search - Result: {result3}, Time: {time3}, Memory: {mem3}")

    result4, time4, mem4 = solution.binary_divide()
    print(f"Binary divide - Result: {result4}, Time: {time4}, Memory: {mem4}")

    print("\n=== Testing pair_even_odd ===")
    short, long = pair_even_odd()
    solution = Solution(short, long)

    result1, time1, mem1 = solution.two_pointers()
    print(f"Two pointers - Result: {result1}, Time: {time1}, Memory: {mem1}")

    result2, time2, mem2 = solution.binary_search()
    print(f"Binary search - Result: {result2}, Time: {time2}, Memory: {mem2}")

    result3, time3, mem3 = solution.exponential_search()
    print(f"Exponential search - Result: {result3}, Time: {time3}, Memory: {mem3}")

    result4, time4, mem4 = solution.binary_divide()
    print(f"Binary divide - Result: {result4}, Time: {time4}, Memory: {mem4}")

    print("\n=== Testing pair_odd_even ===")
    short, long = pair_odd_even()
    solution = Solution(short, long)

    result1, time1, mem1 = solution.two_pointers()
    print(f"Two pointers - Result: {result1}, Time: {time1}, Memory: {mem1}")

    result2, time2, mem2 = solution.binary_search()
    print(f"Binary search - Result: {result2}, Time: {time2}, Memory: {mem2}")

    result3, time3, mem3 = solution.exponential_search()
    print(f"Exponential search - Result: {result3}, Time: {time3}, Memory: {mem3}")

    result4, time4, mem4 = solution.binary_divide()
    print(f"Binary divide - Result: {result4}, Time: {time4}, Memory: {mem4}")

    print("\n=== Testing pair_even_even ===")
    short, long = pair_even_even()
    solution = Solution(short, long)

    result1, time1, mem1 = solution.two_pointers()
    print(f"Two pointers - Result: {result1}, Time: {time1}, Memory: {mem1}")

    result2, time2, mem2 = solution.binary_search()
    print(f"Binary search - Result: {result2}, Time: {time2}, Memory: {mem2}")

    result3, time3, mem3 = solution.exponential_search()
    print(f"Exponential search - Result: {result3}, Time: {time3}, Memory: {mem3}")

    result4, time4, mem4 = solution.binary_divide()
    print(f"Binary divide - Result: {result4}, Time: {time4}, Memory: {mem4}")

    print("\n=== Testing pair_small_long_big_short ===")
    short, long = pair_small_long_big_short()
    solution = Solution(short, long)

    result1, time1, mem1 = solution.two_pointers()
    print(f"Two pointers - Result: {result1}, Time: {time1}, Memory: {mem1}")

    result2, time2, mem2 = solution.binary_search()
    print(f"Binary search - Result: {result2}, Time: {time2}, Memory: {mem2}")

    result3, time3, mem3 = solution.exponential_search()
    print(f"Exponential search - Result: {result3}, Time: {time3}, Memory: {mem3}")

    result4, time4, mem4 = solution.binary_divide()
    print(f"Binary divide - Result: {result4}, Time: {time4}, Memory: {mem4}")

    print("\n=== Testing pair_big_long_small_short ===")
    short, long = pair_big_long_small_short()
    solution = Solution(short, long)

    result1, time1, mem1 = solution.two_pointers()
    print(f"Two pointers - Result: {result1}, Time: {time1}, Memory: {mem1}")

    result2, time2, mem2 = solution.binary_search()
    print(f"Binary search - Result: {result2}, Time: {time2}, Memory: {mem2}")

    result3, time3, mem3 = solution.exponential_search()
    print(f"Exponential search - Result: {result3}, Time: {time3}, Memory: {mem3}")

    result4, time4, mem4 = solution.binary_divide()
    print(f"Binary divide - Result: {result4}, Time: {time4}, Memory: {mem4}")
    