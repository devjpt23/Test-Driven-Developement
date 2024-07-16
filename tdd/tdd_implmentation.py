
class Writing:

    def greeting(self,name):
        if not isinstance(name,str):
            raise ValueError('name must be a string')
        return f"Hello {name}"