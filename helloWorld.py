# print("hello world!!!")
# name = input("please enter your name ")
# print(f"Hello {name}")

# def solution(A, B):
#     count = 0
#     if ((A*B) == 0):
#         return 0
#     b = str(bin(A*B))
#     for i in range(len(b)):
#         if ('1' == b[i]):
#             count += 1
#     return count

# print(solution(3,7))

def transformSentence(sentence):
    # 
    words = sentence.split()
    result = ""
    for i in words:
        result += i[0]
        for j in range(1, len(i)):
            if(i[j-1].lower() < i[j].lower()):
                result += i[j].upper()
            elif (i[j-1].lower() > i[j].lower()):
                result += i[j].lower()
            else:
                result += i[j]
        result += " "
    return result

text = "a Blue MOON"
print(transformSentence(text))