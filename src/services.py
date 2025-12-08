from typing import Optional
from src.models import Person, Activity, ActivityType

def register_person(name: str, age: int, gender: str, weight_kg: float, height_cm: float) -> Person:
    person = Person(name=name.strip(), age=int(age), gender=gender, weight_kg=float(weight_kg), height_cm=float(height_cm))
    return person

def get_person(person: Person) -> str:
    return str(person)

def log_activity(person: Person, activity_name: str, activity_type: str | ActivityType, duration: int) -> Activity:
    # accept either ActivityType or a valid activity_type name
    if isinstance(activity_type, str):
        try:
            activity_type_enum = ActivityType[activity_type]
        except KeyError as exc:
            raise ValueError(f"Unknown activity type: {activity_type}") from exc
    else:
        activity_type_enum = activity_type

    activity = Activity(name=activity_name.strip(), activity_type=activity_type_enum, duration_min=int(duration))
    activity.calculate_calories_burned(person)
    person.add_activity(activity)
    return activity

def summarize_activities(person: Person) -> str:
    total_calories = sum(activity.calories_burned for activity in person.activities)
    lines = [f"Activity Summary for {person.name}:"]
    for activity in person.activities:
        lines.append(str(activity))
    lines.append(f"Total Calories Burned: {total_calories:.2f} kcal")
    return "\n".join(lines)
