#%% Abstract Factory Pattern

class AbstractFactory():
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()



class AbstractProductA():
    def interface_a(self):
        pass


class ConcreteProductA1(AbstractProductA):
    def interface_a(self):
        print("ConcreteProductA1")


class ConcreteProductA2(AbstractProductA):
    def interface_a(self):
        print("ConcreteProductA2")



class AbstractProductB():
    def interface_b(self):
        pass


class ConcreteProductB1(AbstractProductB):
    def interface_b(self):
        print("ConcreteProductB1")


class ConcreteProductB2(AbstractProductB):
    def interface_b(self):
        print("ConcreteProductB2")


def main():
    for factory in (ConcreteFactory1(), ConcreteFactory2()):
        # Client Logic
        product_a = factory.create_product_a()
        product_b = factory.create_product_b()
        product_a.interface_a()
        product_b.interface_b()



if __name__ == "__main__":
    main()



#%%