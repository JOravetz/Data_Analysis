import unicodecsv

with open ( 'enrollments.csv', 'rb' ) as f :
   reader = unicodecsv.DictReader (f)
   enrollments = list ( reader )

enrollments [0]
