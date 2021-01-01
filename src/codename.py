import random
from time import time
from pprint import pprint
class CodeName:
    def __init__(self,row=5,col=5,agentCards=8,assasinCards=1):
        self.row=row
        self.col=col
        self.agentCards=agentCards
        self.assasinCards=assasinCards
        self.starter=None
        #generate seed
        self.seed=(int(time()*100) % 100)
        #print("Init as:%s"%(self.seed))

    def setSeed(self,seed):
        self.seed=seed
        #print("Set as:%s"%(self.seed))

    def newGame(self):
        random.seed(self.seed)
        random.seed(self.seed)
        cards=[]
        #generate brute cards
        for i in range(self.agentCards):
            cards.append("blue")
            cards.append("red")
        for i in range(self.assasinCards):
            cards.append("black")
        for i in range(self.row*self.col-self.agentCards*2-self.assasinCards-1):
            cards.append("white")
        if random.randint(1,2)==1:
            cards.append("blue")
            self.starter="blue"
        else:
            cards.append("red")
            self.starter="red"
        #randomly pick card
        data=[]
        for i in range(self.row):
            line=[]
            for j in range (self.col):
                index=random.randint(0,len(cards)-1)
                line.append(cards.pop(index))
            data.append(line)
        #pprint(data)
        return data
