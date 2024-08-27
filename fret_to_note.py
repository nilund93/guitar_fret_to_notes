
conversion_table = {"E": ["E", "F", "F#", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb"], # 12 notes, 0 mod 12
                    "B": ["B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb"],
                    "G": ["G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb"],
                    "D": ["D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db"],
                    "A": ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"],
                    }

def main():
    while True:
        g_string = input("Please enter a guitar string (E, B, G, D, A): ").upper()
        if g_string not in conversion_table:
            print("Not a valid guitar string.")
        else:
            notes = conversion_table[g_string]
            convert = input("Put in your frets, separate with whitespace: ").split()
            print("--------------------------------------------")
            for note in convert:
                print(notes[int(note) % 12], end=" ")
            
            print("\n")

if __name__ == "__main__":
    # Teststring: 6, 14, 13, 11, 6, 6, 14, 13, 11, 13
    
    main()