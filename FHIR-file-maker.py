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
# %%
from fhirclient import client
from fhirclient.models import (
    fhirdate,
    codeableconcept,
    coding,
    observation,
    quantity,
    reference
)

# create an instance of the FHIR client
smart = client.FHIRClient(settings={'app_id': 'my_web_app', 'api_base': 'https://my-fhir-server.com'})

# create a new observation resource
obs = observation.Observation()

# set the observation status
obs.status = 'final'

# set the observation code
code = coding.Coding()
code.system = 'http://loinc.org'
code.code = '12345-6'
code.display = 'Blood pressure'

obs.code = codeableconcept.CodeableConcept()
obs.code.coding = [code]

# set the observation value
obs.valueQuantity = quantity.Quantity()
obs.valueQuantity.value = 120
obs.valueQuantity.unit = 'mmHg'
obs.valueQuantity.system = 'http://unitsofmeasure.org'

# set the observation reference
obs.subject = reference.Reference()
obs.subject.reference = 'Patient/example'

# set the observation effective time
obs.effectiveDateTime = fhirdate.FHIRDate('2022-01-01T00:00:00.000Z')

# save the observation to the FHIR server
smart.

# %%
