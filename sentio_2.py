def get_char_at_stream_for_index(input_index):
    number_size = 9
    number_length = 1
    total_numbers_passed = 0
    while True:
        total_indexes = number_size * number_length
        if input_index - total_indexes >= 0:
            input_index -= total_indexes
        else:
            break
        total_numbers_passed += number_size
        number_length += 1
        number_size *= 10

    print('{} characters after maximum {} length'.format(
        input_index, number_length-1
    ))

    print("total_numbers_passed {}".format(total_numbers_passed))
    from math import ceil
    number_output = ceil(input_index/number_length) + total_numbers_passed
    actual_digit = input_index % number_length
    print(number_output,number_length,actual_digit)
    print("digit at {} index: {}".format(input_index, str(number_output)[actual_digit-1]))


get_char_at_stream_for_index(251)
