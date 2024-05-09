# -*- coding: utf-8 -*-

"""CCXT: CryptoCurrency eXchange Trading Library"""

# MIT License
# Copyright (c) 2017 Igor Kroitor
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# ----------------------------------------------------------------------------

__version__ = '4.3.18'

# ----------------------------------------------------------------------------

from ccxt_versions.v_4_3_18.base.exchange import Exchange                     # noqa: F401
from ccxt_versions.v_4_3_18.base.precise import Precise                       # noqa: F401

from ccxt_versions.v_4_3_18.base.decimal_to_precision import decimal_to_precision  # noqa: F401
from ccxt_versions.v_4_3_18.base.decimal_to_precision import TRUNCATE              # noqa: F401
from ccxt_versions.v_4_3_18.base.decimal_to_precision import ROUND                 # noqa: F401
from ccxt_versions.v_4_3_18.base.decimal_to_precision import ROUND_UP              # noqa: F401
from ccxt_versions.v_4_3_18.base.decimal_to_precision import ROUND_DOWN            # noqa: F401
from ccxt_versions.v_4_3_18.base.decimal_to_precision import DECIMAL_PLACES        # noqa: F401
from ccxt_versions.v_4_3_18.base.decimal_to_precision import SIGNIFICANT_DIGITS    # noqa: F401
from ccxt_versions.v_4_3_18.base.decimal_to_precision import TICK_SIZE             # noqa: F401
from ccxt_versions.v_4_3_18.base.decimal_to_precision import NO_PADDING            # noqa: F401
from ccxt_versions.v_4_3_18.base.decimal_to_precision import PAD_WITH_ZERO         # noqa: F401

from ccxt_versions.v_4_3_18.base import errors
from ccxt_versions.v_4_3_18.base.errors import BaseError                                # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import ExchangeError                            # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import AuthenticationError                      # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import PermissionDenied                         # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import AccountNotEnabled                        # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import AccountSuspended                         # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import ArgumentsRequired                        # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import BadRequest                               # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import BadSymbol                                # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import OperationRejected                        # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import NoChange                                 # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import MarginModeAlreadySet                     # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import MarketClosed                             # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import BadResponse                              # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import NullResponse                             # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import InsufficientFunds                        # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import InvalidAddress                           # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import AddressPending                           # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import InvalidOrder                             # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import OrderNotFound                            # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import OrderNotCached                           # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import CancelPending                            # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import OrderImmediatelyFillable                 # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import OrderNotFillable                         # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import DuplicateOrderId                         # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import ContractUnavailable                      # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import NotSupported                             # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import ProxyError                               # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import ExchangeClosedByUser                     # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import OperationFailed                          # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import NetworkError                             # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import DDoSProtection                           # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import RateLimitExceeded                        # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import ExchangeNotAvailable                     # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import OnMaintenance                            # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import InvalidNonce                             # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import RequestTimeout                           # noqa: F401
from ccxt_versions.v_4_3_18.base.errors import error_hierarchy                          # noqa: F401

from ccxt_versions.v_4_3_18.ace import ace                                              # noqa: F401
from ccxt_versions.v_4_3_18.alpaca import alpaca                                        # noqa: F401
from ccxt_versions.v_4_3_18.ascendex import ascendex                                    # noqa: F401
from ccxt_versions.v_4_3_18.bequant import bequant                                      # noqa: F401
from ccxt_versions.v_4_3_18.bigone import bigone                                        # noqa: F401
from ccxt_versions.v_4_3_18.binance import binance                                      # noqa: F401
from ccxt_versions.v_4_3_18.binancecoinm import binancecoinm                            # noqa: F401
from ccxt_versions.v_4_3_18.binanceus import binanceus                                  # noqa: F401
from ccxt_versions.v_4_3_18.binanceusdm import binanceusdm                              # noqa: F401
from ccxt_versions.v_4_3_18.bingx import bingx                                          # noqa: F401
from ccxt_versions.v_4_3_18.bit2c import bit2c                                          # noqa: F401
from ccxt_versions.v_4_3_18.bitbank import bitbank                                      # noqa: F401
from ccxt_versions.v_4_3_18.bitbay import bitbay                                        # noqa: F401
from ccxt_versions.v_4_3_18.bitbns import bitbns                                        # noqa: F401
from ccxt_versions.v_4_3_18.bitcoincom import bitcoincom                                # noqa: F401
from ccxt_versions.v_4_3_18.bitfinex import bitfinex                                    # noqa: F401
from ccxt_versions.v_4_3_18.bitfinex2 import bitfinex2                                  # noqa: F401
from ccxt_versions.v_4_3_18.bitflyer import bitflyer                                    # noqa: F401
from ccxt_versions.v_4_3_18.bitget import bitget                                        # noqa: F401
from ccxt_versions.v_4_3_18.bithumb import bithumb                                      # noqa: F401
from ccxt_versions.v_4_3_18.bitmart import bitmart                                      # noqa: F401
from ccxt_versions.v_4_3_18.bitmex import bitmex                                        # noqa: F401
from ccxt_versions.v_4_3_18.bitopro import bitopro                                      # noqa: F401
from ccxt_versions.v_4_3_18.bitpanda import bitpanda                                    # noqa: F401
from ccxt_versions.v_4_3_18.bitrue import bitrue                                        # noqa: F401
from ccxt_versions.v_4_3_18.bitso import bitso                                          # noqa: F401
from ccxt_versions.v_4_3_18.bitstamp import bitstamp                                    # noqa: F401
from ccxt_versions.v_4_3_18.bitteam import bitteam                                      # noqa: F401
from ccxt_versions.v_4_3_18.bitvavo import bitvavo                                      # noqa: F401
from ccxt_versions.v_4_3_18.bl3p import bl3p                                            # noqa: F401
from ccxt_versions.v_4_3_18.blockchaincom import blockchaincom                          # noqa: F401
from ccxt_versions.v_4_3_18.blofin import blofin                                        # noqa: F401
from ccxt_versions.v_4_3_18.btcalpha import btcalpha                                    # noqa: F401
from ccxt_versions.v_4_3_18.btcbox import btcbox                                        # noqa: F401
from ccxt_versions.v_4_3_18.btcmarkets import btcmarkets                                # noqa: F401
from ccxt_versions.v_4_3_18.btcturk import btcturk                                      # noqa: F401
from ccxt_versions.v_4_3_18.bybit import bybit                                          # noqa: F401
from ccxt_versions.v_4_3_18.cex import cex                                              # noqa: F401
from ccxt_versions.v_4_3_18.coinbase import coinbase                                    # noqa: F401
from ccxt_versions.v_4_3_18.coinbaseinternational import coinbaseinternational          # noqa: F401
from ccxt_versions.v_4_3_18.coinbasepro import coinbasepro                              # noqa: F401
from ccxt_versions.v_4_3_18.coincheck import coincheck                                  # noqa: F401
from ccxt_versions.v_4_3_18.coinex import coinex                                        # noqa: F401
from ccxt_versions.v_4_3_18.coinlist import coinlist                                    # noqa: F401
from ccxt_versions.v_4_3_18.coinmate import coinmate                                    # noqa: F401
from ccxt_versions.v_4_3_18.coinmetro import coinmetro                                  # noqa: F401
from ccxt_versions.v_4_3_18.coinone import coinone                                      # noqa: F401
from ccxt_versions.v_4_3_18.coinsph import coinsph                                      # noqa: F401
from ccxt_versions.v_4_3_18.coinspot import coinspot                                    # noqa: F401
from ccxt_versions.v_4_3_18.cryptocom import cryptocom                                  # noqa: F401
from ccxt_versions.v_4_3_18.currencycom import currencycom                              # noqa: F401
from ccxt_versions.v_4_3_18.delta import delta                                          # noqa: F401
from ccxt_versions.v_4_3_18.deribit import deribit                                      # noqa: F401
from ccxt_versions.v_4_3_18.digifinex import digifinex                                  # noqa: F401
from ccxt_versions.v_4_3_18.exmo import exmo                                            # noqa: F401
from ccxt_versions.v_4_3_18.fmfwio import fmfwio                                        # noqa: F401
from ccxt_versions.v_4_3_18.gate import gate                                            # noqa: F401
from ccxt_versions.v_4_3_18.gateio import gateio                                        # noqa: F401
from ccxt_versions.v_4_3_18.gemini import gemini                                        # noqa: F401
from ccxt_versions.v_4_3_18.hitbtc import hitbtc                                        # noqa: F401
from ccxt_versions.v_4_3_18.hitbtc3 import hitbtc3                                      # noqa: F401
from ccxt_versions.v_4_3_18.hollaex import hollaex                                      # noqa: F401
from ccxt_versions.v_4_3_18.htx import htx                                              # noqa: F401
from ccxt_versions.v_4_3_18.huobi import huobi                                          # noqa: F401
from ccxt_versions.v_4_3_18.huobijp import huobijp                                      # noqa: F401
from ccxt_versions.v_4_3_18.hyperliquid import hyperliquid                              # noqa: F401
from ccxt_versions.v_4_3_18.idex import idex                                            # noqa: F401
from ccxt_versions.v_4_3_18.independentreserve import independentreserve                # noqa: F401
from ccxt_versions.v_4_3_18.indodax import indodax                                      # noqa: F401
from ccxt_versions.v_4_3_18.kraken import kraken                                        # noqa: F401
from ccxt_versions.v_4_3_18.krakenfutures import krakenfutures                          # noqa: F401
from ccxt_versions.v_4_3_18.kucoin import kucoin                                        # noqa: F401
from ccxt_versions.v_4_3_18.kucoinfutures import kucoinfutures                          # noqa: F401
from ccxt_versions.v_4_3_18.kuna import kuna                                            # noqa: F401
from ccxt_versions.v_4_3_18.latoken import latoken                                      # noqa: F401
from ccxt_versions.v_4_3_18.lbank import lbank                                          # noqa: F401
from ccxt_versions.v_4_3_18.luno import luno                                            # noqa: F401
from ccxt_versions.v_4_3_18.lykke import lykke                                          # noqa: F401
from ccxt_versions.v_4_3_18.mercado import mercado                                      # noqa: F401
from ccxt_versions.v_4_3_18.mexc import mexc                                            # noqa: F401
from ccxt_versions.v_4_3_18.ndax import ndax                                            # noqa: F401
from ccxt_versions.v_4_3_18.novadax import novadax                                      # noqa: F401
from ccxt_versions.v_4_3_18.oceanex import oceanex                                      # noqa: F401
from ccxt_versions.v_4_3_18.okcoin import okcoin                                        # noqa: F401
from ccxt_versions.v_4_3_18.okx import okx                                              # noqa: F401
from ccxt_versions.v_4_3_18.onetrading import onetrading                                # noqa: F401
from ccxt_versions.v_4_3_18.p2b import p2b                                              # noqa: F401
from ccxt_versions.v_4_3_18.paymium import paymium                                      # noqa: F401
from ccxt_versions.v_4_3_18.phemex import phemex                                        # noqa: F401
from ccxt_versions.v_4_3_18.poloniex import poloniex                                    # noqa: F401
from ccxt_versions.v_4_3_18.poloniexfutures import poloniexfutures                      # noqa: F401
from ccxt_versions.v_4_3_18.probit import probit                                        # noqa: F401
from ccxt_versions.v_4_3_18.timex import timex                                          # noqa: F401
from ccxt_versions.v_4_3_18.tokocrypto import tokocrypto                                # noqa: F401
from ccxt_versions.v_4_3_18.tradeogre import tradeogre                                  # noqa: F401
from ccxt_versions.v_4_3_18.upbit import upbit                                          # noqa: F401
from ccxt_versions.v_4_3_18.wavesexchange import wavesexchange                          # noqa: F401
from ccxt_versions.v_4_3_18.wazirx import wazirx                                        # noqa: F401
from ccxt_versions.v_4_3_18.whitebit import whitebit                                    # noqa: F401
from ccxt_versions.v_4_3_18.woo import woo                                              # noqa: F401
from ccxt_versions.v_4_3_18.yobit import yobit                                          # noqa: F401
from ccxt_versions.v_4_3_18.zaif import zaif                                            # noqa: F401
from ccxt_versions.v_4_3_18.zonda import zonda                                          # noqa: F401

exchanges = [
    'ace',
    'alpaca',
    'ascendex',
    'bequant',
    'bigone',
    'binance',
    'binancecoinm',
    'binanceus',
    'binanceusdm',
    'bingx',
    'bit2c',
    'bitbank',
    'bitbay',
    'bitbns',
    'bitcoincom',
    'bitfinex',
    'bitfinex2',
    'bitflyer',
    'bitget',
    'bithumb',
    'bitmart',
    'bitmex',
    'bitopro',
    'bitpanda',
    'bitrue',
    'bitso',
    'bitstamp',
    'bitteam',
    'bitvavo',
    'bl3p',
    'blockchaincom',
    'blofin',
    'btcalpha',
    'btcbox',
    'btcmarkets',
    'btcturk',
    'bybit',
    'cex',
    'coinbase',
    'coinbaseinternational',
    'coinbasepro',
    'coincheck',
    'coinex',
    'coinlist',
    'coinmate',
    'coinmetro',
    'coinone',
    'coinsph',
    'coinspot',
    'cryptocom',
    'currencycom',
    'delta',
    'deribit',
    'digifinex',
    'exmo',
    'fmfwio',
    'gate',
    'gateio',
    'gemini',
    'hitbtc',
    'hitbtc3',
    'hollaex',
    'htx',
    'huobi',
    'huobijp',
    'hyperliquid',
    'idex',
    'independentreserve',
    'indodax',
    'kraken',
    'krakenfutures',
    'kucoin',
    'kucoinfutures',
    'kuna',
    'latoken',
    'lbank',
    'luno',
    'lykke',
    'mercado',
    'mexc',
    'ndax',
    'novadax',
    'oceanex',
    'okcoin',
    'okx',
    'onetrading',
    'p2b',
    'paymium',
    'phemex',
    'poloniex',
    'poloniexfutures',
    'probit',
    'timex',
    'tokocrypto',
    'tradeogre',
    'upbit',
    'wavesexchange',
    'wazirx',
    'whitebit',
    'woo',
    'yobit',
    'zaif',
    'zonda',
]

base = [
    'Exchange',
    'Precise',
    'exchanges',
    'decimal_to_precision',
]

__all__ = base + errors.__all__ + exchanges
