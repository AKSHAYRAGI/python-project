# python-project

PROBLEM STATEMENT:

Medical decisioning depends on medical history of a patient. Doctors typically use past patient records from multiple visits collected through lab tests, procedures and patient diagnoses records to determine the right treatment. The medical history and patient demographics can be used to identify and analyse patterns that groups patients into cohorts.The cohorts formed vary in terms of diseases, test results and patient data. Electronic Health Records are a systematic way to collect huge amounts of digital health information from multiple sources. Accessing this data and using it to create the cohorts presents initial analysis and proper medical path to be followed for any patient dependingon the results from similar patients belonging to the same cohort.
The problem is clearly identified as an unsupervised machine learning problem and I will use relevant algorithms to distinguish various cohorts based on their differences. Furthermore, this analysis can be used for drug analysis, identifying disease progression and much more.

TITLE: Health care patient clustering using Deep Neural Networks.

OVERALL PROJECT EXECUTION:

 As you can observe we have a notebook and a .py file. we have used the notebook for analysis and .py for implementation.
 
 ANALYSIS:
 (WE HAVE ADDED TEXT DESCRIPTION FOR MOST OF THE STEPS IN THE NOTEBOOK FOR BETTER UNDERSTANDING)

1: Start with collecting the data.

2: We have 4 input files and a som zip file that will be unzipped during the execution.
<img width="257" alt="Screen Shot 2021-12-12 at 2 36 12 PM" src="https://user-images.githubusercontent.com/89653019/145728656-9ef1d8d3-8256-4936-b85a-a8638164f527.png">

3: Import all the required input files.

we also download a open-source engine called tesseract.

Link: https://github.com/UB-Mannheim/tesseract/wiki

Tesseract is an open-source OCR engine developed by HP that recognizes more than 100 languages, along with the support of ideographic and right-to-left languages. Also, we can train Tesseract to recognize other languages.It contains two OCR engines for image processing – a LSTM (Long Short Term Memory) OCR engine and a legacy OCR engine that works by recognizing character patterns.The OCR engine uses the Leptonica library to open the images and supports various output formats like plain text, hOCR (HTML for OCR), PDF, and TSV.
   
   STEP 1: The first step in the execution is importing libraries.
   
   STEP 2: Importing the data.
   
   STEP 3: Data Cleaning.
   
   STEP 4: Visualization and Analysis.
   
   STEP 5: Creating age groups - Grouping creates categories of ages for better clustering.
   
   STEP 6: Diagnosis Data Distribution.
   
   STEP 7: Dividing the PrimaryDiagnosisCode into multiple columns to be able to create better clusters.
   
   STEP 8: Understanding the common OverallDiagnosisCode among different patients.
   
   STEP 9:Data Preparation.
   
   STEP 10:Converting the string values into categories and later into integers with integer encoding.
   
   STEP 11:Data Preprocessing.
   
   STEP 12:Initializing and training the model.
   
   STEP 13:Clustering a random data record.
   
   STEP 14:How good is SOM and dbscan performing.
   
   STEP 15:Comparing our results with another model gives us a good idea on how good the data actually is.I am using the DBSCAN model that decides the number of clusters within a dataset.
   
   SETP 16:The DBSCAN cluster plot at first glance doesnt make much sense but if you look closely you will notice that the blue dots which represent error(-1) cluster falls all over the place but other nodes are fairly clustered. The reason why DBSCAN does not perform well is because the number of error/unclustered data points are high compared to the clustered ones.
   
   STEP 17:Plotting MiniSOM clusters.
   
   STEP 18:Visualizing DBSCAN clusters.
   
   STEP 19:The SOM clusters are better defined compared to DBSCAN and this might be the driving factor for the model to perform well compared to DBSCAN.
   
   STEP 20: We are saving the model to finalized_model.pkl and saving a json file with the categorical data which can be used for implementation.
  
  -----------------------------------
  
  IMPLEMENTAION:
  
1. we have to install xampp first for hosting the website.

LINK:https://www.apachefriends.org/index.html

xampp: XAMPP helps a local host or server to test its website and clients via computers and laptops before releasing it to the main server. It is a platform that furnishes a suitable environment to test and verify the working of projects based on Apache, Perl, MySQL database, and PHP through the system of the host itself. Among these technologies, Perl is a programming language used for web development, PHP is a backend scripting language, and MariaDB is the most vividly used database developed by MySQL. The detailed description of these components is given below.

2.xampp package comes with a folder called htdocs in which we are pushing our json file and plk file.

3.We also place our .py file, upload.php and index.html in the same file.

4. It also comes with a inbuilt folder called upload in which we add our input images.

UPLOAD.PHP: 

It contains the entire code used to read the image and displaying the ouput.

-----------------------------------------

.PY FILE:

1. we use the same .pkl model and category file in here. But we make a few little additions to the code in here.

2. we convert the patient data to float.

3. we fix age range of a patient by considering it as two variables low_num and high_num.

4. we also have some commonly mistaken alphabets and numbers that are considered similar.

![confusion alphabets](https://user-images.githubusercontent.com/89653019/145730807-2dfcf872-5e7e-4e79-92de-9ae00659e573.jpeg)

5. we train the model so that it does not compromise on these issues.
-----------------------------------

Final execution:

1. once all of these steps are perfomed then go head and open xampp.

2. xampp has different modules but we only use apache in it.

3. start the apache and open the admin button next to it .

4. This opens the webiste upload the image saved in the xampp->htdocs->upload.

5. This gives us the coherent to which the patient belongs.
   
[NOTE: system prefrences has to be read and write for everyone for all the applications.]


 
