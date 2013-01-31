import csv

def generateSQL(filename):
	statement_prefix = "INSERT INTO companiesEvaluator_reclamacao VALUES('"
	statement_suffix = "');\n"
	file_read = open(filename, "rb")
	file_write = open("output.sql", "wb")
	reader = csv.reader(file_read, delimiter=';')
	for row in list(reader)[1:]:
		values = "', '".join(row)
		statement = statement_prefix + values + statement_suffix
		file_write.write(statement)
	file_read.close()
	file_write.close()
