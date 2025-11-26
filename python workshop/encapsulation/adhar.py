class Adhar:
    def __init__(self,name,adhar_number,dob,finger_print,retina):
        self.name=name
        self.adhar_number=adhar_number
        self.dob=dob
        self._finger_print=finger_print
        self.__retina=retina

    def display_userData(self):
       print(f"retina:{self.__retina},adhar_number:{self.adhar_number},dob:{self.dob},finger_print:{self._finger_print}")

var=Adhar("priya",364,"24-9-2002","rur","jfn")
var.display_userData()
retina_var=var.getRetina()
print(retina_var)