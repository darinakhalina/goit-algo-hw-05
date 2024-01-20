import timeit
from typing import Callable
from bm import boyer_moore_search
from kmp import kmp_search
from rabin_karp import rabin_karp_search


def read_file(filename):
    with open(filename, "r", encoding="cp1251") as f:
        return f.read()


def benchmark(func: Callable, text_: str, pattern_: str):
    setup_code = f"from __main__ import {func.__name__}"
    stmt = f"{func.__name__}(text, pattern)"
    times = timeit.repeat(
        stmt=stmt,
        setup=setup_code,
        globals={"text": text_, "pattern": pattern_},
        repeat=5,
        number=10,
    )
    return min(times)


if __name__ == "__main__":
    filenames = {
        "стаття 1.txt": {"real": "вид пошуку вимагає", "fake": "вигаданий рядок 1"},
        "стаття 2.txt": {
            "real": "масив логічних елементів",
            "fake": "вигаданий рядок 2",
        },
    }

    results = []

    for filename, patterns in filenames.items():
        text = read_file(filename)
        for pattern_type, pattern in patterns.items():
            time = benchmark(boyer_moore_search, text, pattern)
            results.append((filename, boyer_moore_search.__name__, pattern_type, time))
            time = benchmark(kmp_search, text, pattern)
            results.append((filename, kmp_search.__name__, pattern_type, time))
            time = benchmark(rabin_karp_search, text, pattern)
            results.append((filename, rabin_karp_search.__name__, pattern_type, time))

    title = f"{'Файл':<20} | {'Алгоритм':<20} | {'Тип підрядка':<15} | {'Час, сек':<10}"
    print(title)
    print("-" * len(title))
    for result in results:
        print(
            f"{result[0]:<20} | {result[1]:<20} | {result[2]:<15} | {result[3]:<10.6f}"
        )
