def sum_over_k(sentence, k):
    words = sentence.split()
    count = 0
    
    for word in words:
        if len(word) > k:
            count += 1
    
    return count

# Example usage
sentence = 'Do or do not there is no try'
k = 2
result = sum_over_k(sentence, k)
print(result)  # 3
