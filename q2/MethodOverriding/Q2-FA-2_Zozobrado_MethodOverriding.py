class Patient:
    def __init__(self, name, bill_amount=0):
        self.__name = name
        self.__Bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def set_bill_amount(self, bill_amount):
        self.__Bill_amount = bill_amount

    def get_bill_amount(self):
        return self.__Bill_amount

    def calculate_bill(self):
        self.__Bill_amount += 1000
        return self.__Bill_amount


class SeniorPatient(Patient):
    def __init__(self, name, bill_amount=0):
        super().__init__(name, bill_amount)

    
    def calculate_bill(self):
        self._Patient__Bill_amount += 1000
       
        discount_rate = 0.20
        self._Patient__Bill_amount = self._Patient__Bill_amount * (1 - discount_rate)
        return self._Patient__Bill_amount

    def original_bill(self):
        return self._Patient__Bill_amount


class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount=0,):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        self._Patient__Bill_amount += 1000
       
        discount_rate = 0.15
        self._Patient__Bill_amount = self._Patient__Bill_amount * (1 - discount_rate)
        return self._Patient__Bill_amount
   
    def original_bill(self):
        return self._Patient__Bill_amount

patient1 = Patient("John Doe")
senior_patient1 = SeniorPatient("Jane Smith")
philhealth_patient1 = PhilHealthPatient("Mark Johnson")

print(" ===  HOSPITAL BILLING SYSTEM === ")
print(" ----------------------------------")
print("Patient Name:", patient1.get_name())
print("Original Bill Amount:", patient1.get_bill_amount())
print("Bill Amount:", patient1.calculate_bill())
print("\nPatient Name:", senior_patient1.get_name())
print("Original Bill Amount:", senior_patient1.original_bill())
print("Bill Amount:", senior_patient1.calculate_bill())
print("\nPatient Name:", philhealth_patient1.get_name())
print("Original Bill Amount:", philhealth_patient1.original_bill())
print("Bill Amount:", philhealth_patient1.calculate_bill()) 
print(" ----------------------------------")



 
