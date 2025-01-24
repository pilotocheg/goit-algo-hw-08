import heapq

# Уявіть, що вам на технічному інтерв'ю дають наступну задачу,
# яку треба розв'язати за допомогою купи.

# Є декілька мережевих кабелів різної довжини,
# їх потрібно об'єднати по два за раз в один кабель,
# використовуючи з'єднувачі, у порядку, який призведе до найменших витрат.
# Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин,
# а загальні витрати дорівнюють сумі з'єднання всіх кабелів.
# Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.

cabels = [42, 40, 30, 20, 10]


def min_cost(cabels: list[int]):
    heapq.heapify(cabels)
    total_cost = 0

    while len(cabels) > 1:
        first = heapq.heappop(cabels)
        second = heapq.heappop(cabels)

        result = first + second
        total_cost += result

        heapq.heappush(cabels, result)

    return total_cost


print("Total cost: ", min_cost(cabels))
