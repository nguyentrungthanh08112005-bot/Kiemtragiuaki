def phan_tich_van_ban():
    text = input("Nhập đoạn văn bản của bạn (khoảng 2-3 câu): ")
    punctuation = [".", ",", "!", "?", ":", ";"]
    clean_text = text
    for p in punctuation:
        clean_text = clean_text.replace(p, " ")
    words = clean_text.lower().split()

    total_words = len(words)

    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    if word_count:
        most_frequent_word = max(word_count, key=word_count.get)
        max_occurrences = word_count[most_frequent_word]
    else:
        most_frequent_word = None
        max_occurrences = 0

    print("\n--- KẾT QUẢ PHÂN TÍCH ---")
    print(f"Danh sách các từ: {words}")
    print(f"Tổng số từ: {total_words}")
    if most_frequent_word:
        print(f"Từ xuất hiện nhiều nhất: '{most_frequent_word}' ({max_occurrences} lần)")
    else:
        print("Không có từ nào để phân tích.")

phan_tich_van_ban()