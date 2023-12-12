from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Spouse:
    first_name: str
    last_name: str
    dob: str
    id_type: str
    id_number: str
    middle_name: Optional[str] = None