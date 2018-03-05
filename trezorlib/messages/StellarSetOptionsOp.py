# Automatically generated by pb2py
from __future__ import absolute_import
from .. import protobuf as p


class StellarSetOptionsOp(p.MessageType):
    FIELDS = {
        1: ('source_account', p.BytesType, 0),
        2: ('inflation_destination_account', p.BytesType, 0),
        3: ('clear_flags', p.UVarintType, 0),
        4: ('set_flags', p.UVarintType, 0),
        5: ('master_weight', p.UVarintType, 0),
        6: ('low_threshold', p.UVarintType, 0),
        7: ('medium_threshold', p.UVarintType, 0),
        8: ('high_threshold', p.UVarintType, 0),
        9: ('home_domain', p.UnicodeType, 0),
        10: ('signer_type', p.UVarintType, 0),
        11: ('signer_key', p.BytesType, 0),
        12: ('signer_weight', p.UVarintType, 0),
    }
    MESSAGE_WIRE_TYPE = 215
