numj = sorted(list(map(float, input().split())), reverse=True)
nums = sorted(list(map(float, input().split())), reverse=True)

Pj = 1 / 2 * numj[0] * numj[1]
Ps = 1 / 2 * nums[0] * nums[1]

if Pj == Ps:
    print("=")
elif Pj > Ps:
    print("Jasio")
else:
    print("Stasio")