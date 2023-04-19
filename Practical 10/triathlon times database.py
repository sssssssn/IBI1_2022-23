class triathlon (object):
    first_name = ''
    last_name = ''
    location = ''
    swim = ''
    cycle =''
    run =''
#define attributes     
    def __init__(self,f,la,l,s,c,r):
        self.first_name = f
        self.last_name = la
        self.location = l
        self.swim = s
        self.cycle = c
        self.run = r
#parameter to refer to an instance of the class       
    def record(self):
        print('member:%s%s,location:%s,swim:%d,cycle:%d,run:%d,total:%d'%(self.first_name,self.last_name,self.location,self.swim,self.cycle,self.run,self.swim+self.cycle+self.run))
#method
t = triathlon('yuhao','shen','haining',10,10,10)
t.record()
#example       
     
        
     
    


