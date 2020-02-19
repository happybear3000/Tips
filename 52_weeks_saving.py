"""
功能：52周存钱计算
     用户输入日期，判断具体周数和对应的当周存款金额
应用：列表，math库函数,时间处理库datetime
"""
import math
import datetime

def save_money_inweeks(money_per_week,increase_money,total_week):
    #while i <= total_week:
    #列表记录每周存款
    money_list = []
    #列表记录每周存款累计
    saved_money_list = []
    for i in range(total_week):  #自动循环计数，从0开始计数
        #saving += money_per_week
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        print('第{}周，存入{}元，账户累计{}元'.format(i + 1,money_per_week,saving))
        money_per_week += increase_money
        #i += 1
        saved_money_list.append(saving)
    return saved_money_list
        
def main():
    money_per_week = float(input('输入每周存款：'))
    increase_money = float(input('输入每周递增金额：'))
    total_week = int(input('输入存款周数：'))
    #saving = 0
    #调用函数，返回累计金额列表
    saved_money_list = save_money_inweeks(money_per_week,increase_money,total_week)
    #输入日期
    input_date_str = input('请按格式输入查询日期(yyyy/mm/dd):') 
    #计数对应周数
    input_date = datetime.datetime.strptime(input_date_str,'%Y/%m/%d')
    week_num = input_date.isocalendar()[1]
    print('输入日期属于第{}周，账户累计{}元'.format(week_num, saved_money_list[week_num - 1]))
    
if __name__ == '__main__':
    main()