class Test:

    def instance_methode(self):
        print("Instance_method called by", self)

    @classmethod
    def class_method(cls):
        print("Called class_method by", hex(id(cls)))

    @staticmethod
    def static_method(p):
        print("Called static_method by" , p)


print("1", hex(id(Test)))

t1 = Test()  # we create an instance of the class, we create an object

t1.instance_methode()  # not forget the () , self will get the id of the object

Test.instance_methode(t1)  # the class can call the instance methode if it passes the id of the object

Test.class_method()  # Test.class_method(Test)  class will be automatically passed to the function, convention is to use cls as parameter

Test.static_method("1")  # werkt zoals een gewone functie

t1.static_method("2")  # werkt zoals een gewone functie
'''
an instance method is called by the instance of the class or with the instance of the class, it has always self as the first parameter
instancemethods are use for actions using the data of the objects, by self the methods can access all data of the object
classmethods are used as factories ( alternatieve constructors)
staticmethods can be used by the class and the object but not need access to the class or object
'''