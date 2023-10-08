#Airplane Management System
def Airplane_Management_System():
#Initializing all the variables that are used in the code
    options = ['1. Booking a Ticket', '2. Cancel a Booking','3. Show all Flights']
    admin_func = ['1. Add a Flight','2. Modify a Flight','3. Remove a Flight']
    guest_name = ''
    guest_email = ''
    row_list1 = ''
    row_list2 = ''
    flight_num = ''
    row_num = ''
    seat_num = ''
    choose_company = ''
    
    def user_login():
        #First administrator ask the user to login so that the users can continue booking their flights.
        print('--------------------------------------------------------------------------------')
        print('There is some information required for booking a flight!')
        with open(r'C:\Users\DELL\Documents\P2 COMP 111\user info.txt', 'a') as file : #Start appending the information of the user in the text file called "User Info".

            guest_name = input('Enter Your Name : ')
            guest_email = input('Enter Your Email : ')
            email_password = input('Enter an Email Password : ')
            guest_info = f'Name : {guest_name}, Email : {guest_email}, Email Password : {email_password}'
            file.write (guest_info + '\n') #Save the information of the user in the text file.

        search_password() #Call the search_password() function to verify the user's correct password so the user can continue.

    def search_password():
        with open(r'C:\Users\DELL\Documents\P2 COMP 111\user info.txt', 'r') as fileobj: #The code will read the file and find the password that was just saved.
            lines = fileobj.readlines() #Read all the lines from the file
            found = False

            for line in lines:
                if line not in lines:
                    print("Incorrect Password!") #If the password do not match with the save password, then the code will print the msg "Incorrect Password!".
                    return
            last_line = lines[-1]  # Get the last line (last password added)
            stored_password = last_line.split("Email Password : ")[-1].strip()  # Extract the stored password

            search = input('Enter the Email Password for Verification : ')

            while search != stored_password:
                search = input('Please enter the correct password: ') #The code prompts the user repeatedly until the correct password is found.

            if search == stored_password:
                print('Correct Password!') #If correct password found in the text file, the code will print the msg "Correct Password!".
                found = True

        booking_a_flight()

    def show_flights():
        with open(r'C:\Users\DELL\Documents\P2 COMP 111\flight info.txt', 'r') as fileobj:
            flight_info = fileobj.readlines()  # Read all lines from the file
            found = False

            if not flight_info:
                print('No Flights Available!')
                return

            for info in flight_info:
                if 'Flight Company' in info:
                    flight_com = info.split(':')[1].strip()  # Get the flight company name
                    if flight_com == 'A':
                        print('This is Seat List of Flight Company A:')
                        flight_A()
                    elif flight_com == 'B':
                        print('This is Seat List of Flight Company B:')
                        flight_B()
                else:
                    print(f'Unknown Flight Company: {flight_com}')
    #show_flights()

    def flight_A():
        row_list1 = [['      ','A','B','C','D','E'],
                     ['Row 1:','*','*','*','*','*'],
                     ['Row 2:','X','X','*','X','*'],
                     ['Row 3:','*','*','*','X','X'],
                     ['Row 4:','*','*','X','*','X'],
                     ['Row 5:','*','X','*','X','X'],
                     ['Row 6:','X','*','*','X','X']]
        rows = row_list1[1][2]
        for rows in row_list1:
            for seats in rows:
                print(seats, end='  ')
            print()

    def flight_B():
        row_list2 = [['      ','A','B','C','D','E'],
                     ['Row 1:','X','*','*','X','*'],
                     ['Row 2:','X','X','*','*','*'],
                     ['Row 3:','*','*','*','X','*'],
                     ['Row 4:','*','X','*','*','X'],
                     ['Row 5:','X','*','*','X','X'],
                     ['Row 6:','*','X','*','*','X'],
                     ['Row 7:','*','*','*','X','X']]
        r = row_list2[1][2]
        for r in row_list2:
            for s in r:
                print(s, end='  ')
            print()
    
    def booking_a_flight():
        print('                                                                            ')
        nonlocal choose_company, row_num, seat_num #This line specifies that the variables choose_company, row_num, and seat_num are nonlocal.
        with open(r'C:\Users\DELL\Documents\P2 COMP 111\flight info.txt', 'r') as file: #Read the file
            print('Welcome to the Booking Area!')
            adding_a_flight()
            show_flights()

            while True: #Starts an infinite loop, ensuring that the user can repeatedly choose a flight company until a valid choice is made.
                print('After adding a flight information! You have to choose row and seat number!')
                choose_company = input('Select the Flight Company of Your Corresponding Booking : ')

                if choose_company == 'A':
                    #Display the seat layout for Company A
                    print('Flight Company A - Seat Layout : ')
                    print('There are 6 Rows Avaialable!')
                    flight_A()
                    row_num = input('Enter the Row Number From 1 to 6 : ')
                    seat_num = input('Enter the Seat Number From A to E : ')
                    break
                    
                elif choose_company == 'B':
                    #Display the seat layout for Company B
                    print('Flight Company B - Seat Layout : ')
                    print('There are 8 Rows Available!')
                    flight_B()
                    row_num = input('Enter the Row Number From 1 to 8 : ')
                    seat_num = input('Enter the Seat Number From A to E : ')
                    
                else:
                    print('Invalid choice. Please select A for Company A or B for Company B.')
            print(f'Seat {seat_num} in Row {row_num} has been successfully booked!') #After selecting the row_num and seat_num, it will print the confirmation msg.

        user_information_display() #Call the user_information_display() after booking    
        print('                                                                                ')
        print('Admin just booked a flight!')
        print('Now admin modify that flight in your flight system!')

        modify_a_flight()

    def user_information_display():
        with open(r'C:\Users\DELL\Documents\P2 COMP 111\user info.txt', 'r') as user_file: #Read the file
            user_lines = user_file.readlines() #Read the lines
            guest_name = ''  # Initialize the guest name variable

            # Find the last line containing 'Name'
        for line in reversed(user_lines):
            if 'Name' in line:
                guest_name = line.split(': ')[1].strip()
                break

        with open(r'C:\Users\DELL\Documents\P2 COMP 111\flight info.txt', 'r') as flight_file: #Read the file
            flight_lines = flight_file.readlines()
            arrival_time = '' #Initialize the arrival time variable

            # Find the last line containing 'Arrival Time'
        for line in reversed(flight_lines):
            if 'Arrival Time' in line:
                arrival_time = line.split(': ')[1].strip()
                break

        print('                                                                                    ')    
        print('This is the ticket of the user!')
        print(f'Name : {guest_name}\nFlight : {choose_company}\nArrival Time : {arrival_time}\nRow and Seat : Row {row_num} Seat {seat_num}') #Prints the user's ticket information

    def modify_a_flight():
        with open(r'C:\Users\DELL\Documents\P2 COMP 111\flight info.txt', 'r') as file: #Read the file.
            lines = file.readlines() #Read the lines from the file
            
            print('                                                                                ')
            #print('Admin is modifying a flight...........')
            flight_num = input('Enter the Flight Number you want to modify: ')

        # Check if the flight number exists in the file.
        found = False
        for i, line in enumerate(lines):
            if f'Flight Number : {flight_num}' in line:
                found = True
                break

        if found:
            print(f'Flight {flight_num} found! Modifying the flight...')
            # Remove the old flight information from the file.
            del lines[i:i + 6]  

            # Now, add the new flight information.
            print('Please Add Updated Information : ')
            departure_time = input('Enter the Departure Time of the Flight that to Update : ')
            arrival_time = input('Enter the Arrival Time of the Flight that to Update : ')
            flight_company = input('Enter the Flight Company of the Flight that to Update : ')
            flight_num = input('Enter the Flight Number of the Flight that to Update : ')
            duration = input('Enter the Duration that Flights will Take to Update : ')
            flight_info1 = f'Departure Time : {departure_time}, Arrival Time : {arrival_time}, Flight Company : {flight_company}, Flight Number : {flight_num}, Duration : {duration}'

            new_flight = [flight_info1 + '\n']  # Insert the new flight information (save the information in the file).

            with open(r'C:\Users\DELL\Documents\P2 COMP 111\flight info.txt', 'w') as file: #Append the flight information in text file.
                file.writelines(new_flight)
            print(f'Flight {flight_num} has been modified successfully!')
        else:
            print(f'Flight {flight_num} not found. Please check the Flight Number.')
    
        show_flights()

    def adding_a_flight():
        print('                                                                             ')
        print('Please Add a New Flight to Book!')
        with open(r'C:\Users\DELL\Documents\P2 COMP 111\flight info.txt', 'a') as file: #Admin is start appending the flight's information.
            print('Please Add Some Information of a New Flight : ')

            arrival_time = input('Enter the Arrival Time of the Flight : ')
            departure_time = input('Enter the Departure Time of the Flight : ')
            flight_company = input('Enter the Flight Company Between A and B : ')
            flight_num = input('Enter the Flight Number : ')
            duration = input('Enter the Duration That Flights will Taken : ')
            flight_info = f'Arrival Time : {arrival_time}, Departure Time : {departure_time}, Flight Company : {flight_company}, Flight Number : {flight_num}, Duration : {duration}'

            file.write (flight_info + '\n') #Save the flight's information in the text file called "Flight Info".
            print(flight_info)
            
    def canceling_a_flight():
        print('                                                                                       ')
        print('Admin is canceling a flight............')
        flight_num = input('Enter the Flight Number that You Want to Remove from the File: ')

        with open(r'C:\Users\DELL\Documents\P2 COMP 111\flight info.txt', 'r') as file: #Read the text file.
            lines = file.readlines() #Read the lines.

    # Check if the flight number exists in the file.
        found = False
        for i, line in enumerate(lines):
            if f'Flight Number : {flight_num}' in line:
                found = True
                del lines[i:i + 6]  # Delete the flight information (6 lines).
                break

        # Rewrite the file with the canceled flight.
        with open(r'C:\Users\DELL\Documents\P2 COMP 111\flight info.txt', 'w') as file:
            file.writelines(lines)

        if found:
            print(f'Flight {flight_num} found! Canceling the flight...')
            print('-----------------------------------------------------')
            print(f'Flight {flight_num} has been canceled successfully!')
                
        else:
            print(f'Flight {flight_num} not found. Please check the Flight Number.')
        
        show_flights()       

    def canceling_a_booking():
        print('                                                                           ')
        with open(r'C:\Users\DELL\Documents\P2 COMP 111\user info.txt', 'r') as file: #Read the file to cancel the booking

            print('Admin asks the user to cancel out their flight!')
            print('        *******************************')
            guest_email = input('Admin ask you to enter your Guest Email for verification: ')
        
        # Read all lines from the file
            lines = file.readlines()

        # Check if the guest email exists in the file
            found = False
            for i, line in enumerate(lines):
                if f'Email : {guest_email}' in line:
                    found = True
                    break

            if found:
            # Remove the guest's information from the file
                del lines[i]

                canceling_a_flight()
            
            # Rewrite the file without the canceled booking
                with open(r'C:\Users\DELL\Documents\P2 COMP 111\user info.txt', 'w') as file:
                    file.writelines(lines)

                print('Here is the list of all the bookings!')
                with open(r'C:\Users\DELL\Documents\P2 COMP 111\user info.txt', 'r') as file:
                    lines = file.readlines()

                    for line in lines:
                        print(line.strip())
            else:
                print('Booking not found. Please check your Guest Email.')

    def main_menu():
        print('                            Welcome Users!')
        print('a) If you are new here then press 1 to booking a flight!\nb) If you have booked a flight and want to cancel that flight then press 2!\nc) If you want to see flights before login in then press 3!')    
        for opt in options:
            print(opt)

        while True:
            option_num = input('Enter a Number From 1 to 3 to Choose an Option : ')

            if option_num == '1':
                user_login()
                break  # Break out of the loop if a valid option is chosen
            elif option_num == '2':
                canceling_a_booking()
                break  # Break out of the loop if a valid option is chosen
            elif option_num == '3':
                show_flights()
                break  # Break out of the loop if a valid option is chosen
                option()
            else:
                print('Invalid option! Try Again!')

    def option():
        while True:
            print('                                                                           ')
            main_menu()
            another_action = input('Do you want to perform another action? (yes/no): ').lower() #Converts the input into lowercase

            if another_action in ('yes', 'y'):
                main_menu()
                continue

            elif another_action in ('no', 'n'):
                print('Stop!')
                break

            else:
                print('Invalid Input! ')
    option()

Airplane_Management_System()
