from datetime import datetime, timedelta
from typing import List, Tuple, Dict, Union, Iterator, Iterable, overload
from QuantConnect import Symbol

_import_use_error_message = "This package should only be used by the Lean engine or Skylight. \nIf you want to run this algorithm locally, please follow the instructions on setting up a Python environment with Lean on GitHub (https://github.com/QuantConnect/Lean/blob/master/Algorithm.Python/readme.md). \nIf you are trying to locally develop an algorithm and want to upload your projects to the QuantConnect cloud terminal, you can use Skylight (https://www.quantconnect.com/skylight) to automatically sync your project."


class BaseData:
    '''
    Abstract base data class for data in Lean. It is intended to be extended to define
    generic user customizable data types while at the same time implementing the basics of data where possible
    '''
    IsFillForward: bool
    Time: datetime
    EndTime: datetime
    Symbol: 'Symbol'
    Value: float
    Price: float

class Slice:
    '''
    Provides a data structure for all of an algorithm's data at a single time step
    '''
    Keys: List[Symbol]
    Values: List[BaseData]

    def __iter__(self) -> Iterator['DataDictionary']:
        raise TypeError(_import_use_error_message)

    def ContainsKey(self, key: Union[Symbol, str]) -> bool:
        raise TypeError(_import_use_error_message)

    @overload
    def Get(self, data_type: type) -> List['DataDictionary']:
        '''
        Gets the data of the specified type
        '''
        raise TypeError(_import_use_error_message)

    @overload
    def Get(self, data_type: type, symbol: Union[Symbol, str]) -> BaseData:
        '''
        Gets the data of the specified type and symbol
        '''
        raise TypeError(_import_use_error_message)

class DataDictionary:
    '''
    Provides a base class for types holding base data instances keyed by symbol
    '''
    Key: Symbol
    Value: BaseData