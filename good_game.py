from analyzing import *

def good_game(data, game):
    """
    Analyzes a given game by comparing it to historical results.
    Highlights how often its numbers appear in consecutive and gapped sequences,
    and how frequently it scores high points compared to past games.
    """
    # Get sequences of consecutive numbers and gapped sequences
    consecutive_sequences = get_sequence(game)[0]
    max_gap_sequences = get_max_sequence(game)[0]

    # Identify if the game contains a 100% match sequence
    full_consecutive_seq = next((k for k, v in consecutive_sequences.items() if v == '100.00%'), '')
    full_gap_seq = next((k for k, v in max_gap_sequences.items() if v == '100.00%'), '')

    # Group past results into sets of 15 numbers
    grouped_results = [data[i:i+15] for i in range(0, len(data), 15)]

    # Compare how many numbers the game matches with each historical result
    score_distribution = [15 - len(set(game) - set(result)) for result in grouped_results]

    # Count frequency of high scores (10 to 15 matches)
    frequency_result = {f"{pts} pts": score_distribution.count(pts) for pts in range(10, 16)}

    return (
        f"Match Frequency: {frequency_result}\n"
        f"Full Consecutive Sequence: {full_consecutive_seq or 'None'}\n"
        f"Full Gapped Sequence: {full_gap_seq or 'None'}"
    )

# Example usage
data = organize_data(461)
random_game = sorted(random.sample(range(1, 26), 15))
print(random_game)
print(good_game(data, random_game))