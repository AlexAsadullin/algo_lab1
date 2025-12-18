from algorithms import Solution
from generate_data import pair_odd_odd, pair_even_odd, pair_odd_even, pair_even_even, pair_small_long_big_short, \
    pair_big_long_small_short, pair_intersecting_ranges, pair_no_intersection, pair_identical_values, \
    pair_single_element, pair_empty_array, pair_extreme_size_difference, pair_sequential_overlap, pair_both_empty, gen_sorted_random_parity
import random
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots


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
                # Используем максимум 1e-9 для очень быстрых операций (избегаем нулевых значений на логарифмической шкале)
                time = max(time, 1e-9)
                mem = max(mem, 1)
                time_results[algo].append(time)
                memory_results[algo].append(mem)
                print(f"{algo} - Time: {time:.6f}s, Memory: {mem} bytes")
            except Exception as e:
                # При ошибке добавляем очень маленькое значение вместо -1
                time_results[algo].append(1e-9)
                memory_results[algo].append(1)
                print(f"{algo} - Error: {e}, Time: 1e-9, Memory: 1")

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


def run_tests():
    time_results, memory_results, dataset_names = collect_performance_data()
    create_performance_chart(time_results, memory_results, dataset_names)
    create_memory_chart(time_results, memory_results, dataset_names)

def worst_case():
    data_length = 50_000_000
    print("start data generating")
    m = [i for i in range(2, data_length, 2)] # четные 2 4 6 8
    n = [i for i in range(3, data_length, 2)] #нечетные 3 5 7 9
    print("data is generated")
    common = m[-1] + 150
    m.append(common)
    n.append(common) # худший случай для всех - общий максимум в конце, i-й элемент m < i-го элемента n + разная четность для m[i] и n[i]
    sol = Solution(m, n)

    res1, time1, memory1 = sol.two_pointers()
    print(f"Two Pointers - Результат: {res1}, Время: {time1}сек, Память: {memory1}КБ\n")
    res2, time2, memory2 = sol.binary_search()
    print(f"Binary Search - Результат: {res2}, Время: {time2}сек, Память: {memory2}КБ\n")
    res3, time3, memory3 = sol.exponential_search()
    print(f"Exponential Search - Результат: {res3}, Время: {time3}сек, Память: {memory3}КБ\n")
    res4, time4, memory4 = sol.binary_divide()
    print(f"Binary Divide - Результат: {res4}, Время: {time4}сек, Память: {memory4}КБ\n")

    algorithms = ["Two Pointers", "Binary Search", "Exponential Search", "Binary Divide"]
    times = [time1, time2, time3, time4]
    memories = [memory1, memory2, memory3, memory4]

    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=("Время выполнения", "Используемая память"),
        specs=[[{"type": "bar"}, {"type": "bar"}]]
    )

    fig.add_trace(
        go.Bar(
            x=algorithms,
            y=times,
            name="Время (сек)",
            text=times,
            textposition="auto"
        ),
        row=1, col=1
    )

    fig.add_trace(
        go.Bar(
            x=algorithms,
            y=memories,
            name="Память (КБ)",
            text=memories,
            textposition="auto"
        ),
        row=1, col=2
    )

    fig.update_xaxes(title_text="Алгоритм", row=1, col=1)
    fig.update_yaxes(title_text="Время (сек)", row=1, col=1)

    fig.update_xaxes(title_text="Алгоритм", row=1, col=2)
    fig.update_yaxes(title_text="Память (КБ)", row=1, col=2)

    fig.update_layout(
        title_text="Худший случай: Время и Память",
        height=500,
        showlegend=True
    )

    fig.write_html(os.path.join("charts", "worst_case.html"))