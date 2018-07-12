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
from trezorlib import messages as proto
from trezorlib.client import CallException
from trezorlib.tools import parse_path


@pytest.mark.tron
@pytest.mark.skip_t1
class TestMsgTronGetaddress(TrezorTest):

    def test_tron_getaddress(self):
        self.client.load_device_by_mnemonic(
            mnemonic='abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about',
            pin='',
            passphrase_protection=False,
            label='test',
            language='english')

        assert self.client.tron_get_address(parse_path("m/44'/195'/0'/0/0")) == 'TUEZSdKsoDHQMeZwihtdoBiN46zxhGWYdH'
