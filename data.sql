-- Insertar datos en la tabla Estado de registro
INSERT INTO estado_registro(EstRegCod, EstRegNom)
VALUES
    (1, 'Activo'),
    (2, 'Inactivo');

-- Insertar datos en la tabla Programa
INSERT INTO programa (ProCod, ProNom, ProCodOsh, ProNumCur, ProEstRegCod)
VALUES 
    (1, 'Especialista en Seguridad y Salud en el Trabajo Osha', 'ESST-OSHA', 0, 1),
    (2, 'Supervisor en Seguridad y Salud en el Trabajo Osha', 'SSST-OSHA', 0, 1),

    (3, 'Especialista en Seguridad y Salud Ocupacional Osha', 'ESSO-OSHA', 0, 1),
    (4, 'Trainer de Seguridad y Salud Ocupacional Osha', 'TSSO-OSHA', 0, 1),
    (5, 'Gerencia en Seguridad y Salud Ocupacional Osha', 'GSSO-OSHA', 0, 1),

    (6, 'Director de Prevención de Riesgos Laborales Osha', 'DPRL-OSHA', 0, 1),
    (7, 'Especialista en Prevención de Riesgos Laborales Osha', 'EPRL-OSHA', 0, 1),

    (8, 'Gerencia de la Seguridad en la Industria de la Construcción', 'GSSTIC', 0, 1),
    (9, 'Técnico de Seguridad y Salud Laboral en la Industria de la Construcción Osha', 'TSSLIC-OSHA', 0, 1),
    (10, 'Especialista en Seguridad y Salud en la Construcción', '', 0, 1),

    (11, 'Entrenador de Trabajos en Altura', 'ETA-OSHA', 0, 1),
    (12, 'Trabajos en Altura para Techos', '', 0, 1),
    (13, 'Trainer de Trabajos en Altura Osha', 'TTA-OSHA', 0, 1),

    (14, 'Train The Trainer Osha', 'TT-OSHA', 0, 1),
    (15, 'Trainer Hazmat Osha', 'TH-OSHA', 0, 1),
    (16, 'Especialista Hazmat Nivel IV osha', 'HIV-OSHA', 0, 1);

    (17, 'Trainer de Trabajos Críticos', 'TCW-OSHA', 0, 1),
    (18, 'Gestión de Seguridad de Flotas', '', 0, 1),
    (19, 'Seguridad en la Operación de Equipos Pesados', '', 0, 1),
    (20, 'Especialista en Seguridad hospitalaria de atención médica', '', 0, 1),
    (21, 'Seguridad en el laboratorio de atención médica', '', 0, 1),
    (22, 'Especialista en Seguridad en Laboratorios de Atención a la Salud Bajo Normas Osha', 'ESLAT', 0, 1);

-- Insertar datos en la tabla Curso
INSERT INTO curso (CurCod, CurNom, CurNumMod, CurProCod, CurEstRegCod)
VALUES
    (1, 'Nombre del Curso 1', 4, 1, 1),
    (2, 'Nombre del Curso 2', 3, 1, 2);

-- Insertar datos en la tabla Modulo
INSERT INTO modulo (ModCod, ModNom, ModCurCod, ModEstRegCod)
VALUES
    (1, 'Nombre del Módulo 1', 1, 1),
    (2, 'Nombre del Módulo 2', 1, 1),
    (3, 'Nombre del Módulo 3', 1, 1),
    (4, 'Nombre del Módulo 4', 1, 1),
    (5, 'Nombre del Módulo 1', 2, 1),
    (6, 'Nombre del Módulo 2', 2, 1),
    (7, 'Nombre del Módulo 3', 2, 1);

-- Insertar datos en la tabla
INSERT INTO ()
VALUES
    (),
    ();


-- Insertar datos en otras tablas de manera similar
