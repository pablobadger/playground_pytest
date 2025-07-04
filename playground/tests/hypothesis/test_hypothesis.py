from hypothesis import given, strategies as st


@given(st.integers())
def test_hypothesis(input):
    print(f"Testing with input: {input}")
    assert isinstance(input, int)
