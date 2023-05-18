print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
A, B = input().split()
N = int(A)
# print(N)

print("앞서 적은 원소 개수만큼 뭔자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
names = list(map(str, input().split()))
# print(names)

count = 1
for i in names:
    if i != B:
        count += 1
    else:
        break

print(count)