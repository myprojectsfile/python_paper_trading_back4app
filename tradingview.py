import tradingview_ta as ta

class Tradingview:
    @staticmethod
    def get_tv_analysis(symbols, interval, exchange="binance", screener='crypto'):
        exchange_symbols = [exchange.lower() + ':' + symbol.lower()
                            for symbol in symbols]
        ta_analysis = ta.get_multiple_analysis(
            screener=screener, interval=interval, symbols=exchange_symbols)

        tv_analysis = []

        for exchange_symbol in exchange_symbols:
            try:
                exchange_symbol_analysis = ta_analysis[exchange_symbol.upper()]
                analysis_object = {
                    'SYMBOL': (exchange_symbol.replace(exchange.lower() + ':', '')).upper(),
                    'SUMMARY': exchange_symbol_analysis.summary,
                    'OSCILLATORS': {
                        'RECOMMENDATION': exchange_symbol_analysis.oscillators['RECOMMENDATION'],
                        'BUY': exchange_symbol_analysis.oscillators['BUY'],
                        'SELL': exchange_symbol_analysis.oscillators['SELL'],
                        'NEUTRAL': exchange_symbol_analysis.oscillators['NEUTRAL']
                    },
                    'MOVING_AVERAGES': {
                        'RECOMMENDATION': exchange_symbol_analysis.moving_averages['RECOMMENDATION'],
                        'BUY': exchange_symbol_analysis.moving_averages['BUY'],
                        'SELL': exchange_symbol_analysis.moving_averages['SELL'],
                        'NEUTRAL': exchange_symbol_analysis.moving_averages['NEUTRAL']
                    }
                }

                tv_analysis.append(analysis_object)

            except AttributeError as e:
                print(
                    f"AttributeError for symbol {exchange_symbol}, in [get_tv_analysis] function {e}")

        return tv_analysis

    @staticmethod
    def get_filtered_analysis(tv_analysis, summary_accept_list, oscillators_accept_list, moving_avg_accept_list):
        filtered_tv_analysis = [
            item for item in tv_analysis if (
                item.get('SUMMARY', {}).get('RECOMMENDATION') in summary_accept_list and
                (
                    item.get('OSCILLATORS', {}).get('RECOMMENDATION') in oscillators_accept_list and
                    item.get('MOVING_AVERAGES', {}).get(
                        'RECOMMENDATION') in moving_avg_accept_list
                )
            )
        ]
        return filtered_tv_analysis

    @staticmethod
    def get_filtered_analysis_pairs(tv_analysis, summary_accept_list, oscillators_accept_list, moving_avg_accept_list):
        filtered_tv_analysis = [
            item['SYMBOL'] for item in tv_analysis if (
                item.get('SUMMARY', {}).get('RECOMMENDATION') in summary_accept_list and
                (
                    item.get('OSCILLATORS', {}).get('RECOMMENDATION') in oscillators_accept_list and
                    item.get('MOVING_AVERAGES', {}).get(
                        'RECOMMENDATION') in moving_avg_accept_list
                )
            )
        ]

        return filtered_tv_analysis

    @staticmethod
    def get_buy_sell_pairs(symbols):
        _1m_analysis = Tradingview.get_tv_analysis(
            symbols=symbols, interval=ta.Interval.INTERVAL_1_MINUTE)
        _5m_analysis = Tradingview.get_tv_analysis(
            symbols=symbols, interval=ta.Interval.INTERVAL_5_MINUTES)
        _15m_analysis = Tradingview.get_tv_analysis(
            symbols=symbols, interval=ta.Interval.INTERVAL_15_MINUTES)

        _1m_buy_pairs = Tradingview.get_filtered_analysis_pairs(_1m_analysis, {'STRONG_BUY', 'BUY'},
                                                                {'STRONG_BUY', 'BUY'}, {'STRONG_BUY', 'BUY'})
        _1m_sell_pairs = Tradingview.get_filtered_analysis_pairs(_1m_analysis, {'STRONG_SELL', 'SELL'},
                                                                 {'STRONG_SELL', 'SELL'}, {'STRONG_SELL', 'SELL'})

        _5m_strong_buy_pairs = Tradingview.get_filtered_analysis_pairs(_5m_analysis, {'STRONG_BUY'},
                                                                       {'STRONG_BUY', 'BUY'}, {'STRONG_BUY', 'BUY'})
        _5m_strong_sell_pairs = Tradingview.get_filtered_analysis_pairs(_5m_analysis, {'STRONG_SELL'},
                                                                        {'STRONG_SELL', 'SELL'}, {'STRONG_SELL', 'SELL'})

        _15m_buy_pairs = Tradingview.get_filtered_analysis_pairs(_15m_analysis, {'STRONG_BUY', 'BUY'},
                                                                 {'STRONG_BUY', 'BUY'}, {'STRONG_BUY', 'BUY'})
        _15m_sell_pairs = Tradingview.get_filtered_analysis_pairs(_15m_analysis, {'STRONG_SELL', 'SELL'},
                                                                  {'STRONG_SELL', 'SELL'}, {'STRONG_SELL', 'SELL'})

        # Find the common pairs in all three arrays
        buy_pairs = list(set(_1m_buy_pairs) & set(
            _5m_strong_buy_pairs) & set(_15m_buy_pairs))
        sell_pairs = list(set(_1m_sell_pairs) & set(
            _5m_strong_sell_pairs) & set(_15m_sell_pairs))

        return {'buy_pairs': buy_pairs, 'sell_pairs': sell_pairs}
