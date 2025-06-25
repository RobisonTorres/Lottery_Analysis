import random
import json

def open_file():
     
     # This function opens and loads json files.
     try:
        file = open('results.json')
        previous_result = json.load(file)
        return previous_result
     except:
         return 'File not found.'

def sample_data():

    # This function determines the sample's size.
    total_rounds = len(open_file().values())
    rounds = input(f'Please choose a sample between 1 and {total_rounds} '\
                   f'or press enter to check all of them: ')
    return total_rounds if rounds == '' else int(rounds)

def organize_data(sample):
     
    # This function organizes the data.
    lottery_results = open_file().values()
    results = ''.join(lottery_results).replace('-', '') 
    numbers = [int(results[x: x+2]) for x in range(0, len(results), 2)][-sample * 15:]
    return numbers

def check_duplicate(sample):

    # This function checks the data for repeated results.
    lottery_results = open_file()
    values = list(lottery_results.values())[-sample:]
    count = [v for v in values if values.count(v) >= 2]
    repeat_keys = [k for k in lottery_results.keys() if lottery_results[k] in count]
    if count:
        return(f'Please check the data, these rounds {"-".join(repeat_keys)} '\
               f'have duplicated results.\n')
    return 'Each lottery\'s result is unique in this dataset.\n'

def even_odd(data):

    # This function returns the percentage of even and odd numbers.
    count_even = len([n for n in data if n % 2 == 0])
    even_nums = float(f'{(count_even/ len(data)*100):.2f}')
    return f'In {int(len(data)/ 15)} previous results '\
           f'{even_nums}% of the numbers are even and {100 - even_nums}% are odd.'

def frequency(data):
    
    # This function gets the frequency of each number and shows 
    # the five numbers most and least drawn.    
    fre_nums = {}
    for num in range(1, 26):
        fre_nums[num] = data.count(num)
    # Numbers most an least drawn.
    fre_num_sorted = sorted(fre_nums.items(),key=lambda x:x[1])[::-1]
    numbers = list(dict(fre_num_sorted).keys())    
    return f'Numbers most drawn - {sorted(numbers[0:5])}. '\
           f'Numbers least drawn - {sorted(numbers[20:])}.'     

def frequency_range(data):
    
    # This function groups the numbers in 5 different
    # ranges and shows the most and least drawn.
    fre_ranges = {}
    for x in range(1, 26, 5):
        count_numbers = str(len([n for n in data if n in range(x, x + 5)]))
        fre_ranges[f'{x}-{x + 4}'] = count_numbers
    # Ranges most an least drawn.
    fre_ranges_sorted = sorted(fre_ranges.items(),key=lambda x:int(x[1]))[::-1]
    ranges = list(dict(fre_ranges_sorted).keys())
    return f'Range of numbers most drawn - {[ranges[0]]}. '\
           f'Range of numbers least drawn - {[ranges[-1]]}.'

def get_sequence(data):

    # This function calculates the frequency of sequences of numbers
    # in the previous results. A sequence is defined as a set of
    # consecutive numbers, e.g. 1-2-3-4-5.    
    g_results = [sorted(data[x:x+15]) for x in range(0, len(data), 15)]
    sequence = []    
    for x in range(0, len(g_results)):
        seq = [0]
        [seq.append(seq[-1]+1) if g_results[x][y] + 1 == g_results[x][y+1]
                               else seq.append(0) for y in range(0, 14)]
        sequence.append(max(seq))
    fre_seq = {}
    for num in range(1, 15):
        fre_seq[f"{num} seq."] = f'{(sequence.count(num) / len(g_results)) * 100:.2f}%'
    more_seq = g_results[sequence.index(max(sequence))]
    less_seq = g_results[sequence.index(min(sequence))] 
    return [fre_seq, more_seq, less_seq]

def get_max_sequence(data):

    # This function is similar to get_sequence, but it calculates the maximum
    # sequence even with non consecutive numbers (e.g. 1-2-4-5 -> 2 sequence).
    g_results = [sorted(data[x:x+15]) for x in range(0, len(data), 15)]
    sequence = []    
    for x in range(0, len(g_results)):
        seq = 0
        for y in range(0, 14):
            if g_results[x][y] + 1 == g_results[x][y+1]:
                seq += 1
        sequence.append(seq)
    fre_seq = {}
    for num in range(4, 15):
        fre_seq[f"{num} seq."] = f'{(sequence.count(num) / len(g_results)) * 100:.2f}%'
    more_seq = g_results[sequence.index(max(sequence))]
    less_seq = g_results[sequence.index(min(sequence))]  
    return [fre_seq, more_seq, less_seq]

def display_sequence_patterns(data):

    # This function displays the frequency of sequences and maximum sequences
    # in the previous results, as well as the games with the longest and shortest sequences.
    sequence = get_sequence(data)
    max_sequence = get_max_sequence(data)
    return f'\nFrequency of maximum consecutive sequences: {sequence[0]}.\n'\
           f'Game with the longest sequence: {"-".join(map(str , sequence[1]))}'\
           f'\nGame with the shortest sequence: {"-".join(map(str, sequence[2]))}\n'\
           f'\n'\
           f'Frequency of sequence with gaps: {max_sequence[0]}.\n'\
           f'Game with more numbers in sequence: {"-".join(map(str , max_sequence[1]))}'\
           f'\nGame with less numbers in sequence: {"-".join(map(str, max_sequence[2]))}\n'

def lottery_match_frequencies(data):
    
    # This function calculates the frequency of matches between all previous results.
    # It could be used to find out how many times a new result matches with previous ones.
    # The score is calculated as the number of matches between two results.
    g_results = [data[x:x+15] for x in range(0, len(data), 15)]
    score = []
    while len(g_results) > 1:
        each_result = g_results[0]
        for result in g_results[1:]:
            score.append(15 - len(set(each_result) - set(result)))
        g_results = g_results[1:]
    fre_result = {}
    for num in range(5, 16):
        fre_result[f"{num} pts"] = score.count(num)
    return f'Frequency of repeated results: {fre_result}.\n'

def repetition(data):

    # This function calculates the frequency of repeated numbers 
    # between current result and previous one, except for the first result.
    grouped_results = [data[x:x+15] for x in range(0, len(data), 15)]
    if len(grouped_results) <= 2:
        return 'The sample must be more than 2 to find games that repeat numbers from previous results.\n'
    else:
        rep_numbers = [(15 - len(set(grouped_results[x]) - set(grouped_results[x-1])))
                        for x in range(0, len(grouped_results)) if x != 0]
        # Frequency of repeated numbers.
        fre_result = {}
        for num in range(6, 16):
            fre_result[num] = rep_numbers.count(num)
        # Games that repeated at least 9 numbers from previous result.
        repeated = sum(list(fre_result.values())[3:])   
        return f'Out of {len(grouped_results) - 1} games, in '\
               f'{((repeated / (len(grouped_results) - 1)) * 100):.2f}% '\
               f'of cases a new result had at least 9 numbers the same as the prior result.'             

def simulate_games():

    # This function simulates 326,876 games and calculate scores. 
    # Each game is a selection of 15 numbers between 1 and 25.
    random_games = []
    for x in range(0, 326_876):  
        random_games.append(random.sample(range(1, 26), 15))
    score = []
    random_result = random.sample(range(1, 26), 15)
    for num in range(0, len(random_games)):
            score.append(15 - len(set(random_result) - set(random_games[num])))
    # Frequency of winning prizes.    
    score_prizes = {}
    for num in range(11, 16):
        score_prizes[str(num) + ' pts'] = score.count(num)
    return (f"By simulating 326,876 games, "
        f"the occurrence of each score required to win prizes is:\n"
        f"{score_prizes}.")

if __name__ == "__main__":

    print("Analyzing Previous Results.\n")
    sample = sample_data()
    data = organize_data(sample)
    print(check_duplicate(sample))
    print(even_odd(data))
    print(frequency(data))
    print(frequency_range(data))
    print(repetition(data))
    print(display_sequence_patterns(data))
    print(lottery_match_frequencies(data))
    print('Simulating Games.\n')
    print(simulate_games())