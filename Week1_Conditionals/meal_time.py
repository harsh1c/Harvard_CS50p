def main():
    i = convert(input("What time is it? ").strip())

    if  7 <= i <= 8:
        print("breakfast time")
    elif 12 <= i <= 13:
        print("lunch time")
    elif 18 <= i <=19:
        print("dinner time")
    else:
        print("")


def convert(time):
    time = str(time)
    hours , rest  = time.split(":")
    if "a.m." in rest or "p.m." in rest:
        min,meridiem = rest.split(" ")
        hours = int(hours)
        min_convert = (float(min) /60)
        i = float(i)

        if time.startswith(12) and time.endswith("a.m."):
            i = hours + min_convert - 12
            return i

        elif time.endswith("a.m."):
            i = hours + min_convert
            return i

        elif time.startswith(12) and time.endswith("p.m."):
            i = hours + min_convert
            return i

        elif  time.endswith("p.m."):
            i = hours + min_convert + 12
            return i
        else:
            return None
    else :
        i = int(hours) + (float(rest) /60)
        i = float(i)
        return i

if __name__ == "__main__":
    main()