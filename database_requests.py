
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, VARCHAR
from sqlalchemy.orm import sessionmaker

#importing Base and mappings from ORMmodels.py
from ORMmodels import Base, Persons, Sample, COVID19, S_aureus, S_epidermidis, SequencedSample, Batch, Legionella

#importing Pydantic models
from pydantic_models import Persons_Pyd_model, S_aureus_Pyd_model, S_epidermidis_Pyd_model, Sample_Pyd_model, SequencedSample_Pyd_model, COVID19_Pyd_model, Batch_Pyd_model, Legionella_Pyd_model

from typing import Optional

#db stuff to connect with
server = "localhost"
database = "mydb"
username = "sa"
password = "Slotved2314!" # bad practice - but only for testing
driver = "ODBC Driver 18 for SQL Server" # direct location, because for some reason the standard does not work for me
connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}&TrustServerCertificate=yes"

#Creating the engine, that needs the DB specifications. It uses the connections string to determine the spcifics of the DB (such as db type, like mssql, SQLServer or whatever)
# the create_engine function is a factory method. Essentially it means that it is a OOP method that return an object, without specifying the exact class of the object
engine = create_engine(connection_string)

# Base: acts as a template for the table. It keeps track of all classes that represent the tables in the db
# metadata has all the information about these tables. (has all the blueprints)
# create_all() looks through the collection of data in metadata and builds any table that is missing (it uses the blueprints)
# the bind=engine just tells the builder "create_all()" which db to build the tables in
Base.metadata.create_all(bind=engine)

#creating a session. A temporary database workspace, where I can interact with the database
# autocommit=False: do not commit changes unless i tell you to
# autoflush=False: do not update my db when i modify my objects, unless i use session.flush()
# bind=engine: connect to engine db
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



    # defining a function to retrieve data from db, and convert it into a Pydantic model
def get_all_Persons():
    # definign a local session using "with as", to make sure it is closed after use (this is where the db connection happens)
    with SessionLocal() as session:
        # performing the db query with SQLAlchemy, to get all records from the Persons table, then saving it in a python variable in the structure of the Persons ORM.
        # session.query(Persons).all() returns a list of "Persons" objects, each object representing a row in the db
        person_orm = session.query(Persons).all()
        print(type(person_orm))
        # Transferring the ORM model to a pydantic model using the from_om() method from the pydantic model classes
        # this is possible because it inherits from BaseModel and orm_mode=True in the config (see the pydantic models for reference)
        #it is a basic list comprehension that iterates over every instance in the ORM model list -> person_orm 
        person_pydantic = [Persons_Pyd_model.from_orm(person) for person in person_orm]
        return person_pydantic

def get_all_Sample():
    with SessionLocal() as session:
        sample_orm = session.query(Sample).all()
        sample_pydantic = [Sample_Pyd_model.from_orm(sample) for sample in sample_orm]
        return sample_pydantic


def get_all_COVID19():
    with SessionLocal() as session:
        covid19_orm = session.query(COVID19).all()
        covid19_pydantic = [COVID19_Pyd_model.from_orm(covid19) for covid19 in covid19_orm]
        return covid19_pydantic
    
def get_all_S_aureus():
    with SessionLocal() as session:
        s_aureus_orm = session.query(S_aureus).all()
        s_aureus_pydantic = [S_aureus_Pyd_model.from_orm(s_aureus) for s_aureus in s_aureus_orm]
        return s_aureus_pydantic

def get_all_SequencedSample():
    with SessionLocal() as session:
        sequencedSample_orm = session.query(SequencedSample).all()
        sequencedSample_pydantic = [SequencedSample_Pyd_model.from_orm(sample) for sample in sequencedSample_orm]
        return sequencedSample_pydantic

def get_all_Batch():
    with SessionLocal() as session:
        batch_orm = session.query(Batch).all()
        batch_pydantic = [Batch_Pyd_model.from_orm(batch) for batch in batch_orm]
        return batch_pydantic

def get_all_Legionella():
    with SessionLocal() as session:
        legionella_orm = session.query(Legionella).all()
        legionella_pydantic = [Legionella_Pyd_model.from_orm(legionella) for legionella in legionella_orm]
        return legionella_pydantic

def get_all_S_epidermidis():
    with SessionLocal() as session:
        s_epidermidis_orm = session.query(S_epidermidis).all()
        s_epidermidis_pydantic = [S_epidermidis_Pyd_model.from_orm(s_epidermidis) for s_epidermidis in s_epidermidis_orm]
        return s_epidermidis_pydantic

    

