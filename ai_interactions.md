# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

**Prompt used:**

```
Add advanced edge case tests for the guess comparison function. Test what happens when 
users input values far outside the valid game range (1-500): negative numbers, zero, 
and extremely large numbers. Verify these invalid inputs are still correctly compared 
against the secret number.
```

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Negative number input | Advanced edge case prompt | `test_negative_number_guess()`: -50 vs 50 returns "Too Low" | Yes | Numbers outside valid range (1-500) should still compare correctly; tests robustness against invalid user input |
| Zero input | Advanced edge case prompt | `test_zero_as_guess()`: 0 vs 50 returns "Too Low" | Yes | Zero is a boundary value outside valid range; catches off-by-one or comparison logic errors |
| Extremely large number | Advanced edge case prompt | `test_extremely_large_guess()`: 999999 vs 50 returns "Too High" | Yes | Tests that comparison logic doesn't break with values far beyond game range; guards against overflow or type coercion bugs |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
