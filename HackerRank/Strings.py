def split_and_join(line):
    """
    #1. možnost
    line = line.split(" ")
    line = "-".join(line)

    #2. možnost
    line = line.replace(" ","-")
    """
    # 3. možnost
    line = "-".join(line.split())
    return line


randomVeta = "Dnes je venku krásné počasí"
transformedSentece = split_and_join(randomVeta)
print(transformedSentece)


s = 10
w = len(bin(s).removeprefix("0b"))
# decimal
print(s)
# octal
print(oct(s).removeprefix("0o"))
# hexadecimal
print(hex(s).removeprefix("0x").upper())
# binary
print(bin(s).removeprefix("0b"))

[
    print(
        i,
        oct(i).removeprefix("0o"),
        hex(i).removeprefix("0x").upper(),
        bin(i).removeprefix("0b"),
        sep=" ",
    )
    for i in range(1, s + 1)
]
