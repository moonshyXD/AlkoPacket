class AlgoPacketError(Exception):
    """
    Базовый класс исключений для пакета алгоритмов.
    """

    pass


class StackIsEmpty(AlgoPacketError):
    """
    Исключение, вызываемое при попытке выполнить операцию с пустым стеком.
    """

    pass


class QueueIsEmpty(AlgoPacketError):
    """
    Исключение, вызываемое при попытке выполнить операцию с пустой очередью.
    """

    pass


class TestCasesError(AlgoPacketError):
    """
    Исключение, вызываемое при ошибках генерации тестовых данных.
    """

    pass


class InputError(AlgoPacketError):
    """
    Исключение, вызываемое при ошибках ввода данных.
    """

    pass
