from datetime import datetime, timedelta

def process_files():
    with open("start_times.csv") as start_file, open("submissions.csv") as submission_file:
        students = {}
        for line in start_file:
            line = line.strip().split(";")
            students[line[0]] = {
                "tasks": [],
                "points": [],
                "start_hour": datetime.strptime(line[1], "%H:%M"),
                "ending_hour": []
                }
            
        for line in submission_file:
            line = line.strip().split(";")
            students[line[0]]["tasks"].append(int(line[1]))
            students[line[0]]["points"].append(int(line[2]))
            students[line[0]]["ending_hour"].append(datetime.strptime(line[3], "%H:%M"))

        return students


def final_points() -> dict:
    exam_points = {}
    students = process_files()
    for student, info in students.items():
        tasks = {}
        for index, task in enumerate(info["tasks"]):
            if info["ending_hour"][index] - info["start_hour"] > timedelta(hours=3):
                continue
            elif task not in tasks:
                tasks[task] = info["points"][index]
                continue
            elif info["points"][index] > tasks[task]:
                tasks[task] = info["points"][index]

        for task in tasks:
            if student not in exam_points:
                exam_points[student] = 0
            exam_points[student] += tasks[task]

    return exam_points            


if __name__ == "__main__":
    print(final_points())
