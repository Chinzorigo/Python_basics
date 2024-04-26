def encode_message(base_value):

    step_one_result = base_value * 1024
    encoded_number1 = step_one_result + 46304
    encoded_number2 = encoded_number1 + 100
    return encoded_number1, encoded_number2

base_value = 5

encoded_number1, encoded_number2 = encode_message(base_value)
# print separate with description
print("Encoded number 1:", encoded_number1)
print("Encoded number 2:", encoded_number2)

