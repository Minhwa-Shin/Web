#248540.py

EL = dict()

def getCmd():
    menu='''1.입력\n2.출력\n3.검색\n4.종료\n메뉴를 선택하시오:'''
    cmd=int(input(menu))
    return cmd

def inputData():
    while True:
        Equipment_name = input("장비명:")
        Quantity = int(input("수량:"))
        Production_date = input("생산일(예:1990-01-01):")
        EL[Equipment_name]=(Quantity,Production_date)
        y = input("계속 입력하시겠습니까(y/n)?")
        if y=='n':
            print("")
            break
        else:
            print("")

def outputData():
    print("-----------------------------------------")
    print("%-11s%-9s%-10s"%("장비명","수량","생산일"))
    print("-----------------------------------------")
    for key in EL.keys():
        print("%-15s%-8s%-10s"%(key,EL[key][0],EL[key][1]))
    print("-----------------------------------------\n")

def searchData():
    Equipment_name = input("검색할 장비명을 입력하세요:")
    print("-----------------------------------------")
    print("%-11s%-9s%-10s" % ("장비명", "수량", "생산일"))
    print("-----------------------------------------")
    if Equipment_name in EL:
        print("%-15s%-8s%-10s" % (Equipment_name, EL[Equipment_name][0], EL[Equipment_name][1]))
    print("-----------------------------------------\n")

def exit():
    y=input("프로그램을 종료하시겠습니까?(y/n)?")
    if y=='y':
        return True
    return False

while True:
    cmd=getCmd()
    print("")
    if cmd==1:
        inputData()
    elif cmd==2:
        outputData()
    elif cmd==3:
        searchData()
    elif cmd==4:
        if (exit()):
            break
        else:
            print("")
