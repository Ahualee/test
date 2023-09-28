#!/usr/bin/env python
# coding: utf-8

# # Python 入門
# 
# 資料來源：https://github.com/chengchingwen/Python-Introduction

# ## 基本運算

# In[1]:


1+2       # 加法


# In[2]:


3-4       # 減法


# In[3]:


5*6       # 乘法


# In[4]:


7/8       # 除法


# In[5]:


7//8      # 除法，無條件捨去到個位數


# In[6]:


10%9      # 取餘數


# In[7]:


2 ** 10   # 指數


# In[8]:


2 ** (1/2)   # 開根號


# In[9]:


1+2j         # 複數 (這裡虛部用 j 表示)


# In[10]:


(1+2j) * (3+4j)    # 複數乘法


# In[11]:


abs(-1)      # absolute, 絕對值


# In[12]:


abs(1+2j)    # absolute, 絕對值


# In[13]:


import numpy as np
np.sqrt(5)


# In[14]:


round(3.1415926, 3)     # 四捨五入到小數點後第 3 位


# In[15]:


round(3.1415926, 4)     # 四捨五入到小數點後第 4 位


# ## <font color="Red"> 1.1 熟能生巧 </font>
# <font color="Red"> 練習以下狀況    
# <font color="Red"> 1. 7.23 的 20 次方    
# <font color="Red"> 2. 虛數 i 的平方    
# <font color="Red"> 3. 42 的四次方根   
# <font color="Red"> 補充 : 運算有先後順序，可以用括弧來確保自己想要的順序 

# In[16]:


#------------------- Code Here ------------------------#


#------------------- Stop Here ------------------------#


# ## <font color="Red"> 1.2 數字的顯示方式  % vs. format  
# https://kknews.cc/zh-tw/code/qlpq5nb.html    
# <font color="Red">練習分別使用%與format進行"7.23 的 3.25 次方" 之不同顯示方式(顯示小數點以下第5位)   

# In[17]:


print("7.23 的 3.25 次方是：", 7.23**3.25)
#------------------- Code Here ------------------------#

#------------------- Stop Here ------------------------#


# ## 賦值 (Assign)
# 
# 用 `=` 來給變數內容值

# In[5]:


abcdef = 16
thisYearMonthDay = "2023/09/21"
myNationName = "Taiwan"
print("abcdef=" +str(abcdef)+" thisYearMonthDay=" +str(thisYearMonthDay)+ " myNationName="+str(myNationName))


# ## 型別 (Type)
# 
# 在程式語言中，型別概念上來說就像是物品的種類，例如：「這群是筆，那群是橡皮擦」。
# 
# 
# ## Python 的內建型別 (Built-in Types)
# 
# * int (整數)
# * float (浮點數)
# * complex (複數)
# * str (字串)
# * tuple
# * list
# * dict
# * set
# * ...

# In[19]:


type(42)    # 用 type 可以得知型別


# In[20]:


type(3.14159265358979323846)


# In[21]:


a = 7.23**3.25
b = 3
print(a,b)
print(type(a))
print(type(b))


# In[22]:


"測試"      # str, 字串


# In[10]:


"""我是多行字串"""       # 用 3 個 " 夾起來


# In[6]:


'''
我
是
多
行
字
串
'''       # 也可以用 3 個 ' 夾起來


# In[25]:


(42, 'O w O')    # tuple, 可以放入各種東西的大箱子，放完後不能更動


# In[26]:


foo = (42, 'O w O')
foo[0]          # subscript operator 可以取出其中的值
                 # 注意，index 從 0 開始算


# In[27]:


tu = [42, 'O w O']    # list 和 tuple 相似，但放完後可以更動


# In[28]:


tu[0] = 11


# In[29]:


{'a': 1, 'b': 42}    # dict，冒號左邊的是 key、右邊的是 value，用 key 可以查到 value (想像查字典的狀況)


# In[30]:


d = {'a': 1, 'b': 42}
d['b']


# In[31]:


{1, 2, 3, 3, 3}  # set，數學上的集合，裡面的東西不會重複，也沒有順序


# In[32]:


A = {1, 2, 3}
B = {1, 2, 4}
A | B            # 取聯集


# In[33]:


A & B            # 取交集


# In[34]:


A ^ B            # 取對稱差


# In[35]:


A - B            # 取差集


# ## 真偽值
# 
# * True/False
# * `>` `>=` `<` `<=` `==` `!=` `in`
# * and/or/not
# * is
# * 各種 empty 狀況
#     - 0, 1
#     - "", "abc"
#     - (,), (1, 2)
#     - [], [1, 2]
#     - set(), {1, 2}

# In[36]:


True


# In[37]:


False


# In[38]:


3 > 2


# In[39]:


5 <= 1


# In[40]:


1 != 2


# In[41]:


5 in [1, 2, 3, 4, 5]


# In[42]:


bool(0)   # 用 bool 來看各個資料是 True 還是 False


# In[15]:


bool(-100)


# In[44]:


bool(""), bool("abc")


# In[45]:


bool(tuple()), bool((1, 2))


# In[46]:


bool([]), bool([1, 2])


# In[47]:


bool(set()), bool({1, 2})


# In[48]:


bool(dict()), bool({'a': 1, 'b': 42})


# ## 流程控制
# 
# * if ... elif ... else
# * for ... in ...
# * break
# * continue
# * while ... else ...

# In[29]:


score=int(input("請輸入該科分數"))
if score < 0:
    print('No')
elif score > 100:
    print('Yes')
else:
    print('You are right')    # 如果 3 > 2 的話印出 'Yes'，否則印出 'Nooooooo, why can you come here?'
                                                 # 注意縮排是有影響的


# In[25]:


if 2 > 3:
    print('No')
elif 5 > 54:
    print('Yes')
else:
    print('@_@?')   # 如果 2 > 3 的話印出 'No'，要不然 5 > 4 的話就印出 'Yes'，否則印出 '@_@?'


# ## 利用 input 作為使用者輸入介面，使用 int() 將輸入值改為整數

# In[51]:


temperature = int(input("請輸入今天的溫度："))
if temperature >= 28:
    print("該開冷氣了！")
else:
    print("吹電風扇就好。")


# ## 利用 str 將數值改為字串以輸出顯示

# In[52]:


temperature = int(input("請輸入今天的溫度："))
if temperature >= 28:
    print("今天溫度"+str(temperature)+"度，該開冷氣了！")
else:
    print("今天溫度"+str(temperature)+"度，吹電風扇就好。")


# ## <font color="Red"> 1.3 請增加溫度的判斷，熟能生巧 </font>
# 
# <font color="Red"> 溫度範圍與顯示字串如下：   
# <font color="Red"> 1. 今天溫度 >= 28 度，顯示"今天溫度??度，該開冷氣了！"    
# <font color="Red"> 2. 今天溫度介於 20 到 27 度，顯示"今天溫度??度，吹電風扇就好。"      
# <font color="Red"> 3. 今天溫度介於 10 到 19 度，顯示"今天溫度??度，開窗就可以了。"      
# <font color="Red"> 4. 今天溫度 9 度以下，顯示"今天溫度??度，太冷了，關好窗戶。"    

# In[32]:


temperature = int(input("請輸入今天的溫度："))
if temperature >= 28:
    print("今天溫度"+str(temperature)+"度，該開冷氣了！")
elif 20<temperature<27 :
    print("今天溫度"+str(temperature)+"度，吹電風扇就好。")
elif 10<temperature<19 :
    print("今天溫度"+str(temperature)+"度，開窗就可以了")
else :
    print("今天溫度"+str(temperature)+"度，太冷了 關好窗戶")


# ## 常見的數字計算

# In[54]:


a = 5.5
b = 3.2
c = a+b
d = a-b
e = a*b
f = a/b
print("a = %.2f, b = %.2f, c = a+b = %.2f"%(a,b,c))
print("a = %.2f, b = %.2f, d = a-b = %.2f"%(a,b,d))
print("a = %.2f, b = %.2f, e = a*b = %.2f"%(a,b,e))
print("a = %.2f, b = %.2f, f = a/b = %.2f"%(a,b,f))


# ## <font color="Red"> 1.4 BMI 計算
# <font color="Red"> 讓使用者可以自行輸入身高、體重，接著計算 BMI 值，並輸出小數點以下兩位的格式
# <img src=https://health99.hpa.gov.tw/img/exam/bmi_form.png width="200">

# In[55]:


height = int(input("請輸入你的身高(cm)："))
weight = int(input("請輸入你的體重(kg)："))
#------------------- Code Here ------------------------#

#------------------- Stop Here ------------------------#    


# ## for 迴圈

# In[56]:


for i in [1, 2, 3, 4]:    # i 會依序變成 1, 2, 3, 4 來執行下面 block 的程式，在這邊則是會被印出來
    print(i)


# In[57]:


for i in [1, 2, 3, 4]:
    if i == 3:
        break    # 使用 break 來提早離開，當 i 變成 3 時就離開這個 for loop
    print(i)


# In[58]:


for i in [1, 2, 3, 4]:
    print(i)
else:
    print('End')    # 如果前面的 for 成功跑完的話會執行這段


# In[59]:


for i in [1, 2, 3, 4]:
    if i == 3:
        break
    print(i)
else:
    print('End')    # 如果前面的 for 成功跑完的話會執行這段


# In[60]:


for i in [1, 2, 3, 4]:
    if i == 3:
        continue    # continue 可以跳過這次後面的 code，進入下一輪
    print(i)
else:
    print('End')    # 如果前面的 for 成功跑完的話會執行這段


# ## <font color="Red"> 1.5 使用 for 迴圈計算 [1, 2, 3, 4, 6, 7]的數值總和</font>

# In[61]:


sum = 0
#------------------- Code Here ------------------------#

#------------------- Stop Here ------------------------#    
print("總和為:"+str(sum))    


# ## while 迴圈

# In[62]:


i = 4
while i > 0:   # 當 while 後面接的條件一直符合時就會繼續執行
    print(i)
    i = i - 1


# In[63]:


i = 4
while i > 0:   
    print(i)
    i = i - 1
else:
    print('End')


# In[64]:


i = 4
while i > 0:   
    if i == 3:
        break
    print(i)
    i = i - 1
else:
    print('End')


# ## <font color="Red"> 1.6 使用while計算小於等於40的偶數和

# In[65]:


i = 40
sum = 0;
#------------------- Code Here ------------------------#
 
#------------------- Stop Here ------------------------#    
print("小於等於40的偶數和:"+str(sum))        


# ## <font color="Red"> 1.7 使用while計算小於等於200的 3 或 5 的倍數和

# In[66]:


#Method 1 (使用 if 和 elif)
i = 200
sum = 0;
#------------------- Code Here ------------------------#
 
#------------------- Stop Here ------------------------#    
print("小於等於200的 3 或 5 的倍數和:"+str(sum))   


# In[67]:


#Method 2 (僅使用一個 if)
i = 200
sum = 0;
#------------------- Code Here ------------------------#
  
#------------------- Stop Here ------------------------#    
print("小於等於200的 3 或 5 的倍數和:"+str(sum))   


# ## 更多字串操作
# 
# * string formatting
# * 字串串接
# * slice : `start:stop[:step]`

# In[68]:


'{} | {}'.format(1, 2)    # 用 {} 表示要留著填空，後面用 .format 傳入要填進去的值


# In[69]:


'~ {} ~'.format([1, 2, 3, 4])


# In[70]:


'上上下下' + '左右左右' + 'BA'    # 用 + 可以把字串接起來


# In[71]:


s = 'abcdefghijklmnopqrstuvwxyz'


# In[72]:


s[0]


# In[73]:


s[1:4]    # index 1 到 index 3 (index 4 結束)


# In[74]:


s[-1]     # 負的 index 會倒回去


# In[75]:


s[1:8:2]  # index 1 到 index 7，每次跳兩步


# In[76]:


s[-1:-9:-2]


# In[77]:


s[::-1]   # 顛倒，不指定的話會自動帶入值


# ## Function
# 
# 一些常用的 code 會寫成 function，之後要使用時直接呼叫就可以了

# In[78]:


def hello():          
    print('Hello ~')

hello()   


# In[79]:


def f_42():
    return 42    # 用 return 來回傳資料

x = f_42()
print(x)


# In[80]:


def f(a, b=3):   # a 和 b 是參數，b 預設是 3
    return a+b

x = f(10)
y = f(10, 5)
print(x, y)


# ## <font color="Red"> 1.8 函數練習</font>
# <font color="Red">撰寫函數 test(a,b)，計算傳入兩個數a和b的平均值</font>

# In[81]:


#------------------- Code Here ------------------------#

#------------------- Stop Here ------------------------#
r = test(4,7)
print(r)


# ## <font color="Red"> 1.9 函數練習</font>
# <font color="Red">撰寫函數 test2(a)，計算傳入串列a中所有值的平均 <p>
# 例如：a=[1, 2, 3, 4]</font>

# In[82]:


#------------------- Code Here ------------------------#

#------------------- Stop Here ------------------------#
r = test2([1, 2, 3, 4])
print(r)


# # <font color="Red"> 1.10 函數練習</font>
# <font color="Red">撰寫函數 test3(a)，計算傳入串列a中所有值的平均值(Mean)與變異數(Variance)，再利用串列方式回傳 <p>
# 例如：a=[1, 2, 3, 4]</font>
# 
# <img src="https://images.squarespace-cdn.com/content/v1/533db07de4b0d9f7ba7f1e77/1552186395207-9OQVIKUBI0G3TJPEJJ7R/summary+table+of+mean%2C+variance%2C+and+standard+deviation+formulas?format=1500w%22"  width="700">

# In[83]:


#------------------- Code Here ------------------------#

#------------------- Stop Here ------------------------#
ans = test3([1, 2, 3, 4])
print(ans)


# ## <font color="Red"> 1.11 設計一個程式，輸入一個整數n，並在函式calSquare中計算1到n之間所有數字的平方和。¶

# In[84]:


#------------------- Code Here ------------------------#
  
#------------------- Code Here ------------------------#    
number = int(input("請輸入一個數字"))
cal_number = calSquare(number)
print("1到n之間所有數字平方和為"+str(cal_number))


# ## <font color="Red"> 1.12 設計一個程式，輸入兩個整數a和b，並在函式calSquare5中計算a到b之間5的倍數的平方和。¶

# In[85]:


#------------------- Code Here ------------------------#
   
#------------------- Code Here ------------------------#    
a = int(input("請輸入第一個數字"))
b = int(input("請輸入第二個數字"))
cal_number = calSquare5(a,b)
print(str(a)+"到"+str(b)+"之間所有數字平方和為"+str(cal_number))


# ## <font color="Red"> 1.13 寫一個程式，輸入一個整數n，並在函式checkPrime中判斷n是不是質數。

# In[86]:


#------------------- Code Here ------------------------#
 
#------------------- Code Here ------------------------#    
number = int(input("請輸入一個數字"))
isPrime = checkPrime(number)
print("數字"+str(number)+"是質數嗎？"+isPrime)

