
# 引號的嵌套使用
#str4 = "I'm learning Python."
#str5 = 'He said, "Hello!"'
#print(f"嵌套引號 1: {str4}")
#print(f"嵌套引號 2: {str5}")

# 切片 (Slicing)：用於提取字串的子部分。語法為 [start:end:step]。(從索引0開始算)

#my_string = "Programming"
#print(f"從索引 3 到 7 (不包含): {my_string[3:8]}") # 輸出 gramm [3:8]指的是從索引3 ~ 7
#print(f"從開頭到索引 5 (不包含): {my_string[:5]}") # 輸出 Progr  [:5]指的是從索引0 ~ 5
#print(f"從索引 4 到結尾: {my_string[4:]}") # 輸出 ramming   [4:]指的是從索引4 ~ 最後結尾
#print(f"每隔一個字元: {my_string[::2]}") # 輸出 Pormig   [::2]從索引0開始隔一個
#print(f"反轉字串: {my_string[::-1]}") # 輸出 gnimmargorP  [::-1]從結尾往前推

#x = 15
#x = x + 5
#print(x)

#print(len("95637+12")) # len()算有幾個字元(含標點符號和空格)

# 有縮排和未縮排的差異
#for x in [1,2,3]:
   # x = x ** 2
#print("x=",x)  # print未縮排會print出「最後一次迴圈之後 x 的值(x=6)」

#for x in [1,2,3]:
   # x = x *2
   # print("x=",x)  #print縮排,print出 x=2,x=4,x=6

#print("123"+"abc")

#x=int(98.6)
#print(x)  # 輸出 98

#print(42%10) # 輸出 2  % 是求餘數
#x = 1 + 2 * 3 - 8 / 4
#print(x) # 輸出 5.0

#print(2 > 5 or 3 ==2)  #輸出 False  2 > 5 false , 3 == 2 false
#print(11 // 2  )   # 輸出 5

#a = 31 
#b = 4
#a %= b
#print(a) # 輸出 3


#x = 8
#y = 2
#print(x == y)  # 輸出 False

#print(10 % 4 == 2 and 8 // 3 ==2)  # 輸出True

#a = 5
#b = 10
#c = a
#print(a is not c) # 輸出 False

#print(float('3'))  # 輸出 3.0
#print(int('3')) # 輸出 3

#import random  # 隨機函數
#print(random.randrange(10,20)) # 輸出隨機數(從 10 到 19 之間隨機選一個整數（不包含 20）)


#import fractions  # 分數函數(fractions)
#print(fractions.Fraction(2,5))  # 輸出 2/5

#from fractions import Fraction as F 
#print(1 / F(2,5))  # 輸出 5/2

#print(int('2.8')) # 輸出 Value Error  因為'2.8'不是整數字串,字串只能是整數
#print(int(2.8))  # 輸出 2 (浮點數轉整數),有加 ' ' 或 " " 的是字串
#print(int('python 3')) # 輸出Value Error




