from django import forms

class CSVUploadForm(forms.Form):
    archivo_csv = forms.FileField(label="Subir archivo CSV")
