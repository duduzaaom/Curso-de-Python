import json
import urllib.request

def process_url(url: str) -> json:
    my_request = urllib.request.urlopen(url)

    return json.load(my_request)


def retrieve_all() -> list:
    result = []
    courses = process_url("https://studies.cs.helsinki.fi/stats-mock/api/courses")

    for course in courses:
        if course["enabled"] == False:
            continue
        else:
            result.append((course["fullName"], course["name"], course["year"], sum(course["exercises"])))

    return result


def retrieve_course(course_name: str) -> dict:
    result = {}

    url = f" https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    my_request = urllib.request.urlopen(url)
    course_info = json.load(my_request)
    
    result["weeks"] = len(course_info)
    students_max = 0
    hours = 0
    exercises = 0
    for week, week_info in course_info.items():
        hours += week_info["hour_total"]
        exercises += week_info["exercise_total"]
        if week_info["students"] > students_max:
            students_max = week_info["students"]

    result["students"] = students_max
    result["hours"] = hours
    result["hours_average"] = hours//students_max
    result["exercises"] = exercises
    result["exercises_average"] = exercises//students_max

    return result


if __name__ == "__main__":
    retrieve_course("docker2019")