import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv('enrollments.csv')
daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')

len(enrollments)
print ( "Number of enrollments = ", len (enrollments ) )

unique_enrolled_students = set()
for enrollment in enrollments:
    unique_enrolled_students.add(enrollment['account_key'])
len(unique_enrolled_students)
print ( "Number of unique enrollments = ", len (unique_enrolled_students ) )

len(daily_engagement)
print ( "Number of daily_engagement = ", len (daily_engagement) )

unique_engagement_students = set()
for engagement_record in daily_engagement:
    unique_engagement_students.add(engagement_record['acct'])
len(unique_engagement_students)
print ( "Number of unique daily_engagement = ", len (unique_engagement_students) )

len(project_submissions)
print ( "Number of project_submissions = ", len (project_submissions) )

unique_project_submitters = set()
for submission in project_submissions:
    unique_project_submitters.add(submission['account_key'])
len(unique_project_submitters)
print ( "Number of unique project_submitters = ", len (unique_project_submitters) )

enrollment_num_rows = len(enrollments)
enrollment_num_unique_students = len(unique_enrolled_students)

engagement_num_rows = len(daily_engagement)
engagement_num_unique_students = len(unique_engagement_students)

submission_num_rows = len(project_submissions)
submission_num_unique_students = len(unique_project_submitters)
