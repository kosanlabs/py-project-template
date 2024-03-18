from src.welcome import welcome


def testing_welcome_message():
    testing_function = welcome()
    assert testing_function == "welcome"
