class MakeMeal:

   def prepare(self): pass
   def cook(self): pass
   def eat(self): pass

   def go(self):
      self.prepare()
      self.cook()
      self.eat()

class MakePizza(MakeMeal):
   def prepare(self):
      print ("Prepare Pizza")
   
   def cook(self):
      print ("Cook Pizza")
   
   def eat(self):
      print ("Eat Pizza")

class MakeCoffee(MakeMeal):
   def prepare(self):
      print ("Prepare Coffee")
	
   def cook(self):
      print ("Cook Coffee")
   
   def eat(self):
      print ("Drink Coffee")

makePizza = MakePizza()
makePizza.go()

print ("and")

makeTea = MakeCoffee()
makeTea.go()