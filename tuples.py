

# tuple(元組) 資料不可變動(immutable),對固定資料較有用,可儲存重複項目,有順序性可雙向索引
# 切割(slicing)  (start(開始計數) : stop(計數到stop前一個數字) : step(間格數預設為 1))


#empty_tuple = ()
#print(f"空元組:{empty_tuple},類型:{type(empty_tuple)}")

#my_tuple = (1, "hello", 3.14, True)
#print(f"多元素元組:{my_tuple}")

#single_element_tuple = (42,)
#print(f"單元素元組: {single_element_tuple}")

#another_tuple = 1, 2, 3
#print(f"沒有括號的元組: {another_tuple}")

#.count():傳回所需計數項次的數量
#my_tuple = ('a','p','p','l','e')
#print(my_tuple.count('p')) # print 2
#.index():回傳該項次第一次的索引
#print(my_tuple.index('p')) # print 1

#a = (1,2,3,4,5,6)
#print(a[1:4])

#a = ((11,12,13),[21,22,23])
#print(a[1])  # print [21,22,23]
#print(a[0][1]) # print 12

#print(len(("python",10)))

#a = ('s','i','m','p','l','e')
#print(a[:3])  # print ('s','i','m')
#print(a[4:6]) # print ('l','e')

#mutable_in_tuple = (1, [2, 3], 4)
#print(f"原始元組: {mutable_in_tuple}")
#mutable_in_tuple[1].append(5) # 修改元組中的列表
#print(f"修改後元組: {mutable_in_tuple}")  # print 修改後的元祖:(1,[2,3,5],4)


#coordinates = (10, 20)
#x, y = coordinates # 解包元組
#print(f"X 座標: {x}, Y 座標: {y}")  # print X座標:10   Y座標:20

#def get_user_info():
    #return "Alice", 30, "New York" # 函數返回一個元組

#name, age, city = get_user_info() # 解包函數返回值
#print(f"姓名: {name}, 年齡: {age}, 城市: {city}")

#a, b, *rest = (1, 2, 3, 4, 5)
#星號 * 是 Python 的「可變數量解包」運算符，可以接住一串不定長度的值。
#print(f"a: {a}, b: {b}, rest: {rest}") # print  a:1,b:2,rest"[3,4,5]

