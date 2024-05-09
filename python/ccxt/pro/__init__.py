# -*- coding: utf-8 -*-

"""CCXT: CryptoCurrency eXchange Trading Library (Async)"""

# ----------------------------------------------------------------------------

__version__ = '4.3.18'

# ----------------------------------------------------------------------------

from ccxt_versions.v_4_3_18.async_support.base.exchange import Exchange  # noqa: F401

# CCXT Pro exchanges (now this is mainly used for importing exchanges in WS tests)

from ccxt_versions.v_4_3_18.pro.alpaca import alpaca                                        # noqa: F401
from ccxt_versions.v_4_3_18.pro.ascendex import ascendex                                    # noqa: F401
from ccxt_versions.v_4_3_18.pro.bequant import bequant                                      # noqa: F401
from ccxt_versions.v_4_3_18.pro.binance import binance                                      # noqa: F401
from ccxt_versions.v_4_3_18.pro.binancecoinm import binancecoinm                            # noqa: F401
from ccxt_versions.v_4_3_18.pro.binanceus import binanceus                                  # noqa: F401
from ccxt_versions.v_4_3_18.pro.binanceusdm import binanceusdm                              # noqa: F401
from ccxt_versions.v_4_3_18.pro.bingx import bingx                                          # noqa: F401
from ccxt_versions.v_4_3_18.pro.bitcoincom import bitcoincom                                # noqa: F401
from ccxt_versions.v_4_3_18.pro.bitfinex import bitfinex                                    # noqa: F401
from ccxt_versions.v_4_3_18.pro.bitfinex2 import bitfinex2                                  # noqa: F401
from ccxt_versions.v_4_3_18.pro.bitget import bitget                                        # noqa: F401
from ccxt_versions.v_4_3_18.pro.bithumb import bithumb                                      # noqa: F401
from ccxt_versions.v_4_3_18.pro.bitmart import bitmart                                      # noqa: F401
from ccxt_versions.v_4_3_18.pro.bitmex import bitmex                                        # noqa: F401
from ccxt_versions.v_4_3_18.pro.bitopro import bitopro                                      # noqa: F401
from ccxt_versions.v_4_3_18.pro.bitpanda import bitpanda                                    # noqa: F401
from ccxt_versions.v_4_3_18.pro.bitrue import bitrue                                        # noqa: F401
from ccxt_versions.v_4_3_18.pro.bitstamp import bitstamp                                    # noqa: F401
from ccxt_versions.v_4_3_18.pro.bitvavo import bitvavo                                      # noqa: F401
from ccxt_versions.v_4_3_18.pro.blockchaincom import blockchaincom                          # noqa: F401
from ccxt_versions.v_4_3_18.pro.bybit import bybit                                          # noqa: F401
from ccxt_versions.v_4_3_18.pro.cex import cex                                              # noqa: F401
from ccxt_versions.v_4_3_18.pro.coinbase import coinbase                                    # noqa: F401
from ccxt_versions.v_4_3_18.pro.coinbaseinternational import coinbaseinternational          # noqa: F401
from ccxt_versions.v_4_3_18.pro.coinbasepro import coinbasepro                              # noqa: F401
from ccxt_versions.v_4_3_18.pro.coincheck import coincheck                                  # noqa: F401
from ccxt_versions.v_4_3_18.pro.coinex import coinex                                        # noqa: F401
from ccxt_versions.v_4_3_18.pro.coinone import coinone                                      # noqa: F401
from ccxt_versions.v_4_3_18.pro.cryptocom import cryptocom                                  # noqa: F401
from ccxt_versions.v_4_3_18.pro.currencycom import currencycom                              # noqa: F401
from ccxt_versions.v_4_3_18.pro.deribit import deribit                                      # noqa: F401
from ccxt_versions.v_4_3_18.pro.exmo import exmo                                            # noqa: F401
from ccxt_versions.v_4_3_18.pro.gate import gate                                            # noqa: F401
from ccxt_versions.v_4_3_18.pro.gateio import gateio                                        # noqa: F401
from ccxt_versions.v_4_3_18.pro.gemini import gemini                                        # noqa: F401
from ccxt_versions.v_4_3_18.pro.hitbtc import hitbtc                                        # noqa: F401
from ccxt_versions.v_4_3_18.pro.hollaex import hollaex                                      # noqa: F401
from ccxt_versions.v_4_3_18.pro.htx import htx                                              # noqa: F401
from ccxt_versions.v_4_3_18.pro.huobi import huobi                                          # noqa: F401
from ccxt_versions.v_4_3_18.pro.huobijp import huobijp                                      # noqa: F401
from ccxt_versions.v_4_3_18.pro.hyperliquid import hyperliquid                              # noqa: F401
from ccxt_versions.v_4_3_18.pro.idex import idex                                            # noqa: F401
from ccxt_versions.v_4_3_18.pro.independentreserve import independentreserve                # noqa: F401
from ccxt_versions.v_4_3_18.pro.kraken import kraken                                        # noqa: F401
from ccxt_versions.v_4_3_18.pro.krakenfutures import krakenfutures                          # noqa: F401
from ccxt_versions.v_4_3_18.pro.kucoin import kucoin                                        # noqa: F401
from ccxt_versions.v_4_3_18.pro.kucoinfutures import kucoinfutures                          # noqa: F401
from ccxt_versions.v_4_3_18.pro.lbank import lbank                                          # noqa: F401
from ccxt_versions.v_4_3_18.pro.luno import luno                                            # noqa: F401
from ccxt_versions.v_4_3_18.pro.mexc import mexc                                            # noqa: F401
from ccxt_versions.v_4_3_18.pro.ndax import ndax                                            # noqa: F401
from ccxt_versions.v_4_3_18.pro.okcoin import okcoin                                        # noqa: F401
from ccxt_versions.v_4_3_18.pro.okx import okx                                              # noqa: F401
from ccxt_versions.v_4_3_18.pro.onetrading import onetrading                                # noqa: F401
from ccxt_versions.v_4_3_18.pro.p2b import p2b                                              # noqa: F401
from ccxt_versions.v_4_3_18.pro.phemex import phemex                                        # noqa: F401
from ccxt_versions.v_4_3_18.pro.poloniex import poloniex                                    # noqa: F401
from ccxt_versions.v_4_3_18.pro.poloniexfutures import poloniexfutures                      # noqa: F401
from ccxt_versions.v_4_3_18.pro.probit import probit                                        # noqa: F401
from ccxt_versions.v_4_3_18.pro.upbit import upbit                                          # noqa: F401
from ccxt_versions.v_4_3_18.pro.wazirx import wazirx                                        # noqa: F401
from ccxt_versions.v_4_3_18.pro.whitebit import whitebit                                    # noqa: F401
from ccxt_versions.v_4_3_18.pro.woo import woo                                              # noqa: F401

exchanges = [
    'alpaca',
    'ascendex',
    'bequant',
    'binance',
    'binancecoinm',
    'binanceus',
    'binanceusdm',
    'bingx',
    'bitcoincom',
    'bitfinex',
    'bitfinex2',
    'bitget',
    'bithumb',
    'bitmart',
    'bitmex',
    'bitopro',
    'bitpanda',
    'bitrue',
    'bitstamp',
    'bitvavo',
    'blockchaincom',
    'bybit',
    'cex',
    'coinbase',
    'coinbaseinternational',
    'coinbasepro',
    'coincheck',
    'coinex',
    'coinone',
    'cryptocom',
    'currencycom',
    'deribit',
    'exmo',
    'gate',
    'gateio',
    'gemini',
    'hitbtc',
    'hollaex',
    'htx',
    'huobi',
    'huobijp',
    'hyperliquid',
    'idex',
    'independentreserve',
    'kraken',
    'krakenfutures',
    'kucoin',
    'kucoinfutures',
    'lbank',
    'luno',
    'mexc',
    'ndax',
    'okcoin',
    'okx',
    'onetrading',
    'p2b',
    'phemex',
    'poloniex',
    'poloniexfutures',
    'probit',
    'upbit',
    'wazirx',
    'whitebit',
    'woo',
]
