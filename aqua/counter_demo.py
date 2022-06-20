from collections import Counter
#//ใช้ Counter ในการนับความถี่ของข้อมูล//

def tally():
    orders = ["mocha", "latte", "mocha", "espresso", "americano", "latte", "mocha", "espresso"]
    cnt = {}
    for s in orders:
        if s in cnt:
            cnt[s] += 1
        else:
            cnt[s] = 1
    print(cnt)

def Count_tally():
    orders = ["mocha", "latte", "mocha", "espresso", "americano", "latte", "mocha", "espresso"]
    cnt = Counter(orders)
    print(cnt)
    print(cnt["mocha"])

def tally2():
    s = "HHHTHHTTTTHHHTTTHHHHHTHTH"
    cnt = Counter(s)
    print(cnt)




tally()
# Count_tally()
# tally2()