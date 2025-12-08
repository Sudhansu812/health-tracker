import logging
from src import services as svc
from src.models import Person, Activity, ActivityType

logger = logging.getLogger("health_tracker.cli")
logger.info("Configured CLI process.")

def _prompt_nonempty(prompt: str) -> str:
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("Input cannot be empty.")

def _prompt_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def _prompt_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_person_from_cli() -> Person:
    name = _prompt_nonempty("Enter your name: ")
    age = _prompt_int("Enter your age: ")
    gender = input("Enter your gender (M / F): ").strip().upper()
    while gender not in {"M", "F"}:
        logger.error(f"Invalid gender: {gender}")
        gender = input("Invalid input. Please enter your gender (M / F): ").strip().upper()
    weight = _prompt_float("Enter your weight (in kg): ")
    height = _prompt_float("Enter your height (in cm): ")
    logger.info(f"Registering new person ({name}).")
    return svc.register_person(name, age, gender, weight, height)

def get_activity_from_cli(person: Person) -> Activity:
    activity_name = _prompt_nonempty("Enter activity name: ")
    valid_types = [t.name for t in ActivityType]
    activity_type = input(f"Enter activity type {valid_types}: ").strip().upper()
    while activity_type not in valid_types:
        logger.error(f"Invalid activity type: {activity_type}")
        activity_type = input(f"Invalid input. Please enter a valid activity type {valid_types}: ").strip().upper()
    duration = _prompt_int("Enter duration (in minutes): ")
    activity = svc.log_activity(person, activity_name, activity_type, duration)
    return activity

def run(cfg) -> None:
    person = get_person_from_cli()
    logger.info(f"Person {person.name} registered successfully.")
    print(f"Registered Person:\n{svc.get_person(person)}\n")
    logger.info(f"Logging activities.")
    while True:
        activity = get_activity_from_cli(person)
        print(f"Logged Activity: {activity}")
        more = input("Do you want to log another activity? (y/n): ").strip().lower()
        logger.info(f"Logged Activity: {activity.name}")
        if more != 'y':
            logger.info("Finished logging activities.")
            break
    logger.info(f"Generating activity summary for {person.name}.")
    summary = svc.summarize_activities(person)
    logger.info(f"Activity summary generated.")
    print(summary)

def print_config(cfg):
    print(cfg)
    print(f'Started {cfg["app"]["name"]} v{cfg["app"].get("version")}')
