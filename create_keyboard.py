from __future__ import division

def create_keyboard(keyboard_width, keyboard_height, xstart, ystart):
    
    keyboard=[]
    row1=[0.6,1,1,1,1,1,1,1,1,1,1,1,1,2.2]
    row1_index=['carre','1','2','3','4','5','6','7','8','9','0',')','+','Backward']
    row2=[1.4,1,1,1,1,1,1,1,1,1,1,1,1,1.8]
    row2_index=['Tab','a','z','e','r','t','y','u','i','o','p','^','$','Enter']
    row3=[1.8,1,1,1,1,1,1,1,1,1,1,1,1,1.4]
    row3_index=['Caps','q','s','d','f','g','h','j','k','l','m','%','*','Enter']
    row4=[1,1,1,1,1,1,1,1,1,1,1,1,3]
    row4_index=['Shift','<','w','x','c','v','b','n',',',';',':','!','Shift']
    row5=[1,1,1,1,5.1,0.9,0.9,0.9,0.9,0.9,0.9]
    row5_index=['Ctrl','fn','Windows','Alt','Space','Alt gr','menu','Ctrl','<','^','>']
    total_width=sum(row1)
    current_w=xstart
    current_h=ystart
    for i in range(len(row1)):
        row1[i]=row1[i]/total_width*(9/10)*keyboard_width #1/10 of the keyboard is for the space between the keys
        keyboard.append((current_w, current_h, row1[i], keyboard_height/6))
        current_w+=row1[i]+(1/10)*keyboard_width*(1/len(row1))

    current_w=xstart #reset the current width
    current_h+=keyboard_height/6+keyboard_height/24  #adding the height of a key and the space between the keys
    total_width=sum(row2)
    for i in range(len(row2)):
        row2[i]=row2[i]/total_width*(9/10)*keyboard_width
        keyboard.append((current_w, current_h, row2[i], keyboard_height/6))
        current_w+=row2[i]+(1/10)*keyboard_width*(1/len(row2))

    current_w=xstart #reset the current width
    current_h+=keyboard_height/6+keyboard_height/24  #adding the height of a key and the space between the keys
    total_width=sum(row3)
    for i in range(len(row3)):
        row3[i]=row3[i]/total_width*(9/10)*keyboard_width
        keyboard.append((current_w, current_h, row3[i], keyboard_height/6))
        current_w+=row3[i]+(1/10)*keyboard_width*(1/len(row3))
    
    current_w=xstart #reset the current width
    current_h+=keyboard_height/6+keyboard_height/24  #adding the height of a key and the space between the keys
    total_width=sum(row4)
    for i in range(len(row4)):
        row4[i]=row4[i]/total_width*(9/10)*keyboard_width
        keyboard.append((current_w, current_h, row4[i], keyboard_height/6))
        current_w+=row4[i]+(1/10)*keyboard_width*(1/len(row4))
    
    current_w=xstart #reset the current width
    current_h+=keyboard_height/6+keyboard_height/24  #adding the height of a key and the space between the keys
    total_width=sum(row5)
    for i in range(len(row5)):
        row5[i]=row5[i]/total_width*(9/10)*keyboard_width
        keyboard.append((current_w, current_h, row5[i], keyboard_height/6))
        current_w+=row5[i]+(1/10)*keyboard_width*(1/len(row5))
    

    keyboard_index=row1_index+row2_index+row3_index+row4_index+row5_index

    return keyboard,keyboard_index
