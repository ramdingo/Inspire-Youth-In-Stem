class car:
    def _init_(self,manufacturer,model,yearOfManufacture,engine):
        self.manufacturer=manufacturer
        self.model=model
        self.yearOfManufacture=yearOfManufacture
        self.engine=engine

#getters
    def get_manufacturer(self):
        return self.manufacturer

    def get_model(self):
        return self.model

    def get_year(self):
        return self.yearOfManufacture

    def get_engine(self):
        return self.engine
    
#setters
    def set_manufacturer(self,manufacturer):
        self.manufacturer=manufacturer

    def set_model(self,model):
        self.model=model

    def set_yearOfManufacture(self,yearOfManufacture):
        self.yearOfManufacture=yearOfManufacture

    def set_engine(self,engine):
        self.engine=engine

#objects/instances
car1=car("Nissan","demio",2018,1300)
car2=car("Toyota","Hilux",2020,2600)

car1.set_manufacturer("Nissan")
car1.set_model("demio")
car1.set_yearOfManufacture(2018)
car1.set_engine(1300)

print(car1.get_manufacturer())
print(car1.get_model())
print(car1.get_yearOfManufacture())
print(car1.get_engine())

print(car2.get_manufacturer())
print(car2.get_model())
print(car2.get_yearOfManufacture())
print(car2.get_engine())
