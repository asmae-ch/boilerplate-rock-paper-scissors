# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    counter_moves = {'R': 'P', 'P': 'S', 'S': 'R'}

    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 5:
        return 'P'

    counts = {'R': opponent_history.count('R'),
              'P': opponent_history.count('P'),
              'S': opponent_history.count('S')}

    predicted_move = max(counts, key=counts.get)

    return counter_moves[predicted_move]