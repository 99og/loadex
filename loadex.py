from time import sleep

__author__ = '.zqh aka The nicest guy on the planet'

class loadex:
 """   
   _                 _         
  | |   ___  __ _ __| |_____ __
  | |__/ _ \/ _` / _` / -_) \ /
  |____\___/\__,_\__,_\___/_\_\\ v0.1                                      
 """
 def __init__(self:str,start:str,final:str,frames:str,time:int,sleep:float):
  self.start,self.final,self.frames,self.time,self.sleep=start,final,frames,time,sleep
 def regroup(self):
  self.listed_frames=[]
  stack=''
  for frame in self.frames:
    if frame != " ":
     stack+=frame
    else:
      if stack:
        self.listed_frames+=[stack]
      stack=''
  if stack:
    self.listed_frames+=[stack]
  return self.listed_frames
 def load(self):
  b="{}"
  for g in range(self.time):
   for c in range(len(self.listed_frames)):
    d=self.start+b.format(self.listed_frames[c])
    print(d,end='\r')
    sleep(self.sleep)
    print(' '*len(d),end='\r')
    c+=1
  print(self.final)

  
b=loadex('loading ','Done !','[.] [..] [...]',64,0.2)
b.regroup()
b.load()