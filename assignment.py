team1 = 66
team2 = 69
team3 = 42
team4 = 59
team5 = 66

total = team1 + team2 + team3 + team4 + team5
average = total / 5

print("Total points                :", total)
print("Average per field           :", average)

total_stars = 32
print("Total stars                 :", total_stars)

boxes = total_stars // 10
print("Number of boxes             :", boxes)

remaining_stars = total_stars % 10
print("Remaining stars             :", remaining_stars)

t1_lw = 59
t2_lw = 74
t3_lw = 45
t4_lw = 55
t5_lw = 63

lw_total = t1_lw + t2_lw + t3_lw + t4_lw + t5_lw
print("Better than last week?      :", total > lw_total)
print("Same as last week?          :", total == lw_total)
print("At least as good?           :", total >= lw_total)

average += 27
print("Average after extra credit? :", average)

average -= 4
print("After reviewed externally   :", average)