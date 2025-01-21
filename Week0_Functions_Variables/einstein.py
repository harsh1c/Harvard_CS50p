def recommendation(place_type, location_details):
    # Check if the place type is "country"
    if place_type == "country":
        if len(location_details) == 1:
            # If there is only one location detail, display and return the place_id
            print(f'Country: {location_details[0]["country"]}')
            return location_details[0]["place_id"]
        else:
            # If multiple countries have same name
            options = {}
            for i in range(len(location_details)):
                details = location_details[i]
                print(f'{i+1}. Country:{details["country"]}", Country code: "{details["country_code"]}"')
                options[i] = f'{details["place_id"]}'
        place_id = choose(options)
        return place_id

    # Check if the place type is "state"
    elif place_type == "state":
        if len(location_details) == 1:
            print(f'State: {location_details[0]["state"]}, Country: {location_details[0]["country"]}')
            return location_details[0]["place_id"]
        else:
            # If multiple states have same name
            options = {}
            for i in range(len(location_details)):
                details = location_details[i]
                print(f'{i + 1}. State: "{details["state"]}, Country:{details["country"]}"')
                options[i] = f'{details["place_id"]}'
        place_id = choose(options)
        return place_id

    # Check if the place type is "city"
    elif place_type == "city":
        if len(location_details) == 1:
            details = location_details[0]
            print(f'City: {details["city"]}, State: {details["state"]}, Country:{details["country"]}')
            return location_details[0]["place_id"]
        else:
            # If multiple cities have same name
            options = {}
            for i in range(len(location_details)):
                details = location_details[i]
                print(f'{i + 1}. City: "{details["city"]}, State: "{details["state"]}, Country:{details["country"]}"')
                options[i] = f'{details["place_id"]}'
        place_id = choose(options)
        return place_id

    # Check if the place type is "district"
    elif place_type == "district":
        if len(location_details) == 1:
            details = location_details[0]
            print(f'City: {details["district"]}, State: {details["state"]}, Country:{details["country"]}')
            return location_details[0]["place_id"]
        else:
            # # If multiple districts have same name
            options = {}
            for i in range(len(location_details)):
                details = location_details[i]
                print(f'{i + 1}. District: "{details["district"]}, State: "{details["state"]}, Country:{details["country"]}"')
                options[i] = f'{details["place_id"]}'
        place_id = choose(options)
        return place_id

    # when the user don't know place type ("no" by user)
    else:
        j = 0
        options = {}
        for i in range(len(location_details)):
            place_type = location_details[i]["result_type"]
            details = location_details[i]

            if place_type == "country":
                if len(location_details) == 1:
                    print(f'Country: {location_details[0]["country"]}')
                    return location_details[0]["place_id"]
                else:
                    print(f'{j + 1}. Country:{details["country"]}, Country code: {details["country_code"]}')
                    options[j] = f'{details["place_id"]}'
                    j += 1

            elif place_type == "state":
                if len(location_details) == 1:

                    print(f'State: {location_details[0]["state"]}, Country: {location_details[0]["country"]}')
                    return location_details[0]["place_id"]
                else:
                    print(f'{j + 1}. State: "{details["state"]}, Country:{details["country"]}"')
                    options[j] = f'{details["place_id"]}'
                    j += 1

            elif place_type == "city":
                if len(location_details) == 1:
                    print(f'City: {location_details[0]["city"]}, State: {location_details[0]["state"]}, Country: {location_details[0]["country"]}')
                    return location_details[0]["place_id"]
                else:
                    print(f'{j + 1}. City: "{details["city"]}, State: {details["state"]}, Country:{details["country"]}"')
                    options[j] = f'{details["place_id"]}'
                    j += 1

            elif place_type == "district":
                if len(location_details) == 1:
                    print(f'City: {location_details[0]["district"]}, State: {location_details[0]["state"]}, Country: {location_details[0]["country"]}')
                    return location_details[0]["place_id"]
                else:
                    print(f'{j + 1}. District: "{details["district"]}, State: {details["state"]}, Country:{details["country"]}"')
                    options[j] = f'{details["place_id"]}'
                    j += 1

            else:
                # Handle other place types such as "suburb" or "county"
                if "name" in details:
                    print(f'{j + 1}. Name: "{details["name"]}, State: "{details["state"]}, Country:{details["country"]}"')
                    options[j] = f'{details["place_id"]}'
                elif place_type == "suburb":
                    print(f'{j + 1}. Suburb: "{details["suburb"]}, State: "{details["state"]}, Country:{details["country"]}"')
                    options[j] = f'{details["place_id"]}'
                else:
                    print(f'{j + 1}. County: "{details["county"]}, State: "{details["state"]}, Country:{details["country"]}"')
                    options[j] = f'{details["place_id"]}'
                j += 1
        place_id = choose(options)
        return place_id