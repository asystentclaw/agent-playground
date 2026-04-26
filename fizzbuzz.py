def fizzbuzz_value(n: int) -> str:
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def generate_fizzbuzz(start: int = 1, end: int = 100) -> list[str]:
    return [fizzbuzz_value(n) for n in range(start, end + 1)]


def main() -> None:
    for line in generate_fizzbuzz():
        print(line)


if __name__ == "__main__":
    main()
