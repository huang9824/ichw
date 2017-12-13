from urllib.request import urlopen 


    
def exchange(currency_from,currency_to,amount_from):
    #将Cornell网站汇率结合
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+str(currency_from)+'&to='+str(currency_to)+'&amt='+str(amount_from)) 
    docstr = doc.read() 
    doc.close() 
    jstr = docstr.decode('ascii')  
    nlen=len(jstr) 
    x='"to" : "' 
    for i in range(nlen-1): 
        if jstr[i:i+8]==x: 
            break 
        else: 
            continue 
    #找出字符串中，换出的汇率的所在范围
    currencyTo=i+8 
    new=jstr[currencyTo:] 
    amount=new.find(' ') 
    numstr=new[:amount] 
    #将转换后的汇率剪出来 
    amount_to=float(numstr) 
    return amount_to 
    
   
    
    
def test_get_from(): 
#带入数据测试结果
    assert(exchange('USD','EUR',2.5)==2.0952375) 
    
     
def testAll(): 
#测试所有程序
    test_get_from() 
    print("All tests passed") 
    #打印测试结果
     
    
def main(): 
#输入数据
    currency_from=input('Currency from:') 
    currency_to=input('Into currency:') 
    amount_from=input('Amount of money:') 
    result=exchange(currency_from,currency_to,amount_from) 
    return result 
   
    
print('Exchanged currency:',main()) 
#开始计算 
testAll() 
