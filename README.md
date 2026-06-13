# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Game's Purpose:** A number guessing game where players try to guess a secret number within a difficulty-based range (Easy: 1-20, Normal: 1-100, Hard: 1-500). Players receive hints about whether their guess is too high or too low, have a limited number of attempts, and earn points based on how quickly they find the secret number.

- [x] **Bugs Found:**
  1. High/Low hint messages were inverted (Too High said "Go HIGHER", Too Low said "Go LOWER")
  2. Hard difficulty range was 1-50 instead of 1-500
  3. Attempts initialized to 1 instead of 0, causing off-by-one errors
  4. Range was hardcoded to 1-100 instead of using the difficulty-based low/high variables
  5. New Game button didn't properly reset score, status, and history
  6. Secret number type mismatch on even attempts
  7. Inconsistent scoring for Too High vs Too Low outcomes

- [x] **Fixes Applied:**
  1. Fixed hint messages in `check_guess()` to correctly indicate direction (Too High → "Go LOWER", Too Low → "Go HIGHER")
  2. Updated Hard difficulty range from 1-50 to 1-500 in `get_range_for_difficulty()`
  3. Changed attempts initialization from 1 to 0
  4. Replaced hardcoded range with dynamic low/high values from `get_range_for_difficulty()`
  5. Fixed New Game button to reset all session state (attempts, score, status, history, secret)
  6. Removed type conversion bug with secret number
  7. Standardized scoring to consistently deduct 5 points for incorrect guesses
  8. Moved game logic functions to `logic_utils.py` and verified imports in `app.py`

## 📸 Demo Walkthrough
1. User enters a guess of 40
2. Game returns "Too Low"
3. User enters a guess of 70 → "Too High"
4. Score updates correctly after each guess
5. Game ends after the correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

### Challenge 1: Advanced Edge-Case Testing

**Edge cases identified and tested:**
1. **Negative numbers** — Guesses like -50 are outside the valid range (1-500) but should still compare correctly
2. **Zero as a guess** — Zero is outside the valid range but should be handled as "Too Low"
3. **Extremely large values** — Guesses like 999999 exceed any valid range but should be detected as "Too High"

```
============================= test session starts ==============================
platform darwin -- Python 3.11.14, pytest-9.0.3, pluggy-1.6.0 -- /opt/miniconda3/envs/deeplearning/bin/python
cachedir: .pytest_cache
rootdir: /Users/awini/GitHub/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.12.1
collecting ... collected 8 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 12%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 25%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 37%]
tests/test_game_logic.py::test_too_high_message_correct PASSED           [ 50%]
tests/test_game_logic.py::test_too_low_message_correct PASSED            [ 62%]
tests/test_game_logic.py::test_negative_number_guess PASSED              [ 75%]
tests/test_game_logic.py::test_zero_as_guess PASSED                      [ 87%]
tests/test_game_logic.py::test_extremely_large_guess PASSED              [100%]

============================== 8 passed in 0.01s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
