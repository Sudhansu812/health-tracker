from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import List

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
    activity_type: ActivityType
    duration_min: int
    calories_burned: float = 0.0

    def __post_init__(self):
        if self.duration_min <= 0:
            raise ValueError("duration_min must be positive")

    def calculate_calories_burned(self, person: 'Person') -> float:
        met = self.activity_type.value
        self.calories_burned = (met * 3.5 * person.weight_kg / 200) * self.duration_min
        return self.calories_burned

    def __str__(self) -> str:
        return f'Activity: {self.name}, Type: {self.activity_type.name}, Duration: {self.duration_min} mins, Calories Burned: {self.calories_burned:.2f} kcal'

    def __repr__(self) -> str:
        return f'Activity(name={self.name!r}, activity_type={self.activity_type.name!r}, duration_min={self.duration_min!r}, calories_burned={self.calories_burned!r})'

@dataclass
class Person:
    name: str
    age: int
    gender: str
    weight_kg: float
    height_cm: float
    activities: List[Activity] = field(default_factory=list)
    bmi: float = 0.0

    def __post_init__(self):
        self.gender = (self.gender or "").upper()
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
        return (
            f'Name: {self.name}\n'
            f'Age: {self.age}\n'
            f'Gender: {self.gender}\n'
            f'Weight (kg): {self.weight_kg}\n'
            f'Height (cm): {self.height_cm}\n'
            f'BMI: {self.bmi:.2f}\n'
            f'Activities: {len(self.activities)}'
        )

    def __repr__(self):
        return f'Person(name={self.name!r}, age={self.age!r}, gender={self.gender!r}, weight_kg={self.weight_kg!r}, height_cm={self.height_cm!r}, bmi={self.bmi!r}, activities={self.activities!r})'
