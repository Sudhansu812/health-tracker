from dataclasses import dataclass, field
from enum import Enum
from string import Template

class ActivityType(Enum):
    SLOW_WALKING = 2.0
    MODERATE_WALKING = 3.8
    FAST_WALKING = 5.0
    JOGGING = 8.0
    RUNNING = 9.0
    LIGHT_ACTIVITY = 2.5
    MODERATE_ACTIVITY = 6.0
    INTENSE_ACTIVITY = 12.0

@dataclass
class Activity:
    name: str
    activity_type: str
    duration_min: int
    calories_burned: float = 0.0

    def calculate_calories_burned(self, person: Person) -> float:
        self.calories_burned = (ActivityType[self.activity_type].value * 3.5 * person.weight_kg / 200) * self.duration_min
        return self.calories_burned

    def __str__(self) -> str:
        return f'Activity: {self.name}, Duration: {self.duration_min} mins, Calories Burned: {self.calories_burned:.2f} kcal'

    def __repr__(self) -> Template:
        return t'Activity(name={self.name}, activity_type={self.activity_type}, duration={self.duration_min}, calories_burned={self.calories_burned})'

@dataclass
class Person:
    name: str
    age: int
    gender: str
    weight_kg: float
    height_cm: float
    activities: list[Activity] = field(default_factory=list)
    bmi: float = 0

    def __post_init__(self):
        self.gender = self.gender.upper()
        if self.gender not in {"M", "F"}:
            raise ValueError("gender must be 'M' or 'F'")
        if self.height_cm <= 0:
            raise ValueError("height_cm must be positive")
        if self.weight_kg <= 0:
            raise ValueError("weight_kg must be positive")
        self.bmi = self.calculate_bmi()

    def calculate_bmi(self) -> float:
        self.bmi = self.weight_kg / ((self.height_cm / 100.0) ** 2)
        return self.bmi

    def add_activity(self, activity: Activity) -> None:
        self.activities.append(activity)

    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nWeight (in kg): {self.weight_kg}\nHeight (in cm): {self.height_cm}'

    def __repr__(self):
        return t'Person(name={self.name}, age={self.age}, gender={self.gender}, weight_kg={self.weight_kg}, height_cm={self.height_cm}, bmi={self.bmi}, activities={self.activities})'