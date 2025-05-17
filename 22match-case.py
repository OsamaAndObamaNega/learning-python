while True:
    user_input = input("Enter a day number (1-7) or 'q' to quit: ")
    
    if user_input.lower() == 'q':
        break
    
    try:
        day_number = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a number (1-7) or 'q' to quit.")
        continue
    
    match day_number:
        case 1:
            day_name = "Sunday"
        case 2 :
            day_name = "Monday"
        case 3:
            day_name = "Tuesday"
        case 4:
            day_name = "Wednesday"
        case 5:
            day_name = "Thursday"
        case 6:
            day_name = "Friday"
        case 7:
            day_name = "Saturday"
        case _:
            day_name = "Invalid day number (must be 1-7)"
    
    print(day_name)