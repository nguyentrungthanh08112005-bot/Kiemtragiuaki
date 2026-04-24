import random
import time

def mini_hangman():
    words = ["python", "apple", "river", "coding", "orange",]
    secret_word = random.choice(words)
    
    guessed_letters = []
    wrong_attempts = 0
    max_wrong = 5
    start_time = time.time()

    print("TRÒ CHƠI ĐOÁN CHỮ (THE HANGMAN)")
    print(f"Từ bí mật gồm có {len(secret_word)} chữ cái.")

    while wrong_attempts < max_wrong:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nTừ cần đoán: {display_word}")
        print(f"Số lượt sai còn lại: {max_wrong - wrong_attempts}")
        
        if "_" not in display_word:
            end_time = time.time()
            play_time = round(end_time - start_time, 2)
            print(f"Chúc mừng! Bạn đã thắng. Thời gian chơi: {play_time} giây.")
            save_result("Thắng", max_wrong - wrong_attempts, play_time)
            return

        guess = input("Nhập một chữ cái: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Vui lòng chỉ nhập một chữ cái duy nhất!")
            continue

        if guess in guessed_letters:
            print(f"Bạn đã đoán chữ '{guess}' rồi, hãy thử chữ khác.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Chính xác! Chữ '{guess}' có trong từ.")
        else:
            wrong_attempts += 1
            print(f"Sai rồi! Không có chữ '{guess}'.")

    print(f"\nRất tiếc, chúc bạn may mắn lần sau! Từ đúng là: '{secret_word}'")
    save_result("Thua", 0, "N/A")

def save_result(status, lives_left, duration):
    with open("system_log.txt", "a", encoding="utf-8") as f:
        f.write(f"Trạng thái: {status} | Lượt sai còn lại: {lives_left} | Thời gian: {duration}s\n")
    print("=> Kết quả đã được ghi vào hệ thống.")

mini_hangman()