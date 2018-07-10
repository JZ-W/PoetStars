# from ClassPoet import Poet
# LiBai = Poet('LiBai',761,820,'Taibai','Qinglian',['shixian','Qijue'],'Sichuan')
# LiBai.detail()
# print(LiBai.GetAge())

srcPath = r"E:\A-Winter\PoetStart.txt"
with open(srcPath,'r') as f:
    listPoets = f.readlines()
    print('lenth: ',len(listPoets))
    for eachPoet in listPoets:
        listEachPoet = eachPoet.split()
        d = {listEachPoet[0]:listEachPoet[1:]}
        print(d)
        
