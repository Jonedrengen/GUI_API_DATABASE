# for validation of data
from pydantic import BaseModel, ConfigDict

#for specifying dates in the pydantic models
from datetime import date

#Pydantic models: used to define response and requests data in the API
#ORM models: used to directly interact with the database (querying)

from typing import List

#creating pydantic models. They are to validate the data received from the database
class Persons_Pyd_model(BaseModel):
     # the class Config from_attributes = True, makes it so that the .from_orm() function able to transform the orm objects into pydantic models
    class Config:
        from_attributes = True
        
    CPR: str
    Phone_number: str
    Region: str
    Gender: str

    

class Sample_Pyd_model(BaseModel):
    class Config:
        from_attributes = True
    
    SampleID: str
    CPR: str | None
    SampleDate: date
    Host: str | None
    Ct: str | None




class Batch_Pyd_model(BaseModel):
    class Config:
        from_attributes = True
    
    BatchID: str
    BatchDate: date
    Platform: str
    BatchSource: str

class COVID19_Pyd_model(BaseModel):
    class Config:
        from_attributes = True
    CovidID: str
    Pango_designation: str
    WhoVariant: str
    QcScore: str

class Legionella_Pyd_model(BaseModel):
    class Config:
        from_attributes = True
    LegionellaID: str
    Genotype: str
    Disease: str
    DiseasePhenotype: str
    DanishLocation: str
    ForeignLocation: str
    AcquiredFood: str


class SequencedSample_Pyd_model(BaseModel):
    class Config:
        from_attributes = True
    SequencedSampleID: str
    SampleContent: str
    DateSequencing: str
    Quality: str
    Organism: str
    OrganismID: str
    SampleID: str
    BatchID: str

class S_aureus_Pyd_model(BaseModel):
    class Config:
        from_attributes = True
    AreusID: str
    Genotype: str
    Disease: str
    DiseasePhenotype: str
    DanishLocation: str
    ForeignLocation: str
    AcquiredHospital: str
    AcquiredSurgery: str
    Infectionlocation: str


class S_epidermidis_Pyd_model(BaseModel):
    class Config:
        from_attributes = True
    EpidermidesID: str
    Genotype: str
    Disease: str
    DiseasePhenotype: str
    DanishLocation: str
    ForeignLocation: str
    AcquiredHospital: str
    AcquiredSurgery: str
    Infectionlocation: str

    


#creating the API response model: Handles the automatic JSON conversion (when used in the API endpoint) as well as validating the data
class API_Response(BaseModel):
    class Config:
        from_attributes = True

    
    persons: List[Persons_Pyd_model]
    samples: List[Sample_Pyd_model]
    batches: List[Batch_Pyd_model]
    covid19: List[COVID19_Pyd_model]
    legionella: List[Legionella_Pyd_model]
    sequencedsample: List[SequencedSample_Pyd_model]
    s_aureus: List[S_aureus_Pyd_model]
    s_epidermidis: List[S_epidermidis_Pyd_model]