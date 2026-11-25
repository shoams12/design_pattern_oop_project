from game import Game


if __name__ == '__main__':
    # Open a new game
    game = Game("Player 1", "Falcon")

    # Game 1 - lose


    game.start()  # NewGame -> Normal

    game.take_hit(15)  # 35 hit points - Normal
    game.complete_level()  # level 2
    game.take_hit(20)  # 15 hit points - Normal -> Danger
    game.repair(10)  # 25 hit points - Danger -> Normal
    game.take_hit(30)  # 0 hit points  -> GameOverLose

    # Game 2 - win
    game.start()  # GameOverLose -> NewGame -> Normal
    game.complete_level()  # level 2
    game.take_hit(35)  # 15 hit points -> Danger
    game.complete_level()  # level 3
    game.complete_level()  # finished level 3 -> GameOverWin
    game.take_hit(5)  # game is over

    # Wait for user
    input("Press Enter to exit...")


