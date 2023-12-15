from binance_historical_data import BinanceDataDumper
data_dumper = BinanceDataDumper(
    path_dir_where_to_dump=".",
    asset_class="spot",  # spot, um, cm
    data_type="klines",  # aggTrades, klines, trades
    data_frequency="5m",
)

data_dumper.dump_data(
    tickers='BTCUSDT',
    date_start=None,
    date_end=None,
    is_to_update_existing=False,
    tickers_to_exclude=["UST"],
)
