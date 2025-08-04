grades = [12,16,60,88,74]
# list(可變動資料)用[]  tuple(不可變動資料) 用()
#print(grades[1:4])  # 索引1-4,不包含索引4
#grades [1:4] = []  # 把索引1:4(不含索引4)刪除,list只剩頭尾
#len(grades)  # grades 這個列表的長度
data = [[3,4,5],[6,7,8]]
#print(data[0][2]) # data的第一個索引(指的是[3,4,5]內的索引2
#print(data[1])
#data[0][0:2]=[5,5,5] # list 把第一個索引的索引0和索引0:2不含2的數字換成5
#data(3,4,5)
#data[0]=5  # tuple不可變動資
#print(data)



# 字串轉換為浮點數
string_to_float = float("3.14159")
#print(f"float(\"3.14159\") = {string_to_float}")
# 這行的 \\"3.14159\\" 是為了讓印出來的結果裡 包含引號
# 如果要在字串裡直接放一個引號，就得用 \\ 來跳脫它，否則 Python 會以為字串結束了。
#print(f"float("3.14159") = {string_to_float}")   錯誤用法,這個寫法無法 print 出 float("3.14159")中的 " "

#monthly_sales = [12500.75, 15000.50, 11000.20, 13500.90, 14000.00]

#total_sales = sum(monthly_sales) # 計算總銷售額
#num_months = len(monthly_sales)
#average_monthly_sales = total_sales / num_months # 計算平均月銷售額

#print(f"總銷售額: ${total_sales:,.2f}") # 格式化貨幣輸出 # .2f 小數點後2位
#print(f"平均月銷售額: ${average_monthly_sales:,.2f}")

import math
# 計算圓的面積
#r = 5.5 # 半徑
#area = math.pi * (r ** 2)
#print(f"半徑為 {r} 的圓的面積: {area:.4f}")

# 計算兩點之間的距離 (歐幾里得距離  euclidean distance)
def euclidean_distance(x1, y1, x2, y2):      # - 兩個點的座標：點1是 (x1, y1)，點2是 (x2, y2)

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) #sqrt 代表「開根號」的意思 math.sqrt()
    return distance

point1 = (1.0, 2.0)
point2 = (4.0, 6.0)
dist = euclidean_distance(point1[0], point1[1], point2[0], point2[1])
print(f"點 {point1} 和 {point2} 之間的距離: {dist:.2f}")