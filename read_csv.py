import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv('enrollments.csv')
daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')

row_count = sum(1 for row in open('enrollments.csv', 'rb') )
print ("Number of rows in enrollments.csv = ", row_count)
row_count = sum(1 for row in open('daily_engagement.csv', 'rb') )
print ("Number of rows in daily_engagement.csv = ", row_count)
row_count = sum(1 for row in open('project_submissions.csv', 'rb') )
print ("Number of rows in project_submissions.csv = ", row_count)
