# This file is part of the Trezor project.
#
# Copyright (C) 2012-2018 SatoshiLabs and contributors
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the License along with this library.
# If not, see <https://www.gnu.org/licenses/lgpl-3.0.html>.

import pytest

from .common import TrezorTest
from .common import TrezorTest
from .conftest import TREZOR_VERSION
from binascii import hexlify, unhexlify
from trezorlib import messages as proto
from trezorlib.client import CallException
from trezorlib.tools import parse_path
import binascii
import base64

TRON_DEFAULT_PATH = "m/44'/195'/0'/0/0"

@pytest.mark.tron
@pytest.mark.skip_t1
class TestMsgTronSigntx(TrezorTest):

    def test_tron_send_trx(self):
        self.client.load_device_by_mnemonic(
            mnemonic='abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about',
            pin='',
            passphrase_protection=False,
            label='test',
            language='english')
        
        transaction = proto.TronTransaction(ref_block_bytes = bytes.fromhex("C565"), ref_block_hash = bytes.fromhex("6CD623DBE83075D8"),
                            expiration = 1528768890000,timestamp = 1528768831987)
        transaction.contract = [proto.TronContract(type=proto.TronContractType.TransferContract,
                        parameter=proto.TronParameter(api="type.googleapis.com/protocol.TransferContract",
                        payload=proto.TronContractMessages(
                                transfer_contract=proto.TronTransferContract(owner_address= b'TUEZSdKsoDHQMeZwihtdoBiN46zxhGWYdH',
                                                to_address =b'TKSXDA8HfE9E1y39RczVQ1ZascUEtaSToF',
                                                amount = 1000000 )
                            )                        
                        ) )]

        signature = self.client.tron_sign_tx(parse_path(TRON_DEFAULT_PATH), transaction)
        assert signature.signature == unhexlify('ff4ea446cae4475a500fdfec4019160a42c7bcef4c5b18ab709a74ef9fcb1f405a1ca978a7f783487d3593bf76e1a43c4ed42e201fcf2ebbc90460103c1b768a01')

    def test_tron_send_token(self):
        self.client.load_device_by_mnemonic(
            mnemonic='abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about',
            pin='',
            passphrase_protection=False,
            label='test',
            language='english')
        
        transaction = proto.TronTransaction(ref_block_bytes = bytes.fromhex("E7C3"), ref_block_hash = bytes.fromhex("69E2ABB19969F1E7"),
                            expiration = 1528997142000,timestamp = 1528997083831)
        transaction.contract = [proto.TronContract(type=proto.TronContractType.TransferAssetContract,
                        parameter=proto.TronParameter(api="type.googleapis.com/protocol.TransferAssetContract",
                        payload=proto.TronContractMessages(
                                transfer_asset_contract=proto.TronTransferAssetContract(asset_name=b'CryptoChainToken', owner_address= b'TUEZSdKsoDHQMeZwihtdoBiN46zxhGWYdH',
                                                to_address =b'THChUb7p2bwY6ReAiJXao6qc2ZGn88T46v',
                                                amount = 1 )
                            )                        
                        ) )]

        signature = self.client.tron_sign_tx(parse_path(TRON_DEFAULT_PATH), transaction)
        assert signature.signature == unhexlify('c3244d575efc0bf11a4a4ac6c24f3d7f195cab200a127382d581a8e4accbf74c2b6f385047350edb00bb4f3455684b2ce6cd73112a7510a2022ebd0201d9b7c700')
