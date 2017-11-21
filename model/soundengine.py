import os

from pygame import mixer

mixer.init()


def load(file):
    return mixer.Sound(file)


path = os.path.join('model', 'sounds', 'deadmau5_Strobe.ogg')
main_song = load(path)
path1 = os.path.join('model', 'sounds', 'effect1.ogg')
effect1 = load(path1)
path2 = os.path.join('model', 'sounds', 'effect2.ogg')
effect2 = load(path2)
path3 = os.path.join('model', 'sounds', 'effect3.ogg')
effect3 = load(path3)
path4 = os.path.join('model', 'sounds', 'effect4.ogg')
effect4 = load(path4)
path5 = os.path.join('model', 'sounds', 'effect5.ogg')
effect5 = load(path5)

""""""


def play_effect1():
    effect1.play(maxtime=1000)


def play_effect2():
    effect2.play(maxtime=1000)


def play_effect3():
    effect3.play(maxtime=1000)


def play_effect4():
    effect4.play(maxtime=1000)


def play_effect5():
    effect5.play(maxtime=1000)


def play_main_song():
    main_song.play(loops=-1, fade_ms=300)
