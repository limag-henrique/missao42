#!/usr/bin/python3

def find_redheads(família_dupont):
    def is_red(valor):
        if família_dupont[valor] == "red":
            return True
        else:
            return False
        
    final = filter(is_red, família_dupont.keys())
    final = list(final)
    return final

família_dupont = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_redheads(família_dupont))