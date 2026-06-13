from logic_utils import check_guess, parse_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_message_correct():
    # Bug fix: verify "Too High" message says "Go LOWER" (not "Go HIGHER")
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message

def test_too_low_message_correct():
    # Bug fix: verify "Too Low" message says "Go HIGHER" (not "Go LOWER")
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message


# Challenge 1: Advanced Edge-Case Testing

def test_negative_number_guess():
    # Edge case: Negative numbers are outside the valid range (1-500)
    # Should be detected as "Too Low" since -50 < 50
    outcome, message = check_guess(-50, 50)
    assert outcome == "Too Low"
    assert message is not None

def test_zero_as_guess():
    # Edge case: Zero is outside the valid range (1-500)
    # Should be detected as "Too Low" since 0 < 50
    outcome, message = check_guess(0, 50)
    assert outcome == "Too Low"
    assert message is not None

def test_extremely_large_guess():
    # Edge case: Extremely large values (999999) are outside any valid range
    # Should be detected as "Too High" since 999999 > 50
    outcome, message = check_guess(999999, 50)
    assert outcome == "Too High"
    assert message is not None
