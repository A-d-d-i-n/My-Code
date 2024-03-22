from Calls import RecentCounter

counter_data = RecentCounter()
hasil = [counter_data.ping(1),
counter_data.ping(100),
counter_data.ping(3001),  
counter_data.ping(3002)]

print(hasil)