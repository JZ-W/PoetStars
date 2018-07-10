class Poet:
    def __init__(self,name,birth,end,Zi,Hao,Chenghu,hometown):
        self.name = name
        self.birth = birth
        self.end = end
        self.Zi = Zi
        self.Hao = Hao
        self.Chenghu = Chenghu
        self.hometown = hometown

    def detail(self):
        print('name: ',self.name)
        print('birth: ',self.birth)
        print('end: ',self.end)
        print('Zi: ',self.Zi)
        print('Hao: ',self.Hao)
        print('Chenghu: ',self.Chenghu)
        print('hometown: ',self.hometown)

