from view.gameengine import GameEngine
from view.screen_sizes import Resolution

game = GameEngine(Resolution.LARGE.value)
game.run()
