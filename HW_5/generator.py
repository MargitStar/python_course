def my_generator(start):
    while start != 100:
        if start % 3 == 0:
            yield "Василий"
            start += 1
        else:
            yield start
            start += 1


generator = my_generator(1)

for i in generator:
    print(i)
