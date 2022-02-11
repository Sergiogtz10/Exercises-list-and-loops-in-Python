def lyrics_generator(list):
    repeat = 0
    lyrics = ""
    for i in list:
        if i == 0:
            lyrics += "Boom "
        elif i == 1:
            lyrics += "Drop the base "
            repeat += 1
            if repeat == 3:
                lyrics += "!!!Break the base!!! "
                repeat = 0
    return lyrics
            




# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))