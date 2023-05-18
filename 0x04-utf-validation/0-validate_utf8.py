#!/usr/bin/python3
"""
Utf-8 validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Return:
        True if data is a valid UTF-8 encoding, else return False

    Description:
        * Prototype: def validUTF8(data)
        * A character in UTF-8 can be 1 to 4 bytes long
        * The data set can contain multiple characters
        * The data will be represented by a list of integers
        * Each integer represents 1 byte of data, therefore you only
        need to handle the 8 least significant bits of each integer
    """
    number_of_bytes = 1

    # iterate through the data set
    for datum in data:

        # mask datum to get the 8 least significant bits
        datum = datum & 0b11111111

        if number_of_bytes == 1:
            # check if tdatum is 2-byte character
            if datum >> 5 == 0b110:
                number_of_bytes = 2
            # check if datum is 3-byte character
            elif datum >> 4 == 0b1110:
                number_of_bytes = 3
            # check if datum is 4-byte character
            elif datum >> 3 == 0b11110:
                number_of_bytes = 4
            # chekc if datum is a valid utf-8 character
            elif datum >> 7 == 0b1:
                # not a valid utf-8
                return False
        else:
            # check if datum is a continuation byte
            if datum >> 6 != 0b10:
                # if not a continuation byte
                return False
            number_of_bytes -= 1

    return number_of_bytes == 1
