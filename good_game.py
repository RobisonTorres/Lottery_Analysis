from analyzing import*

def good_game(data, game):

    # This function analyzes a game by comparing it to historical results,
    # highlighting how often its numbers appear in long or consecutive sequences.
    sequence = get_sequence(game)
    max_sequence = get_max_sequence(game)
    g_results = [data[x:x+15] for x in range(0, len(data), 15)]
    score = []
    
    for result in g_results:
        score.append(15 - len(set(game) - set(result)))

    fre_result = {}
    for num in range(5, 16):
        fre_result[f"{num} pts"] = score.count(num)

    return f'Results: {fre_result}.\n\n'\
           f'Frequency of numbers in sequence: {sequence[0]}\n\n'\
           f'Frequency of maximum consecutive sequences: {max_sequence[0]}'

data = organize_data(461)
game = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print(good_game(data, game))