
input_nums = input("Input a list of nums ").split()
for n in range(0, len(input_nums)):
  input_nums[n] = int(input_nums[n])

avgNum = 0

for num in input_nums:
    avgNum = avgNum + num

avgNum = avgNum/ len(input_nums)

print(round(avgNum))


