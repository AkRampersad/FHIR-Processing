# %%

#below is the immplementation hard writing the json fields as str's 
import sqlite3
from fhir.resources.patient import Patient
from fhir.resources.observation import Observation
from fhir.resources.observation import ObservationComponent
from fhir.resources.humanname import HumanName
from fhir.resources.codeableconcept import  CodeableConcept
from fhir.resources.coding import Coding 
from fhir.resources.reference import Reference
import orjson


import os
downloads_folder = os.path.expanduser("~") + "/Downloads/"
db_file = downloads_folder + "exampleinput.sqlite"
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('SELECT * from variant')
rows=cursor.fetchall()
print(rows)
coding = Coding()


#json string 
json_str = {"resourceType": "Observation" } 


#Write ReferenceType resource in str
subj_obj = {"resourceType": "Reference",
            }

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