from models import Person, Activity

def register_person(name: str, age: int, gender: str, weight_kg: float, height_cm: float) -> Person:
    return Person(name=name, age=age, gender=gender, weight_kg=weight_kg, height_cm=height_cm)

def get_person(person) -> str:
    return str(person)

def log_activity(person: Person, activity_name: str, activity_type: str, duration: int) -> Activity:
    activity = Activity(name=activity_name, activity_type=activity_type, duration_min=duration)
    activity.calculate_calories_burned(person)
    person.add_activity(activity)
    return activity

def summarize_activities(person: Person) -> str:
    total_calories = sum(activity.calories_burned for activity in person.activities)
    summary = f"Activity Summary for {person.name}:\n"
    for activity in person.activities:
        summary += str(activity) + "\n"
    summary += f"Total Calories Burned: {total_calories} kcal\n"
    return summary
