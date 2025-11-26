from typing import Any, Callable

from src.data_structures.queue import (
    QueueOnLinkedList,
    QueueOnList,
    QueueOnStack,
)
from src.data_structures.stack import (
    StackOnLinkedList,
    StackOnList,
    StackOnQueue,
)
from src.factorial_fibonachi.factorial import Factorial
from src.factorial_fibonachi.fibonachi import Fibonachi
from src.sorts.bubble_sort import BubbleSort
from src.sorts.bucket_sort import BucketSort
from src.sorts.counting_sort import CountingSort
from src.sorts.heap_sort import HeapSort
from src.sorts.quick_sort import QuickSort
from src.sorts.radix_sort import RadixSort
from src.utils.base import BaseQueue, BaseStack

cmp_map: dict[str, Callable[[Any, Any], int] | None] = {
    "default": None,
    "reverse": lambda a, b: (b > a) - (b < a),
}

key_map: dict[str, Callable[[Any], Any] | None] = {
    "default": None,
    "abs": abs,
    "len": len,
}

sort_command_map: dict[str, Callable[..., list[Any]]] = {
    "Bubble-sort": BubbleSort.execute,
    "Bucket-sort": BucketSort.execute,
    "Counting-sort": CountingSort.execute,
    "Heap-sort": HeapSort.execute,
    "Quick-sort": QuickSort.execute,
    "Radix-sort": RadixSort.execute,
}

stack_map: dict[str, type[BaseStack]] = {
    "list": StackOnList,
    "linked-list": StackOnLinkedList,
    "queue": StackOnQueue,
}

queue_map: dict[str, type[BaseQueue]] = {
    "list": QueueOnList,
    "linked-list": QueueOnLinkedList,
    "stack": QueueOnStack,
}

factorial_map: dict[str, Callable[[int], int]] = {
    "iterative": Factorial.factorial,
    "recursive": Factorial.factorial_recursive,
}

fibonacci_map: dict[str, Callable[[int], int]] = {
    "iterative": Fibonachi.fibo,
    "recursive": Fibonachi.fibo_recursive,
}
