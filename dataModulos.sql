--Eliminar los registros de la tabla
DELETE FROM modulo;
--DELETE FROM programa_cursos;
--DELETE FROM curso;

-- Insertar datos en la tabla Modulo
-- Para el Id del ModCod primero va el
-- id del curso XXXX
-- y el numero del modulo Y
-- FOMATO: XXXY
INSERT INTO modulo (ModCod, ModNom, ModCurCod, ModEstRegCod)
VALUES
    (10501, 'Controles y etiquetado', 105, 1),
    (10502, 'Hojas de datos de seguridad (SDS)', 105, 1),

    (10701, 'Planes de actuación en caso de emergencia (EAP)', 107, 1),
    (10702, 'Planes de prevención de incendios (PPI)', 107, 1),

    (10801, 'Requisitos generales de EPP y tipos de EPP', 108, 1),
    (10802, 'Tipos de EPP o EPI (continuación)', 108, 1),
    
    (11201, 'La primera responsabilidad "STAR"', 112, 1),
    (11202, 'Más responsabilidades "STAR"', 112, 1),

    (11301, '¿Qué es el liderazgo?', 113, 1),
    (11302, 'Liderazgo en acción', 113, 1),

    (11401, 'Riesgos de superficie que causan caídas', 114, 1),
    (11402, 'Protección contra caídas', 114, 1),

    (11501, 'Peligros electricos', 115, 1),
    (11502, 'Medidas de protección', 115, 1),

    (11601, 'Normas, recursos y medición', 116, 1),
    (11602, 'Consecuencias y evaluación', 116, 1),

    (11701, '¿Qué es el reconocimiento efectivo?', 117, 1),
    (11702, 'Reglas e ideas', 117, 1),

    (11901, 'Peligros de la conducción', 119, 1),
    (11902, 'Prácticas de conducción segura', 119, 1),

    (12001, 'Peligros', 120, 1),
    (12002, 'Soluciones', 120, 1),

    (12101, '¿Qué es la educación en seguridad?', 121, 1),
    (12102, 'Cualificaciones de formador y desarrollo de cursos', 121, 1),

    (12201, 'Identificación de riesgos', 122, 1),
    (12202, 'Control de riesgos', 122, 1),

    (12301, 'Pasos de la redacción: determinación de los peligros', 123, 1),
    (12302, 'Medidas preventivas-Procedimiento de trabajo seguro', 123, 1),

    (13801, 'Higiene y limpieza', 138, 1),
    (13802, 'Enfermedades contagiosas', 138, 1),
    (13803, 'La prevención de enfermedades', 138, 1),

    (13901, 'Procedimientos de limpieza y desinfección', 139, 1),

    (14401, 'Acerca de OSHA', 144, 1),
    (14402, 'Derechos y responsabilidades', 144, 1),

    (15001, 'Factores de riesgo y peligros', 150, 1),
    (15002, 'Riesgos medioambientales y ergonómicos', 150, 1),

    (15101, 'Factores de riesgo biológico', 151, 1),
    (15102, 'Animales e insectos infecciosos', 151, 1),

    (15201, 'Factores de riesgo ergonómicos', 152, 1),
    (15202, 'Soluciones a los riesgos ergonómicos', 152, 1),

    (15301, 'Identificación de riesgos ergonómicos', 153, 1),
    (15302, 'Control de los riesgos ergonómicos', 153, 1),

    (15401, 'Peligros de las piezas móviles', 154, 1),
    (15402, 'Métodos de protección de máquinas', 154, 1),

    (15501, 'Procesos y riesgos de soldadura', 155, 1),
    (15502, 'Prácticas de trabajo seguras en soldadura y EPP', 155, 1),

    (15601, 'El montacargas', 156, 1),
    (15602, 'Operar el montacargas', 156, 1),

    (15701, 'Los peligros', 157, 1),
    (15702, 'Sistemas de protección', 157, 1),

    (15801, 'Obligaciones, responsabilidades e inspecciones', 158, 1),
    (15802, 'Operaciones, señalización y elevación', 158, 1),

    (15901, 'Ruido y pérdida auditiva', 159, 1),
    (15902, 'Controles de riesgos y medidas de protección', 159, 1),

    (16101, 'Higienistas industriales, calidad del aire y sustancias químicas peligrosas', 161, 1),
    (16102, 'Riesgos biológicos y físicos para la salud', 161, 1),

    (16201, 'Recopilando los datos', 162, 1),
    (16202, 'Analizando los hechos', 162, 1),

    (17001, 'Prevención de la alergia al látex', 170, 1),

    (17101, 'Productos químicos peligrosos en la atención sanitaria', 171, 1),

    (17201, 'Peligros del glutaraldehído', 172, 1),

    (17301, 'Peligros de mercurio', 173, 1),

    (17401, 'Riesgos de incendio', 174, 1),

    (17501, 'Legionelosis', 175, 1),
    (17502, 'MRSA en la atención sanitaria', 175, 1),
    (17503, 'Tuberculosis', 175, 1),

    (17601, 'Violencia en la atención sanitaria', 176, 1),
    (17602, 'Estrés en la atención sanitaria', 176, 1),

    (17701, 'Seguridad ELECTRICA', 177, 1),

    (17801, 'Equipo de protección personal', 178, 1),

    (18301, 'Radiación en la atención sanitaria', 183, 1),

    (60301, 'Tipos de escaleras', 603, 1),
    (60302, 'Requisitos generales: escaleras', 603, 1),
    (60303, 'Requisitos generales: escaleras(gradas)', 603, 1),

    (60401, 'Conceptos básicos de andamios', 604, 1),
    (60402, 'Andamios soportados', 604, 1),
    (60403, 'Andamios suspendidos', 604, 1),
    
    (60501, 'Conceptos básicos de espacios confinados', 605, 1),
    (60502, 'Equipo de entrada a espacios confinados', 605, 1),
    (60503, 'Rescates en espacios confinados', 605, 1),
    (60504, 'Requisitos de capacitación en espacios confinados', 605, 1),
    (60505, 'Espacios confinados en la construcción', 605, 1),

    (61101, 'Conceptos básicos de la pistola de clavos', 611, 1),
    (61102, 'Entrenamiento con pistola de clavos', 611, 1),
    (61103, 'Lesiones por pistola de clavos y otros peligros', 611, 1),
    
    (61201, 'Riesgos viales en la zona de trabajo', 612, 1),
    (61202, 'Seguridad del ángulo muerto', 612, 1),
    (61203, 'Carteles, señales y barricadas', 612, 1),

    (62301, 'Programa de seguridad y salud', 623, 1),
    (62302, 'Controles de manipulación de pacientes', 623, 1),
    (62303, 'Otros riesgos ergonómicos', 623, 1),

    (62401, 'Principales riesgos y soluciones', 624, 1),
    (62402, 'Herramientas y recursos', 624, 1),

    (65601, '¿Qué son los patógenos transmitidos por la sangre?', 656, 1),
    (65602, 'Patógenos específicos transmitidos por la sangre', 656, 1),
    (65603, 'Transmisión de patógenos sanguíneos', 656, 1),
    (65604, 'Plan de control de la exposición de su empresa', 656, 1),
    (65605, 'Reconocer el potencial de exposición', 656, 1),
    (65606, 'Métodos de control de la exposición', 656, 1),
    (65607, 'Seguridad de las agujas', 656, 1),
    (65608, 'Precauciones universales', 656, 1),
    (65609, 'Equipos de protección individual', 656, 1),
    (65610, 'Seguridad en el laboratorio', 656, 1),
    (65611, 'Vacunación contra la hepatitis B (VHB)', 656, 1),
    (65612, 'Cuándo se produce una exposición', 656, 1),
    (65613, 'Limpieza', 656, 1),
    (65614, 'Comunicar un peligro', 656, 1),

    (66001, 'Visión general de HAZWOPER', 660, 1),
    (66002, 'HAZWOPER para operaciones de limpieza', 660, 1),
    (66003, 'HAZWOPER para instalaciones TSD', 660, 1),
    (66004, 'HAZWOPER para el personal de emergencias', 660, 1),
    (66005, 'Brownfields y laboratorios clandestinos de drogas', 660, 1),

    (66101, 'Programa de seguridad y salud HAZWOPER', 661, 1),
    (66102, 'Programa de seguridad y salud HAZWOPER ', 661, 1),
    (66103, 'Programa de seguridad y salud HAZWOPER ', 661, 1),
    (66104, 'Planificación y organización', 661, 1),
    (66105, 'Formación', 661, 1),

    (66201, 'Introducción a la identificación y el control de riesgos', 662, 1),
    (66202, 'Introducción a las sustancias peligrosas', 662, 1),
    (66203, 'Propiedades físicas de las sustancias peligrosas', 662, 1),
    (66204, 'Toxicología', 662, 1),
    (66205, 'Peligros para la salud', 662, 1),

    (66301, 'Responsabilidades generales', 663, 1),
    (66302, 'Analizar el lugar de trabajo', 663, 1),
    (66303, 'Riesgos químicos en la construcción', 663, 1),
    (66304, 'Etiquetado de envases', 663, 1),
    (66305, 'Fichas de datos de seguridad (FDS)', 663, 1),
    (66306, 'Información y formación', 663, 1),

    (66401, 'Caracterización del emplazamiento - Fuera del emplazamiento', 664, 1),
    (66402, 'Caracterización del emplazamiento - Encuesta in situ', 664, 1),
    (66403, 'Identificación, análisis y control de riesgos', 664, 1),
    (66404, 'Control del aire', 664, 1),
    (66405, 'Prácticas generales de control', 664, 1),

    (66501, 'Conceptos básicos sobre equipos de protección individual (EPI)', 665, 1),
    (66502, 'Selección de ropa y accesorios de protección', 665, 1),
    (66503, 'Selección de ropa de protección química (CPC)', 665, 1),
    (66504, 'Selección, uso e inspección del conjunto', 665, 1),
    (66505, 'Inspección y almacenamiento de CPC', 665, 1),
    (66506, 'Estrés por frío y calor', 665, 1),

    (66601, 'Control de obras', 666, 1),
    (66602, 'Seguridad del sitio y buenas prácticas', 666, 1),
    (66603, 'Descontaminación ', 666, 1),
    (66604, 'Descontaminación (continuación)', 666, 1),

    (66701, 'Conceptos básicos de seguridad en espacios confinados', 667, 1),
    (66702, 'Peligros atmosféricos', 667, 1),
    (66703, 'Riesgos no atmosféricos', 667, 1),
    (66704, 'Control de riesgos en espacios confinados', 667, 1),
    (66705, 'Entrada y rescate en espacios confinados', 667, 1),
    (66706, 'Requisitos de formación sobre espacios confinados', 667, 1),

    (66801, 'Seguridad en los andamios', 668, 1),
    (66802, 'Resbalones, tropezones y caídas', 668, 1),
    (66803, 'Escaleras y peldaños', 668, 1),
    (66804, 'Trabajar con electricidad', 668, 1),
    (66805, 'Excavación y zanjeo', 668, 1),
    (66806, 'Grúas y aparejos', 668, 1),
    (66807, 'Carretillas elevadoras, vehículos pesados y control de tráfico', 668, 1),

    (66901, 'Patógenos transmitidos por la sangre', 669, 1),
    (66902, 'Formación en respuesta a emergencias', 669, 1),
    (66903, 'Manipulación de bidones y contenedores', 669, 1),
    (66904, 'Derechos y protección de los trabajadores', 669, 1),
    (66905, 'Guía de respuesta a emergencias', 669, 1),
    
    (70001, 'Compromiso y liderazgo', 700, 1),
    (70002, 'Rendición de cuentas', 700, 1),
    (70003, 'Participación de los empleados', 700, 1),
    (70004, 'Comunicaciones de seguridad', 700, 1),
    (70005, 'Identificación y control de riesgos', 700, 1),
    (70006, 'Investigación de accidentes', 700, 1),
    (70007, 'Educación para la seguridad', 700, 1),
    (70008, 'Mejora continua', 700, 1),

    (70201, 'Conceptos básicos', 702, 1),
    (70202, 'Paso 1: Asegurar la escena', 702, 1),
    (70203, 'Paso 2: Documentar la escena', 702, 1),
    (70204, 'Paso 3: Realizar entrevistas', 702, 1),
    (70205, 'Paso 4: Realización del análisis de sucesos', 702, 1),
    (70206, 'Paso 5: Realizar un análisis de causas', 702, 1),
    (70207, 'Paso 6: Desarrollar soluciones', 702, 1),
    (70208, 'Paso 7: Redactar el informe', 702, 1),

    (70301, 'Panorama general', 703, 1),
    (70302, 'Categorías de educación', 703, 1),
    (70303, 'Desarrollo de programas', 703, 1),
    (70304, 'Funciones y responsabilidades', 703, 1),
    (70305, 'Evaluación de programas - ANSI', 703, 1),
    (70306, 'Paso 5: Realizar un análisis de causas', 703, 1),
    (70307, 'Paso 6: Desarrollar soluciones', 703, 1),
    (70308, 'Paso 7: Redactar el informe', 703, 1),

    (70401, 'Conceptos básicos', 704, 1),
    (70402, 'Categorías de peligro', 704, 1),
    (70403, 'Identificación de riesgos', 704, 1),
    (70404, 'Analizar el lugar de trabajo', 704, 1),
    (70405, 'Control de riesgos', 704, 1),
    (70406, 'Resolución de problemas', 704, 1),
    (70407, 'Recomendaciones eficaces', 704, 1),

    (70501, 'Responsabilidades generales', 705, 1),
    (70502, 'Analizar el lugar de trabajo', 705, 1),
    (70503, 'Etiquetado de envases', 705, 1),
    (70504, 'Fichas de datos de seguridad', 705, 1),
    (70505, 'Información y formación', 705, 1),

    (70601, 'Preparativos para llevar a cabo las JAI', 706, 1),
    (70602, 'Enumerar los pasos', 706, 1),
    (70603, 'Describir los peligros', 706, 1),
    (70604, 'Desarrollar medidas preventivas', 706, 1),
    (70605, 'Redactar el procedimiento de trabajo seguro', 706, 1),
    (70606, 'Mejorar el proceso JAI', 706, 1),

    (70901, 'Requisitos generales', 709, 1),
    (70902, 'Requisitos de formación en EPI', 709, 1),
    (70903, 'Protección ocular y facial', 709, 1),
    (70904, 'Protección respiratoria', 709, 1),
    (70905, 'Protección de cabeza, manos y pies', 709, 1),
    (70906, 'Equipos de protección eléctrica', 709, 1),
    (70907, 'Protección auditiva', 709, 1),

    (71001, 'Objeto, ámbito y aplicación', 710, 1),
    (71002, 'Componentes del programa de control de la energía', 710, 1),
    (71003, 'Formación y comunicación', 710, 1),
    (71004, 'Inspección periódica', 710, 1),
    (71005, 'Materiales y equipos', 710, 1),
    (71006, 'Aplicación de los dispositivos de control de la energía', 710, 1),
    (71007, 'Liberación del bloqueo/etiquetado', 710, 1),
    (71008, 'Contratistas, bloqueo y etiquetado en grupo', 710, 1),

    (71101, 'Definición de ergonomía', 711, 1),
    (71102, 'Factores de riesgo en el trabajador', 711, 1),
    (71103, 'Factores de riesgo en la tarea', 711, 1),
    (71104, 'Factores de riesgo en el medio ambiente', 711, 1),
    (71105, 'Control de los factores de riesgo', 711, 1),

    (71301, 'Conceptos básicos sobre espacios confinados', 713, 1),
    (71302, 'Elementos del programa', 713, 1),
    (71303, 'Permiso para espacios confinados', 713, 1),
    (71304, 'Peligros atmosféricos', 713, 1),
    (71305, 'Riesgos no atmosféricos', 713, 1),
    (71306, 'Control de riesgos', 713, 1),
    (71307, 'Equipo de entrada en espacios confinados', 713, 1),
    (71308, 'Rescate en espacios confinados', 713, 1),
    (71309, 'Requisitos de formación', 713, 1),

    (71401, 'Preguntas importantes', 714, 1),
    (71402, 'Programa de protección contra caídas', 714, 1),
    (71403, 'Identificación y evaluación de los riesgos de caída', 714, 1),
    (71404, 'Acceso asistido y suspendido', 714, 1),
    (71405, 'Sistemas de protección anticaídas I', 714, 1),
    (71406, 'Sistemas de protección contra caídas II', 714, 1),
    (71407, 'Formación sobre protección contra caídas', 714, 1),
    (71408, 'Inspección y mantenimiento', 714, 1),
    (71409, 'Rescate en altura', 714, 1),

    (71501, 'La electricidad es peligrosa', 715, 1),
    (71502, 'Peligros de las descargas eléctricas', 715, 1),
    (71503, 'Quemaduras eléctricas', 715, 1),
    (71504, 'El modelo de seguridad eléctrica', 715, 1),
    (71505, 'Reconocer los peligros', 715, 1),
    (71506, 'Evaluación del riesgo', 715, 1),
    (71507, 'Entornos de trabajo seguros', 715, 1),
    (71508, 'Trabajar en circuitos en tensión', 715, 1),
    (71509, 'Prácticas laborales seguras', 715, 1),
    (71510, 'Equipos de protección eléctrica', 715, 1),

    (71701, 'Preguntas básicas', 717, 1),
    (71702, 'Desarrollo del PAE', 717, 1),
    (71703, 'Políticas y procedimientos', 717, 1),
    (71704, 'Responsabilidades y formación', 717, 1),
    (71705, 'Revisar, coordinar y actualizar', 717, 1),

    (71801, 'Preguntas básicas', 718, 1),
    (71802, 'Control de riesgos', 718, 1),
    (71803, 'Sistemas fijos de extinción', 718, 1),
    (71804, 'Sistemas de alarma para empleados', 718, 1),
    (71805, 'Extintores portátiles', 718, 1),
    (71806, 'Requisitos de la ruta de salida', 718, 1),
    (71807, 'Responsabilidades y formación', 718, 1),
    (71808, 'Inspección y mantenimientoEvaluación del programa FPP', 718, 1),

    (71901, 'Panorama general', 719, 1),
    (71902, 'Funciones y responsabilidades', 719, 1),
    (71903, 'Responsabilidades del operador', 719, 1),
    (71904, 'Selección del conductor', 719, 1),
    (71905, 'Formación y evaluación de conductores', 719, 1),
    (71906, 'Investigación de accidentes', 719, 1),
    (71907, 'Selección y mantenimiento', 719, 1),

    (72101, '¿Es la formación la respuesta?', 721, 1),
    (72102, 'Necesidades de formación', 721, 1),
    (72103, 'Metas y objetivos', 721, 1),
    (72104, 'Actividades de aprendizaje', 721, 1),
    (72105, 'Documentación sobre formación', 721, 1),

    (72301, 'Prepárate...', 723, 1),
    (72302, 'Prepárate...', 723, 1),
    (72303, '¡Adelante!', 723, 1),
    (72304, '¡Pregúntalo!', 723, 1),
    (72305, '¡Manos a la obra!', 723, 1),
    (72306, 'Los 7 pasos del proceso OJT', 723, 1),

    (72501, 'Tipos de carretillas elevadoras', 725, 1),
    (72502, 'Formación de operadores', 725, 1),
    (72503, 'Cómo funciona una carretilla elevadora', 725, 1),
    (72504, 'Operaciones con carretillas elevadoras', 725, 1),
    (72505, 'Operaciones con carretillas elevadoras (Cont.)', 725, 1),
    (72506, 'Mantenimiento de carretillas elevadoras', 725, 1),
    (72507, 'Mantenimiento de carretillas elevadoras', 725, 1),

    (72601, 'Aspectos básicos de la protección de máquinas', 726, 1),
    (72602, 'Métodos de protección de máquinas - Resguardos', 726, 1),
    (72603, 'Métodos de protección de máquinas - Dispositivos', 726, 1),
    (72604, 'Más métodos de protección', 726, 1),
    (72605, 'Construcción de protecciones para máquinas', 726, 1),
    (72606, 'Mantenimiento y reparación de maquinaria', 726, 1),

    (75701, 'Las normas', 757, 1),
    (75702, 'Normas OSHA relacionadas', 757, 1),
    (75703, 'Control de los riesgos de laboratorio', 757, 1),
    (75704, 'Riesgos químicos en el laboratorio', 757, 1),
    (75705, 'Riesgos biológicos', 757, 1),
    (75706, 'Patógenos transmitidos por la sangre', 757, 1),
    (75707, 'Seguridad en los laboratorios de animales de investigación', 757, 1),
    (75708, 'Riesgos físicos y otros', 757, 1),
    (75709, 'Peligros para la seguridad', 757, 1),

    (80001, 'La cultura de la seguridad', 800, 1),
    (80002, 'Trabajar con contratistas', 800, 1),
    (80003, 'Implicación en la seguridad', 800, 1),
    (80004, 'CSMS y análisis del lugar de trabajo', 800, 1),
    (80005, 'Prevención y control de riesgos', 800, 1),
    (80006, 'Educación y formación', 800, 1),

    (80201, 'Conceptos básicos', 802, 1),
    (80202, 'Características y tipos de suelo', 802, 1),
    (80203, 'Mecánica del suelo', 802, 1),
    (80204, 'Métodos de protección', 802, 1),
    (80205, 'Requisitos del empleador', 802, 1),
    (80206, 'Seguridad en el lugar de trabajo', 802, 1),

    (80301, 'Programa de seguridad para andamios', 803, 1),
    (80302, 'Supervisión de proyectos', 803, 1),
    (80303, 'Requisitos de formación sobre andamios', 803, 1),
    (80304, 'Protección contra caídas en andamios', 803, 1),

    (80401, 'Directrices básicas', 804, 1),
    (80402, 'Inspección de andamios fabricados con bastidor', 804, 1),
    (80403, 'Inspección de otros andamios soportados', 804, 1),
    (80404, 'Andamios soportados de uso especial', 804, 1),
    (80405, 'Inspección de andamios colgantes', 804, 1),
    (80406, 'Inspección de andamios colgantes de uso especial', 804, 1),

    (80501, 'Verdad y consecuencias', 805, 1),
    (80502, 'Prepararse para prevenir las caídas', 805, 1),
    (80503, 'Identificación y evaluación de los riesgos de caída', 805, 1),
    (80504, 'Acceso asistido y suspendido', 805, 1),
    (80505, 'Sistemas de protección anticaídas', 805, 1),
    (80506, 'Sistemas de protección contra caídas (continuación)', 805, 1),
    (80507, 'Formación sobre protección contra caídas', 805, 1),
    (80508, 'Inspección y mantenimiento', 805, 1),
    (80509, 'Rescate en altura', 805, 1),

    (80601, '¿Qué es un riesgo de caída?', 806, 1),
    (80602, 'Protegerse de los riesgos de caída', 806, 1),

    (80701, '¿Qué son los riesgos intermedios?', 807, 1),
    (80702, 'Protéjase de los riesgos de quedar atrapado/entre dos aguas', 807, 1),
    
    (80801, '¿Qué es un peligro de atropello?', 808, 1),
    (80802, 'Protegerse de los riesgos de atropello', 808, 1),

    (80901, '¿Qué son los riesgos de electrocución?', 809, 1),
    (80902, 'Cómo protegerse de los riesgos de electrocución', 809, 1),

    (81001, 'Reconocer los peligros', 810, 1),
    (81002, 'Seguridad de las herramientas manuales', 810, 1),
    (81003, 'Seguridad de las herramientas eléctricas', 810, 1),
    (81004, 'Herramientas eléctricas', 810, 1),
    (81005, 'Disco abrasivo portátil y herramientas neumáticas', 810, 1),
    (81006, 'Herramientas accionadas por combustible, hidráulicas y por pólvora', 810, 1),

    (81301, 'Andamios y plataformas elevadoras', 813, 1),
    (81302, 'Resbalones, tropezones y caídas', 813, 1),
    (81303, 'Escaleras y peldaños', 813, 1),
    (81304, 'Trabajar con electricidad', 813, 1),
    (81305, 'Excavación y zanjeo', 813, 1),
    (81306, 'Grúas y aparejos', 813, 1),
    (81307, 'Carretillas elevadoras y seguridad de los vehículos', 813, 1),
    (81308, 'Peligros químicos', 813, 1),
    (81309, 'Peligros para la salud', 813, 1),
    (81310, 'Equipos de protección individual (EPI)', 813, 1),
    (81311, 'Espacios confinados en la construcción', 813, 1),

    (81401, 'Conceptos básicos sobre maquinaria pesada', 814, 1),
    (81402, 'Peligros de la maquinaria pesada', 814, 1),
    (81403, 'Controles y buenas prácticas', 814, 1),
    (81404, 'Seguridad de los operadores', 814, 1),
    (81405, 'Seguridad en las zonas de trabajo y control del tráfico', 814, 1),

    (81501, 'Elementos básicos del programa de demolición', 815, 1),
    (81502, 'Prevención de incendios, servicios médicos y seguridad', 815, 1),
    (81503, 'Riesgos asociados a la demolición de edificios', 815, 1),
    (81504, 'Demolición de estructuras de hormigón pretensado', 815, 1),
    (81505, 'Demolición de estructuras especiales', 815, 1),
    (81506, 'Retirada de escombros y limpieza', 815, 1),
    (81507, 'Control de la exposición al amianto', 815, 1),
    (81508, 'Control de la exposición al plomo', 815, 1),
    (81509, 'Control de la exposición al sílice', 815, 1),

    (81601, 'Conceptos básicos sobre espacios confinados en la construcción', 816, 1),
    (81602, 'Programa de Espacio Autorizado (PSP)', 816, 1),
    (81603, 'Procedimientos de entrada en el espacio autorizado', 816, 1),
    (81604, 'Programa de permisos de entrada', 816, 1),
    (81605, 'Formación y funciones del equipo de entrada en espacios confinados', 816, 1),
    (81606, 'Rescate de emergencia', 816, 1),

    (81701, 'Preparación del terreno', 817, 1),
    (81702, 'Grúas', 817, 1),
    (81703, 'Estabilidad estructural', 817, 1),
    (81704, 'Edificios metálicos y riesgos aéreos', 817, 1),
    (81705, 'Protección contra caídas', 817, 1),
    (81706, 'Formación sobre seguridad en la erección de acero', 817, 1),

    (82001, 'Conceptos básicos sobre grúas y torres de perforación', 820, 1),
    (82002, 'Responsabilidades del empresario y del trabajador', 820, 1),
    (82003, 'Montaje y desmontaje', 820, 1),
    (82004, 'Seguridad de las líneas eléctricas', 820, 1),
    (82005, 'Inspecciones', 820, 1),
    (82006, 'Inspección, selección e instalación de cables de acero', 820, 1),

    (82101, 'Operación', 821, 1),
    (82102, 'Señales y protección contra caídas', 821, 1),
    (82103, 'Alejarse de los peligros', 821, 1),
    (82104, 'Cualificación y certificación', 821, 1),
    (82105, 'Personal de elevación', 821, 1),
    (82106, 'Múltiples operaciones de grúa/grúa puente', 821, 1),
    (82107, 'Grúas torre y torres de perforación', 821, 1),
    (82108, 'Grúas y equipos especializados', 821, 1),

    (83301, 'Sentar las bases', 833, 1),
    (83302, 'Proceso 3D: Diseño', 833, 1),
    (83303, 'Proceso 3D: Desarrollar', 833, 1),
    (83304, 'Políticas y procesos', 833, 1),
    (83305, 'Procedimientos y prácticas', 833, 1),
    (83306, 'Proceso 3D: Despliegue', 833, 1),
    (83307, 'Análisis del lugar de trabajo', 833, 1),
    (83308, 'Control de los riesgos en el lugar de trabajo', 833, 1),
    (83309, 'Gestión de subcontratistas', 833, 1),
    (83310, 'Mejorar el CSMS', 833, 1),

    (85001, 'Salud y seguridad de los trabajadores de la construcción', 850, 1),
    (85002, 'Riesgos físicos en la construcción', 850, 1),
    (85003, 'Riesgos biológicos para la salud', 850, 1),
    (85004, 'Riesgos ergonómicos en la construcción', 850, 1),

    (90001, 'La cultura de la seguridad', 900, 1),
    (90002, 'Trabajar con contratistas', 900, 1),
    (90003, 'Implicación en la seguridad', 900, 1),
    (90004, 'SMS y análisis de pozos', 900, 1),
    (90005, 'Prevención y control de riesgos', 900, 1),
    (90006, 'Educación y formación', 900, 1),

    (90401, 'Temas de inspección de la respuesta de emergencia', 904, 1),
    (90402, 'Sistemas eléctricos y protección de máquinas', 904, 1),
    (90403, 'Herramientas manuales y eléctricas', 904, 1),
    (90404, 'Protección contra caídas', 904, 1),
    (90405, 'Escaleras y pasarelas', 904, 1),
    (90406, 'Líneas y eslingas', 904, 1),
    (90407, 'Líneas y eslingas (continuación)', 904, 1),
    (90408, 'Escaleras y plataformas', 904, 1),
    (90409, 'Mangueras, pasadores y soportes', 904, 1),
    (90410, 'Peligros químicos', 904, 1),
    (90411, 'Otros ámbitos', 904, 1),

    (90701, 'Mantenimiento de registros, SWA y UWA', 907, 1),
    (90702, 'Elementos de gestión, cultura y programas', 907, 1),
    (90703, 'Análisis y gestión del cambio (MOC)', 907, 1),
    (90704, 'Criterios del programa (Parte 1)', 907, 1),
    (90705, 'Criterios del programa (Parte 2)', 907, 1),
    (90706, 'Requisitos de auditoría', 907, 1),
    (90707, 'Evaluación del BSEE', 907, 1),
    (90708, 'Mantenimiento de registros, SWA y UWA', 907, 1),

    (90801, 'Directrices generales', 908, 1),
    (90802, 'Directrices generales (continuación)', 908, 1),
    (90803, 'Equipos de protección individual (EPI)', 908, 1),
    (90804, 'Protección contra caídas', 908, 1),
    (90805, 'Respuesta y notificación en caso de emergencia', 908, 1),
    (90806, 'Prevención de incendios', 908, 1),
    (90807, 'Servicios y apoyo médicos', 908, 1),

    (90901, 'Prácticas de seguridad eléctrica', 909, 1),
    (90902, 'Control de energía peligrosa (bloqueo/etiquetado)', 909, 1),
    (90903, 'Seguridad de herramientas y equipos', 909, 1),
    (90904, 'Cualificaciones y buenas prácticas del operador de grúa', 909, 1),
    (90905, 'Control de sustancias y productos químicos peligrosos', 909, 1),
    (90906, 'Seguridad en la manipulación, el aparejo y la elevación de materiales', 909, 1),
    (90907, 'Buenas prácticas varias', 909, 1),

    (100001, 'Planificación de la protección contra caídas', 1000, 1),
    (100002, 'Uso de protección contra caídas', 1000, 1),
    (100003, 'Importancia de la protección contra caídas', 1000, 1),
    (100004, 'Las caídas son la causa número 1 de lesiones y muertes', 1000, 1),
    (100005, 'Como hacer una buena inspección de los equipos de protección contra caídas', 1000, 1),
    (100006, 'Cuerdas salva vidas horizontales', 1000, 1),
    (100007, 'Anclajes', 1000, 1),
    (100008, 'Claraboyas', 1000, 1),
    (100009, 'Traslado de materiales', 1000, 1),
    (100010, 'Caídas durante la reparación de techos', 1000, 1),
    (100011, 'Caídas de Andamios fijos', 1000, 1),
    (100012, 'Identificación del peligro', 1000, 1),
    (100013, 'Peligro, errores comunes', 1000, 1),

    (111001, 'Gestión y Reconocimiento del Sistema Globalmente Armonizado SGA', 1110, 1),
    (111002, 'Clasificación de un producto con base en los criterios de clasificación SGA', 1110, 1),

    (120001, 'Química general en la industria 1', 1200, 1),

    (120101, 'Química básica 2', 1201, 1),

    (120301, 'Introducción a la Toxicología', 1203, 1),
    (120302, 'Toxicología general I', 1203, 1),
    (120303, 'Toxicología complementaria intoxicaciones', 1203, 1),
    (120304, 'Toxicología rutinaria metales y plaguicidas', 1203, 1),

    (555501, 'Toxicocinética', 5555, 1),

    (555601, 'Toxicodinamia', 5556, 1),

    (555701, 'Tratamiento General del Paciente Intoxicado', 5557, 1),

    (555801, 'Tratamientos Específicos', 5558, 1),

    (555901, 'Hipoxias Tóxicas Monóxido de Carbono', 5559, 1),

    (556001, 'Hipoxias Tóxicas por Cianuro', 5560, 1),

    (556101, 'Hipoxias Tóxicas Metahemoglobinemia', 5561, 1),

    (556201, 'Radiotoxicidad', 5562, 1),

    (556301, 'Intoxicación con Etanol', 5563, 1),

    (556401, 'Intoxicación con Metanol', 5564, 1),

    (556501, 'Intoxicación con Glicoles', 5565, 1),

    (556601, 'Hidrocarburos Generalidades', 5566, 1),

    (556701, 'Hidrocarburos Alifáticos o Lineales', 5567, 1),

    (556801, 'Hidrocarburos Alogenados Clorado', 5568, 1),

    (556901, 'Hidrocarburos Cíclicos Aromáticos', 5569, 1),

    (557001, 'Hidrocarburos Nitrogenados', 5570, 1),

    (557101, 'Arsénico', 5571, 1),

    (557201, 'Plomo', 5572, 1),

    (557301, 'Mercurio', 5573, 1),

    (557401, 'Cromo', 5574, 1),

    (557501, 'Manganeso', 5575, 1),

    (557601, 'Talio', 5576, 1),

    (557701, 'Hierro', 5577, 1),

    (557801, 'Organofosforados', 5578, 1),

    (557901, 'Organoclorados', 5579, 1),

    (558001, 'Dicumarinicus', 5580, 1),

    (558101, 'Bipiridilos', 5581, 1),

    (558201, 'Piretrinas', 5582, 1);