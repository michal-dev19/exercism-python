"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """
    i = 0
    condition = 0
    seats = ['A', 'B', 'C', 'D']
    while condition < number:
        yield seats[i]
        i += 1
        if i == 4:
            i = 0
        condition += 1


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For exampl: 3C, 3D, 4A, 4B

    """
    
    i = 0
    row = 1
    condition = 0
    seat_letters = generate_seat_letters(number)
    while condition < number:
        if row == 13:
            row = 14
        yield str(row) + next(seat_letters)
        i += 1
        if i == 4:
            i = 0
            row += 1
        condition += 1



def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """
    passenger_dict = {}
    seats = generate_seats(len(passengers))
    for item in passengers:
        passenger_dict[item] = next(seats)
    return passenger_dict
    

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """
    ticket_length = 12
    for item in seat_numbers:
        initial_ticket = item + flight_id
        required_zeros = ticket_length - len(initial_ticket)
        yield initial_ticket + (required_zeros*'0')
