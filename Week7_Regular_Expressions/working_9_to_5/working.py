import re
import sys


def main():
    try:
        answer = convert(input("Hours: ").strip())
        print(answer)
    except ValueError:
        sys.exit("ValueError")

def con_arival(arrival):
    time = arrival[0]
    meridiem = arrival[1]

    if meridiem == "AM":

        if ":" in time:
            hour, minute = time.split(":")
            hour = int(hour)

            if hour == 12:
                hour = 0

            if hour in range(10):
                return f"0{hour}:{minute}", minute
            else:
                return f"{hour}:{minute}", minute
        else:
            if int(time) == 12:
                time = 0

            if int(time) in range(10):
                return f"0{time}:00"
            else:
                return f"{time}:00"

    elif meridiem == "PM":

        if ":" in time:

            hour, minute = time.split(":")
            hour = int(hour)
            if hour == 12:
                hour = 0
            new_hour = hour + 12

            return f"{new_hour}:{minute}", minute
        else:
            if int(time) == 12:
                time = 0
            new_time = int(time) + 12
            return f"{new_time}:00"


def con_departure(departure):
    time = departure[0]
    meridiem = departure[1]

    if meridiem == "AM":

        if ":" in time:
            hour, minute = time.split(":")
            hour = int(hour)

            if hour == 12:
                hour = 0

            if hour in range(10):
                return f"0{hour}:{minute}", minute
            else:
                return f"{hour}:{minute}", minute
        else:
            if int(time) == 12:
                time = 0

            if int(time) in range(10):
                return f"0{time}:00"
            else:
                return f"{time}:00"

    elif meridiem == "PM":

        if ":" in time:

            hour, minute = time.split(":")
            hour = int(hour)
            if hour == 12:
                hour = 0
            new_hour = hour + 12

            return f"{new_hour}:{minute}", minute
        else:
            if int(time) == 12:
                time = 0
            new_time = int(time) + 12
            return f"{new_time}:00"


def convert(s):

        pattern = r"(\d{1,2}|\d{1,2}:\d\d) (AM|PM) to (\d{1,2}|\d{1,2}:\d\d) (AM|PM)"
        match = re.fullmatch(pattern, s)

        if match:
            arrival, departure = (match.group(1), match.group(2)), (
                match.group(3),
                match.group(4),
            )
            converted_arival = con_arival(arrival)
            converted_departure = con_departure(departure)

            if len(converted_arival) == 2:
                minute = converted_arival[1]

                if int(minute) > 59:
                    raise ValueError
                return f"{converted_arival[0]} to {converted_departure[0]}"
            else:
                return f"{converted_arival} to {converted_departure}"
        else:
            raise ValueError




if __name__ == "__main__":
    main()