import os
from collections import defaultdict 
  
  

class TestReading():
        # Function to return a default 
    # values for keys that is not 
    # present 
    def def_value(): 
        return "Not Present"
      
    alarm_list=[]
    # Defining the dict 

    d = defaultdict(def_value) 
    record=["",False]
    if __debug__:
        print(os.getcwd())
    nextAlarm= False
    with open('/home/guozhenghao/clustering/log/test/alarm_text.txt', 'r') as f:
        data = f.readlines()  #txt中所有字符串读入data
        for index, line in enumerate(data):
            
            line=line.strip()
            if record[1]:
                d[record[0]]=line
                record[1]=False
                
                
                
   
            if index==0 or nextAlarm or len(line)==0:
                if index==0:
                    d["name"]=line
                    #print(line)
              
                if nextAlarm and len(line)!=0:
                    d["name"]=line
                    nextAlarm=False
                    #print(line)
                continue
            
            if line=="【此告警需要处理，请点击下方我的告警或登录告警平台进行操作】":
                alarm_list.append(d)
                nextAlarm=True
                
            
            alarm = line.split()        #将单个数据分隔开存好
            if alarm[0][-1]==":":
                record=[alarm[0][:-1],True]
        #@classmethod
        def init_variable(cls,alarm_list):
            cls.alarm_list=alarm_list
    
                
           
    
    
    
    
    # with open('alarm_text.txt','a') as file:
    #      write_str = '%f %f\n'%(float_data1,float_data2)
    #      file.write(write_str)


