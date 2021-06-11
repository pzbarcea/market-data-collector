# market-data-collector
Collects market data using ETrade's api and stores them for later use and analysis

# Important:
Currently this tool only works for collecting Historical data for 1 second time interval candlestick charts from US stock exchanges. Will update for more functionality in the future.
Future plans include: live data collection, functionality for different time intervals, and functionality for different chart types.

# How To Use:
- Go to this site for Historical data: https://www.dukascopy.com/swiss/english/marketwatch/historical/
- In the widget, scroll to Stocks(CFD) and select US.
- From there, scroll through the list and select one of the stocks that are tracked for historical data. Alternatively, use the search function at the top right of the widget to search for a specific stock ticker.
- After selecting your specific stock, look towards the bottom of the widget. Where it says "Candlestick:" select 1 and then change the drop-down menu from "Tick" to Second.
- The rest of the settings are up to you. Choose your desired date, and choose BID or ASK. For day start time, I recommend using UTC and Local.
- Click download. You will need to create a free account (most likely to verify you are not a bot)
- After clicking download wait as the CSV file is generated for you. Click save as .csv to download the file to your computer.
- Download as many files as you want, then move them to the same directory as file_renamer.py
- Run file_renamer.py using python
- Your files should all have the same clean name now
