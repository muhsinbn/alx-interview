#!/usr/bin/python3
""" Method that determines if a given data set represents a valid UTF-8"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
    data (list): A list of integers where each integer represents one
    byte of data.

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.

    A character in UTF-8 can be 1 to 4 bytes long.
    The data set can contain multiple characters.
    The data will be represented by a list of integers.

    Each integer represents 1 byte of data, therefore only the 8 least
    significant bits of each integer are used.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the leading bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    # For each integer in the data array
    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Determine the number of bytes in the char
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            # 1-byte chars (ASCII) or invalid byte (more than 4 leading 1s)
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Continuation bytes must start with 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the number of bytes
        num_bytes -= 1

    # If we end with num_bytes not being 0, then its an invalid UTF-8 sequence
    return num_bytes == 0
