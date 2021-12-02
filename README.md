# ecg-identifier
<h2>why this project</h2>
<p>
  According to the World Health Organization (WHO), cardiovascular diseases
(CVDs) are the number one cause of death today. Over 17.7 million people died from CVDs in the year 2017 all over the world which is about 31% of all deaths, and over 75% of these deaths occur in low and middle income countries. Arrhythmia is a representative type of CVD that refers to any irregular change from the normal heart rhythms. There are several types of arrhythmia including atrial fibrillation, premature contraction, ventricular fibrillation, and tachycardia. Although single arrhythmia heartbeat may not have a serious impact on life, continuous arrhythmia beats can result in fatal circumstances. For example, prolonged premature ventricular contraction (PVCs) beats occasionally turn into a ventricular tachycardia (VT) or ventricular fibrillation (VF) beats which can immediately lead to heart failure. Thus, it is important to periodically monitor the heart rhythms to manage and prevent the CVDs. Electrocardiogram (ECG) is a non-invasive medical tool that displays the rhythm and status of the heart. Therefore, automatic detection of irregular heart rhythms from ECG signals is a significant task in the field of cardiology.
</p>

<h2>Why automated ECG classification is necessary?![image](https://user-images.githubusercontent.com/84030708/144447606-b699b0f2-2e0d-4db3-b781-892efd985392.png)</h2>
<ul>
  <li>Identification of arrhythmia condition from ECG signal takes a lot of experience even for experienced cardiologists.</li>
  <li>Harmful arrhythmia conditions occur rarely so less data for analysis and prediction</li>
  <li>Neural networks are good at signal classification.</li>
  <li> lot of wearable devices available to monitor ECG of the user</li>
  </ul>
<h2>scope of the project</h2>
<p>
  This project is intended to identify and classify various heart conditions using a 2-D convolutional neural network in which we classify ECG into five categories, one being normal and the other four being different types of arrhythmia beats.The user will have a website to upload the raw ecg signal and the website will diplay the result of classification
</p>
<h2>previously used approach</h2>
<ul>
  <li>Wavelet transform/Fourier transform</li>
  <li>Conv1D neural network</li>
  <li>Window based approach</li>
</ul>

<h2>my approach</h2>
<ul>
  <li>Conv2D network was used for classification and cnn is trained using grayscale images of ECG signals</li>
  <li>r-r interval is used instead of window based apporach</li>
  <li>The system is able to take ECG signal at various sampling frequency</li>
  <li>The system has a display and store unit which can be used by physicians for further reference</li> 
</ul>
<h2>subtasks of the projects</h2>
<ul>
  <li>Peak detection.</li>
<li>Dividing the signal into multiple sub parts using peaks obtained from peak detection.</li>
<li>Converting the segmented signal into image.</li>
<li>Training of the CNN neural network using images of signals</li>
<li>Classification of ECG signal whether it is normal or harmful</li>
<li>Website to load and visualize the classification results</li>
</ul>

<h2>peak detection</h2>
<ul>
  <li>Pantombkins algorithm(my choice)</li>
<li>Wavelet transformation</li>
<li>Two moving averages</li>
<li>Hamilton algorithm</li>
</ul>
<p>I tested neurokit2 python package for detection of r peaks.checked the annotation provided with original annotation.neurokit2 was able to predict annotation with 99.8% accuracy.also documentation of neurokit2 has functions to take ecg signal of various sampling ffrequency.I am currently developing pantombkins algorithm using python  </p>

<h2>MIT-Arrythmia Database</h2>
[dataset](https://physionet.org/content/mitdb/1.0.0/)

<b>360HZ</b>

48 Samples of 30 minutes, 2 leads
47 Patients:

* 100 series: 23 samples
* 200 series: 25 samples. **Contains uncommon but clinically important arrhythmias**

| Symbol|   Meaning                                   |
|-------|---------------------------------------------|
|· or N |	Normal beat                                 |
|L      |   Left bundle branch block beat             |
|R      |	Right bundle branch block beat              |
|A      |	Atrial premature beat                       |
|a      |	Aberrated atrial premature beat             |
|J      |	Nodal (junctional) premature beat           |
|S      |	Supraventricular premature beat             |
|V      |	Premature ventricular contraction           |
|F      |	Fusion of ventricular and normal beat       |
|[      |	Start of ventricular flutter/fibrillation   |
|!      |	Ventricular flutter wave                    |
|]      |	End of ventricular flutter/fibrillation     |
|e      |	Atrial escape beat                          |
|j      |	Nodal (junctional) escape beat              |
|E      |	Ventricular escape beat                     |
|/      |	Paced beat                                  |
|f      |	Fusion of paced and normal beat             |
|x      |	Non-conducted P-wave (blocked APB)          |
|Q      |	Unclassifiable beat                         |
||      |	Isolated QRS-like artifact                  |

[beats and rhythms](https://physionet.org/physiobank/database/html/mitdbdir/tables.htm#allrhythms)



### AAMI recomendation for MIT
There are 15 recommended classes for arrhythmia that are classified into 5 superclasses:

| SuperClass| | | | | | |
|------|--------|---|---|---|---|-|
| N  (Normal)  | N      | L | R |  |  | |
| SVEB (Supraventricular ectopic beat) | A      | a | J | S |  e | j |
| VEB  (Ventricular ectopic beat)| V      | E |   |   |   | |
| F    (Fusion beat) | F      |   |   |   |   | |
| Q   (Unknown beat)  | P      | / | f | u |   |    |

<h2>deliverables</h2>
<ol>
<li>2d cnn model that is able to classify ecg signals</li>
<li>website that can take the ecg signal as input and output the classification result</li>
</ol>

<h2>tools used</h2>
<ol>
<li>python</li>
<li>tensorflow</li>
<li>html</li>
<li>css</li>
<li>numpy</li>
<li>tensorflow</li>
<li>pandas</li>
<li>wfdb</li>


</ol>
<h2>progress</h2>
<ol>
<li>week1,2:litreature review</li>
<li>week3:training of a 1d cnn model using kaggle dataset and demonstration</li>
<li>week4:converting the raw signal and annotation into csv and txt file</li>
<li>week5:learn html,css,javascrpt</li>
<li>week6:website development</li>
<li>week6:converting the ecg signal into grayscale images,dividing of images into 5 super classes for training purposes</li>
<li>week7,week8,week 9:training of the neural network and optimization of neural network </li>
<li>week 10,week 11:implementation of pan tompkins algorithm to detect r peaks,testing of neurokit2 library</li>
<li>week 12:setting up a jupyter notebook for mid evaluation</li>
  



</ol>

<h2>to be done</h2>
<ol>
<li>training the neural network with V1 lead</li>
<li>fine tuning the neural network </li>
<li>setting up the GUI using Tkinter for demonstration</li>
  



</ol>

<h2>segmentation of signal</h2>
<ul>
  
  <li>initially the signal and annotations were converted into csv file for easy formatting.</li>
  <li>then the signal is segmented into segments.each segment represent R-R intervalof a signal</li>
  
  <li>then segments are grouped into 5 categories namely normal,fusion,sveb,veb and unknown beats</li>
  ![segmented-samples](https://github.com/juzailml98/ecg-identifier/blob/master/readme-photos/png-file/samples.png?raw=true)
  
<li>the data samples used for training are [101,106, 108, 109, 112, 114, 115, 116, 118, 119, 122, 124, 201, 203, 205, 207, 208, 209, 215, 220, 223, 230]</li>
<li>the data samples used for testing are [100, 103, 105, 111, 113, 117, 121, 123, 200, 202, 210, 212, 213, 214, 219, 221, 222, 228, 231, 232, 233, 234]</li>
<li>hold out validation is used so that to identify how the neural network performs well for new dataset and restricted computation power </li>
 </ul>
 <p>jupyter notebook used for segmenting and grouping of ecg signal is</p> [annotator](https://github.com/juzailml98/ecg-identifier/blob/master/annotator.ipynb)

<h2>training of model</h2>
<ul>
  <li>the dataset used for training of neural network has the following distribution</li>
  ![distribution](https://github.com/juzailml98/ecg-identifier/blob/master/readme-photos/png-file/data-distribution.png?raw=true)
  <li>the model trained was able to classify the signal into 5 categories</li> 
  <li>the model was trained for 2 epoch and obtained accuracy of 90.9,recall of 89.1 and precision of 91.1</li>
  
  <li>intended to downsample the number of normal samples</li>
</ul>
<p>for better identifying the abnormal beats
classification is done on 4 classes they are sveb,veb,usion ,normal
  two state architecture is to be used</p>


<h2>nature of dataset</h2>
<p>the original mit-bih dataset consists of</p>
<ul>
  <li>normal beats:83000</li>
  <li>sveb beats:3013</li>
  <li>veb beats:6335</li>
  <li>fusion beats:801</li>
  <li>other beats:2309</li>
 </ul>
   <p>the dataset is very unbalanced due to high availability of normal beats and low availability of other classes</p>
   <p>normal beats are divided into 45035 and 38032 as training set and testing set</p>
   <p>the training set normal beats are downsampled to 10000 from 45000</p>
   
<h2>website</h2>
<p>the ecg-classifer website is built using css,javascript and html.the website takes the raw ecg signal or csv converted ecg signal as input.the file uploaded will be sent to backend where the classification happens.the backend is being built using flask.</p>
![sample](https://github.com/juzailml98/ecg-identifier/blob/master/readme-photos/png-file/website.png?raw=true)
