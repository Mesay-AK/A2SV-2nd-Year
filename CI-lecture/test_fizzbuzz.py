from main import fizzbuzz

def test_fizzbuzz(capsys):
    fizzbuzz(15)
    captured = capsys.readouterr()
    output_lines = captured.out.strip().split("\n")

    expected_output = [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz"
    ]

    assert output_lines == expected_output
