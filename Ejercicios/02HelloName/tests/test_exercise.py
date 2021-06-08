import pytest
import src.main

def test_exercise(capsys):
    input_values = ["Carlos"]
    output = []

    # This function will store the strings provided to 'input' within the code
    def mock_input(s):
        output.append(s)
        return input_values[0]

    # Redefinitions of standard functions (input and print) within the module
    # Make sure to use the name of the source file
    # In this case it is 'src.main'
    src.main.input = mock_input
    src.main.print = lambda s : output.append(s)

    # Call the function to evaluate
    src.main.main()

    # List all the outputs the program will have, including input prompts
    # After the outputs expected comes a message to clarify the error
    assert output == ['Enter your name: ', f'Hello {input_values[0]}!'], \
            "Expected the message: 'Hello Carlos!'"
