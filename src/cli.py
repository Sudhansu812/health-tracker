import logging
import services as svc
from src.models import Person, Activity

logger = logging.getLogger("health_tracker.cli")
logger.info("Configured CLI process.")

def get_person_from_cli() -> Person:
    name: str = input("Enter your name: ")
    age: int = int(input("Enter your age: "))
    gender: str = input("Enter your gender (M / F): ")
    while gender not in ["M", "F"]:
        logger.error(f"Invalid gender: {gender}")
        gender = input("Invalid input. Please enter your gender (M / F): ")
    weight: float = float(input("Enter your weight (in kg): "))
    height: float = float(input("Enter your height (in cm): "))
    logger.info(f"Registering new person ({name}).")
    return svc.register_person(name, age, gender, weight, height)

def get_activity_from_cli(person: Person) -> Activity:
    activity_name: str = input("Enter activity name: ")
    activity_type: str = input("Enter activity type (SLOW_WALKING, MODERATE_WALKING, FAST_WALKING, JOGGING, RUNNING, LIGHT_ACTIVITY, MODERATE_ACTIVITY, INTENSE_ACTIVITY): ")
    while activity_type not in ["SLOW_WALKING", "MODERATE_WALKING", "FAST_WALKING", "JOGGING", "RUNNING", "LIGHT_ACTIVITY", "MODERATE_ACTIVITY", "INTENSE_ACTIVITY"]:
        activity_type = input("Invalid input. Please enter a valid activity type: ")
    duration: int = int(input("Enter duration (in minutes): "))
    return svc.log_activity(person, activity_name, activity_type, duration)

def run(cfg) -> None:
    person: Person = get_person_from_cli()
    logger.info(f"Person {person.name} registered successfully.")
    print(f"Registered Person:\n{svc.get_person(person)}\n")
    logger.info(f"Logging activities.")
    while True:
        activity: Activity = get_activity_from_cli(person)
        print(f"Logged Activity: {activity}")
        more: str = input("Do you want to log another activity? (y/n): ")
        logger.info(f"Logged Activity: {activity.name}")
        if more.lower() != 'y':
            logger.info("Finished logging activities.")
            break
    logger.info(f"Generating activity summary for {person.name}.")
    summary: str = svc.summarize_activities(person)
    logger.info(f"Activity summary generated.")
    print(summary)

def print_config(cfg):
    print(cfg)
    print(f'Started {cfg["app"]["name"]} v{cfg["app"].get("version")}')
