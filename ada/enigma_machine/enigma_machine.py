from enigma.machine import EnigmaMachine

# Sheet settings
ROTORS = "IV I V"
RINGS = "20 5 10"
PLUGBOARD = "AV BS CG DL FU HZ IN KM OW RX"

def use_enigma_machine(msg, rotor_start):
    # Set up the Enigma machine
    machine = EnigmaMachine.from_key_sheet(rotors=ROTORS, reflector="B", ring_settings=RINGS, plugboard_settings=PLUGBOARD)

    # Set the initial position of the rotors
    machine.set_display(rotor_start)

    transformed_msg = machine.process_text(msg)
    return transformed_msg

encoded = use_enigma_machine("I love coding", "ABC")
decoded = use_enigma_machine(encoded, "ABC")

print(encoded)
print(decoded)
