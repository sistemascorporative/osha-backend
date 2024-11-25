--Eliminar los registros de la tabla
DELETE FROM programa_cursos;
DELETE FROM programa;

-- Insertar datos en la tabla Programa
INSERT INTO programa (ProCod, ProNom, ProCodOsh, ProNumHor, ProNumCur, ProEstRegCod)
VALUES
    --(1001, 'Train The Trainer Osha', 'TT-OSHA', 320, 26, 1),
    --(1002, 'Trainer de Trabajos Críticos', 'TTC-OSHA', 320, 0, 1),
    --(1010, 'Trainer Hazmat Osha', 'TH-OSHA', 320, 0, 1),
    --(1015, 'Trainer de Espacios Confinados Osha', 'TEC-OSHA', 320, 0, 1),
    --(1016, 'Trainer de Seguridad y Salud Ocupacional Osha', 'TSSO-OSHA', 320, 33, 1),
    --(1019, 'Trainer de Trabajos en Altura Osha', 'TTA-OSHA', 320, 0, 1),
    --(1060, "Trainer de Seguridad y Salud en el Trabajo en la Industria de la Construcción", "TSSTIC-OSHA", 320, 0, 1),
    --(1051, "Gerente de Seguridad y Salud Laboral Osha", "GSSL-OSHA", 360, 0, 1),
    --(1052, 'Gerencia de la Seguridad en la Industria de la Construcción', 'GSIC-OSHA', 360, 0, 1),
    --(1071, 'Director de Prevención de Riesgos Laborales Osha', 'DPRL-OSHA', 320, 0, 1),
    --(2010, 'Especialista en Seguridad y Salud en el Trabajo Osha', 'ESST-OSHA', 260, 0, 1),
    --(2020, 'Especialista en Seguridad y Salud Ocupacional Osha', 'ESSO-OSHA', 260, 32, 1),
    --(2030, 'Especialista en Prevención de Riesgos Laborales Osha', 'EPRL-OSHA', 260, 0, 1),
    --(2040, 'Técnico de Seguridad y Salud Laboral en la Industria de la Construcción Osha', 'TSSLIC-OSHA', 220, 0, 1),
    --(2056, 'Especialista Hazmat Nivel IV Osha', 'EHIV-OSHA', 260, 0, 1);


    (0000, 'Prueba', 'PRUEBA-OSHA', 0, 0, 0),
    (1001, 'Train The Trainer Osha', 'TT-OSHA', 320, 0, 1),
    (1002, 'Trainer de Trabajos Críticos', 'TTC-OSHA', 320, 0, 1),
    (1010, 'Trainer Hazmat Osha', 'TH-OSHA', 320, 0, 1),
    (1016, 'Trainer de Seguridad y Salud Ocupacional Osha', 'TSSO-OSHA', 320, 0, 1),
    (1019, 'Trainer de Trabajos en Altura Osha', 'TTA-OSHA', 320, 0, 1),
    (1020, "Trainer de Seguridad y Salud en el Trabajo en la Industria de la Construcción", "TSSTIC-OSHA", 320, 0, 1),

    (1040, 'Supervisor en Seguridad y Salud en el Trabajo Osha', 'SSST-OSHA', 360, 0, 1),

    (1060, 'Gerencia de la Seguridad en la Industria de la Construcción', 'GSIC-OSHA', 360, 0, 1),
    (1061, 'Gerencia en Seguridad y Salud Ocupacional Osha', "GSSO-OSHA", 360, 0, 1),

    (1080, 'Director de Prevención de Riesgos Laborales Osha', 'DPRL-OSHA', 360, 0, 1),
    
    (2010, 'Especialista en Seguridad y Salud en el Trabajo Osha', 'ESST-OSHA', 260, 0, 1),
    (2020, 'Especialista en Seguridad y Salud Ocupacional Osha', 'ESSO-OSHA', 260, 0, 1),
    (2030, 'Especialista en Prevención de Riesgos Laborales Osha', 'EPRL-OSHA', 260, 0, 1),
    (2040, 'Especialista Hazmat Nivel IV Osha', 'EHIV-OSHA', 260, 0, 1),
    (2050, 'Especialista en Seguridad y Salud en la Construcción Osha', 'ESSC-OSHA', 260, 0, 1),
    (2060, 'Especialista en Seguridad Hospitalaria de Atención Médica', 'ESHAM-OSHA', 260, 0, 1),

    (3010, 'Técnico de Seguridad y Salud Laboral en la Industria de la Construcción Osha', 'TSSLIC-OSHA', 220, 0, 1),

    (5000, 'Seguridad en la Operación de Equipos Pesados', 'SOEP', 220, 0, 1),
    (5001, 'Trabajos en Altura para Techos', 'TAPT', 220, 0, 1),
    (5010, 'Seguridad en el Laboratorio de Atención Médica', 'SLAM', 220, 0, 1);

