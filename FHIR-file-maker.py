#%%
import sqlite3
from fhir.resources.patient import Patient
from fhir.resources.observation import Observation
from fhir.resources.humanname import HumanName

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

patient0.name = [name]
print(patient0.name)

coding.system = "http://loinc.org"
coding.code = "8480-6"
code = CodeableConcept()
code.coding = [coding]

observation_resource = Observation(status="final",code=code)

observation_resource.effectiveDateTime = '2023-05-10'
observation_resource.subject = "Patient"

for row in rows:
    component = observation.ObservationComponent()
    component.code = {'coding': [{'system': 'http://loinc.org', 'code': '48018-6', 'display': 'Genetic variant'}]}
    component.valueCodeableConcept = {'coding': [{'system': 'http://www.genenames.org', 'code': row[1], 'display': row[1]}]}
    component.valueQuantity = {'value': row[2], 'unit': '%', 'system': 'http://unitsofmeasure.org', 'code': '%'}
    component.interpretation = [{'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation', 'code': 'POS', 'display': 'positive'}]}]



# %%

#below is the immplementation hard writing the json fields as str's 
import sqlite3
from fhir.resources.patient import Patient
from fhir.resources.observation import Observation
from fhir.resources.humanname import HumanName
from fhir.resources.reference import Reference
from fhir.resources.quantity import Quantity
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
import os

downloads_folder = os.path.expanduser("~") + "/Downloads/"
db_file = downloads_folder + "exampleinput.sqlite"
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('SELECT * from variant')
rows=cursor.fetchall()
print(rows)
coding = Coding()

coding.system = "http://loinc.org"
coding.code = "8480-6"
code = CodeableConcept()
code.coding = [coding]

observation = Observation(status="final", code=code)
#observation.subject = {
#    "subject" : {
#       "reference" : "Akash Rampersad"
#    }}
observation.code = {
    "coding": [
        {
            "system" : "http://loinc.org",
            "code": "8480-6",
            "display" : "Genetic Variant"
        }
    ],
    "text": "Genetic Variant"
}

observation.method = {
    "method" : {
        "coding" : [
            {
                "system" : "http://loinc.org",
                "code" : "LA26398-0",
                "display" : "Sequencing"
      }
    ]
  }
}

print(observation.json())

