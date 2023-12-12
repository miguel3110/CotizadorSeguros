from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Dependent: 
    first_name: str
    last_name: str
    dob: str
    gender: str
    middle_name: Optional[str] = None