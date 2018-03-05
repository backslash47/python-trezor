# Automatically generated by pb2py
from __future__ import absolute_import
from .. import protobuf as p
from .StellarAssetType import StellarAssetType


class StellarChangeTrustOp(p.MessageType):
    FIELDS = {
        1: ('source_account', p.BytesType, 0),
        2: ('asset', StellarAssetType, 0),
        3: ('limit', p.UVarintType, 0),
    }
    MESSAGE_WIRE_TYPE = 216
