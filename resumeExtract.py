from pyresparser import ResumeParser
data = ResumeParser('test.pdf').get_extracted_data()
print(data)