# add your Student class here!

class Student:
    def __init__(self, name, year, classes_list):
        self.name = name
        self.year = year
        self.classes_list = classes_list
    
    def add_class(self, class_to_add):
        self.classes_list.append(class_to_add)
        return self.classes_list

    def get_num_classes(self):
        return len(self.classes_list)

    def summary(self):
        return f"{self.name} is a {self.year} enrolled in {self.get_num_classes()} classes"

    
