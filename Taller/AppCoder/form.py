from django import forms

class ServicioFormulario(forms.Form):

  nombre = forms.CharField(max_length=20)
  apellido = forms.CharField(max_length=20)
  marca_de_carro = forms.CharField(max_length=20)
  modelo = forms.CharField(max_length=20)
  placa= forms.UUIDField(primary_key=True) 
  email= forms.EmailField()
  descripcionRev= forms.TextField()

class Estado_revisioFormulario(forms.Form):

  placa = forms.IntegerField()
  entrada = forms.DateTimeField()
  tipo_reparacion = forms.CharField(max_length=20)

  LOAN_STATUS = (('m', 'Maintenance'),('o', 'On loan'),('a', 'Available'),('r', 'Ready')),

  
  
  status = forms.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m')