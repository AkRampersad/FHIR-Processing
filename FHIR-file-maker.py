#%%
import sqlite3
from fhir.resources.patient import Patient
from fhir.resources.observation import Observation
from fhir.resources.observation import ObservationComponent
from fhir.resources.humanname import HumanName
from fhir.resources.codeableconcept import  CodeableConcept
from fhir.resources.coding import Coding 
from fhir.resources.reference import Reference
import json


import os

downloads_folder = os.path.expanduser("~") + "/Downloads/"
db_file = downloads_folder + "exampleinput.sqlite"
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('SELECT * from variant')
rows=cursor.fetchall()

coding = Coding()



#create a blank ReferenceType
subj = Reference()
#Assign reference variable as "Patient" for the Observation subject 
subj.reference = "Patient"

print(subj)
print(isinstance (subj, Reference))

subject0 = subj
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


print(isinstance(pat.name,dict))
print(isinstance(json_obj, dict))

coding.system = "http://loinc.org"
coding.code = "8480-6"
code = CodeableConcept()
code.coding = [coding]

observation0 = Observation(status="final",code=code,subject=subj)


print(observation0.code)

observation0.effectiveDateTime = '2023-05-10'

print(observation0.subject == subject0)



#for row in rows:
#   component = observation0.component()
#  component.code = {'coding': [{'system': 'http://loinc.org', 'code': '48018-6', 'display': 'Genetic variant'}]}
#   component.valueCodeableConcept = {'coding': [{'system': 'http://www.genenames.org', 'code': row[1], 'display': row[1]}]}
#   component.valueQuantity = {'value': row[2], 'unit': '%', 'system': 'http://unitsofmeasure.org', 'code': '%'}
#   component.interpretation = [{'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation', 'code': 'POS', 'display': 'positive'}]}]






# %%
