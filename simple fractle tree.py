#利用递归绘制分形树
import turtle

#绘制分枝
def draw_branch(length):
    #分形树主干颜色
    turtle.color('brown')
    #分形树主干粗细
    turtle.pensize(3)
    if length > 5:
        if length <= 15:
            #分形树末端2层颜色
            turtle.color('green')
            #分形树末端2层粗细
            turtle.pensize(1)
            
        #绘制右侧树枝
        turtle.forward(length)
        turtle.right(30)
        draw_branch(length - 5)
        #绘制左侧树枝
        turtle.left(60)
        draw_branch(length - 5)
        #返回之前的树枝
        turtle.right(30)
        turtle.penup()
        turtle.backward(length)
        turtle.pendown()
        
            
        
def main():
    turtle.left(100)
    turtle.penup()
    turtle.backward(100)
    turtle.pendown()
    draw_branch(40)
    turtle.exitonclick()

if __name__ == '__main__':
    main()