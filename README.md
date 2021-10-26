# ecg-identifier
<h2>why this project</h2>
<p>
  According to the World Health Organization (WHO), cardiovascular diseases
(CVDs) are the number one cause of death today. Over 17.7 million people died from CVDs in the year 2017 all over the world which is about 31% of all deaths, and over 75% of these deaths occur in low and middle income countries. Arrhythmia is a representative type of CVD that refers to any irregular change from the normal heart rhythms. There are several types of arrhythmia including atrial fibrillation, premature contraction, ventricular fibrillation, and tachycardia. Although single arrhythmia heartbeat may not have a serious impact on life, continuous arrhythmia beats can result in fatal circumstances. For example, prolonged premature ventricular contraction (PVCs) beats occasionally turn into a ventricular tachycardia (VT) or ventricular fibrillation (VF) beats which can immediately lead to heart failure. Thus, it is important to periodically monitor the heart rhythms to manage and prevent the CVDs. Electrocardiogram (ECG) is a non-invasive medical tool that displays the rhythm and status of the heart. Therefore, automatic detection of irregular heart rhythms from ECG signals is a significant task in the field of cardiology.
</p>
<h2>scope of the project</h2>
<p>
  This project is intended to do ECG arrhythmia classification using a 2-D convolutional neural network in which we classify ECG into five categories, one being normal and the other four being different types of arrhythmia using deep two-dimensional CNN with grayscale ECG images. 
</p>
<h2>MIT-Arrythmia Database</h2>
<a>https://physionet.org/content/mitdb/1.0.0/</a>

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
<li>week5:learn html,css,javascrpt,</li>
<li>week6:website development</li>


</ol>

<h2>to be done</h2>
<ol>
<li>identification of peaks in the signal</li>
<li>training of 2d cnn model </li>



</ol>
<h2>insights so far</h2>
<ol>
<li>try transfer learning instead of data augmentation as training the model using original dataset is very time consuming and resource consuming</li>




</ol>

<h2>segmentation of signal</h2>
<ul>
  
  <li>initially the signal and annotations were converted into csv file for easy formatting.</li>
  <li>then the signal is segmented into segments.each segment represent R-R intervalof a signal</li>
  
  <li>then segments are grouped into 5 categories namely normal,fusion,sveb,veb and unknown beats</li>
<li>the data samples used for training are [101,106, 108, 109, 112, 114, 115, 116, 118, 119, 122, 124, 201, 203, 205, 207, 208, 209, 215, 220, 223, 230]</li>
<li>the data samples used for testing are [100, 103, 105, 111, 113, 117, 121, 123, 200, 202, 210, 212, 213, 214, 219, 221, 222, 228, 231, 232, 233, 234]</li>
<li>hold out validation is used so that to identify how the neural network performs well for new dataset and restricted computation power </li>
 </ul>
 <p>jupyter notebook used for segmenting and grouping of ecg signal is "annotator.ipynb"</p>

<h2>training of model</h2>
<ul>
  <li>the dataset used for training of neural network has the following distribution</li>
  <li>the model trained was able to classify</li> 
  <li>the model was trained for 1 epoch and obtained ...............</li>
  <li>for one epoch with google gpu backend took 5 hours.</li>
  <li>so intended to downsample the number of normal samples</li>
</ul>
<p>for better identifying the abnormal beats
classification is done on 4 classes they are sveb,veb,usion ,normal
  two state architecture is to be used</p>



<h2>website</h2>
<p>the ecg-classifer website is built using css,javascript and html.the website takes the raw ecg signal or csv converted ecg signal as input.the file uploaded will be sent to backend where the classification happens.the backend is being built using flask.</p>
