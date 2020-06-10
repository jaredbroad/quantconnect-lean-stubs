from enum import Enum
from datetime import datetime


class Resolution(Enum):
    '''
    Resolution of the data requested.
    '''
    Tick = 0
    Second = 1
    Minute = 2
    Hour = 3
    Daily = 4

class Security:
    '''
    A base vehicle properties class for providing a common interface to all assets in QuantConnect.
    '''
    Symbol: 'Symbol'

class SecurityIdentifier:
    '''
    Defines a unique identifier for securities
    '''
    Symbol: str
    Date: datetime
    Market: str
    SecurityType: 'SecurityType'

class SecurityType(Enum):
    '''
    Type of tradable security / underlying asset
    '''
    Base = 0
    Equity = 1
    Option = 2
    Commodity = 3
    Forex = 4
    Future = 5
    Cfd = 6
    Crypto = 7

class Symbol:
    '''
    Represents a unique security identifier. This is made of two components,
    the unique SID and the Value. The value is the current ticker symbol while
    the SID is constant over the life of a security
    '''
    Value: str
    ID: SecurityIdentifier
    Underlying: 'Symbol'
    SecurityType: 'SecurityType'

