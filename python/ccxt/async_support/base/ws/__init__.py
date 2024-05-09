# -*- coding: utf-8 -*-

from ccxt_versions.v_4_3_18.base import errors

# -----------------------------------------------------------------------------

from ccxt_versions.v_4_3_18.base import decimal_to_precision

from ccxt_versions.v_4_3_18 import BaseError                  # noqa: F401
from ccxt_versions.v_4_3_18 import ExchangeError              # noqa: F401
from ccxt_versions.v_4_3_18 import NotSupported               # noqa: F401
from ccxt_versions.v_4_3_18 import AuthenticationError        # noqa: F401
from ccxt_versions.v_4_3_18 import PermissionDenied           # noqa: F401
from ccxt_versions.v_4_3_18 import AccountSuspended           # noqa: F401
from ccxt_versions.v_4_3_18 import InvalidNonce               # noqa: F401
from ccxt_versions.v_4_3_18 import InsufficientFunds          # noqa: F401
from ccxt_versions.v_4_3_18 import InvalidOrder               # noqa: F401
from ccxt_versions.v_4_3_18 import OrderNotFound              # noqa: F401
from ccxt_versions.v_4_3_18 import OrderNotCached             # noqa: F401
from ccxt_versions.v_4_3_18 import DuplicateOrderId           # noqa: F401
from ccxt_versions.v_4_3_18 import CancelPending              # noqa: F401
from ccxt_versions.v_4_3_18 import NetworkError               # noqa: F401
from ccxt_versions.v_4_3_18 import DDoSProtection             # noqa: F401
from ccxt_versions.v_4_3_18 import RateLimitExceeded          # noqa: F401
from ccxt_versions.v_4_3_18 import RequestTimeout             # noqa: F401
from ccxt_versions.v_4_3_18 import ExchangeNotAvailable       # noqa: F401
from ccxt_versions.v_4_3_18 import OnMaintenance              # noqa: F401
from ccxt_versions.v_4_3_18 import InvalidAddress             # noqa: F401
from ccxt_versions.v_4_3_18 import AddressPending             # noqa: F401
from ccxt_versions.v_4_3_18 import ArgumentsRequired          # noqa: F401
from ccxt_versions.v_4_3_18 import BadRequest                 # noqa: F401
from ccxt_versions.v_4_3_18 import BadResponse                # noqa: F401
from ccxt_versions.v_4_3_18 import NullResponse               # noqa: F401
from ccxt_versions.v_4_3_18 import OrderImmediatelyFillable   # noqa: F401
from ccxt_versions.v_4_3_18 import OrderNotFillable           # noqa: F401


__all__ = decimal_to_precision.__all__ + errors.__all__  # noqa: F405
