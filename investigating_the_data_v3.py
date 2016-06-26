import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

def get_unique_students(data):
    unique_students = set()
    for data_point in data:
        unique_students.add(data_point['account_key'])
    return unique_students

enrollments = read_csv('enrollments.csv')
daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')

len(enrollments)
print ( "Number of enrollments = ", len (enrollments ) )

unique_enrolled_students = get_unique_students(enrollments)
len(unique_enrolled_students)
print ( "Number of unique enrollments = ", len (unique_enrolled_students ) )

### Change header string value from "acct" to "account_key" ###
for engagement_record in daily_engagement:
    engagement_record['account_key'] = engagement_record['acct']
    del[engagement_record['acct']]

len(daily_engagement)
print ( "Number of daily_engagement = ", len (daily_engagement) )

unique_engagement_students = get_unique_students(daily_engagement)
len(unique_engagement_students)
print ( "Number of unique daily_engagement = ", len (unique_engagement_students) )

len(project_submissions)
print ( "Number of project_submissions = ", len (project_submissions) )

unique_project_submitters = get_unique_students (project_submissions)
len(unique_project_submitters)
print ( "Number of unique project_submitters = ", len (unique_project_submitters) )

enrollment_num_rows = len(enrollments)
enrollment_num_unique_students = len(unique_enrolled_students)

engagement_num_rows = len(daily_engagement)
engagement_num_unique_students = len(unique_engagement_students)

submission_num_rows = len(project_submissions)
submission_num_unique_students = len(unique_project_submitters)

print daily_engagement[0]['account_key']

for enrollment in enrollments:
    student = enrollment['account_key']
    if student not in unique_engagement_students:
        print enrollment
        break

num_problem_students = 0
for enrollment in enrollments:
    student = enrollment['account_key']
    if (student not in unique_engagement_students and 
            enrollment['join_date'] != enrollment['cancel_date']):
        print enrollment
        num_problem_students += 1

print num_problem_students

