trains = [
    ("tr6", 2),
    ("tr1", 10),
    ("tr4", 20),
    ("tr5", 2),
    ("tr3", 15),
    ("tr2", 9),
]


print(sorted(
    trains, key=lambda x:x[1]
))
print(
    list(
        map(
            lambda x:x[1]%2==0,
            trains
        )
    )
)
print(
    list(
        filter(
            lambda x:x[1]%2==0,
            trains
        )
    )
)