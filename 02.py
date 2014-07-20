while True:

    text = input("Enter text: ")

    shift = int(input("Enter shift: "))

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    output = ""

    for i in text:

        if i.lower() in alphabet:
            output += alphabet[(alphabet.index(i.lower()) + shift) % len(alphabet)] if i.islower() else alphabet[(alphabet.index(i.lower()) + shift) % len(alphabet)].upper()
        else:
            output += i

    print("Output is: " + output)
