"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

COLOUR_CODES = {"absolute zero": "#0048ba",
                "acid green": "#b0bf1a",
                "aliceBlue": "f0f8ff",
                "alizarin crimson": "#e32636",
                "ameranth": "#e52b50",
                "dogerBlue": "1e90ff",
                "dutch white": "#efdfbb",
                "ebony": "#555d50",
                "eggshell": "f0ead6",
                "eton blue": "96c8a2"
}


colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
        print(f"The code for \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
        colour_name = input("Enter a colour name: ").lower()

