import csv
from io import StringIO
from datetime import datetime

# ETH volumes data
eth_volumes_data = """
"2022-03","2.52 ETH"
"2022-04","1.02 ETH"
"2022-07","0.21 ETH"
"2024-03","0.08 ETH"
"2021-06","0.03 ETH"
"2021-07","0.20 ETH"
"2021-08","0.04 ETH"
"2021-09","0.11 ETH"
"2021-10","0.11 ETH"
"2021-11","0.06 ETH"
"2021-12","0.01 ETH"
"2021-06","0.03 ETH"
"2021-06","0.01 ETH"
"2021-07","0.23 ETH"
"2021-08","0.04 ETH"
"2021-10","0.01 ETH"
"2021-12","0.05 ETH"
"2021-06","0.00 ETH"
"2021-07","0.01 ETH"
"2021-08","0.00 ETH"
"2021-10","0.00 ETH"
"2021-07","0.86 ETH"
"2021-08","2.55 ETH"
"2021-09","0.17 ETH"
"2021-10","0.16 ETH"
"2021-11","0.08 ETH"
"2021-12","0.01 ETH"
"2022-01","0.01 ETH"
"2022-03","0.01 ETH"
"2023-08","8.91 ETH"
"2021-07","0.05 ETH"
"2021-09","0.01 ETH"
"2021-11","0.03 ETH"
"2022-01","0.03 ETH"
"2021-07","0.01 ETH"
"2021-08","0.01 ETH"
"2021-10","0.03 ETH"
"2021-11","0.01 ETH"
"2022-01","0.01 ETH"
"2019-10","0.52 ETH"
"2019-11","5.36 ETH"
"2019-12","3.36 ETH"
"2020-01","5.24 ETH"
"2020-02","3.30 ETH"
"2020-03","9.82 ETH"
"2020-04","9.50 ETH"
"2020-05","54.59 ETH"
"2020-06","5.96 ETH"
"2020-07","4.70 ETH"
"2020-08","0.34 ETH"
"2020-09","3.13 ETH"
"2020-10","4.65 ETH"
"2020-11","7.81 ETH"
"2020-12","2.85 ETH"
"2021-01","3.69 ETH"
"2021-02","7.25 ETH"
"2021-03","98.51 ETH"
"2021-04","8.46 ETH"
"2021-05","1.50 ETH"
"2021-06","1.68 ETH"
"2021-07","3.57 ETH"
"2021-08","27.69 ETH"
"2021-09","3.67 ETH"
"2021-10","21.94 ETH"
"2021-11","8.10 ETH"
"2021-12","25.36 ETH"
"2022-01","4.86 ETH"
"2022-02","1.45 ETH"
"2022-03","1.58 ETH"
"2022-04","1.77 ETH"
"2022-05","0.34 ETH"
"2022-06","1.27 ETH"
"2022-07","0.83 ETH"
"2022-08","0.30 ETH"
"2022-09","0.30 ETH"
"2022-10","1.01 ETH"
"2022-11","0.06 ETH"
"2022-12","2.01 ETH"
"2023-01","14.20 ETH"
"2023-02","4.18 ETH"
"2023-03","0.00 ETH"
"2023-04","0.25 ETH"
"2023-06","0.21 ETH"
"2023-07","0.12 ETH"
"2023-08","0.00 ETH"
"2023-09","0.03 ETH"
"2023-11","0.22 ETH"
"2023-12","0.58 ETH"
"2024-02","0.00 ETH"
"2024-03","0.02 ETH"
"2024-05","0.01 ETH"
"2024-06","0.02 ETH"
"2024-07","0.00 ETH"
"2024-08","1.28 ETH"
"2024-09","0.00 ETH"
"2021-07","0.02 ETH"
"2021-10","0.01 ETH"
"2022-04","0.01 ETH"
"2022-10","0.05 ETH"
"2021-08","1.06 ETH"
"2021-09","0.10 ETH"
"2021-10","0.33 ETH"
"2021-11","0.10 ETH"
"2021-12","0.01 ETH"
"2022-01","0.07 ETH"
"2022-10","0.07 ETH"
"2023-01","0.10 ETH"
"2021-12","0.10 ETH"
"2021-09","0.08 ETH"
"2021-12","0.10 ETH"
"2022-01","0.17 ETH"
"2022-04","0.01 ETH"
"""

# ETH prices data
eth_prices_data = """
2019-12-01,200.9293947877407
2020-01-01,229.39495367897192
2020-02-01,323.6384563864424
2020-03-01,402.63477809326486
2020-04-01,336.25701728651313
2020-05-01,412.5485232074862
2020-06-01,599.2034051698487
2020-07-01,616.0017979134913
2020-08-01,1236.2041731409245
2020-09-01,1866.3714147322837
2020-10-01,1716.9329162894508
2020-11-01,2198.531544922302
2020-12-01,2360.899106212294
2021-01-01,1899.6982955190392
2021-02-01,2014.2122340049366
2021-03-01,3283.817202284697
2021-04-01,3137.5071429835743
2021-05-01,3859.2237676444397
2021-06-01,4317.181504641245
2021-07-01,3850.4365543054396
2021-08-01,3143.3115671606347
2021-09-01,2710.572484964096
2021-10-01,2893.4617796564958
2021-11-01,2988.6213928026136
2021-12-01,2029.5402860219015
2022-01-01,1214.4716549112397
2022-02-01,1372.6159188363388
2022-03-01,1646.9331730951023
2022-04-01,1297.3429632676725
2022-05-01,1294.9383241952974
2022-06-01,1211.174021750855
2022-07-01,1320.383642860818
2022-08-01,1338.9504619661423
2022-09-01,1640.7576533250544
2022-10-01,1566.776732720371
2022-11-01,1788.4232680670714
2022-12-01,1902.6992444172167
2023-01-01,1845.5098123002003
2023-02-01,1918.1494100375064
2023-03-01,1894.126860975001
2023-04-01,1794.2919436572447
2023-05-01,1584.0714361954506
2023-06-01,1574.7253818528143
2023-07-01,1889.105889734754
2023-08-01,2217.8628216766915
2023-09-01,2305.800746759518
2023-10-01,2293.891429678897
2023-11-01,3037.2825822995887
2023-12-01,3327.4616293917593
2024-01-01,3053.7472340509457
2024-02-01,3082.2013530233053
2024-03-01,3583.1389292133667
2024-04-01,3098.541031423556
2024-05-01,2520.254925851683
2024-06-01,2537.470473176252
2024-07-01,2614.2401871498755
2024-08-01,2614.2401871498755
2024-09-01,2614.2401871498755
"""

# Parse ETH volumes
eth_volumes = {}
for line in eth_volumes_data.strip().split("\n"):
    date, volume = line.strip('"').split('","')
    volume = float(volume.replace(" ETH", ""))
    if date in eth_volumes:
        eth_volumes[date] += volume
    else:
        eth_volumes[date] = volume

# Parse ETH prices
eth_prices = {}
reader = csv.reader(StringIO(eth_prices_data.strip()))
for row in reader:
    date = row[0]
    price = float(row[1])
    eth_prices[date] = price

# Calculate total USD value
total_usd = 0
for date, volume in eth_volumes.items():
    year_month = datetime.strptime(date, "%Y-%m")
    price_date = year_month.replace(day=1).strftime("%Y-%m-%d")
    if price_date in eth_prices:
        price = eth_prices[price_date]
        usd_value = volume * price
        total_usd += usd_value
    else:
        print(f"Warning: No price data for {date}")

print(f"Total USD value: ${total_usd:,.2f}")