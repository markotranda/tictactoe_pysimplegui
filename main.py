from tictactoe import TicTacToe
from AI import AI

def translate(button):
    move_list = ['7', '8', '9', '4', '5', '6', '1', '2', '3']
    for i in range(len(move_list)):
        if move_list[i] == button:
            return i
    return None


def main():
    game = TicTacToe()
    ai_player = AI(-1)
    print(game)
    while not game.is_over():
        if game.get_current_player() == 1:
            game.play(translate(input()))
        else:
            game.play(ai_player.pick_move(game.copy_current_state()))
        print(game)

if __name__ == '__main__':
    main()