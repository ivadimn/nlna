from dataclasses import dataclass


@dataclass
class Teacher:
    pk: int = None
    login: str = None
    fio: str = None
    phone: str = None
    email: str = None
    comment: str = None
    user_id: int = None
