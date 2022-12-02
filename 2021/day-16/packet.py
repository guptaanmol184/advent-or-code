class Packet:
    def __init__(self, packet_version: int, type_id: int) -> None:
        self.packet_version = packet_version
        self.type_id = type_id
        self.data = None  # Container for arbritary data


class Literal(Packet):
    def __init__(self, packet_version: int, type_id: int, data) -> None:
        super().__init__(packet_version, type_id)
        self.data = data  # the value of the literal packet [int]


class Operator(Packet):
    def __init__(self, packet_version: int, type_id: int, data: list[Packet]) -> None:
        super().__init__(packet_version, type_id)
        self.data = data  # sub-packets in of this operator packet, List[Packet]
