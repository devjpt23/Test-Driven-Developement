class calculations:

    def multiply(self,x,y):
        if not isinstance(x,int) and not isinstance(x,float):
            if not x.replace('.','',1).isnumeric():
                raise TypeError('value must be an integer')
            x = float(x)
        
        if not isinstance(y,int) and not isinstance(y,float):
            if not y.replace('.','',1).isnumeric():
                raise TypeError('value must be an integer')
            y = float(y)
                    
        return x * y
    

calc = calculations()

print(calc.multiply(2,2))
print(calc.multiply('2.2','2.2'))
# print(calc.multiply('dev',2))
    