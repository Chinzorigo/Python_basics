def test_get_player_choice():
    game = RockPaperScissors()  # Assuming you have a class named RockPaperScissors

    # Test valid choices
    user_inputs = ["rock", "paper", "scissors"]
    for user_input in user_inputs:
        # Mock user input
        def input(_): return user_input
        game.input = input

        assert game.get_player_choice() == user_input

    # Test invalid choices
    user_inputs = ["invalid", "123", "rockk"]
    for user_input in user_inputs:
        # Mock user input
        def input(_): return user_input
        game.input = input

        assert game.get_player_choice() == None


test_get_player_choice()
