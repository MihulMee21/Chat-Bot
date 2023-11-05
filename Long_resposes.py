import random

R_eating="I don't like eating because I'm a Bot obviously!"
R_name="I am a bot,I don't have any name!"


def unknown():
    responce=['could you please re-phrase that?',
              "....",
              "Sounds about right",
              "What does that mean?"][random.randrange(4)]
    return responce