from datetime import datetime, timedelta

def cheaters() -> list:
    start_times = {}
    ending_times = {}
    cheaters = []

    with open('start_times.csv') as start_file:
        for line in start_file:
            line = line.strip().split(";")
            start_times[line[0]] = datetime.strptime(line[1], "%H:%M")

    with open("submissions.csv") as ending_file:
        for line in ending_file:
            line = line.strip().split(";")
            if line[0] not in ending_times:
                ending_times[line[0]] = [datetime.strptime(line[3], "%H:%M")]
                continue
            ending_times[line[0]].append(datetime.strptime(line[3], "%H:%M"))

    for student, times in ending_times.items():
        for time in times:
            if time - start_times[student] > timedelta(hours=3):
                cheaters.append(student)
                break

    return cheaters

if __name__ == "__main__":
    print(cheaters())

