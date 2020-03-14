def initialize(context):
    context.stocks = [sid(24), sid(46632), sid(16841), sid(39840), sid(19725), sid(5061), sid(351)]
    context.stocks_weight = 1.0 / len(context.stocks)

    schedule_function(trading, 
                      date_rules.every_day(), 
                      time_rules.market_open(hours=1))
    
    
def trading(context, data):
    for stock in context.stocks:
        hist = data.history(stock, 'price', 50, '1d')

        sma_50 = hist.mean()
        sma_20 = hist[-20:].mean()
        
        open_orders = get_open_orders()
        
        if stock not in open_orders and data.can_trade(stock):
            if sma_20 > sma_50:
                order_target_percent(stock, context.stocks_weight)
            elif sma_20 < sma_50:
                order_target_percent(stock, -context.stocks_weight)