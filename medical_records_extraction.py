# in-built libraries
import pytesseract
import shutil
import os
import random
try:
 from PIL import Image
except ImportError:
 import Image
import cv2
import pickle
import json
import numpy


def fix_code1(code):
    lower_case_fixes = {"l":1, "b":6, "o":0, "g":9, "q":9}
    upper_case_fixes = {"G":6, "F":7, "Z":2, "Q":2, "O":0, "B":8, "D":0, "S":5, "Y":5, "T":7, "U":0}
    fixed_code = code[0]
    for letter in code[1:]:
        if letter in lower_case_fixes:
            fixed_code += str(lower_case_fixes[letter])
        elif letter in upper_case_fixes:
            fixed_code += str(upper_case_fixes[letter])
        else:
            fixed_code += letter
    return fixed_code

def fix_age_range(age_range):
    try:
        low_num = ["10", "20", "30", "40", "50", "60", "70", "80", "90"]
        high_num = ["19", "29", "39", "49", "59", "69", "79", "89", "99"]
        range_num = ["10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79" ,"80-89", "90-99"]
        low_number = age_range.split("-")[0]
        high_number = age_range.split("-")[1]
        if low_number in low_num:
            return range_num[low_num.index(low_number)]
        elif high_number in high_num:
            return range_num[high_num.index(high_number)]
        else:
            return "50-59"
    except:
        return "50-59"

def get_cat_key(cat_dictionary, value):
    key_list = list(cat_dictionary.keys())
    val_list = list(cat_dictionary.values())
    position = val_list.index(value)
    return key_list[position]


image_path_in_colab="upload/hand-written-text.jpg"
img = Image.open(image_path_in_colab)

extractedInformation = pytesseract.image_to_string(img)
print(extractedInformation)
extracted_text = extractedInformation.split("\n")
new_patient_info = [extracted_text[0].replace("AdmissionID - ", ""), extracted_text[1].replace("OverallDiagnosisCode - ", ""), extracted_text[2].replace("DiagnesisCodel - ", ""), extracted_text[3].replace("DiagnesisCode2 - ", ""), extracted_text[4].replace("PatientGender - ", ""), extracted_text[5].replace("PatientRace - ", ""), extracted_text[6].replace("PatientMaritalStatus - ", ""), extracted_text[7].replace("PetientLanguage ~ ", ""), extracted_text[8].replace("AgeRange - ", "")]
new_patient_info[2] = fix_code1(new_patient_info[2])
new_patient_info[8] = fix_age_range(new_patient_info[8])

cat_file = open("categories_data.json", "r")
cat_dictionary = json.load(cat_file)

new_patient_info[1] = get_cat_key(cat_dictionary["overall_diag_code_dict"], new_patient_info[1])
new_patient_info[2] = get_cat_key(cat_dictionary["diag_code_1_dict"], new_patient_info[2])
new_patient_info[4] = get_cat_key(cat_dictionary["gender_dict"], new_patient_info[4])
new_patient_info[5] = get_cat_key(cat_dictionary["race_dict"], new_patient_info[5])
new_patient_info[6] = get_cat_key(cat_dictionary["marital_status_dict"], new_patient_info[6])
new_patient_info[7] = get_cat_key(cat_dictionary["lang_dict"], new_patient_info[7])
new_patient_info[8] = get_cat_key(cat_dictionary["age_dict"], new_patient_info[8])

new_patient_info[0] = float(new_patient_info[0])
new_patient_info[1] = float(new_patient_info[1])
new_patient_info[2] = float(new_patient_info[2])
new_patient_info[3] = float(new_patient_info[3])
new_patient_info[4] = float(new_patient_info[4])
new_patient_info[5] = float(new_patient_info[5])
new_patient_info[6] = float(new_patient_info[6])
new_patient_info[7] = float(new_patient_info[7])
new_patient_info[8] = float(new_patient_info[8])

arr = numpy.array(new_patient_info)

filename = "finalized_model.pkl"
loaded_model = pickle.load(open(filename, 'rb'))
print(loaded_model.winner(arr))