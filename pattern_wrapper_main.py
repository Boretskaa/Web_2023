import pattern_wrapper

myCoffee = pattern_wrapper.Concrete_Coffee()
print('Ingredients: '+myCoffee.get_ingredients()+
   '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

myCoffee = pattern_wrapper.Milk(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients()+
   '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

myCoffee = pattern_wrapper.Vanilla(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients()+
   '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

myCoffee = pattern_wrapper.Sugar(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients()+
   '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))