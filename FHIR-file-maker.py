#%%
import sqlite3
from fhir.resources.patient import Patient
from fhir.resources.observation import Observation
from fhir.resources.humanname import HumanName
from fhir.resources.codeableconcept import  CodeableConcept
from fhir.resources.coding import Coding 
import json


import os

downloads_folder = os.path.expanduser("~") + "/Downloads/"
db_file = downloads_folder + "exampleinput.sqlite"
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('SELECT * from variant')
rows=cursor.fetchall()
print(rows)
coding = Coding()



#create patient
patient0 = Patient()
name = HumanName()
name.use = "official"
name.family = "Rampersad"
name.given = ["Akash"]

json_obj = {"resourceType": "Patient", 
            "id": "p001",
            "active" : True,
            "name":[{"text": "Akash Rampersad"}],
            "birthDate": "1998-05-05"
}

patient0.name = [name]
pat = Patient.parse_obj(json_obj)

print(isinstance(pat, Patient))

#print(json.dumps(patient0))

coding.system = "http://loinc.org"
coding.code = "8480-6"
code = CodeableConcept()
code.coding = [coding]

observation = Observation(status="final",code=code)

print(observation.code)

observation.effectiveDateTime = '2023-05-10'

observation.subject = [pat]



for row in rows:
    component = observation.ObservationComponent()
    component.code = {'coding': [{'system': 'http://loinc.org', 'code': '48018-6', 'display': 'Genetic variant'}]}
    component.valueCodeableConcept = {'coding': [{'system': 'http://www.genenames.org', 'code': row[1], 'display': row[1]}]}
    component.valueQuantity = {'value': row[2], 'unit': '%', 'system': 'http://unitsofmeasure.org', 'code': '%'}
    component.interpretation = [{'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation', 'code': 'POS', 'display': 'positive'}]}]






# %%
