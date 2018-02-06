class Patient:
    def __init__(self, name):
        self.name = name

    def discharge(self):
        raise NotImplementedError("Abstract method")

class EmergencyPatient(Patient):
    def __init__(self, name):
        Patient.__init__(self, name)

    def discharge(self):
        """returns the name and type of patient that was admitted"""
        label = [self.name, 'Emergency Patient']
        print(label)

class HospitalizedPatient(Patient):
    def __init__(self, name):
        Patient.__init__(self, name)

    def discharge(self):
        """ returns the name and type of patient that was admitted"""
        label = [self.name, 'Hospitalized Patient']
        print(label)

class Hospital:
    def __init__(self, patients, cost):
        self.patients = patients
        self.cost = cost

    def admit(self, patients):
        self.patients.append(patients)

    def discharge_all(self):
        for patient in self.patients:
            patient.discharge()

    def get_total_cost(self):

        totalcost = self.cost
        for patient in self.patients:
            if patient.__class__ == EmergencyPatient:
                totalcost += 1000
            elif patient.__class__ == HospitalizedPatient:
                totalcost += 2000

        return totalcost

myHospital = Hospital([],0)
E1 = EmergencyPatient("Robert")
E2 = EmergencyPatient("John")
H1 = HospitalizedPatient("Paul")
H2 = HospitalizedPatient("George")
H3 = HospitalizedPatient("Ringo")

myHospital.admit(E1)
myHospital.admit(E2)
myHospital.admit(H1)
myHospital.admit(H2)
myHospital.admit(H3)

myHospital.discharge_all()

print(myHospital.get_total_cost())

