-- Insertar datos en la tabla Estado de registro
--INSERT INTO estado_registro(EstRegCod, EstRegNom)
INSERT INTO estado_registro("EstRegCod", "EstRegNom")
VALUES
    (1, 'Activo'),
    (0, 'Inactivo');


-- Insertar datos en la tabla Estado de examen
--INSERT INTO estado_examen(EstExaCod, EstExaNom)
INSERT INTO estado_examen("EstExaCod", "EstExaNom")
VALUES
    (1, 'Aprobado'),
    (0, 'Reprobado'),
    (2, 'Pendiente');