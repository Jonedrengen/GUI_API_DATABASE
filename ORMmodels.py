from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, NVARCHAR, Date
from sqlalchemy.ext.declarative import declarative_base
# for describing relationships
from sqlalchemy.orm import relationship

#Pydantic models: used to define response and requests data in the API
#ORM models: used to directly interact with the database (querying)


#creating a Base class for declerative class definitions. 
#this Base class will serve as a foundation for all ORM mappings to database tables.
#it allows us to define classes in a way that SQLAlchemy can interpret and translate into database tables.
Base = declarative_base() 

# defining a class that inherits from Base (the class will function in a way SQLalchemy understands)
# The class is a mapping of the table in the db (ORM concept)
class Persons(Base):
    __tablename__ = "Persons" #name of table the class maps to
    __table_args__ = {'schema': 'main'} #name of Schema

    # the actual "map": Defining the columns of the table
    CPR = Column("CPR", NVARCHAR(10), primary_key=True)
    Phone_number = Column("Phone_number", NVARCHAR(50))
    Region = Column("Region", NVARCHAR(50), nullable=True)
    Gender = Column("Gender", CHAR(1))
    
    # contructer of the person class
    # it initializes a new instance of the Persons class, with specific values for the attributes (attributes match columns in table)
    # When creating a new instance of a class, you have to add the values specified in the constructer
    # so new_class_instance = Person(CPR="xxxx", Phone_number="xxxx", and so on)
    def __init__(self, CPR, Phone_number, Region, Gender):
        self.CPR = CPR
        self.Phone_number = Phone_number
        self.Region = Region
        self.Gender = Gender

    # just a specification on how it should print a person
    def __repr__(self): #function that allows us to specify how we would like to print a person
        return f"{self.CPR}, {self.Phone_number}, {self.Region}, {self.Gender}"
    

# Repeat of Persons class
class Sample(Base): #inherits from Base class
    __tablename__ = "Sample"
    __table_args__ = {'schema': 'main'}

    SampleID = Column("SampleID", NVARCHAR(50), primary_key=True)
    # I am defining a ForeignKey here. It does not matter that it is not defined in the DB
    CPR = Column("CPR", NVARCHAR(20), ForeignKey("main.Persons.CPR"), nullable=True)
    SampleDate = Column("SampleDate", Date)
    Host = Column("Host", NVARCHAR(50), nullable=True)
    Ct = Column("Ct", NVARCHAR(50), nullable=True)

    #If attribute can have NULL, then describe it in the constructor (order does not matter here, only that NULLS, should be in the end)
    def __init__(self, SampleID, SampleDate, CPR=None, Host=None, Ct=None): #self references its own class (so Sample class)
        self.SampleID = SampleID
        self.CPR = CPR
        self.SampleDate = SampleDate
        self.Host = Host
        self.Ct = Ct

    def __repr__(self):
        return f"{self.SampleID}, {self.CPR}, {self.SampleDate}, {self.Host}, {self.Ct}"

result = Sample
print(type(result))

class COVID19(Base):
    __tablename__ = "COVID19"
    __table_args__ = {'schema': 'main'}

    CovidID = Column("CovidID", NVARCHAR(50), primary_key=True)
    Pango_designation = Column("Pango_designation", NVARCHAR(20), nullable=True)
    WhoVariant = Column("WhoVariant", NVARCHAR(50), nullable=True)
    QcScore = Column("QcScore", NVARCHAR(50), nullable=True)

    def __init__(self, CovidID, Pango_designation=None, WhoVariant=None, QcScore=None):
        self.CovidID = CovidID
        self.Pango_designation = Pango_designation
        self.WhoVariant = WhoVariant
        self.QcScore = QcScore

    def __repr__(self):
        return f"{self.CovidID}, {self.Pango_designation}, {self.WhoVariant}, {self.QcScore}"
    

class Legionella(Base):
    __tablename__ = "Legionella"
    __table_args__ = {'schema': 'main'}

    LegionellaID = Column("LegionellaID", NVARCHAR(50), primary_key=True)
    Genotype = Column("Genotype", NVARCHAR(20), nullable=True)
    Disease = Column("Disease", NVARCHAR(400),  nullable=True)
    DiseasePhenotype = Column("DiseasePhenotype", NVARCHAR(4000), nullable=True)
    DanishLocation = Column("DanishLocation", NVARCHAR(4000), nullable=True)
    ForeignLocation = Column("ForeignLocation", NVARCHAR(4000), nullable=True)
    AcquiredFood = Column("AcquiredFood", NVARCHAR(100), nullable=True)

    def __init__(self, LegionellaID, Genotype=None, Disease=None, DiseasePhenotype=None, DanishLocation=None, ForeignLocation=None, AcquiredFood=None):
        self.LegionellaID = LegionellaID
        self.Genotype = Genotype
        self.Disease = Disease
        self.DiseasePhenotype = DiseasePhenotype
        self.DanishLocation = DanishLocation
        self.ForeignLocation = ForeignLocation
        self.AcquiredFood = AcquiredFood
    
    def __repr__(self):
        return f'data: {self.LegionellaID} {self.Genotype} {self.Disease} {self.DiseasePhenotype} {self.DanishLocation} {self.ForeignLocation} {self.AcquiredFood}'
    
class Batch(Base):
    __tablename__ = "Batch"
    __table_args__ = {"schema": "main"}

    BatchID = Column("BatchID", NVARCHAR(50), primary_key=True)
    BatchDate = Column("BatchDate", Date)
    Platform = Column("Platform", NVARCHAR(50))
    BatchSource = Column("BatchSource", NVARCHAR(50))

    def __init__(self, BatchID, BatchDate, Platform, BatchSource):
        self.BatchID = BatchID
        self.BatchDate = BatchDate
        self.Platform = Platform
        self.BatchSource = BatchSource
    
    def __repr__(self):
        return f'data: {self.BatchID} {self.BatchDate} {self.Platform} {self.BatchSource}'
    

class SequencedSample(Base):
    __tablename__ = "SequencedSample"
    __table_args__ = {"schema": "main"}

    SequencedSampleID = Column("SequencedSampleID", NVARCHAR(50), primary_key=True)
    SampleContent = Column("SampleContent", NVARCHAR(20), nullable=True)
    DateSequencing = Column("DateSequencing", NVARCHAR(50))
    Quality = Column("Quality", NVARCHAR(50), nullable=True)
    Organism = Column("Organism", NVARCHAR(50), nullable=True)
    OrganismID = Column("OrganismID", NVARCHAR(50), nullable=True)  # Generic ID
    SampleID = Column("SampleID", NVARCHAR(50), ForeignKey("main.Sample.SampleID"), nullable=True)
    BatchID = Column("BatchID", NVARCHAR(50), ForeignKey("main.Batch.BatchID"), nullable=True)

    # Application logic needed to handle which organism this ID refers to

    def __init__(self, SequencedSampleID, DateSequencing, SampleContent=None, Quality=None, Organism=None, OrganismID=None, SampleID=None, BatchID=None):
        self.SequencedSampleID = SequencedSampleID
        self.SampleContent = SampleContent
        self.DateSequencing = DateSequencing
        self.Quality = Quality
        self.Organism = Organism
        self.OrganismID = OrganismID
        self.SampleID = SampleID
        self.BatchID = BatchID

    # Representation and other methods...
    def __repr__(self):
        return f'data: {self.SequencedSampleID} {self.SampleContent} {self.DateSequencing} {self.Quality} {self.Organism} {self.OrganismID} {self.SampleID} {self.BatchID}'

    
class S_aureus(Base): 
    __tablename__ = "S_aureus"
    __table_args__ = {"schema": "main"}

    AreusID = Column("AreusID", NVARCHAR(50), primary_key=True)
    Genotype = Column("Genotype", NVARCHAR(20), nullable=True)
    Disease = Column("Disease", NVARCHAR(400), nullable=True)
    DiseasePhenotype = Column("DiseasePhenotype", NVARCHAR(4000), nullable=True)
    DanishLocation = Column("DanishLocation", NVARCHAR(4000), nullable=True)
    ForeignLocation = Column("ForeignLocation", NVARCHAR(4000), nullable=True)
    AcquiredHospital = Column("AcquiredHospital", NVARCHAR(100), nullable=True)
    AcquiredSurgery = Column("AcquiredSurgery", NVARCHAR(400), nullable=True)
    Infectionlocation = Column("Infectionlocation", NVARCHAR(400), nullable=True)

    def __init__(self, AreusID, Genotype=None, Disease=None, DiseasePhenotype=None, DanishLocation=None, ForeignLocation=None, AcquiredHospital=None, AcquiredSurgery=None, Infectionlocation=None):
        self.AreusID = AreusID
        self.Genotype = Genotype
        self.Disease = Disease
        self.DiseasePhenotype = DiseasePhenotype
        self.DanishLocation = DanishLocation
        self.ForeignLocation = ForeignLocation
        self.AcquiredHospital = AcquiredHospital
        self.AcquiredSurgery = AcquiredSurgery
        self.Infectionlocation = Infectionlocation

    def __repr__(self):
        return f'data: {self.AreusID} {self.Genotype} {self.Disease} {self.DiseasePhenotype} {self.DanishLocation} {self.ForeignLocation} {self.AcquiredHospital} {self.AcquiredSurgery} {self.Infectionlocation}'


class S_epidermidis(Base):
    __tablename__ = "S_epidermidis" #Beware typo in column "Epidermides instead of Epidermidis"
    __table_args__ = {"schema": "main"}
    
    EpidermidesID = Column("EpidermidesID", NVARCHAR(50), primary_key=True)
    Genotype = Column("Genotype", NVARCHAR(20), nullable=True)
    Disease = Column("Disease", NVARCHAR(400), nullable=True)
    DiseasePhenotype = Column("DiseasePhenotype", NVARCHAR(4000), nullable=True)
    DanishLocation = Column("DanishLocation", NVARCHAR(4000), nullable=True)
    ForeignLocation = Column("ForeignLocation", NVARCHAR(4000), nullable=True)
    AcquiredHospital = Column("AcquiredHospital", NVARCHAR(100), nullable=True)
    AcquiredSurgery = Column("AcquiredSurgery", NVARCHAR(400), nullable=True)
    Infectionlocation = Column("Infectionlocation", NVARCHAR(400), nullable=True)
    
    def __init__(self, EpidermidesID, Genotype=None, Disease=None, DiseasePhenotype=None, DanishLocation=None, ForeignLocation=None, AcquiredHospital=None, AcquiredSurgery=None, Infectionlocation=None):
        self.EpidermidesID = EpidermidesID
        self.Genotype = Genotype
        self.Disease = Disease
        self.DiseasePhenotype = DiseasePhenotype
        self.DanishLocation = DanishLocation
        self.ForeignLocation = ForeignLocation
        self.AcquiredHospital = AcquiredHospital
        self.AcquiredSurgery = AcquiredSurgery
        self.Infectionlocation = Infectionlocation
    
    def __repr__(self):
        return f'data: {self.EpidermidesID} {self.Genotype} {self.Disease} {self.DiseasePhenotype} {self.DanishLocation} {self.ForeignLocation} {self.AcquiredHospital} {self.AcquiredSurgery} {self.Infectionlocation}'
    

