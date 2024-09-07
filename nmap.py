import nmap    
# диапазон портов для сканирования
begin = 75
end = 80
  
# IP-адрес для сканирования
target = '127.0.0.1'
   
scanner = nmap.PortScanner() 
   
for i in range(begin,end+1): 
   
    res = scanner.scan(target,str(i)) 
   
    # Результатом проверки будет, открыт или закрыт порт 
    # в диапазоне сканирования  
    res = res['scan'][target]['tcp'][i]['state'] 
   
    print(f'port {i} is {res}.') 