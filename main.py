from collections import Counter


def sum_numbers(id_customer):
    id_customer = id_customer
    sum = 0
    while id_customer != 0:
        sum = sum + id_customer % 10
        id_customer = id_customer//10
    return sum


def case1():
    n_customers = int(input(print("Введите количество клиентов: ")))
    id_customers = [i for i in range(n_customers)]
    groups = []
    for i in id_customers:
        temp = sum_numbers(i)  # считаем сумму цифр в id
        groups.append(temp)  # группы с повторениями
    print("ID клиентов: ", id_customers)
    print("Группы с повторениями: ", groups)
    counts = Counter(groups)  # считаем уникальные группы и число вхождений в них
    print("Группы:\t", counts.keys())
    print("Число вхождений:\t", counts.values())


def case2():
    n_customers = int(input(print("Введите количество клиентов: ")))
    n_first_id = int(input(print("Введите первый ID в последовательности: ")))
    id_customers = [i for i in range(n_first_id, n_first_id+n_customers)]
    groups = []
    for i in id_customers:
        temp = sum_numbers(i)  # считаем сумму цифр в id
        groups.append(temp)  # группы с повторениями
    print("ID клиентов: ", id_customers)
    print("Группы с повторениями: ", groups)
    counts = Counter(groups)  # считаем уникальные группы и число вхождений в них
    print("Группы:\t", counts.keys())
    print("Число вхождений:\t", counts.values())


def main():
    case1()
    case2()


if __name__ == '__main__':
    main()
