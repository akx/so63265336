.PHONY: main

main: badges.csv
	python read_csv_to_pd.py

badges.csv: badges.xml
	python read_xml_to_csv.py

badges.xml:
	python generate_xml.py