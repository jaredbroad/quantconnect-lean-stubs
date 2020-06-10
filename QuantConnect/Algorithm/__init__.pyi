from typing import Union
from datetime import datetime, timedelta

from QuantConnect import Resolution, Symbol, Security
from QuantConnect.Data import Slice
from QuantConnect.Securities import SecurityPortfolioManager

_import_use_error_message = "This package should only be used by the Lean engine or Skylight. \nIf you want to run this algorithm locally, please follow the instructions on setting up a Python environment with Lean on GitHub (https://github.com/QuantConnect/Lean/blob/master/Algorithm.Python/readme.md). \nIf you are trying to locally develop an algorithm and want to upload your projects to the QuantConnect cloud terminal, you can use Skylight (https://www.quantconnect.com/skylight) to automatically sync your project."

class QCAlgorithm:
    '''
    QC Algorithm Base Class - Handle the basic requirements of a trading algorithm,
    allowing user to focus on event methods. The QCAlgorithm class implements Portfolio,
    Securities, Transactions and Data Subscription Management.
    '''
    Portfolio: SecurityPortfolioManager

    def Initialize(self) -> None: 
        '''
        Initial stage of an algorithm. Here, we setup any 
        symbols we want to use, as well as potentially define universe settings.
        This method is called only when the algorithm is starting.
        '''
        raise TypeError(_import_use_error_message)

    def SetStartDate(self, year: int, month: int, day: int) -> None:
        '''
        Sets the algorithm's initial starting date.
        In live mode, this method has no effect, and does not affect
        your algorithm's execution.
        '''
        raise TypeError(_import_use_error_message)

    def SetEndDate(self, year: int, month: int, day: int) -> None: 
        '''
        Sets the algorithm's end date.
        In live mode, this method has no effect, and does not affect
        your algorithm's execution.
        '''
        raise TypeError(_import_use_error_message)

    def SetCash(self, starting_cash: int) -> None: 
        '''
        Sets the starting cash for your algorithm in backtesting.
        In live mode, the cash is automatically set to the current
        amount of cash in your brokerage. 
        This method has no effect in live mode, and does not 
        affect your algorithm's execution
        '''
        raise TypeError(_import_use_error_message)

    def AddEquity(self, ticker: str, resolution: Resolution) -> Security:
        '''
        Adds a new equity (stock) to the algorithm.
        You will receive data for this equity in `OnData`
        at the `Resolution` provided to this method.
        '''
        raise TypeError(_import_use_error_message)

    def OnData(self, data: Slice) -> None:
        '''
        Passes new data into your algorithm.
        The `Slice` object will contain all definitions
        for any corporate events that can occur in equities.
        To learn more about the `Slice` object, visit the
        QuantConnect docs page: https://www.quantconnect.com/docs/algorithm-reference/handling-data
        '''
        raise TypeError(_import_use_error_message)

    def SetHoldings(self, symbol: Union[Symbol, str], target: float) -> None:
        '''
        Buys/Sells new assets for the provided Symbol. 
        `target` is a percentage value indicating how
        much of your portfolio you want to buy/sell of the asset.
        The `target` percentage value uses decimal values with
        1.00 equaling 100%.
        '''
        raise TypeError(_import_use_error_message)

    def Log(self, log: str) -> None:
        '''
        Logs the provided value into the terminal
        '''
        raise TypeError(_import_use_error_message)

    def Debug(self, log: str) -> None:
        '''
        Logs the provided value as a debug line
        in the terminal.
        '''
        raise TypeError(_import_use_error_message)

    def Quit(self, message: str) -> None:
        '''
        Quits the algorithm with `message`
        provided as the reason.
        '''
        raise TypeError(_import_use_error_message)

