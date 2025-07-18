from pydantic import BaseModel

class Address(BaseModel):
    state: str
    country: str
    pinCode: int

class Patient(BaseModel):
    name: str
    age: int
    address : Address


patientAddressData = {
    "state" : "Odisa",
    "country" : "India",
    "pinCode" : 761024
}
patientAddress = Address(**patientAddressData)

storePatientData = {
    "name" : "Arupa Nanda Swain",
    "age" : 21,
    "address" : patientAddressData
}

def viewTheData(patient):
    print(patient.name)
    print(patient.address)
    print(patient.address.pinCode)
    print("viewed..")

patient = Patient(**storePatientData)
viewTheData(patient)

temp = patient.model_dump(include=['name'])
temp1 = patient.model_dump(exclude={"address":['pinCode']})

returnJson = patient.model_dump_json()
print(returnJson)
print(type(returnJson))
print(temp)
print(type(temp))
print(temp1)
print(type(temp1))