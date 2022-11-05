import pyglet


sound = pyglet.media.load('tomas-i-ego-druzya-komanda-iz-8-mi-druzey.mp3', streaming=False)
sound.play()
pyglet.app.run()
