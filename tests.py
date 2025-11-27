from algorithms import Solution
from generate_data import pair_odd_odd, pair_even_odd, pair_odd_even, pair_even_even, pair_small_long_big_short, \
    pair_big_long_small_short, pair_intersecting_ranges, pair_no_intersection, pair_identical_values, \
    pair_single_element, pair_empty_array, pair_extreme_size_difference, pair_sequential_overlap, pair_both_empty
import numpy as np
import json
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def collect_performance_data():
    datasets = {
        'pair_odd_odd': pair_odd_odd,
        'pair_even_odd': pair_even_odd,
        'pair_odd_even': pair_odd_even,
        'pair_even_even': pair_even_even,
        'pair_small_long_big_short': pair_small_long_big_short,
        'pair_big_long_small_short': pair_big_long_small_short,
        'pair_intersecting_ranges': pair_intersecting_ranges,
        'pair_no_intersection': pair_no_intersection,
        'pair_identical_values': pair_identical_values,
        'pair_single_element': pair_single_element,
        'pair_empty_array': pair_empty_array,
        'pair_extreme_size_difference': pair_extreme_size_difference,
        'pair_sequential_overlap': pair_sequential_overlap,
        'pair_both_empty': pair_both_empty
    }

    algorithms = ['two_pointers', 'binary_search', 'exponential_search', 'binary_divide']
    time_results = {algo: [] for algo in algorithms}
    memory_results = {algo: [] for algo in algorithms}

    for dataset_name, dataset_func in datasets.items():
        print(f"\n=== Testing {dataset_name} ===")
        short, long = dataset_func()
        solution = Solution(short, long)

        for algo in algorithms:
            method = getattr(solution, algo)
            try:
                result, time, mem = method()
                time_results[algo].append(time)
                memory_results[algo].append(mem)
                print(f"{algo} - Time: {time:.6f}s, Memory: {mem} bytes")
            except Exception as e:
                time_results[algo].append(-1)
                memory_results[algo].append(-1)
                print(f"{algo} - Error: {e}, Time: -1, Memory: -1")

    return time_results, memory_results, list(datasets.keys())


def create_performance_chart(time_results, memory_results, dataset_names):

    fig = go.Figure()

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # Цвета для алгоритмов

    algorithms = ['two_pointers', 'binary_search', 'exponential_search', 'binary_divide']
    algorithm_names = {
        'two_pointers': 'Two Pointers',
        'binary_search': 'Binary Search',
        'exponential_search': 'Exponential Search',
        'binary_divide': 'Binary Divide'
    }

    for i, algo in enumerate(algorithms):
        fig.add_trace(go.Scatter(
            x=dataset_names,
            y=time_results[algo],
            name=algorithm_names[algo],
            line=dict(color=colors[i], width=3),
            marker=dict(size=8, color=colors[i]),
            mode='lines+markers'
        ))

    fig.update_layout(
        title='Сравнение производительности алгоритмов на разных датасетах',
        xaxis_title='Датасеты',
        yaxis_title='Время выполнения (секунды)',
        yaxis_type='log',  # Логарифмическая шкала для оси Y
        height=600,
        font=dict(size=12),
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        )
    )

    fig.write_html('charts/time.html')
    print("\nГрафик сохранен в charts/time.html")


def create_memory_chart(time_results, memory_results, dataset_names):

    fig = go.Figure()

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # Цвета для алгоритмов

    algorithms = ['two_pointers', 'binary_search', 'exponential_search', 'binary_divide']
    algorithm_names = {
        'two_pointers': 'Two Pointers',
        'binary_search': 'Binary Search',
        'exponential_search': 'Exponential Search',
        'binary_divide': 'Binary Divide'
    }

    for i, algo in enumerate(algorithms):
        fig.add_trace(go.Scatter(
            x=dataset_names,
            y=memory_results[algo],
            name=algorithm_names[algo],
            line=dict(color=colors[i], width=3),
            marker=dict(size=8, color=colors[i]),
            mode='lines+markers'
        ))

    fig.update_layout(
        title='Сравнение использования памяти алгоритмами на разных датасетах',
        xaxis_title='Датасеты',
        yaxis_title='Использование памяти (байты)',
        yaxis_type='log',  # Логарифмическая шкала для оси Y
        height=600,
        font=dict(size=12),
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        )
    )

    fig.write_html('charts/memory.html')
    print("График сохранен в charts/memory.html")


if __name__ == "__main__":
    time_results, memory_results, dataset_names = collect_performance_data()
    create_performance_chart(time_results, memory_results, dataset_names)
    create_memory_chart(time_results, memory_results, dataset_names)