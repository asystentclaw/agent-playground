def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


if __name__ == '__main__':
    samples_c = [-40, 0, 100]
    samples_f = [32, 68, 212]

    print('Celsius -> Fahrenheit')
    for c in samples_c:
        print(f'{c}C = {celsius_to_fahrenheit(c)}F')

    print('\nFahrenheit -> Celsius')
    for f in samples_f:
        print(f'{f}F = {fahrenheit_to_celsius(f)}C')
