class AlgoPacketError(Exception):
    """
    Базовый класс исключений для пакета алгоритмов.
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
