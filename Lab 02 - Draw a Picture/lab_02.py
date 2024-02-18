import arcade

# Constants
SCREEN_TITLE = "Python Image"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
    

def draw_two(r_w, r_h, value, top, color_1, color_2):
    white = arcade.color.WHITE
    
    if top == True: 
        move = r_h*value+10
        
        # BLOCK ONE
        arcade.draw_rectangle_filled((SCREEN_WIDTH/2) - (r_w/2), move, r_w, r_h, color_1)
        # arcade.draw_rectangle_outline((SCREEN_WIDTH/2) - (r_w/2), move, r_w, r_h, white)

        # BLOCK TWO
        arcade.draw_rectangle_filled((SCREEN_WIDTH/2) + (r_w/2), r_h*value, r_w, r_h+20, color_2)
        # arcade.draw_rectangle_outline((SCREEN_WIDTH/2) + (r_w/2), r_h*value, r_w, r_h+20, white)
        
    else:
        move = r_h*value-10
        
        # BLOCK ONE
        arcade.draw_rectangle_filled((SCREEN_WIDTH/2) - (r_w/2), r_h*value, r_w, r_h+20, color_1)
        # arcade.draw_rectangle_outline((SCREEN_WIDTH/2) - (r_w/2), r_h*value, r_w, r_h+20, white)
    
        # BLOCK TWO
        arcade.draw_rectangle_filled((SCREEN_WIDTH/2) + (r_w/2), move, r_w, r_h, color_2)
        # arcade.draw_rectangle_outline((SCREEN_WIDTH/2) + (r_w/2), move, r_w, r_h, white)
    
    
def draw_four(r_w, r_h, value, top, color_1, color_2, color_3, color_4):
    # arcade.draw_rectangle_filled(left, bottom, width, height, color)
    white = arcade.color.WHITE
    
    # BLOCK ONE
    if top:
        arcade.draw_rectangle_filled((((SCREEN_WIDTH/2) - r_w*2) + r_w/2)-5, (r_h*value)-8, r_w, r_h+16, color_1)
        # arcade.draw_rectangle_outline((((SCREEN_WIDTH/2) - r_w*2) + r_w/2)-5, (r_h*value)-8, r_w, r_h+17, white)
    else:
        arcade.draw_rectangle_filled((((SCREEN_WIDTH/2) - r_w*2) + r_w/2)-5, r_h*value, r_w, r_h, color_1)
        # arcade.draw_rectangle_outline((((SCREEN_WIDTH/2) - r_w*2) + r_w/2)-5, r_h*value, r_w, r_h, white)
    
    # BLOCK TWO
    if top:  
        arcade.draw_rectangle_filled((SCREEN_WIDTH/2) + (r_w/2), r_h*value, r_w, r_h, color_2)
        # arcade.draw_rectangle_outline((SCREEN_WIDTH/2) + (r_w/2), r_h*value, r_w, r_h, white)
    else:
        arcade.draw_rectangle_filled((SCREEN_WIDTH/2) + (r_w/2), r_h*value, r_w+10, r_h, color_2)
        # arcade.draw_rectangle_outline((SCREEN_WIDTH/2) + (r_w/2), r_h*value, r_w+10, r_h, white)
    
    # BLOCK THREE
    if top == False: 
        arcade.draw_rectangle_filled((SCREEN_WIDTH/2) - (r_w/2), r_h*value, r_w, r_h, color_3)
        # arcade.draw_rectangle_outline((SCREEN_WIDTH/2) - (r_w/2), r_h*value, r_w, r_h, white)
    else:
        arcade.draw_rectangle_filled((SCREEN_WIDTH/2) - (r_w/2), r_h*value, r_w+10, r_h, color_3)
        # arcade.draw_rectangle_outline((SCREEN_WIDTH/2) - (r_w/2), r_h*value, r_w+10, r_h, white)
        
    
    # BLOCK FOUR
    if top == False:
        arcade.draw_rectangle_filled((((SCREEN_WIDTH/2) + r_w*2) - r_w/2)+5, r_h*value+8, r_w, r_h+16, color_4)
        # arcade.draw_rectangle_outline((((SCREEN_WIDTH/2) + r_w*2) - r_w/2)+5, r_h*value+9, r_w, r_h+17, white)
    else:
        arcade.draw_rectangle_filled((((SCREEN_WIDTH/2) + r_w*2) - r_w/2)+5, r_h*value, r_w, r_h, color_4)
        # arcade.draw_rectangle_outline((((SCREEN_WIDTH/2) + r_w*2) - r_w/2)+5, r_h*value, r_w, r_h, white)

def draw_pic():
    r_w = 100
    r_h = 100
    fourth_floor = 4
    third_floor = 3.03
    second_floor = 1.97
    first_floor = 1
    
    

    # 2
    draw_two(r_w, r_h, fourth_floor, True, (arcade.color.SKY_BLUE), (arcade.color.SKY_BLUE))
    draw_four(r_w, r_h, third_floor, True, (arcade.color.SKY_BLUE), (arcade.color.SKY_BLUE), (arcade.color.SKY_BLUE), (arcade.color.YELLOW))
    draw_four(r_w, r_h, second_floor, False, (arcade.color.SKY_BLUE), (arcade.color.YELLOW), (arcade.color.YELLOW), (arcade.color.YELLOW))
    draw_two(r_w, r_h, first_floor, False, (arcade.color.YELLOW), (arcade.color.YELLOW))
    
    # HEAD
    arcade.draw_ellipse_filled((SCREEN_WIDTH/2) - r_w, r_h*4+10, 100, 100, arcade.color.SKY_BLUE)
    arcade.draw_ellipse_filled((SCREEN_WIDTH/2) + r_w, r_h*1-10, 100, 100, arcade.color.YELLOW)
    
    # EYES
    arcade.draw_ellipse_filled((SCREEN_WIDTH/2) - r_w, r_h*4+10, 30, 30, arcade.color.GRAY)
    arcade.draw_ellipse_filled((SCREEN_WIDTH/2) + r_w, r_h*1-10, 30, 30, arcade.color.GRAY)
    


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.GRAY)

    arcade.start_render()
    
    draw_pic()

    arcade.finish_render()

    arcade.run()

if __name__ == "__main__":
    main()
