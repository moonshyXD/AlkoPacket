class AlgoPacketError(Exception):
    pass


class StackIsEmpty(AlgoPacketError):
    pass


class QueueIsEmpty(AlgoPacketError):
    pass


class TestCasesError(AlgoPacketError):
    pass
