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
    (100, 'Introducción a OSHAcademy', 0, 0, 1),
    (105, 'Comunicación de peligros: Básico', 0, 0, 1),
    (107, 'Planes de Actuación de Emergencias y Prevención de Incendios', 0, 0, 1),
    (108, 'Equipo de Protección Personal: Básico', 0, 0, 1),
    (112, 'Introducción a la Supervisión de Seguridad', 0, 0, 1),
    (113, 'Introducción al Liderazgo en Seguridad', 0, 0, 1),
    (114, 'Superficies para caminar-trabajar y protección contra caídas', 0, 0, 1),
    (115, 'Seguridad Eléctrica para Empleados: Básica', 0, 0, 1),
    (116, 'Introducción a la responsabilidad en materia de seguridad', 0, 0, 1),
    (117, 'Introducción al reconocimiento de seguridad', 0, 0, 1),
    (121, 'Introducción a la Formación en Seguridad', 0, 0, 1),
    (122, 'Introducción a los controles de peligros', 0, 0, 1),
    (123, 'Introducción al análisis de riesgos laborales', 0, 0, 1),
    (138, 'Higiene del Trabajo y Prevención de Enfermedades', 0, 0, 1),
    (144, 'Introducción a OSHA', 0, 0, 1),
    (150, 'Peligros para la salud física en la construcción', 0, 0, 1),
    (151, 'Peligros biológicos para la salud en la construcción', 0, 0, 1),
    (152, 'Riesgos ergonómicos en la construcción', 0, 0, 1),
    (153, 'Riesgos ergonómicos en la industria general', 0, 0, 1),
    (154, 'Protección de máquinas: básica', 0, 0, 1),
    (155, 'Seguridad en la soldadura: básica', 0, 0, 1),
    (156, 'Seguridad en montacargas: Básico', 0, 0, 1),
    (157, 'Seguridad en la excavación: Básico', 0, 0, 1),
    (158, 'Seguridad en grúas: básica', 0, 0, 1),
    (159, 'Protección Auditiva: Básica', 0, 0, 1),
    (160, 'Seguridad de herramientas: básica', 0, 0, 1),
    (161, 'Higiene Industrial: Básica', 0, 0, 1),
    (162, 'Investigación de Accidentes: Básico', 0, 0, 1),
    (170, 'Atención sanitaria: Alergia al látex', 0, 0, 1),
    (171, 'Atención sanitaria: productos químicos peligrosos', 0, 0, 1),
    (172, 'Atención sanitaria: seguridad del glutaraldehído', 0, 0, 1),
    (173, 'Atención sanitaria: seguridad contra el mercurio', 0, 0, 1),
    (174, 'Atención sanitaria: seguridad contra incendios', 0, 0, 1),
    (175, 'Atención sanitaria: peligros biológicos', 0, 0, 1),
    (176, 'Atención sanitaria: estrés y violencia laboral', 0, 0, 1),
    (177, 'Sanidad: Seguridad Eléctrica', 0, 0, 1),
    (178, 'Atención sanitaria: Equipo de protección personal', 0, 0, 1),
    (179, 'Atención médica: Introducción a los peligros hospitalarios comunes', 0, 0, 1),
    (181, 'Atención médica: seguridad con objetos punzantes', 0, 0, 1),
    (182, 'Atención sanitaria: seguridad del óxido de etileno', 0, 0, 1),
    (183, 'Atención sanitaria: seguridad radiológica', 0, 0, 1),
    (500, 'EM 385-1-1 (Capítulos 1-6): 2014', 0, 0, 1),
    (501, 'EM 385-1-1 (Capítulos 7-13): 2014', 0, 0, 1),
    (502, 'EM 385-1-1 (Capítulos 14-19): 2014', 0, 0, 1),
    (503, 'EM 385-1-1 (Capítulos 20-26): 2014', 0, 0, 1),
    (504, 'EM 385-1-1 (Capítulos 27-34): 2014', 0, 0, 1),
    (600, 'Introducción a la Seguridad y Salud en el Trabajo', 0, 0, 1),
    (601, 'Fundamentos de Seguridad y Salud en el Trabajo', 0, 0, 1),
    (602, 'Seguridad contra el estrés por calor y frío', 0, 0, 1),
    (603, 'Seguridad en escaleras y escaleras', 0, 0, 1),
    (604, 'Seguridad en andamios', 0, 0, 1),
    (605, 'Seguridad en espacios confinados', 0, 0, 1),
    (610, 'Seguridad en la limpieza', 0, 0, 1),
    (611, 'Seguridad con pistolas de clavos', 0, 0, 1),
    (612, 'Seguridad del tráfico en la zona de trabajo', 0, 0, 1),
    (613, 'Seguridad de los trabajadores en restaurantes', 0, 0, 1),
    (614, 'Equipos de protección personal y salvamento', 0, 0, 1),
    (615, 'Seguridad Eléctrica: Peligros y Controles', 0, 0, 1),
    (617, 'Gestión de la Seguridad y la Salud: Industria General', 0, 0, 1),
    (618, 'Gestión de la Seguridad y la Salud: Construcción', 0, 0, 1),
    (619, 'Seguridad en el manejo de materiales', 0, 0, 1),
    (621, 'Control de energía peligrosa (bloqueo/etiquetado)', 0, 0, 1),
    (623, 'Prevención de lesiones ergonómicas', 0, 0, 1),
    (624, 'Atención médica: prevención de resbalones, tropezones y caídas', 0, 0, 1),
    (628, 'Atención médica: seguridad de la ecografía', 0, 0, 1),
    (629, 'Planificación de emergencias en el lugar de trabajo', 0, 0, 1),
    (630, 'Atención sanitaria: seguridad en farmacia', 0, 0, 1),
    (655, 'Patógenos transmitidos por la sangre: en el lugar de trabajo', 0, 0, 1),
    (656, 'Patógenos transmitidos por la sangre: en el ámbito sanitario', 0, 0, 1),
    (660, 'HAZWOPER para trabajadores de sitio general I', 0, 0, 1),
    (661, 'HAZWOPER para trabajadores de sitios generales II', 0, 0, 1),
    (662, 'HAZWOPER para trabajadores de sitios generales III', 0, 0, 1),
    (663, 'HAZWOPER para trabajadores generales del sitio IV', 0, 0, 1),
    (664, 'HAZWOPER para trabajadores generales del sitio V', 0, 0, 1),
    (665, 'HAZWOPER para trabajadores de sitio general VI', 0, 0, 1),
    (666, 'HAZWOPER para trabajadores de sitios generales VII', 0, 0, 1),
    (667, 'HAZWOPER para trabajadores de sitios generales VIII', 0, 0, 1),
    (668, 'HAZWOPER para trabajadores generales del sitio IX', 0, 0, 1),
    (669, 'HAZWOPER para trabajadores generales del sitio X', 0, 0, 1),
    (700, 'Introducción a la Gestión de la Seguridad', 0, 0, 1),
    (701, 'Operaciones efectivas del Comité de Seguridad', 0, 0, 1),
    (702, 'Investigación efectiva de accidentes', 0, 0, 1),
    (703, 'Introducción a la Formación en SST', 0, 0, 1),
    (704, 'Análisis y Control de Peligros', 0, 0, 1),
    (705, 'Programa de comunicación de peligros', 0, 0, 1),
    (706, 'Realización de un análisis de riesgos laborales (JHA)', 0, 0, 1),
    (707, 'Reuniones efectivas del Comité de SST', 0, 0, 1),
    (708, 'Conceptos básicos del mantenimiento de registros de OSHA', 0, 0, 1),
    (709, 'Equipo de Protección Personal', 0, 0, 1),
    (710, 'Programa de control de energía (bloqueo/etiquetado)', 0, 0, 1),
    (711, 'Introducción a la Ergonomía', 0, 0, 1),
    (712, 'Supervisión y Liderazgo de Seguridad', 0, 0, 1),
    (713, 'Programa de Espacios Confinados', 0, 0, 1),
    (714, 'Programa de protección contra caídas', 0, 0, 1),
    (715, 'Seguridad Eléctrica: para Técnicos y Supervisores', 0, 0, 1),
    (716, 'Evaluación del Sistema de Gestión de Seguridad', 0, 0, 1),
    (717, 'Planes de Acción de Emergencia', 0, 0, 1),
    (718, 'Planes de Prevención de Incendios', 0, 0, 1),
    (719, 'Gestión de Seguridad de Flotas', 0, 0, 1),
    (720, 'Prevención de la violencia en el lugar de trabajo', 0, 0, 1),
    (721, 'Desarrollo de Capacitación en SST', 0, 0, 1),
    (722, 'Gestión del Programa de Ergonomía', 0, 0, 1),
    (723, 'Realización de capacitación en SST', 0, 0, 1),
    (725, 'Gestión del Programa de Seguridad de Montacargas', 0, 0, 1),
    (726, 'Introducción a la protección de máquinas', 0, 0, 1),
    (736, 'Introducción a la Gestión de la Seguridad de Procesos (PSM)', 0, 0, 1),
    (744, 'Trabajar con OSHA', 0, 0, 1),
    (750, 'Introducción a la Higiene Industrial', 0, 0, 1),
    (751, 'Gestión del Programa de Conservación de la Audición', 0, 0, 1),
    (755, 'Patógenos transmitidos por la sangre: gestión del programa', 0, 0, 1),
    (757, 'Seguridad de laboratorio', 0, 0, 1),
    (776, 'Prevención de la violencia laboral: en el sector sanitario', 0, 0, 1),
    (800, 'Introducción a la Gestión de la Seguridad en la Construcción', 0, 0, 1),
    (802, 'Seguridad en zanjas y excavaciones', 0, 0, 1),
    (803, 'Gestión del Programa de Seguridad de Andamios', 0, 0, 1),
    (804, 'Montaje e inspección segura de andamios', 0, 0, 1),
    (805, 'Protección contra caídas en la construcción: elementos para 29 CFR 1926.500-503', 0, 0, 1),
    (806, 'Enfoque cuatro: Peligros de caídas', 0, 0, 1),
    (807, 'Enfoque cuatro: Atrapados entre peligros', 0, 0, 1),
    (808, 'Enfoque cuatro: Peligros de ser golpeado', 0, 0, 1),
    (809, 'Enfoque cuatro: Peligros de electrocución', 0, 0, 1),
    (810, 'Seguridad con herramientas manuales y eléctricas', 0, 0, 1),
    (812, 'Enfoque cuatro de OSHA', 0, 0, 1),
    (813, 'Seguridad en el lugar de trabajo de construcción', 0, 0, 1),
    (814, 'Seguridad de Equipo Pesado', 0, 0, 1),
    (815, 'Seguridad en la demolición', 0, 0, 1),
    (816, 'Seguridad en espacios confinados en la construcción', 0, 0, 1),
    (820, 'Seguridad de Grúas y Cabrias I', 0, 0, 1),
    (821, 'Seguridad en Grúas y Cabrias II', 0, 0, 1),
    (833, 'Desarrollo de un sistema de gestión de seguridad en la construcción', 0, 0, 1),
    (850, 'Riesgos para la Salud en la Construcción', 0, 0, 1),
    (900, 'Gestión de la Seguridad del Petróleo y Gas', 0, 0, 1),
    (901, 'Concientización sobre los peligros del petróleo y el gas', 0, 0, 1),
    (902, 'Preparación del sitio del pozo y seguridad de la perforación', 0, 0, 1),
    (903, 'Seguridad en la finalización y el mantenimiento del sitio del pozo', 0, 0, 1),
    (904, 'Inspección de pozos de petróleo y gas ', 0, 0, 1),
    (906, 'Limpieza de derrames de petróleo', 0, 0, 1),
    (907, 'Introducción a SEMS II: 30 CFR 250.1900-1933', 0, 0, 1),
    (908, 'Seguridad del petróleo y el gas costa afuera I', 0, 0, 1),
    (909, 'Seguridad del petróleo y el gas costa afuera I', 0, 0, 1);

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
