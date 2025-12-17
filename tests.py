from algorithms import Solution
import random
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def worst_case():
    m, n = [1], [1]
    print("generating data")
    data_length = 50_000_000
    for i in range(data_length):
        term = random.randint(3, 10)
        m.append(m[-1] + term)
    for i in range(data_length):
        n.append(m[-1] + 1)
    common = m[-1] + 150
    m.append(common)
    n.append(common) # худший случай для всех - общий максимум в конце, i-й элемент m < i-го элемента n
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
    fig.update_yaxes(title_text="Время (сек)", type="log", row=1, col=1)

    fig.update_xaxes(title_text="Алгоритм", row=1, col=2)
    fig.update_yaxes(title_text="Память (КБ)", type="log", row=1, col=2)

    fig.update_layout(
        title_text="Худший случай: Время и Память",
        height=500,
        showlegend=True
    )

    fig.write_html(os.path.join("charts", "worst_case.html"))