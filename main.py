#Not protected
import time
d = {}
tc = 0
def str_com(command = '', d = d):
    if command == '':
        command = input("Type the command: ")
    global time_cond
    if time_cond == 1:
        ftime = time.clock()
    if command[:4] == 'new ':
        new_m(command[4:], d)
    elif command[:4] == 'add ':
        c = 4
        for i in command[4:]:
            c += 1
            if i == ' ':
                break
        add_m(command[4:c - 1], command[c:], d)
    elif command[:4] == 'del ':
        c = 4
        for i in command[4:]:
            c += 1
            if i == ' ':
                break
        if c != len(command):
            del_elm(command[4:c - 1], command[c:], d)
        else:
            del_m(command[4:], d)
    elif command[:6] == 'union ':
        c1 = 6
        for i in command[6:]:
            c1 += 1
            if i == ' ':
                break
        c2 = c1
        for i in command[c1:]:
            c2 += 1
            if i == '[':
                break
        if c2 != len(command):
            uni_m(command[6:c1 - 1], command[c1:c2 - 2], command[c2:len(command) - 1], d)
        else:
            uni_m(command[6:c1 - 1], command[c1:], '', d)
    elif command[:9] == 'intersec ':
        c1 = 9
        for i in command[9:]:
            c1 += 1
            if i == ' ':
                break
        c2 = c1
        for i in command[c1:]:
            c2 += 1
            if i == '[':
                break
        if c2 != len(command):
            intersec_m(command[9:c1 - 1], command[c1:c2 - 2], command[c2:len(command) - 1], d)
        else:
            intersec_m(command[9:c1 - 1], command[c1:], '', d)
    elif command[:5] == 'diff ':
        c1 = 5
        for i in command[5:]:
            c1 += 1
            if i == ' ':
                break
        c2 = c1
        for i in command[c1:]:
            c2 += 1
            if i == '[':
                break
        if c2 != len(command):
            diff_m(command[5:c1 - 1], command[c1:c2 - 2], command[c2:len(command) - 1], d)
        else:
            diff_m(command[5:c1 - 1], command[c1:], '', d)
    elif command[:9] == 'simmdiff ':
        c1 = 9
        for i in command[9:]:
            c1 += 1
            if i == ' ':
                break
        c2 = c1
        for i in command[c1:]:
            c2 += 1
            if i == '[':
                break
        if c2 != len(command):
            simmdif_m(command[9:c1 - 1], command[c1:c2 - 2], command[c2:len(command) - 1], d)
        else:
            simmdif_m(command[9:c1 - 1], command[c1:], '', d)
    elif command[:5] == 'show ':
        show_m(command[5:], d)
    elif command[:7] == 'showall':
        showall_m(d)
    elif command[:4] == 'exit':
        return True
    elif command[:9] == 'contains ':
        c = 9
        for i in command[9:]:
            c += 1
            if i == ' ':
                break
        contains_m(command[9:c - 1], command[c:], d)
    elif command[:5] == 'isin ':
        c = 5
        for i in command[5:]:
            c += 1
            if i == ' ':
                break
        isin_m(command[5:c - 1], command[c:], d)
    elif command[:6] == 'exist ':
        exist_m(command[6:], d, True)
    elif command[:5] == 'open ':
        ftime = time.clock()
        TF = open_scr(command[5:], d)
        if TF == True:
            return True
        global tc
        if tc == 1:
            time_cond = 1
    #New Commands
    elif command[:5] == 'sort ':
        sort_m(command[5:], d)
    elif command[:4] == 'time':
        ntime()
    elif command[:5] == 'file ':
        nfile(command[5:], d)
    elif command[:7] == 'delodd ':
        del_odd(command[7:],d)
    if time_cond == 1:
        try:
            print(int(time.clock()-ftime))
        except:
            a = 0
    return False

def new_m(name_m, d = d):
    d[name_m] = []
    return d

def add_m(name_m, name_el, d = d):
    #if exist_m(name_m) == True:
        #d[name_m].append(name_el)
    #d[name_m].append(name_el)
    #d[name_m] = sort_m(name_m)
    '''try:#
        name_el = int(name_el)#
    except:#
        return d#
    if d[name_m] != []:
        if d[name_m][-1] < name_el:
            d[name_m].append(name_el)
        else:
            d[name_m].append(name_el)
            d[name_m].sort()
    else:
        d[name_m].append(name_el)'''
    d[name_m].append(int(name_el))
    return d

def isin_el(name_m, name_el, d = d):
    try:#
        name_el = int(name_el)#
    except:#
        return d#
    #if name_el not in d[name_m]:
    if TFBS(d[name_m], name_el) == False:#
        return False
    else:
        return True

def del_elm(name_m, name_el, d = d):
        '''try:#
            name_el = int(name_el)#
        except:#
            return d#'''
    #if exist_m(name_m) == True: 
        '''c = 0
        for i in d[name_m]:
            if d[name_m][c] == name_el:
                break
            else:
                c += 1
        if d[name_m] != []:
            d[name_m].pop(c)'''
        if TFBS(d[name_m], int(name_el)) == True:
            global last_r
            d[name_m].pop(last_r)
        return d

def del_m(name_m, d = d):
    #if exist_m(name_m) == True:
        #d.pop(name_m)
    d.pop(name_m)#
    return d

def uni_m(name_m1, name_m2, res = '', d = d):
    #if (exist_m(name_m1) == True & exist_m(name_m2) == True):
        if res == '':
            res_p = []
            for i in d[name_m1]:
                res_p.append(i) 
            for i in d[name_m2]:
                #if i not in res_p:
                #    res_p.append(i)
                if TFBS(res_p, i) == False:#
                    res_p.append(i)#
            print(res_p)
        else:
            d[res] = []
            for i in d[name_m1]:
                d[res].append(i)
            for i in d[name_m2]:
                #if i not in d[res]:
                #    d[res].append(i)
                if TFBS(d[res], i) == False:#
                    d[res].append(i)#                
        return d

def intersec_m(name_m1, name_m2, res = '', d = d):
    #if (exist_m(name_m1) == True & exist_m(name_m2) == True):
        if res == '':
            d[res] = []
            for i in d[name_m1]:
                d[res].append(i)
            '''for i in d[res]:
                #if i not in d[name_m2]:
                if TFBS(d[name_m2], i) == False:#
                    del_elm(res, i, d)'''
            delc = 0#
            for i in range(len(d[res])):#
                if TFBS(d[name_m2], d[res][i-delc]) == False:#
                    del_elm(res, d[res][i-delc], d)#
                    delc+=1#
            print(d[res])
            del_m(res, d)
        else:
            d[res] = []
            for i in d[name_m1]:
                d[res].append(i)
            '''for i in d[res]:
                #if i not in d[name_m2]:
                if TFBS(d[name_m2], i) == False:#
                    del_elm(res, i, d)'''    
            delc = 0#
            for i in range(len(d[res])):#
                if TFBS(d[name_m2], d[res][i-delc]) == False:#
                    del_elm(res, d[res][i-delc], d)#
                    delc+=1#
        return d

def diff_m(name_m1, name_m2, res = '',d = d):
    #if (exist_m(name_m1) == True & exist_m(name_m2) == True):
        if res == '':
            d[res] = []
            for i in d[name_m1]:
                d[res].append(i)
            for i in d[name_m2]:
                #if i in d[res]:
                if TFBS(d[res], i) == True:#
                    del_elm(res, i, d)
            print(d[res])
            del_m(res, d)
        else:
            d[res] = []
            for i in d[name_m1]:
                d[res].append(i)
            for i in d[name_m2]:
                #if i in d[res]:
                if TFBS(d[res], i) == True:#
                    del_elm(res, i, d)
        return d

def simmdif_m(name_m1, name_m2, res = '', d = d):
    #if (exist_m(name_m1) == True & exist_m(name_m2) == True):
        if res == '':
            d[res] = []
            for i in d[name_m1]:
                d[res].append(i)
            for i in d[name_m2]:
                #if i in d[res]:
                if TFBS(d[res], i) == True:#
                    del_elm(res, i, d)
                else:    
                    d[res].append(i)
            print(d[res])
            del_m(res, d)
        else:
            d[res] = []
            for i in d[name_m1]:
                d[res].append(i)
            for i in d[name_m2]:
                #if i in d[res]:
                if TFBS(d[res], i) == True:#
                    del_elm(res, i, d)
                else:    
                    d[res].append(i)
        return d

def show_m(name_m, d = d):
    #if exist_m(name_m) == True:
        print(name_m, '=', d[name_m])

def showall_m(d = d):
    for i in d:
        print(i, '=', d[i])

def contains_m(name_el, name_m, d = d):
    #if exist_m(name_m) == True:
        #if name_el in d[name_m]:
        if TFBS(d[name_m], name_el) == True:#
            print(True)
            return True
        else:
            print(False)
            return False

def isin_m(name_m1, name_m2, d = d):
    #if (exist_m(name_m1) == True & exist_m(name_m2) == True):
        for i in d[name_m1]:
            #if i not in d[name_m2]:
            if TFBS(d[name_m2], i) == False:#
                print(False)
                return False
        print(True)
        return True

def exist_m(name_m, d = d, vis = False):
    for i in d:
        if i == name_m:
            if vis:
                print(True)
            return True
    if vis:
        print(False)
    return False

def open_scr(file, d = d):
    f = open(file, 'r')
    global time_cond
    if time_cond == 1:
        time_cond = 0
        global tc
        tc = 1
    for i in f:
        if i[len(i)-1] == '\n':
            i = i[:len(i) - 1]
        #print(i)
        if i == 'exit':
            return True
        str_com(i, d = d)
    f.close()

def sort_m(a, d=d):
    return d[a].sort()

def bin_search(a, key):
    l = -1
    r = len(a)
    while l < (r-1):
        m = int((l+r)/2)
        if a[m] < key:
            l = m
        else:
            r = m
    global last_r
    last_r = r
    return r
last_r = float('inf')
def TFBS(a, key):
    try:
        if a[bin_search(a, key)] == key:
            return True
        else:
            return False
    except:
        return False
            
def del_odd(m, d = d):
    test = float('inf')
    c = 0
    del_odd_m = []
    for i in d[m]:
        if i == test:
            #d[m].pop(c)
            del_odd_m.append(c)#
        else:
            test = i
        c+=1
    sizedeloddm = len(del_odd_m)
    for i in range(sizedeloddm):
        d[m].pop(del_odd_m[i]-i)
def nfile(name, d=d):
    to_file = open(str(name)+'.txt','w')
    for i in d:
        to_file.write(str(i)+' = '+str(d[i])+'\n')
    to_file.close()
time_cond = 0
def ntime():
    global time_cond
    if time_cond == 0:
        time_cond = 1
    else:
        time_cond = 0
countexit = False
while countexit == False:
    try:
        countexit = str_com()
    except: 
        print('Error')
exit = input('Exit...')