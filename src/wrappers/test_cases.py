import random


class TestCases:
    def _set_seed(self, seed: int | None = None) -> None:
        if seed is not None:
            random.seed(seed)

    def rand_int_array(
        self,
        n: int,
        lo: int,
        hi: int,
        distinct: bool = False,
        seed: int | None = None,
    ) -> list[int]:
        self._set_seed(seed)

        if distinct:
            return random.sample(range(lo, hi + 1), n)

        return [random.randint(lo, hi) for _ in range(n)]

    def rand_float_array(
        self, n: int, lo: float = 0.0, hi: float = 1.0, seed: int | None = None
    ) -> list[float]:
        self._set_seed(seed)
        return [random.uniform(lo, hi) for _ in range(n)]

    def nearly_sorted(
        self, n: int, swaps: int, seed: int | None = None
    ) -> list[int]:
        self._set_seed(seed)
        array = list(range(n))

        for _ in range(swaps):
            i = random.randint(0, n - 1)
            j = random.randint(0, n - 1)
            array[i], array[j] = array[j], array[i]

        return array

    def reverse_sorted(self, n: int) -> list[int]:
        return list(range(n - 1, -1, -1))

    def many_duplicates(
        self, n: int, k_unique: int = 5, seed: int | None = None
    ) -> list[int]:
        self._set_seed(seed)
        unique_values = list(range(k_unique))
        return [random.choice(unique_values) for _ in range(n)]
