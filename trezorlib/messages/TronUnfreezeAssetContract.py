# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class TronUnfreezeAssetContract(p.MessageType):
    FIELDS = {
        1: ('owner_address', p.BytesType, 0),
    }

    def __init__(
        self,
        owner_address: bytes = None,
    ) -> None:
        self.owner_address = owner_address
