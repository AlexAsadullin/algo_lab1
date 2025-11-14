from algorythms import Solution
import numpy as np
import json
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def run_tests(tests_num: int):
    methods = ['two_pointers', 'binary_search', 'exponential_search', 'binary_divide']
    method_funcs = {
        'two_pointers': Solution.two_pointers,
        'binary_search': Solution.binary_search,
        'exponential_search': Solution.exponential_search,
        'binary_divide': Solution.binary_divide
    }

    print("Running tests...")
    for test_num in range(tests_num):
        data = np.load(f'data/{test_num}.npy', allow_pickle=True)
        arr_m, arr_n = data
        sol = Solution(arr_m, arr_n)

        results = {}
        times = []
        mems = []
        labels = []

        for m_name in methods:
            res, t, m = method_funcs[m_name](sol)
            results[m_name] = {'res': res, 'time': t, 'mem': m}
            times.append(t)
            mems.append(m)
            labels.append(m_name.replace('_', ' ').title())

        fig = make_subplots(rows=1, cols=2, subplot_titles=('Time (s)', 'Memory (bytes)'))
        fig.add_trace(go.Bar(x=labels, y=times, name='Time'), row=1, col=1)
        fig.add_trace(go.Bar(x=labels, y=mems, name='Memory'), row=1, col=2)
        fig.update_yaxes(type='log', row=1, col=1)
        fig.update_yaxes(type='log', row=1, col=2)
        fig.update_layout(title_text=f'Test {test_num} Comparison', showlegend=False)
        fig.write_html(f'charts/{test_num}.html')

        report = {'test_num': test_num, 'results': results}
        with open(f'reports/{test_num}.json', 'w') as f:
            json.dump(report, f, indent=2)
        print(f"Test {test_num} completed.")
    print("Tests completed.")

    print("Generating summary...")
    total_times = {m: 0 for m in methods}
    max_mems = {m: 0 for m in methods}

    for test_num in range(tests_num):
        with open(f'reports/{test_num}.json', 'r') as f:
            report = json.load(f)
        for m in methods:
            t = report['results'][m]['time']
            mem = report['results'][m]['mem']
            total_times[m] += t
            max_mems[m] = max(max_mems[m], mem)

    for m in methods:
        print(f"{m}: Total Time: {total_times[m]:.3f}s, Max Mem: {max_mems[m]} bytes")