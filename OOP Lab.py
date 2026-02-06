# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 19:38:21 2026

@author: nouran
"""

class Person():
    def __init__(self,name,money,mood,healthRate):
        self.name= name
        self.money= money
        self.mood= mood
        self.healthRate= healthRate
   
    
    def sleep(self,hours):
        if hours == 7:
            self.mood="happy"
        elif hours < 7:
            self.mood="tired"
        else:
            self.mood="lazyyy"
            
        
    def eat(self,meals):
        if meals == 3:
            self.healthRate= "100%"
        elif meals == 2:
             self.healthRate= "75%" 
        elif meals == 1:
            self.healthRate= "25%"
        
    def buy(self,items):
        self.money-= items*10
        
        
        
class car():
    def __init__(self,name,fuelRate,velocity):
        self.name= name
        self._fuelRate= fuelRate
        self._velocity= velocity
    
    @property
    def velocity(self):
        return self._velocity
    
    @velocity.setter
    def velocity(self,value):
        if value > 200:
            self._velocity= 200
        elif value < 0:
            self._velocity= 0
        else:
            self._velocity= value
        
    @property 
    def fuelRate(self):
        return self._fuelRate
    
    @fuelRate.setter 
    def fuelRate(self,value):
         if value > 100:
             self._fuelRate= 100
         elif value < 0:
             self._fuelRate= 0
         else:
             self._fuelRate= value
        
        
        
    def run(self, velocity, distance):
        self.velocity= velocity
        required_fuel= (distance/10)*10 
        
        if self.fuelRate >= required_fuel:
            self.fuelRate-= required_fuel
            self.stop(0)
        else:
            
        
    def stop(self):
        
   
    
   
    
class Employee(Person):
    def __init__(self,name,money,mood,healthRate,id,car,email,salary,distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id= id
        self.car= car
        self.email= email
        self.salary= salary
        self.distanceToWork= distanceToWork
    
    def work(self,hours):
        if hours == 8:
            self.mood= "happy"
        elif hours > 8:
            self.mood= "tired"
        else:
            self.mood= "lazy"
        
    def drive(self,distance):
        ###############
        pass
        
    def refuel(self,gasAmount=100):
        ##############
        pass
        
        
    def send_mail(self,):
        
    
    
    
    
    