# Automatically generated by pb2py
from __future__ import absolute_import
from .. import protobuf as p
from .StellarAssetType import StellarAssetType


class StellarManageOfferOp(p.MessageType):
    FIELDS = {
        1: ('source_account', p.BytesType, 0),
        2: ('selling_asset', StellarAssetType, 0),
        3: ('buying_asset', StellarAssetType, 0),
        4: ('amount', p.UVarintType, 0),
        5: ('price_n', p.UVarintType, 0),
        6: ('price_d', p.UVarintType, 0),
        7: ('offer_id', p.UVarintType, 0),
    }
    MESSAGE_WIRE_TYPE = 213
