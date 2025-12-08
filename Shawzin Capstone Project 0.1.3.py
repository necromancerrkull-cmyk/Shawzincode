# ============================
# Shawzin Capstone Project
# ============================

Key = {
    'B':'A', 'J':'B', 'R':'C', 'h':'D', 'Z':'E', 'x':'F', 'p':'G',
    '5':'H', 'C':'I', 'K':'J', 'S':'K', 'i':'L', 'a':'M', 'y':'N',
    'q':'O', '6':'P', 'E':'Q', 'M':'R', 'U':'S', 'k':'T', 'c':'U',
    '0':'V', 's':'W', '8':'XYZ', 'GJ':'1', 'GZ':'2', 'G5':'3',
    'EK5':'4', 'Ea5':'5', 'E7':'6', 'M7':'7', 'c7':'8', '/':'9',
    'H':'0', 'F':'!', 'EJ':'@', 'ER':'#', 'Eh':'$', 'EZ':'%',
    'Ex':'^', 'Ep':'&', 'E5':'*', 'BM':'(', 'N':')', 'MR':'-',
    'Mh':'_', 'MZ':'=', 'Mx':'+', 'Mp':'[', 'M5':'{', 'BU':']',
    'JU':'}', 'Uh':'|', 'ZU':';', 'Ux':':', '5U':'"', 'Bk':',',
    'Jk':'<', 'Rk':'.', 'I':'>', 'Zk':'/', 'xk':'?', 'pk':'`',
    '5k':'~'
}

# reverse dictionary
RevKey = {}
for k, v in Key.items():
    if len(v) == 1:
        RevKey[v] = k
    else:
        for ch in v:
            RevKey[ch] = k

# ============================
# Placement Pair Auto-Increment
# ============================

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")

def next_pair(pair):
    first, second = pair[0], pair[1]
    idx_second = alphabet.index(second)

    if idx_second < len(alphabet) - 1:
        return first + alphabet[idx_second + 1]

    idx_first = alphabet.index(first)

    if idx_first < len(alphabet) - 1:
        return alphabet[idx_first + 1] + alphabet[0]

    return alphabet[0] + alphabet[0]  # wrap AA


# ============================
# Helpers
# ============================

def split_fragments(code):
    code = code[1:]
    frags = []
    for i in range(0, len(code), 3):
        if i+3 <= len(code):
            frags.append(code[i:i+3])
    return frags


def merge_fragments(frags):
    merged = []
    i = 0
    while i < len(frags):
        cur = frags[i]
        if i+1 < len(frags):
            nxt = frags[i+1]
            if cur[1:] == nxt[1:]:
                merged.append(cur[0] + nxt[0])
                i += 2
                continue
        merged.append(cur[0])
        i += 1
    return merged


# ============================
# UNMASK
# ============================

def unmask(code):
    frags = split_fragments(code)
    mains = merge_fragments(frags)
    result = ""
    for m in mains:
        if m in Key:
            result += Key[m]
        else:
            for ch in m:
                if ch in Key:
                    result += Key[ch]
    return result

# ============================
# Menu
# ============================

def main():
    while True:
        print("\n=== Shawzin Encoder/Decoder ===")
        print("1) Unmask (Shawzin → Text)")
        print("2) Exit")
        choice = input("Select: ")

        if choice == "1":
            code = input("Enter Shawzincode: ")
            print("Decoded message:\n", unmask(code))
        elif choice == "2":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()



