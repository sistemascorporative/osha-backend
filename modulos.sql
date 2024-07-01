-- Insertar datos en la tabla puente programa_cursos
INSERT INTO programa_cursos (programa_id, curso_id) VALUES
(1, 1),
(1, 2),
(2, 1);

-- Insertar datos en la tabla Modulo
INSERT INTO modulo (ModCod, ModNom, ModCurCod, ModEstRegCod)
VALUES
    (1, 'Capacitación de la academia OSHA', 100, 1),
    (2, 'Cursos de formación', 100, 1),
    (3, 'Panel de estudiantes', 100, 1),
    (4, 'Documentos oficiales', 100, 1),

    (5, 'Controles y etiquetado', 105, 1),
    (6, 'Hojas de datos de seguridad (SDS)', 105, 1),

    (7, 'Introducción a OSHA', 107, 1),
    (8, 'Conciencia de peligros', 107, 1),

    (9, 'Requisitos generales de PPE y tipos de PPE', 108, 1),
    (10, 'Tipos de EPP (continuación)', 108, 1),
    
    (11, 'La primera responsabilidad "STAR"', 112, 1),
    (12, 'Más responsabilidades "STAR"', 112, 1),

    (13, '¿Qué es el liderazgo?', 113, 1),
    (14, 'Liderazgo en acción', 113, 1),

    (15, 'Peligros en la superficie que causan caídas', 114, 1),
    (16, 'Protección contra caídas', 114, 1),

    (17, 'Peligros electricos', 115, 1),
    (18, 'Medidas de protección', 115, 1),

    (19, 'Estándares, recursos y medición', 116, 1),
    (20, 'Consecuencias y evaluación', 116, 1),

    (21, '¿Qué es el reconocimiento efectivo?', 117, 1),
    (22, 'Reglas e ideas', 117, 1),

    (23, '¿Qué es la educación en seguridad?', 121, 1),
    (24, 'Cualificaciones del formador y desarrollo de cursos', 121, 1),

    (25, 'Identificación de peligros', 122, 1),
    (26, 'Controlar los peligros', 122, 1),

    (27, 'Pasos de escritura: determinación de peligros', 123, 1),
    (28, 'Medidas preventivas-Procedimiento de trabajo seguro', 123, 1),

    (29, 'Higiene y limpieza', 138, 1),
    (30, 'Enfermedades contagiosas', 138, 1),
    (31, 'La prevención de enfermedades', 138, 1),

    (32, 'Acerca de OSHA', 144, 1),
    (33, 'Derechos y responsabilidades', 144, 1),

    (34, 'Factores de riesgo y peligros', 150, 1),
    (35, 'Peligros ambientales y ergonómicos', 150, 1),

    (36, 'Factores de riesgo biológico', 151, 1),
    (37, 'Animales e insectos infecciosos', 151, 1),

    (38, 'Factores de riesgo ergonómicos', 152, 1),
    (39, 'Soluciones a los riesgos ergonómicos', 152, 1),

    (40, 'Identificación de peligros ergonómicos', 153, 1),
    (41, 'Controlar los riesgos ergonómicos', 153, 1),

    (42, 'Peligros de las piezas móviles', 154, 1),
    (43, 'Métodos de protección de máquinas', 154, 1),

    (44, 'Procesos y riesgos de soldadura', 155, 1),
    (45, 'Prácticas de trabajo seguras en soldadura y EPP', 155, 1),

    (46, 'El montacargas', 156, 1),
    (47, 'Operar el montacargas', 156, 1),

    (48, 'Los peligros', 157, 1),
    (49, 'Sistemas de protección', 157, 1),

    (50, 'Deberes, responsabilidades e inspecciones', 158, 1),
    (51, 'Operaciones, Señalización e Izado', 158, 1),

    (52, 'Ruido y pérdida auditiva', 159, 1),
    (53, 'Controles de peligros y medidas de protección', 159, 1),

    (54, 'Seguridad con herramientas manuales', 160, 1),
    (55, 'Seguridad de las herramientas eléctricas', 160, 1),

    (56, 'Higienistas industriales, calidad del aire y productos químicos peligrosos', 161, 1),
    (57, 'Peligros biológicos y físicos para la salud', 161, 1),

    (58, 'Recopilando los hechos', 162, 1),
    (59, 'Analizando los hechos', 162, 1),

    (60, 'Prevención de la alergia al látex', 170, 1),

    (61, 'Productos químicos peligrosos en la atención sanitaria', 171, 1),

    (62, 'Peligros del glutaraldehído', 172, 1),

    (63, 'Peligros de mercurio', 173, 1),

    (64, 'Riesgos de incendio', 174, 1),

    (65, 'Legionelosis', 175, 1),
    (66, 'MRSA en la atención sanitaria', 175, 1),
    (67, 'Tuberculosis', 175, 1),

    (68, 'Violencia en la atención sanitaria', 176, 1),
    (69, 'Estrés en la atención sanitaria', 176, 1),

    (70, 'Seguridad ELECTRICA', 177, 1),

    (71, 'Equipo de protección personal', 178, 1),

    (72, 'Ubicaciones de peligro comunes', 179, 1),
    (73, 'Tipos de peligro', 179, 1),

    (74, 'Seguridad de objetos punzantes y contenedores', 181, 1),

    (75, 'Óxido de etileno', 182, 1),

    (76, 'Radiación en la atención sanitaria', 183, 1),

    (77, 'Gestión de programas y proceso AHA', 500, 1),
    (78, 'Saneamiento', 500, 1),
    (79, 'Requisitos médicos y de primeros auxilios', 500, 1),
    (90, 'Instalaciones temporales', 500, 1),
    (91, 'Equipo de seguridad y protección personal', 500, 1),
    (92, 'Agentes y entornos peligrosos o tóxicos', 500, 1),

    (93, 'Encendiendo', 501, 1),
    (94, 'Señales de prevención de accidentes', 501, 1),
    (95, 'Prevención y protección contra incendios', 501, 1),
    (96, 'Soldadura y Corte', 501, 1),
    (97, 'Eléctrico', 501, 1),
    (98, 'Control de Energía Peligrosa', 501, 1),
    (99, 'Herramientas manuales y eléctricas', 501, 1),

    (100, 'Manejo, almacenamiento y eliminación de materiales', 502, 1),
    (101, 'Aparejo', 502, 1),
    (102, 'Equipos de manipulación de carga', 502, 1),
    (103, 'Transportadores', 502, 1),
    (104, 'Vehículos, Maquinaria y Equipo', 502, 1),
    (105, 'Plantas Flotantes y Actividades Marinas', 502, 1),

    (106, 'Equipos y sistemas presurizados', 503, 1),
    (107, 'Protección contra caídas', 503, 1),
    (108, 'Plataformas de trabajo y andamios', 503, 1),
    (109, 'Demolición, renovación y reocupación', 503, 1),
    (110, 'Acceso seguro', 503, 1),
    (111, 'Excavaciones y zanjas', 503, 1),
    (112, 'Construcción subterránea', 503, 1),

    (113, 'Concreto, mampostería, techado y construcción residencial', 504, 1),
    (114, 'Erección de acero', 504, 1),
    (115, 'Voladura', 504, 1),
    (116, 'Operaciones de buceo', 504, 1),
    (117, 'Mantenimiento y remoción de árboles', 504, 1),
    (118, 'Operaciones de aeródromos y aeronaves', 504, 1),
    (119, 'Operaciones de residuos peligrosos y respuesta a emergencias (HAZWOPER)', 504, 1),
    (120, 'Entrada a espacios confinados', 504, 1),

    (121, 'Introducción a OSHA', 600, 1),
    (122, 'Conciencia de peligros', 600, 1),
    (123, 'Controles de peligros', 600, 1),
    (124, 'Equipo de Protección Personal (EPP)', 600, 1),
    (125, 'Planes de acción de emergencia (PAE)', 600, 1),
    (126, 'Planes de Prevención de Incendios (FPP)', 600, 1),

    (127, 'Comunicaciones de peligro', 601, 1),
    (128, 'Líquidos inflamables y combustibles', 601, 1),
    (129, 'Resbalones, tropezones y caídas', 601, 1),
    (130, 'Prevención de la violencia en el lugar de trabajo', 601, 1),
    (131, 'Programas de seguridad y salud', 601, 1),

    (132, 'Estrés por calor y seguridad', 602, 1),
    (133, 'Estrés por frío y seguridad', 602, 1),

    (134, 'Tipos de escaleras', 603, 1),
    (135, 'Requisitos generales: escaleras', 603, 1),
    (136, 'Requisitos generales: escaleras(gradas)', 603, 1),

    (137, 'Conceptos básicos de andamios', 604, 1),
    (138, 'Andamios soportados', 604, 1),
    (139, 'Andamios suspendidos', 604, 1),
    
    (140, 'Conceptos básicos de espacios confinados', 605, 1),
    (141, 'Equipo de entrada a espacios confinados', 605, 1),
    (142, 'Rescates en espacios confinados', 605, 1),
    (143, 'Requisitos de capacitación en espacios confinados', 605, 1),
    (144, 'Espacios confinados en la construcción', 605, 1),

    (145, 'Los productos químicos de limpieza y su salud', 610, 1),
    (146, 'Materiales contaminados', 610, 1),
    (147, 'Prevención de lesiones', 610, 1),

    (148, 'Conceptos básicos de la pistola de clavos', 611, 1),
    (149, 'Entrenamiento con pistola de clavos', 611, 1),
    (150, 'Lesiones por pistola de clavos y otros peligros', 611, 1),
    
    (151, 'Riesgos viales en la zona de trabajo', 1, 1),
    (152, '', 1, 1),
    (153, '', 1, 1),
    (154, '', 1, 1),
    (155, '', 1, 1),
    (156, '', 1, 1),
    (157, '', 1, 1),
    (158, '', 1, 1),
    (159, '', 1, 1),
    (1610, '', 1, 1),
    (161, '', 1, 1),
    (162, '', 1, 1),
    (163, '', 1, 1),
    (164, '', 1, 1),
    (165, '', 1, 1),
    (166, '', 1, 1),
    (167, '', 1, 1),
    (168, '', 1, 1),
    (169, '', 1, 1),
    (170, '', 1, 1),
    (171, '', 1, 1),
    (172, '', 1, 1),
    (173, '', 1, 1),
    (174, '', 1, 1),
    (175, '', 1, 1),
    (176, '', 1, 1),
    (177, '', 1, 1),
    (178, '', 1, 1),
    (179, '', 1, 1),
    (180, '', 1, 1),
    (181, '', 1, 1),
    (182, '', 1, 1),
    (183, '', 1, 1),
    (184, '', 1, 1),
    (185, '', 1, 1),
    (186, '', 1, 1),
    (187, '', 1, 1),
    (188, '', 1, 1),
    (189, '', 1, 1),
    (190, '', 1, 1),
    (191, '', 1, 1),
    (192, '', 1, 1),
    (193, '', 1, 1),
    (194, '', 1, 1),
    (195, '', 1, 1),
    (196, '', 1, 1),
    (197, '', 1, 1),
    (198, '', 1, 1),
    (199, '', 1, 1),
    (200, '', 1, 1),
    (201, '', 1, 1),
    (202, '', 1, 1),
    (203, '', 1, 1),
    (204, '', 1, 1),
    (205, '', 1, 1),
    (206, '', 1, 1),
    (207, '', 1, 1),
    (208, '', 1, 1),
    (209, '', 1, 1);


-- Insertar datos en la tabla
INSERT INTO ()
VALUES
    (),
    ();


-- Insertar datos en otras tablas de manera similar