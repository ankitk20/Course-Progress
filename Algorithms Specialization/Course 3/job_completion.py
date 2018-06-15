with open('jobs.txt') as file:
	lines = file.readlines()

jobsdiff = []
jobsratio = []
completiontime = 0
jobcount = int(lines.pop(0))

for line in lines:
	w, l = list(map(int, line.split()))
	jobsdiff.append((w, l, w - l))
	jobsratio.append((w, l, w / l))

jobsdiff.sort(reverse=True, key=lambda x:(x[2], x[0]))
jobsratio.sort(reverse=True, key=lambda x:(x[2], x[0]))

lengthdiff, lengthratio, timediff, timeratio = 0, 0, 0, 0
for jdiff, jratio in zip(jobsdiff, jobsratio):
	lengthdiff += jdiff[1]
	timediff += jdiff[0] * lengthdiff
	lengthratio += jratio[1]
	timeratio += jratio[0] * lengthratio

print((timediff, timeratio))