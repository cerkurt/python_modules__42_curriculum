def recursive_harvest(n, time) -> None:
    if n == time:
        print("Day", time)
        print("Harvest time!")
    else:
        print("Day", n)
        recursive_harvest(n + 1, time)


def ft_count_harvest_recursive() -> None:
    time = int(input("Days until harvest: "))
    recursive_harvest(1, time)
