# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").


When I first ran the game, the guessing logic had multiple issues that made gameplay confusing and inconsistent. The hints were backwards when the guess was too high, it told you to "Go HIGHER!" instead of "Go LOWER!". The attempt counter started at 1 instead of 0, throwing off the attempt tracking. Additionally, the range display was hardcoded to always show "1 to 100" regardless of difficulty, and the Hard difficulty range (1-50) was actually narrower than Normal (1-100), making it easier rather than harder.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 60 when secret is 50 | Display "Too High" with hint "Go LOWER!" | Displayed "Too High" with hint "Go HIGHER!" | Misleading hint direction |
| Hard difficulty selected | Range should be 1-500 | Range was 1-50 (narrower than Normal) | Debug info showed Hard difficulty easier than Normal |
| Click "New Game" button | Reset attempts to 0, clear history, generate new secret | Only reset secret and attempts, didn't reset score/status/history | Old game state persisted |
| Guess on even-numbered attempt | Guess compared as integer to integer secret | Secret was converted to string on even attempts | Type mismatch caused unpredictable behavior |
| Initial game state | Attempts should start at 0 | Attempts counter started at 1 | First guess showed "Attempts left: 7" instead of 8 for Normal difficulty |

---

## 2. How did you use AI as a teammate?

I used Claude Code (Claude Opus 4.8) to help identify, understand, and fix the bugs in this project. The AI correctly identified that the hint messages in the `check_guess` function were inverted and suggested swapping the "Go LOWER!"/"Go HIGHER!" messages, which I verified by running the test suite (`pytest tests/test_game_logic.py`) and confirming all tests passed. The AI also helped me understand that the secret number was being incorrectly converted to a string on even attempts, causing type comparison issues. I verified this was a real bug by examining the code logic and seeing how it would break the game flow. The AI was consistently accurate in analyzing the codebase structure and suggesting targeted fixes that addressed root causes rather than symptoms.

---

## 3. Debugging and testing your fixes

I decided a bug was really fixed by running the test suite and verifying that the game behaved correctly both in automated tests and manual gameplay. I ran `pytest tests/test_game_logic.py` which included specific tests like `test_too_high_message_correct()` that verified the hint messages contained the correct words ("LOWER" for too-high guesses, "HIGHER" for too-low guesses). These tests caught the inverted hint bug immediately—they were failing before the fix and passed after I corrected the logic. I also manually tested the game in Streamlit by selecting different difficulties and making guesses to confirm that the range display, attempt counter, and New Game reset all worked correctly. The AI helped me understand what the tests were checking for and why certain assertions mattered for catching these bugs.

---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit "reruns" the entire script from top to bottom every time a user interacts with the app (clicking a button, typing in a text box, etc.), which is very different from traditional web frameworks. To persist data across reruns, you use `st.session_state`, which acts like a dictionary that remembers values between script reruns. I'd explain it like this to a friend: "Every time you click something in a Streamlit app, the code re-executes completely from the start. Session state is like a sticky note that survives each rerun—you can write values to it (like `st.session_state.attempts = 5`) and they stay there even after the script reruns." This is why the bug with initializing attempts to 1 mattered—that line runs on every rerun, but because of the `if "attempts" not in st.session_state:` check, it only sets it once. The New Game button bug was particularly tricky because it needed to reset ALL the state variables (score, status, history, secret) in the right order for the game to work correctly.

---

## 5. Looking ahead: your developer habits

One habit I want to keep is writing tests that explicitly verify the exact behavior you care about like the test that checks not just that "Too High" is returned, but that the message contains "LOWER" and doesn't contain "HIGHER". These specific assertions caught the inverted hint bug immediately. I'd also like to continue using Git commits to track my fixes and document exactly what changed, which makes it easy to review my work and explain what I fixed. Next time I work with AI on a coding task, I'll ask for more targeted help on specific functions rather than asking for broad refactoring, and I'll verify each fix by running tests immediately instead of trying to fix multiple things at once.

This project changed how I think about AI-generated code because I realized that even code that seems reasonable and runs without errors can have subtle logic bugs that break the user experience. I now see AI as a helpful debugger and explainer rather than a source of production-ready code, and I know I need to actively test and question what it generates.
