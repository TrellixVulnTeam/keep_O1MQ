if __name__ == "__main__":
    metro_areas = [
        ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
        ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
    ]

    print("{:15} | {:9} | {:9}".format("", "lat.", "long."))
    fmt = "{:15} | {:9f} | {:9.4f}"
    for name, cc, pop, (latitude, longitude) in metro_areas:
        if longitude > 0:
            print(fmt.format(name, latitude, longitude))
