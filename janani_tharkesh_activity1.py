"""

This script will draw a table,cake,and candle by using the turtle library.
By making a function that will draw a rectangle, we can use it as our incremental step to make all the other functions
First it will make a table with four legs, the size and color of the table is based on the users input.
Second it will draw a cake that will have differently colored layers and the size will be dependent on the user's input.
Lastly it will make a candle on the top of the cake.
"""

from turtle import Screen, Turtle

# function to draw rectangle
def rectangle(x,y,length, width, color, turta):

    """

    this function is used to draw rectangle
    rectangle(x,y,length, width, color, turta)
    
    x = will be the x coordinates
    y = will be the y coordinates
    length =  will be the length of the rectangle
    width = will be the width of the rectangle
    color = will be the color of the rectangle


    """

    turta.penup()
    turta.goto(x,y)
    
    turta.begin_fill()
    turta.fillcolor(color)
    for i in range(2):
        turta.forward(length)
        turta.left(90)
        turta.forward(width)
        turta.left(90)

    turta.end_fill()

# table long leg
def table_leg(x,y,length, breadth, color, turta):

    """

    this function is used to draw 2 legs of the table
    table_leg(x,y,length, breadth, color, turta)
    
    x = the x coordinates of the table leg
    y = the y coordinates of the table leg
    length = length of the table leg 
    breadth = width of the table leg
    color = color of the table leg

    """
    rectangle(x,y,length,breadth,color, turta)
    

# table small leg
def small_leg(x,y,length, breadth, color, turta):

    """

    this function is used to draw 2 legs of the table
    small_leg(x,y,length, breadth, color, turta)

    x = x coordinates of the small legs
    y = y coordinates of the small legs
    length = length of the small legs
    breath = width of the small legs
    color = colors of the small legs

    """
    rectangle(x,y,length,breadth,color, turta)


# table
def draw_table(x, y, length, color, turta):

    """

    this functions is used to draw the table by calling the rectangle function and functions to draw the table legs
    draw_table(x,y,length, color, turta)
    
    x = x coordinates starting for the table
    y = y coordinates starting for the table
    length = the length of the table 
    color = the color of the table

    """
    rectangle(x, y, length, 20, color, turta)
    table_leg(x + 5, y - 50, 10, 50, "white", turta)
    small_leg(x + 40, y, -10, -30, "white", turta)
    table_leg(x + length - 15, y - 50, 10, 50, "white", turta)
    small_leg(x + length - 30, y, -10, -30, "white", turta)

#function to draw cake
def draw_cake(x1, y1, length, breadth, color1, color2, color3, color4, cake):

    """

    this function draws the cake by calling rectangle function and returns the y coordinate 
    draw_cake(x1,y1, length, breadth, color1, color2, color2, color3, color4, cake)

    x1 = the starting x coordinate of the cake
    y2 = the starting y coordinate of the cake
    length = the length of the cake
    breadth = the width of the cake
    color1 = the color of the first layer
    color2 = the color of the second layer
    color3 = the color of the third layer
    color4 = the color of the fourth layer

    """
    
    cake.goto(x1, y1)
    
    rectangle(x1, y1, length, breadth, color1, cake)
    y1 += 10
    cake.goto(x1, y1)
    
    rectangle(x1, y1, length, breadth + 10, color2, cake)
    y1 += 20
    cake.goto(x1, y1)
    
    rectangle(x1, y1, length, breadth, color3, cake)
    y1 += 10
    cake.goto(x1, y1)
    rectangle(x1, y1, length, breadth - 2, color4, cake)

    return y1
    

# Function to draw a candle on top of the cake
def draw_candle(turta, x, y, size, height):

    """
    This function will draw a candle by calling the rectangle function, and it's gonna center itself on top of the cake.
    then at the top of the candle it will draw a circle that will act as the flame

    x = the x coordinates of the candle
    y = the y coordinates of the candle
    size = the size of the candle
    height = how tall the candle is

    """

    turta.penup()
    turta.goto(x + size / 2 - 2.5, y)  # Center the candle
    
    turta.fillcolor("yellow")
    turta.begin_fill()
    for _ in range(2):
        turta.forward(5)
        turta.left(90)
        turta.forward(height)
        turta.left(90)
    turta.end_fill()

    # Draw flame
    turta.penup()
    turta.goto(x + size / 2, y + height)
    
    turta.fillcolor("red")
    turta.begin_fill()
    turta.circle(3)
    turta.end_fill()




# Main function to handle user input and drawing the scene
def main():

    """
    This is the main function that will call all previous functions and execute the whole program
    
    table_size = reads the size of the table from the user
    table_color = reads the color of the table from the user
    cake_size = reads the size of the cake from the user

    

    """
    
   
    
    table_size = int(input("Enter the length of one side of the table (10-100): "))
    table_color = input("Enter the color of the table: ")
    cake_size = int(input("Enter the size of the cake (10-100, must be smaller than the table size): "))

    table_size = table_size + 40  
    cake_size = cake_size +20

    table_x = -table_size 
    table_y = -100
    

    
    cake_x = table_x + table_size // 10
    cake_y = table_y + 20
    cake_color1 = "blue"
    cake_color2="purple"
    cake_color3 = "pink"
    cake_color4="orange"

    
    
    sc = Screen()
    turta=Turtle()
    sc.bgcolor("light blue")
    
    print("Your cake is loading! Happy Birthday!")

    draw_table(table_x, table_y, table_size, table_color, turta)
    top_of_cake = draw_cake(cake_x, cake_y, cake_size, 10, cake_color1, cake_color2, cake_color3, cake_color4, turta)
    draw_candle(turta, cake_x, top_of_cake + 10, cake_size, 20)
    turta.hideturtle()

    sc.exitonclick()

if __name__ == "__main__":
    main()






