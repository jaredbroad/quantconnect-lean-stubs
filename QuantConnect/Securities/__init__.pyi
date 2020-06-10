class SecurityPortfolioManager:
    '''
    Portfolio manager class groups popular properties and makes them accessible through one interface.
    It also provide indexing by the vehicle symbol to get the Security.Holding objects.
    '''
    Invested: bool