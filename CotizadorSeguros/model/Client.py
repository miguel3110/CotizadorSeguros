from dataclasses import dataclass, field
from typing import List, Optional
from model.Spouse import Spouse
from model.Dependent import Dependent

@dataclass
class Client: 
    first_name: str
    last_name: str 
    email: str
    dob: str
    age: int
    id_type: str
    id_number: str
    gender: str
    company: str
    location: str
    AccountExecutive: str
    has_spouse: bool = False
    has_children: bool = False
    number_of_dependent: int = 0
    dependent: List[Dependent] = field(default=list)
    spouse: Optional[Spouse] = None
    middle_name: Optional[str] = None
    last_name2: Optional[str] = None
