# Sistema-de-Gesti-n-de-Cl-nicas-Veterinarias-No-Lista-15
Sistema de Gestión de Clínicas Veterinarias de acuerdo con los modelos de la clase




 Sistema de Gestión de Clínicas Veterinarias

Entidad	Atributos	Tipo de Campo
Mascota	id_mascota, nombre_mascota, especie, raza, fecha_nacimiento, genero, peso_kg, id_propietario, chip_identificacion, color, esterilizado	INT, VARCHAR(100), VARCHAR(50), VARCHAR(50), DATE, CHAR(1), DECIMAL(5,2), INT, VARCHAR(50), VARCHAR(50), BOOLEAN
Propietario	id_propietario, nombre, apellido, direccion, telefono, email, fecha_registro, dni, ocupacion	INT, VARCHAR(100), VARCHAR(100), VARCHAR(255), VARCHAR(20), VARCHAR(100), DATE, VARCHAR(20), VARCHAR(100)
Veterinario	id_veterinario, nombre, apellido, especialidad, telefono, email, licencia_veterinaria, fecha_contratacion, salario	INT, VARCHAR(100), VARCHAR(100), VARCHAR(100), VARCHAR(20), VARCHAR(100), VARCHAR(50), DATE, DECIMAL(10,2)
Consulta	id_consulta, id_mascota, id_veterinario, fecha_consulta, motivo_consulta, diagnostico, tratamiento, peso_mascota_consulta, observaciones	INT, INT, INT, DATETIME, TEXT, TEXT, TEXT, DECIMAL(5,2), TEXT
Vacuna	id_vacuna, nombre_vacuna, descripcion, laboratorio, fecha_vencimiento_lote, tipo_enfermedad	INT, VARCHAR(100), TEXT, VARCHAR(100), DATE, VARCHAR(100)
Historial_Vacunacion	id_historial_vac, id_mascota, id_vacuna, fecha_aplicacion, fecha_proxima_dosis, id_veterinario_aplico, numero_lote, comentarios	INT, INT, INT, DATE, DATE, INT, VARCHAR(50), TEXT
Factura_Veterinaria	id_factura, id_propietario, fecha_emision, total_factura, estado_pago, metodo_pago, id_consulta_asociada, fecha_vencimiento	INT, INT, DATE, DECIMAL(10,2), VARCHAR(50), VARCHAR(50), INT, DATE
Relaciones:

Mascota (id_propietario) -> Propietario (id_propietario) (Muchos a Uno)
Consulta (id_mascota) -> Mascota (id_mascota) (Muchos a Uno)
Consulta (id_veterinario) -> Veterinario (id_veterinario) (Muchos a Uno)
Historial_Vacunacion (id_mascota) -> Mascota (id_mascota) (Muchos a Uno)
Historial_Vacunacion (id_vacuna) -> Vacuna (id_vacuna) (Muchos a Uno)
Historial_Vacunacion (id_veterinario_aplico) -> Veterinario (id_veterinario) (Muchos a Uno)
Factura_Veterinaria (id_propietario) -> Propietario (id_propietario) (Muchos a Uno)
Factura_Veterinaria (id_consulta_asociada) -> Consulta (id_consulta) (Muchos a Uno)
