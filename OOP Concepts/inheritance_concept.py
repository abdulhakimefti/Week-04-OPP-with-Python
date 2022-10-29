from lib2to3.pytree import Base


#base class 
#parent class
class BaseClass :
    pass 

#derived class
#child class
class DerivedClass(BaseClass):
    pass
# 1. single level inheritance(parent--> child)
# 2.multi level inheritance(grandpa->parent-->child)
# 3. multiple inheritance(father,mother: child -->(father,mother))
# 4.Hierarchical Inheritance(father : you ---> father,brother --> fathe,sister-->father)
# 5. Hybrid Inheritance