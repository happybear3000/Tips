"""
功能：计算基础代谢率BMR
计算公式：
    BMR(男)=(13.7*体重(kg))+(5.0*身高(cm))-(6.8*年龄)+66
    BMR(女)=(9.6*体重(kg))+(1.8*身高(cm))-(4.7*年龄)+655
技术：数据类型type()
     输入BMR参数，输出结果
     字符串分割，格式化输出
     异常处理

"""

#def BMR_CAL():


def main():
    """
    #输入性别，体重，身高，年龄
    gender = input('性别:')
    #print(type(gender))
    weight = float(input('体重(kg):'))
    #print(type(weight))
    height = float(input('身高(cm):'))
    age = int(input('年龄:'))
    """
    print('输入BMR参数信息，并用空格分割')
    input_str = input('性别 体重(kg) 身高(cm) 年龄:')
    #字符串分割
    str_list = input_str.split(' ')
    #异常处理
    try:
        gender = str_list[0]
        weight = float(str_list[1])
        height = float(str_list[2])
        age = float(str_list[3])
    
        if gender == '男':
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
        elif gender == '女':
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else:
            bmr = -1
        
        if bmr != -1:
            #字符串格式化输出和占位符
            print('性别:{},体重:{}公斤,身高:{}厘米,年龄:{}岁'.format(gender,weight,height,age))
            print('基础代谢率BMR:{}大卡'.format(bmr))
        else:
            print('Invalid gender Parameter')
    #异常处理    
    except ValueError:
        print('错误提示：输入信息错误！')
    except IndexError:
        print('错误提示：输入信息数量过少！')
    except:
        print('程序异常')
        
        
if __name__ == '__main__':
    main()