#coding=utf-8

# 算法出处
# ## 根因分析初探：一种报警聚类算法在业务系统
# https://tech.meituan.com/2019/02/28/root-clause-analysis.html

# 未来方向  基于分布式计算抽取日志信息
import copy


def abstract_info(alarms:list,mini_size =10 )->list:

    """
    :param alarms:所有告警
    :return:   抽取出来的告警信息
    mini_size: 群的最小尺寸
    """

    #进行一次浅拷贝-->列表仅仅拷贝了元素地址
    T = copy.copy(alarms)
  
    #最后产生的信息  [(alam,count)]
    messages=[]

    #属性树
    Trees = T[0].Trees
    

    while True:
        # 报警计数器
        counter = {}
        # 元素计数器
        element_counter = [dict() for i in range(len(T[0]))]
        #当集合中的元素的个数不足mini_size时，直接退出
        if len(T) < mini_size :
            messages+=T
            break

        stand_out =set()
        for item in T:
            #为每个元素计数
        
            for i in range(len(item)):
                k = item[i]
                c = element_counter[i].get(k,0)
                element_counter[i][k]  = c + 1

            #返回一个原始值
        
            c1 = counter.get(item,0)
            #alarm coutner
            counter[item] = c1 + 1
       
        if __debug__:
            print("counter:",counter)
        for m  in counter:
            if counter[m] >= mini_size:
                stand_out.add(m)

        #满足条件可以聚类时
        if stand_out:
            for i in stand_out:
                messages.append((i,counter[i]))
            #更新T-->过滤
            if __debug__:
                print("满足聚类后被添加的信息：",messages)
            # 寻找可以继续更新的报警
            T = [i for i in T if i not in stand_out]
            
        
        if T:
            #print("-----------------\n满足聚类聚类\n-----------------")
            # 选择一个属性，更新父类,更新列表T
            # 找到最大优先级，然后更新值

            #collector:（key,count） ->str,int
            
            collector=[]

            #chosen_attr ： index of attribute
            choosen_attr=None
            #最下计数
            min=None
          
            
             
            for i in range(len(element_counter)):
                #泛化程度最小的
                k = Trees[i].max_key(element_counter[i].keys())
                if __debug__:
                    print("这课树中泛化程度最小：",k)
                
                #i =  (Trees[i].one_array == k).argmax()
                if __debug__:
                    print("element counter: ", element_counter)
                 
                collector.append((k,element_counter[i][k]))
                #分别储存两课属性树的最高级和count
                if __debug__:
                    print("collctor: ",collector)
                #选择 Fi 值最小的属性 Ai 进行泛化。
                if (min is None)  or ( element_counter[i][k] < min) :
                    min = element_counter[i][k]
                    choosen_attr = i
                    

            #获取需要更新的属性
            update_key = collector[choosen_attr][0]
            if __debug__:
                print("需要被update:",update_key)


            #更新集合里有这个属性的所有报警
            T = [item.update(choosen_attr) if item[choosen_attr] ==update_key else item for item in T ]
            if __debug__:
                print("T:",T)
        else:
            #加上所有的不满足聚类（《minsize）的alarm
            messages+=T
            break

    return messages
