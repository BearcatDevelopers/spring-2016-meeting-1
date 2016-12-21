# This is a comment, no code here will run

# Import module to read csv files
import csv

# "Open" the csv file
file = open('./Files/initial.csv')
csv_file = csv.reader(file)

male_emails = []
female_emails = []

# Loop through the csv file
for row in csv_file:
    
    # Do something to the csv file
    if row[4] == 'Male':
        male_emails.append(row[3])
    elif row[4] == 'Female':
        female_emails.append(row[3])

print len(male_emails)
print len(female_emails)

# Output and save the modified csv file

male_outputFile = open('./Files/male_output.csv', 'wb')
output_writer = csv.writer(male_outputFile)
output_writer.writerows(zip(male_emails))
male_outputFile.close()

female_outputFile = open('./Files/female_output.csv', 'wb')
output_writer = csv.writer(female_outputFile)
output_writer.writerows(zip(female_emails))
female_outputFile.close()