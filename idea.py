import random

# なぞなぞリスト（問題、答え、解説）
riddles = [
    {
        "question": "パンはパンでも食べられないパンはなに？",
        "answer": "フライパン",
        "explanation": "フライパンは料理に使う道具で、食べ物ではありません。"
    },
    {
        "question": "学校で使うけど、食べられるものはなに？",
        "answer": "コンパス",
        "explanation": "「コンパス」は「コンパス（文房具）」と「コンパス（魚の名前）」のダジャレです。"
    },
    {
        "question": "四角いのに丸いものってなに？",
        "answer": "座布団",
        "explanation": "座布団は形は四角いですが、「座る」と丸くなる（丸く座る）という意味です。"
    },
    {
        "question": "穴があいているのに水がたまるものはなに？",
        "answer": "おたま",
        "explanation": "おたま（お玉杓子）は穴があいていても水をすくえます。"
    },
    {
        "question": "上がると下がるものはなに？",
        "answer": "気温",
        "explanation": "気温は上がったり下がったりします。"
    }
]

def main():
    riddle = random.choice(riddles)
    print("なぞなぞです！")
    print(riddle["question"])
    user_answer = input("あなたの答えは？：").strip()
    print("\n【あなたの答え】", user_answer)
    print("【正解】", riddle["answer"])
    print("【解説】", riddle["explanation"])

if __name__ == "__main__":
    main()