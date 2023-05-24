#%%
import sqlite3
from fhir.resources.patient import Patient
from fhir.resources.observation import Observation
from fhir.resources.observation import ObservationComponent
from fhir.resources.humanname import HumanName
from fhir.resources.codeableconcept import  CodeableConcept
from fhir.resources.coding import Coding 
from fhir.resources.reference import Reference
from fhir.resources.bundle import Bundle
import os


#get file from PATH
downloads_folder = os.path.expanduser("~") + "/Downloads/"
db_file = downloads_folder + "exampleinput.sqlite"
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('SELECT * from variant')
rows=cursor.fetchall()

#create an instance of a BUNDLE resource 
bundle = Bundle(type="batch")

#create a blank ReferenceType
subj = Reference()
#Assign reference variable as "Patient" for the Observation subject 
subj.reference = "Patient"
subject0 = subj

#create patientType
patient0 = Patient()
#create nameType
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

#Fill in patientType 
pat = Patient.parse_obj(json_obj)


#Save loinc url for ease of access
loinc = "http://loinc.org"


obs_list = []

for row in rows:
   #create codingType for row Observation
   coding = Coding()
   coding.system = loinc
   coding.code = "8480-6"
   code = CodeableConcept()
   code.coding = [coding]

   #Get Alleles from sqlite file  
   ref = row[4]
   alt = row[5]

   #create Observation Resource for row  
   obs_row = Observation(status="final", code=code, subject=subj)

   #Make Componenet for reference allele 
   coding_ref = Coding()
   coding_ref.system = loinc
   coding_ref.code = "69547-8" #always code for reference allele
   code_ref = CodeableConcept()
   code_ref.coding = [coding_ref]
   comp_ref = ObservationComponent(code=code_ref)
   comp_ref.valueString = alt

   #Make Componenet for (alt)ernate allele
   coding_alt = Coding()
   coding_alt.system = loinc
   coding_alt.code = "69551-0"
   code_alt = CodeableConcept()
   code_alt.coding = [coding_alt]
   comp_alt = ObservationComponent(code=code_alt)
   comp_alt.valueString = alt

   #add componenets to row observation
   obs_row.component = [comp_ref, comp_alt]

   #add row observation to list of observations 
   obs_list.append(obs_row)

entry = []
print(len(obs_list) == len(rows))

for ind_obs in obs_list:
   entry.append({"resource": ind_obs})

bundle.entry = entry
json_str = bundle.json()

print(json_str)

file_path = "output.json"

with open("output.json", "w") as file:
   file.write(json_str)
# %%
