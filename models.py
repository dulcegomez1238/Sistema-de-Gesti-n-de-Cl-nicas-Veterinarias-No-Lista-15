from django.db import models


class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    fecha_registro = models.DateField()
    dni = models.CharField(max_length=20)
    ocupacion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Mascota(models.Model):
    nombre_mascota = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1)
    peso_kg = models.DecimalField(max_digits=5, decimal_places=2)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    chip_identificacion = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    esterilizado = models.BooleanField()

    def __str__(self):
        return self.nombre_mascota


class Veterinario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    licencia_veterinaria = models.CharField(max_length=50)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Consulta(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    fecha_consulta = models.DateTimeField()
    motivo_consulta = models.TextField()
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    peso_mascota_consulta = models.DecimalField(max_digits=5, decimal_places=2)
    observaciones = models.TextField()

    def __str__(self):
        return f"Consulta {self.id} - {self.mascota.nombre_mascota}"


class Vacuna(models.Model):
    nombre_vacuna = models.CharField(max_length=100)
    descripcion = models.TextField()
    laboratorio = models.CharField(max_length=100)
    fecha_vencimiento_lote = models.DateField()
    tipo_enfermedad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_vacuna


class HistorialVacunacion(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    vacuna = models.ForeignKey(Vacuna, on_delete=models.CASCADE)
    fecha_aplicacion = models.DateField()
    fecha_proxima_dosis = models.DateField()
    veterinario_aplico = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    numero_lote = models.CharField(max_length=50)
    comentarios = models.TextField()

    def __str__(self):
        return f"Vacunación {self.id} - {self.mascota.nombre_mascota}"


class FacturaVeterinaria(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    fecha_emision = models.DateField()
    total_factura = models.DecimalField(max_digits=10, decimal_places=2)
    estado_pago = models.CharField(max_length=50)
    metodo_pago = models.CharField(max_length=50)
    consulta_asociada = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return f"Factura {self.id} - {self.propietario.nombre}"

