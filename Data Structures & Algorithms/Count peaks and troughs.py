# P2 (Medium) Count peaks and troughs
# A peak is an index i (0 < i < n-1) where arr[i] > arr[i-1] and
# arr[i] > arr[i+1]. A trough is where arr[i] < both neighbours.
# Consecutive equal values form a plateau: treat a run of equal values as one
# point. A plateau counts as a peak if the values on both sides of the run are
# lower, and as a trough if both sides are higher. The first and last
# elements (or runs touching the ends) are never peaks or troughs.
# Return (number_of_peaks, number_of_troughs).
# Example: [1, 3, 2, 4, 1]       -> (2, 1)
#          [1, 3, 3, 2]          -> (1, 0)   plateau 3,3 is one peak
#          [5, 5, 5]             -> (0, 0)

def peaks_and_troughs(arr: List[int]) -> Tuple[int, int]:
    runs = []
    for x in arr:
        if not runs or runs[-1] != x:
            runs.append(x)
    peaks = troughs = 0
    for i in range(1, len(runs) - 1):
        if runs[i] > runs[i - 1] and runs[i] > runs[i + 1]:
            peaks += 1
        elif runs[i] < runs[i - 1] and runs[i] < runs[i + 1]:
            troughs += 1
    return peaks, troughs
