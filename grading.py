#program to calculate the statistical mean, variance, and standard deviation from a text file with a number on each line
import statistics

#list to store all the students' scores
scores = []
scoreFile = open(studentScores, 'r')
outputFile = open(scoreStatistics, 'w+')

for line in scoreFile.readlines():
	line = line.strip() #getting rid of the \n characters
	scores.append(line)

#writes a student's score line by line
def display_scores(scoreList)
	for score in scoreList:
		outputFile.write(score)
		outputFile.write("\n")

def display_average(scoreList)
	average = statistics.mean(scoreList)
	outputFile.write("Average score: %s", %average)
	outputFile.write("\n")
	
def display_variance(scoreList)
	variance = statistics.pvariance(scoreList)
	outputFile.write("Variance of the scores: %s", %variance)
	outputFile.write("\n")
	
def display_stdev(scoreList)
	stdev = statistics.stdev(scoreList)
	outputFile.write("Standard deviation of the scores: %s", %stdev)
	outputFile.write("\n")
	
display_average(scores)
display_stdev(scores)

scoreFile.close()
outputFile.close()
