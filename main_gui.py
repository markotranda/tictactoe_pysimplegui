from tkinter.constants import CENTER
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED
from tictactoe import TicTacToe
from AI import AI
import PySimpleGUI as sg


def main():
    game = TicTacToe()
    ai_player = AI(-1)

    layout = [
        [sg.Text('TicTacToe - PySimpeGUI')],
        [sg.Column([[sg.Button(button_text='', key='0', size=(4, 2)), sg.Button(button_text='', key='1', size=(4, 2)), sg.Button(button_text='', key='2', size=(4, 2))]])],
        [sg.Column([[sg.Button(button_text='', key='3', size=(4, 2)), sg.Button(button_text='', key='4', size=(4, 2)), sg.Button(button_text='', key='5', size=(4, 2))]])],
        [sg.Column([[sg.Button(button_text='', key='6', size=(4, 2)), sg.Button(button_text='', key='7', size=(4, 2)), sg.Button(button_text='', key='8', size=(4, 2))]])]
    ]
    window = sg.Window('TicTacToe', layout, size=(200, 220), element_justification=CENTER)
    while not game.is_over():
        if game.get_current_player() == 1:
            event, _ = window.read()
            if event == WINDOW_CLOSED:
                break
        else:
            event = str(ai_player.pick_move(game.copy_current_state()))
        game.play(int(event))
        window[event].update(game.get_state()[int(event)])

    # window.close()

if __name__ == '__main__':
    main()