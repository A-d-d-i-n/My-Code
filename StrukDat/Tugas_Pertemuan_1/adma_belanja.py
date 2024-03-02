N = int(input())  # Amount of goods

goods_w_price = []  # Array for goods & price
goods_alone = []
pick_times = 0  # When Adma pick something up


for i in range(N):
    B,M = map(int, input().split())  # Goods + price
    goods_w_price.append(f"{M} {B}")  # "Goods + price" -> "price + goods"
    
goods_w_price.sort()  # From cheapest to most expensive


loop = 0
for j in range(N):
    M,B = goods_w_price[loop].split()
    goods_alone.append(B)
    loop += 1


X = str(input())  # The stuff she wants

while goods_alone[0] != X:
    goods_alone.pop(0)  # Picking up one by one
    pick_times += 1
    
    if len(goods_alone) == 0:  # There's nothing left
        print("Barangnya ga ada beb")
        break

if len(goods_alone) != 0: print(pick_times)  
# Found X, at *output*th time picking up