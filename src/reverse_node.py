#画面反転値計算用
__center_x_mm = 59/2
__center_y_mm = 105/2
while True:
    abs_x = int(input("x"))
    abs_y = int(input("y"))
    moved_x = abs_x - __center_x_mm
    moved_y = abs_y - __center_y_mm 
    moved_x *= -1
    moved_y *= -1
    target_x = moved_x + __center_x_mm
    target_y = moved_y + __center_y_mm
    print("{0},{1}".format(target_x,target_y ) )