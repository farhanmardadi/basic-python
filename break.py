#untuk menghentikan iterasi pada saat kondisi tertentu, dan tidak dilanjutkan iterasi berikutnya

# for i in range(5):
#     if i == 3:
#         break
#     print(i)

text = input()

while True:
    if text == "stop" or text == "end":
        print("Program has stopped.")
        break
    print("text: {}".format(text))
    text = input()