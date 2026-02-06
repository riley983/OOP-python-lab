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
            self.healthRate= 100
        elif meals == 2:
             self.healthRate= 75
        elif meals == 1:
            self.healthRate= 25
        
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
            covered_distance= (self.fuelRate/10)*10
            self.fuelRate = 0
            self.stop(distance - covered_distance)
            
        
    def stop(self,remaining_distance):
        self.velocity = 0
        if remaining_distance == 0:
            print("You arrived at your destination")
        else:
            print(f"You ran out of fuel. Remaining distance: {remaining_distance} km")
            
        
   
    
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
        self.car.run(60,distance)
        
    def refuel(self,gasAmount=100):
        self.car.fuelRate += gasAmount
        
    def send_mail(self,to,subject):
        print(f"mail sent to {to} regarding {subject}")
        
        

class Office():
    employeesNum= 0
    
    def __init__(self,name):
        self.name= name
        self.employees= []
        
    
    @classmethod   
    def change_emps_num(cls, num):
        cls.employeesNum= num
        
    def get_all_employees(self):
        return self.employees
    
    def get_employee(self, empid):
        for emp in self.employees:
           if emp.id == empid:
              return emp
        return None
    
    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum+=1
        
    def fire(self,empid):
        self.employees = [e for e in self.employees if e.id != empid] 
        Office.employeesNum -= 1
        
    def deduct(self, empid, deduction):
        emp= self.get_employee(empid)
        if emp:
            emp.salary -= deduction
    
    def reward(self,empid,reward):
        emp= self.get_employee(empid)
        if emp:
            emp.salary += reward
            
    
    @staticmethod    
    def calculate_lateness(targetHour,moveHour,distance,velocity):
        travel_time= distance/velocity
        arrival_time= moveHour+travel_time
        return arrival_time > targetHour
    
    def check_lateness(self,empid,moveHour):
        emp= self.get_employee(empid)
        isLate= self.calculate_lateness(9, moveHour, emp.distanceToWork, 60)
        
        if isLate:
            self.deduct(empid, 10)
        else:
            self.reward(empid, 10)
    
    
    
    
    
    