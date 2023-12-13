
# Import Union from the typing module to allow for type hints that can accept multiple types (basically a parameter can be multiple datatypes, when passing)
from typing import Union

# for creating the api and handling HTTPExceptions
from fastapi import FastAPI, HTTPException

# importing the db engine created with SQLAlchemy
from database_requests import engine, get_all_Batch, get_all_COVID19, get_all_Legionella, get_all_Persons, get_all_S_aureus, get_all_S_epidermidis, get_all_Sample, get_all_SequencedSample
from sqlalchemy.orm import Session

#Importing pydantic models for validation and automatic JSON conversion
from pydantic_models import API_Response, Persons_Pyd_model, S_aureus_Pyd_model, S_epidermidis_Pyd_model, Sample_Pyd_model, SequencedSample_Pyd_model, COVID19_Pyd_model, Batch_Pyd_model, Legionella_Pyd_model

#
from typing import List


#creating an intance, where I will be connection all the routes to 
app = FastAPI()
# RUN: uvicorn name_of_file:app --reload ======== uvicorn fastAPI-main:app --reload

# ERROR WHEN RUNNING UVICORN: when running it normally "uvicorn fastAPI-main:app --reload" an error arises, likely because a wring environment is used to receive packages
# the solution I came up with wah to specify the path to the environment before starting the program "/Users/jonsztukslotved/anaconda3/envs/env/bin/python -m uvicorn fastAPI-main:app --reload"
# I must say that I am unsure if this is a sustainable solution for future iterations


#this might be redundant, since I call functions, where the db already is specified
def get_db():
    #creating a new session, which is bound to the engine imported from another file (engine=db connection)
    db = Session(bind=engine)
    try:
        yield db
    except Exception as e:
        print(f'an error occurred {e}')
        raise HTTPException(status_code=500, detail='Database connection error')
    finally:
        # no matter if the try block or except block runs, the db will be closed for ressource management
        db.close()

#class data_type(BaseModel):



#this is a FastAPI endpoint definition. When a GET request is made to "/fakedata",
# this function will be called to handle the request.
# get request happens when clent requests data from a server (like when you enter a website)
@app.get("/fakedata", response_model=API_Response)
def read_data() -> API_Response:
    # Retrieve data from the Persons table by calling the get_all_Persons function.
    # this function returns a list of Pydantic model instances.
    Person_data = get_all_Persons()

    # Similarly, retrieve data from other tables by calling their respective functions.
    # Each function returns a list of Pydantic model instances corresponding to the table.
    Batch_data = get_all_Batch()
    Sample_data = get_all_Sample()
    Covid_data = get_all_COVID19()
    Legio_data = get_all_Legionella()
    Areus_data = get_all_S_aureus()
    Epider_data = get_all_S_epidermidis()
    Sequence_data = get_all_SequencedSample()
    
    # Construct an API_Response object by passing the retrieved data.
    # This object is a Pydantic model that represents the structure of the response.
    return API_Response(persons=Person_data,
                        batches=Batch_data,
                        samples=Sample_data,
                        covid19=Covid_data,
                        legionella=Legio_data,
                        s_aureus=Areus_data,
                        s_epidermidis=Epider_data,
                        sequencedsample=Sequence_data
                        )

# Note: The endpoint can be accessed at http://127.0.0.1:active_port/fakedata once the FastAPI server is running.
# The returned data will be in JSON format as defined by the API_Response Pydantic model.



@app.get("/samples", response_model=List[Sample_Pyd_model])
def get_samples():
    try:
        samples = get_all_Sample()  # Function to fetch data from your database
        return samples
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")



@app.get("/persons", response_model=List[Persons_Pyd_model])
def read_Persons_data():
    try:
        Persons_data = get_all_Persons()
        return Persons_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'{e}')

#result = read_data()
#print(type(result)) -> dict


@app.get("/sequencedsample", response_model=List[SequencedSample_Pyd_model])
def read_sequencedsample_data():
    try:
        sequencedsample_data = get_all_SequencedSample()
        return sequencedsample_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'{e}')

@app.get("/batch", response_model=List[Batch_Pyd_model])
def read_batch_data():
    try:
        batch_data = get_all_Batch()
        return batch_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'{e}')
    
@app.get("/covid19", response_model=List[COVID19_Pyd_model])
def read_covid_data():
    try:
        covid_data = get_all_COVID19()
        return covid_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'{e}')

@app.get("/legionella", response_model=List[Legionella_Pyd_model])
def red_legio_data():
    try:
        legio_data = get_all_Legionella()
        return legio_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'{e}')
    

@app.get("/saureus", response_model=List[S_aureus_Pyd_model])
def read_saureus_data():
    try:
        saureus_data = get_all_S_aureus()
        return saureus_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'{e}')
    
@app.get("/epidermidis", response_model=List[S_epidermidis_Pyd_model])
def read_epidermidis_data():
    try:
        epidermidis_data = get_all_S_epidermidis()
        return epidermidis_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'{e}')
