--Eliminar los registros de la tabla
DELETE FROM programa_cursos;
DELETE FROM programa;

-- Insertar datos en la tabla Programa
INSERT INTO programa (ProCod, ProNom, ProNomEng, ProDip, ProDipEng, ProCodOsh, ProNumHor, ProNumCur, ProEstRegCod)
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


    (0000, 'NOmbre grado español', 'nombre grado ingles', 'Nombre de diploma español', 'Nombre de diploma en ingles', 'PRUEBA-OSHA', 0, 0, 0),
    (1001, 'Entrenador de Seguridad y Salud en el Trabajo del Instituto Osha', 'Occupational Safety and Health Trainer of Osha-Institute', 'Entrenador en  Seguridad y Salud en el  Trabajo de Osha ','Train the Trainer', 'TT-OSHA', 320, 0, 1),
    (1002, 'Entrenador de Trabajos Críticos', ' Critical Work Trainer', 'Supervisor Especialista en Trabajos Criticos', 'Critical Work Specialist Supervisor','TTC-OSHA', 320, 0, 1),
    (1010, 'Entrenador de Materiales Peligrosos OSHA', 'Trainer Hazmat Osha', 'Instructor en Gestión de Materiales Peligrosos', 'Instructor in Integral Management of Hazardous Materials', 'TH-OSHA', 320, 0, 1),
    (1016, 'Entrenador de Seguridad y salud ocupacional OSHA', 'Occupational Safety and Health Trainer OSHA', 'Gerencia en la Seguridad y Salud en el Trabajo Bajo normas OSHA', 'Management in Occupational Health and Safety Under OSHA Standards', 'TSSO-OSHA', 320, 0, 1),
    (1019, 'Entrenador de Trabajos en Altura Osha','Work at Height Trainer Osha', 'Supervisor de Trabajos en Altura basado a las normas OSHA-EE.UU', 'Supervisor of work at heights based on U.S. OSHA standards', 'TTA-OSHA', 320, 0, 1),
    (1020, "Entrenador de Seguridad y Salud en el Trabajo en la Industria de la Construcción", 'Workplace Safety and Health Trainer in the Construction Industry', 'Gerencia en Seguridad y Salud en el Trabajo en la Industria de la Construcción','Occupational Health and Safety Management in the Construction Industry', "TSSTIC-OSHA", 320, 0, 1),

    (1040, 'Supervisor en Seguridad y Salud en el Trabajo Osha', 'Work Health and Safety Supervisor Osha', 'Supervisión de Seguridad Efectiva basado en las normas OSHA-EE.UU', 'Effective Safety Supervision Based on U.S. OSHA Standards', 'SSST-OSHA', 360, 0, 1),

    (1060, 'Gerencia de la Seguridad en la Industria de la Construcción','Safety Managenent in the Construction Industry',  'Seguridad en la Industria de la Construcción Basado en las Normas OSHA-EE. UU', 'Safety in the Construction Industry Based on U.S. Osha Standards', 'GSIC-OSHA', 360, 0, 1),
    (1061, 'Gerente en Seguridad y Salud Laboral Osha', 'Labor Safety and Health Manager Osha ', '"Gerencia de Seguridad y salud en el trabajo bajo normas OSHA', 'Occupational Health and Safety Management under OSHA standards', "GSSL-OSHA",  360, 0, 1),

    (1080, 'Director de Prevención de Riesgos Laborales Osha', 'Director of Occupational Risk Prevention Osha', '', '', 'DPRL-OSHA', 360, 0, 1),
    
    (2010, 'Especialista en Seguridad y Salud en el Trabajo Osha', 'Specialist in Safety and Health at Work', 'Supervisor de Seguridad y Salud en el Trabajo', 'Occupational Health and Safety Supervisor', 'ESST-OSHA', 260, 0, 1),
    (2020, 'Especialista en Seguridad y Salud Ocupacional Osha', 'Ocupational Health and specialist Osha', 'Gerencia en la Seguridad y Salud Ocupacional Bajo normas Osha', 'Occupational Health and Safety Management ', 'ESSO-OSHA', 260, 0, 1),
    (2030, 'Especialista en Prevención de Riesgos Laborales Osha', 'Specialist in Labor risk Prevention Osha', 'Gestión de la Prevención de Riesgos Laborales bajo Normas OSHA','Occupational Risk Prevention Management', 'EPRL-OSHA', 260, 0, 1),
    (2040, 'Especialista Hazmat Nivel IV Osha', 'Hazmat IV Hazardous Materials Specialist', 'Instructor en Gestión de Materiales Peligrosos', 'Instructor in Integral Management of Hazardous Materials', 'EHIV-OSHA', 260, 0, 1),
    (2050, 'Especialista en Seguridad y Salud en la Construcción Osha', 'Specialist in Safety and Health in Construction Osha', 'Seguridad y Salud en la Construccion Osha', 'Construction Safety and Health Osha', 'ESSC-OSHA', 260, 0, 1),
    (2060, 'Especialista de Seguridad Hospitalaria de Atención Médica', 'Health Care Hospital Safety Specialist', '', '', 'ESHAM-OSHA', 260, 0, 1),
    (2070, 'Especialista en Seguridad en Laboratorios de Atención a la Salud Bajo Normas Osha', 'Safety Specialist in Health Care Laboratories Under Osha Regulations', 'Seguridad en el laboratorio de Atención Medico ', 'Safety in the Medical Care Laboratory ', 'ESLAS-OSHA', 260, 0, 1),
    (3010, 'Técnico de Seguridad y Salud Laboral en la Industria de la Construcción Osha', 'Occupational Health and Safety Thechinician in the Construction Industry Osha ', 'Seguridad en la Industria de la Construcción Basado en las Normas OSHA-EE. UU ', 'Construction Industry Safety Based on US OSHA Standards', 'TSSLIC-OSHA', 220, 0, 1);

    --(5000, 'Seguridad en la Operación de Equipos Pesados', 'SOEP', 220, 0, 1),