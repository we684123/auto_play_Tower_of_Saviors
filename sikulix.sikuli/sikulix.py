def log_a(ee,e3=''):
    log = '[%s] %s\n' % (time.strftime("%Y-%m-%d %I:%M:%S"), str(ee)+str(e3))
    f = open('log.txt', 'a')
    f.write(log)
    f.close()
#------------------------------------------
def exists_click(image ,time=5,sleep_time=0.3):
    exists(image,time)
    click(image)
    sleep(sleep_time)
    return 0
#------------------------------------------
def exists_click_not_move(image ,aims ,exists_time=5 ,interval=0.5 ,frequency=3):
    exists(image,exists_time)
    frequency = 0
    while 1:
        result = find(image)
        first_xy = get_xy(result)
        sleep(interval)
        result = find(image)
        second_xy = get_xy(result)
        ens1 = first_xy[0] == second_xy[0]
        ens2 = first_xy[1] == second_xy[1]
        if ens1 == ens2:
            frequency += 1
        else:
            frequency = 0
        if frequency>=aims:
            click(image)
            return 0
#------------------------------------------
def click_to_fighting():
    exists_click("1530207110217.png",sleep_time=0.3)
    exists_click(Pattern("1530231003617.png").similar(0.81),sleep_time=0.3)
    exists_click("1530231191185.png",sleep_time=0.3)
    exists_click("1530231201713.png",sleep_time=0.3)
    exists_click("1530231284750.png",sleep_time=0.3)
    exists_click(Pattern("1530207264056.png").similar(0.61) ,time=18 ,sleep_time=0.3)
    exists_click_not_move("1530114965937.png",2)
    exists_click_not_move("1530231763456.png",2)
    return 0
#------------------------------------------
def zzz():
    z = 0
    while 1:
        image = "1530113389303.png"
        sleep(5)
        if not exists("1530119289139.png",5):
           first_innings() 
        if exists(image,5):
            vul3 = find(image)
            z += 1 
            log_a("zzz = ",z)
            mouseMove(vul3)  # .targetOffset(-1,103)
            mouseMove(0, 100)
            mouseDown(Button.LEFT)
            sleep(0.5)
            mouseMove(-40,0)
            mouseUp(Button.LEFT)
        else:
            print("一局結束，收尾中!")
            sleep(7)
            exists("1530110300148.png",12)
            exists("1530111465100.png",15)
            click("1530109338588.png")
            sleep(1)
            if  exists("1530111576491.png",5):
                click("1530111606355.png")
                
            exists("1530111625291.png",5)
            
            click("1530109393282.png")
            sleep(1)
            exists("1530109412706.png",5)
            click("1530109412706.png")
            break
    return 0
            
        
#------------------------------------------
def first_innings():
    sleep(5)
    if exists("1530110042059.png",15):
        exists(leader,10)
        top = find(leader)
        exists(Pattern("1530092208377.png").targetOffset(127,1))
        down = find(Pattern("1530432991919.png").targetOffset(128,1))
        log_a(top)
        log_a(down)

        exists("1530110928091.png",7)
        dark_bead_list ,dark_list_obj = get_all_bead("1530089249612.png")
        
        exists("1530111023346.png",7)
        green_bead_list ,green_list_obj = get_all_bead("1530091267784.png")
            
        log_a("dark_bead_list：")
        log_a(dark_bead_list)
        log_a("green_bead_list：")
        log_a(green_bead_list)
        log_a("-----------------------------")
        
        #資料蒐集完畢^
        DorG = select_DorG(dark_bead_list ,green_bead_list)
        log_a("1111")
        table ,move_w_len ,move_h_len = full_and_get_table(top ,dark_bead_list ,green_bead_list ,down ,DorG)
        #score = get_score(table)
        log_a("2222")
        if DorG != 0: 
            if DorG == 1:#暗
                aims_obj = dark_list_obj
                log_a("aims_obj = dark_list_obj")
            else:
                aims_obj = green_list_obj
                log_a("aims_obj = green_list_obj")
            
            s = 0
            cl = 0
            max = len(aims_obj)
            while s<3:
                sleep(10)
                if exists("1530119289139.png",5):
                    ans = find("1530119289139.png")
                    score = ans.getScore()
                    log_a("score = ",score)

                    if score>0.9: 
                        print("已進入特殊排列")
                        return 0
                if DorG == 1:#暗
                    dark_bead_list ,dark_list_obj = get_all_bead("1530089249612.png")
                    log_a("dark_bead_list：")
                    log_a(dark_bead_list)
                else:
                    green_bead_list ,green_list_obj = get_all_bead("1530091267784.png")
                    log_a("green_bead_list：")
                    log_a(green_bead_list)
                print("-----------------------------")
                #資料蒐集完畢^
                #DorG = select_DorG(dark_bead_list ,green_bead_list)
                table ,move_w_len ,move_h_len = full_and_get_table(top ,dark_bead_list ,green_bead_list ,down ,DorG)
                
                if s == 0:
                    log_a("s = ",s)
                    e = click_bead_form_xy(table,col=5,row=4)
                    
                    if e == 0:
                        mouseMove(aims_obj[cl])
                        mouseDown(Button.LEFT)
                        mouseMove(Pattern("1530433107636.png").targetOffset(112,-39))
                        mouseUp(Button.LEFT)
                        #s += e
                        #n=n+1
                    else:
                        s += 1
                if s == 1:
                    log_a("s = ",s)
                    e = click_bead_form_xy(table,col=4,row=4)
                    
                    if e == 0:
                        mouseMove(aims_obj[cl])
                        mouseDown(Button.LEFT)
                        mouseMove(Pattern("1530433120996.png").targetOffset(64,-44))
                        mouseUp(Button.LEFT)
                        #s += e
                    else:
                        s += 1
                if s == 2:
                    log_a("s = ",s)
                    e = click_bead_form_xy(table,col=3,row=4)
                    
                    if e == 0:
                        mouseMove(aims_obj[cl])
                        mouseDown(Button.LEFT)
                        mouseMove(Pattern("1530433142899.png").targetOffset(22,-41))
                        mouseUp(Button.LEFT)
                        #s += e
                    else:
                        s += 1
                cl += 1
                if cl>=max:
                    cl = 0
                log_a("cl = ",cl)
            return 0
        else:
            log_a("珠不夠rrrrrrr")
            return 1
    return 0
# x = col_score.index(max(col_score))
# y = row_score.index(max(row_score))
#------------------------------------------
def click_bead_form_xy(table,col,row):
    if table[row][col] > 0:
        return 1
    else:
        return 0
    
#------------------------------------------
def get_score(table):
    col,row
    col_score = [0,0,0,0,0,0]
    row_score = [0,0,0,0,0]
    for i in range(0,6): #計算col分數
        for j in range(0,5):
            if table[i][j]>0:
                col_score[i] += 1
    for i in range(0,5): #計算row分數
        for j in range(0,6):
            if table[i][j]>0:
                row_score[i] += 1
    return table
    
#------------------------------------------
def full_and_get_table(top ,dark_bead_list ,green_bead_list ,down ,DorG):
    log_a("3333")
    top_xy = get_xy(top)
    log_a(str(top_xy))
    down_xy = get_xy(down)
    log_a(str(down_xy))
    log_a(down_xy[0])
    log_a("4444")
    table_width = int(down_xy[0]) + int(down_xy[2]) - int(top_xy[0])
    table_high  = int(down_xy[1]) - int(top_xy[1])
    log_a("table_width = ",table_width)
    log_a("table_high = ",table_high)
    log_a("5555")
    dark_len = len(dark_bead_list)
    green_len = len(green_bead_list)
    table = [
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0]
            ]
    #0未知 ,1暗 ,2綠

    #開始取代table內容以利計算
    if DorG == 1:
        for i in range(0,dark_len): #1暗
            log_a("i = " + str(i))
            d = get_xy(dark_bead_list[i])
            log_a(int(d[0]))
            log_a(int(top_xy[0]))
            log_a(int(table_width))
            
            log_a(int(d[1]))
            log_a(int(top_xy[1]))
            log_a(int(table_high))

            lxl = int( int(d[0]) - int(top_xy[0]) )
            lxo = int(table_width) / 6
            
            col = int( lxl/lxo  )
            row = int((int(d[1]) - int(top_xy[1]))/(int(table_high)  / 5))
            log_a("****-----****")
            log_a(col)
            log_a(row)
            table[row][col] = 1
    elif DorG == 2:
        for i in range(0,green_len): #2綠
            log_a("i = " + str(i))
            d = get_xy(green_bead_list[i])
            log_a(int(d[0]))
            log_a(int(top_xy[0]))
            log_a(int(table_width))
            
            log_a(int(d[1]))
            log_a(int(top_xy[1]))
            log_a(int(table_high))

            lxl = int( int(d[0]) - int(top_xy[0]) )
            lxo = int(table_width) / 6
            
            col = int( lxl/lxo  )
            row = int((int(d[1]) - int(top_xy[1]))/(int(table_high)  / 5))
            log_a("****-----****")
            log_a(col)
            log_a(row)
            table[row][col] = 2
    return table ,(table_width / 6) ,(table_high  / 5)
#------------------------------------------
def select_DorG(dark_bead_list ,green_bead_list):
    #基本資訊
    dark_len = len(dark_bead_list)
    green_len = len(green_bead_list)

    #基本門檻
    if dark_len < 3 and green_len < 3:
        rt = 0
        return rt
    if dark_len <= green_len:
        rt = 2
    else:
        rt = 1
    return rt
    
#------------------------------------------    
def get_all_bead(bead):
    findAll(bead)
    bead_list = []
    bead_list_obj = []
    mm = SCREEN.getLastMatches()
    while mm.hasNext(): 
        bead_data = mm.next()
        log_a("找到：" + str(bead_data))
        bead_list.append(bead_data)
        bead_list_obj.append(bead_data)
    return bead_list ,bead_list_obj
#------------------------------------------      
def get_xy(find_obj):
    r1 = re.compile('M\[(.+)\]@')
    r10 = r1.findall(str(find_obj))
    r2 = re.compile('\d+')
    r20 = r2.findall(str(r10)) #[x,y,w,h]
    log_a("***----****") 
    log_a(str(find_obj))
    log_a(r10)
    log_a(r20) 
    log_a("***^^^^^***")
    return r20
#------------------------------------------
def main(aims_Quantity):
    log_a("==========================")
    aq = int(aims_Quantity)
    log_a("目標數量為：" + str(aq))
    for i in range(0,aq):
        click_to_fighting()
        #try:
        exists("1530110487347.png",6)
        #except:
        #    rt = first_innings(leader)
        #try:
        rt = first_innings()
        #except:
        #    zzz()
        if rt ==0:
            zzz()
        else:
            log_a("QQ請手動解決!")
            return 1
        sleep(1)
        log_a("完成數量：",i+1)

#------------------------------------------------------------------
import re
leader = Pattern("leader.png").targetOffset(-18,-1)
aims_Quantity = 15
main(aims_Quantity)

#click_to_fighting()
#exists("1530110487347.png",16)
#first_innings(leader)
#try:
#zzz()
#except Exception :
#    log_a(Exception)


