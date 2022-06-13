import numpy as np
from sklearn.metrics import multilabel_confusion_matrix

label_aktual = ["abimanyu", "anoman", "arjuna", "abimanyu", "anoman", "arjuna", "abimanyu", "anoman", "arjuna"]
label_prediksi = ["abimanyu", "arjuna", "arjuna", "abimanyu", "anoman", "anoman", "abimanyu", "anoman", "arjuna"]

hasil = multilabel_confusion_matrix(label_aktual, label_prediksi, labels=["abimanyu", "anoman", "arjuna"])
print(hasil)