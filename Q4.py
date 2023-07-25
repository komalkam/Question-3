def count_pairs_with_sum(arr, target_sum):
    count = 0
    num_freq = {}

    for num in arr:
        complement = target_sum - num
        if complement in num_freq:
            count += num_freq[complement]
        num_freq[num] = num_freq.get(num, 0) + 1

    return count


if __name__ == "__main__":
   
    arr = [1, 5, 7, -1, 5]
    target_sum = 6

    result = count_pairs_with_sum(arr, target_sum)
    print("Number of pairs with sum", target_sum, ":", result)
