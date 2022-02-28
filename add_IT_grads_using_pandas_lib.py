#!/usr/bin/env python3
import pandas as pd

# DATA FROM UNIVERSITY
# read the unarchived data from university
uni_data = pd.read_csv('./universities-intake-enrolment-and-graduates-by-course.csv')

# eliminate commas from the data
uni_data['graduates'] = uni_data['graduates'].str.replace(',', '')

# extract data that contained "Information Technology" and "MF" in the respective columns
extract_udata = uni_data[(uni_data.course == "Information Technology") & (uni_data.sex == "MF")]

# save extracted data to .csv and eliminate the left-most index column 
extract_udata.to_csv('./uni_extracted_data.csv', index = False)

# read processed extracted data from .csv
read_uni_extracted = pd.read_csv('./uni_extracted_data.csv')

# gathering total of IT grads from university over the years
uni_total_it_grads = read_uni_extracted['graduates'].sum()
print (f"Total IT graduates from University from year 2005 to 2020: {uni_total_it_grads}")

# DATA FROM POLYTECHNIC
# read the unarchived data from polytechnic
poly_data = pd.read_csv('./polytechnics-intake-enrolment-and-graduates-by-course.csv')

# eliminate commas from the data
poly_data['graduates'] = poly_data['graduates'].str.replace(',', '')

# extract data that contained "Information Technology" and "MF" in the respective columns
extract_pdata = poly_data[(poly_data.course == "Information Technology") & (poly_data.sex == "MF")]

# save extracted data to .csv and eliminate the left-most index column 
extract_pdata.to_csv('./poly_extracted_data.csv', index = False)

# read processed extracted data from .csv
read_poly_extracted = pd.read_csv('./poly_extracted_data.csv')

# gathering total of IT grads from polytechnic over the years
poly_total_it_grads = read_poly_extracted['graduates'].sum()
print (f"Total IT graduates from Polytechnic from year 2005 to 2020: {poly_total_it_grads}")

# totalling IT grads from both university and polytechic
grand_total_it_grads = uni_total_it_grads + poly_total_it_grads
print(f"Total IT graduates from University and Polytechnic from year 2005 to 2020: {grand_total_it_grads}")