# Leetcode With Tests

A compilation of leetcode questions with their solutions.

I realized I don't really write unittests, mainly because I don't see much point in writing them for my silly little projects (I know it's controversial, but you can check out ![Theo.gg's video][https://www.youtube.com/watch?v=ZGKGb109-I4] on the topic).

I don't really do much leetcode anymore either, but to change things up and practice writing tests, I decided to write unittests for the rest of the questions I will solve, you know, to show I can actually write unittests and structure code, and also I typically do leetcode questions when there's no internet access, so I can't really use Leetcode's testing suite.

This follows best practices (kind of), so follow along or something if you haven't learned how to write unittests in Python.

## Running all tests:

`python3 -m unittest -v`

With pytest:
`pytest -v`

## Testing a specific module:

`python3 -m unittest tests.<your_test> -v`

pytest:

`pytest tests/<your_test>.py -v`

Example:

`python3 -m unittest tests.test_array -v`

pytest:

`pytest tests/test_array.py -v`
