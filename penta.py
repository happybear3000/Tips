#五角星画法
"""
画法1: 循环
画法2: 递归
"""

import turtle

#绘制五角星method version1
def draw_pentagram(size):
    #计数器
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count = count + 1
#绘制五角星method version2 - recursion
def recursive_draw_pentagram(size):
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1
    size += 10
    if size <= 100:
        recursive_draw_pentagram(size)

def main():
    #主函数
    
    turtle.penup()
    turtle.backward(100)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('blue')
    
    size = 50
    """
    #Using method version1
    while size <= 100:
        draw_pentagram(size)
        size = size + 10
    """
    #Using method version2 - recursion
    recursive_draw_pentagram(size)
    turtle.exitonclick()

if __name__ == '__main__':
    main()