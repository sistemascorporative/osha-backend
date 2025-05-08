--INSERT INTO pregunta(PreCod, PreTex, PreExp, PreNumMod, PreExaCod, PreEstRegCod)
INSERT INTO pregunta("PreCod", "PreTex", "PreExp", "PreNumMod", "PreExaCod", "PreEstRegCod")
VALUES

---examen 112
(1200101, '', 
'', 
, , 1),



--INSERT INTO pregunta(PreCod, PreTex, PreExp, PreNumMod, PreExaCod, PreEstRegCod)
INSERT INTO pregunta("PreCod", "PreTex", "PreExp", "PreNumMod", "PreExaCod", "PreEstRegCod")
VALUES
-- Pregunta 1
(1200101, 'El Hidróxido de calcio, Ca(OH)2. ¿Es considerado un Peróxido?', 
'No se considera un peróxido porque los peróxidos contienen un enlace oxígeno-oxígeno, como H₂O₂, cosa que no ocurre en Ca(OH)₂.', 
120001, 12001, 1),
-- Pregunta 2
(1200102, '¿El concepto propio de Química inorgánica es?', 
'', 
120001, 12001, 1),
-- Pregunta 3
(1200103, 'Cuando hablamos de hidróxido de litio estamos hablando específicamente de que:', 
'', 
120001, 12001, 1),
-- Pregunta 4
(1200104, 'El Hidróxido de Sodio es asociado con:', 
'', 
120001, 12001, 1),
-- Pregunta 5
(1200105, 'El Hidróxido de Hierro se Utiliza como antiácido o laxante?', 
'', 
120001, 12001, 1),
-- Pregunta 6
(1200106, 'La química inorgánica estudia todos los mencionados menos una:', 
'', 
120001, 12001, 1),
-- Pregunta 7
(1200107, 'La química orgánica estudia:', 
'', 
120001, 12001, 1),
-- Pregunta 8
(1200108, '¿El hidróxido de aluminio también se emplea como antiácido en las denominadas “sales de fruta”?', 
'', 
120001, 12001, 1),
-- Pregunta 9
(1200109, 'Todos estos Ejemplos de aplicaciones y procesos de la química orgánica pertenecen menos 1 indique cual es la incorrecta.', 
'', 
120001, 12001, 1),
-- Pregunta 10
(1200110, 'Es cierto que La geoquímica (rama de la química inorgánica) estudia la composición y los procesos que ocurren en los suelos y los océanos desde el punto de vista químico?', 
'', 
120001, 12001, 1),





--INSERT INTO alternativa(AltCod, AltTex, AltCor, AltPreCod, AltEstRegCod)
INSERT INTO alternativa("AltCod", "AltTex", "AltCor", "AltPreCod", "AltEstRegCod")
VALUES
-- Pregunta 1
(120010101, 'Sí.', False, 1200101, 1),
(120010102, 'No.', True, 1200101, 1),
(120010103, 'Ninguna de los anteriores.', False, 1200101, 1),
(120010104, 'Dependiendo su composición.', False, 1200101, 1),
(120010105, 'Si se encuentra en el depósito adecuado.', False, 1200101, 1),

-- Pregunta 2
(120010201, 'Estudia los compuestos químicos, así como las reacciones químicas que se desarrollan en los organismos vivientes.', False, 1200102, 1),
(120010202, 'Estudia todos los elementos y compuestos cuya estructura no está basada fundamentalmente en el carbono.', True, 1200102, 1),
(120010203, 'Estudia la materia utilizando la combinación de conceptos físicos y químicos.', False, 1200102, 1),
(120010204, 'Establece métodos y técnicas para analizar la composición cuantitativa y cualitativa de las sustancias.', False, 1200102, 1),

-- Pregunta 3
(120010301, 'Se asocia a la industria de los jabones y los productos de belleza y cuidado corporal.', True, 1200103, 1),
(120010302, 'Tiene un papel intermediario en algunos procesos como el de la obtención del carbonato sódico.', False, 1200103, 1),
(120010303, 'Se usa en la fabricación de cerámica, mientras que el de magnesio se usa como antiácido o laxante.', False, 1200103, 1),
(120010304, 'En el proceso de fertilización de plantas.', False, 1200103, 1),
(120010305, 'Ninguna de las anteriores.', False, 1200103, 1),

-- Pregunta 4
(120010401, 'Por ejemplo, se asocia a la industria de los jabones y los productos de belleza y cuidado corporal.', True, 1200104, 1),
(120010402, 'Tiene un papel intermediario en algunos procesos como el de la obtención del carbonato sódico.', False, 1200104, 1),
(120010403, 'Se usa en la fabricación de cerámica, mientras que el de magnesio se usa como antiácido o laxante.', False, 1200104, 1),
(120010404, 'Se utiliza en el proceso de fertilización de plantas.', False, 1200104, 1),

-- Pregunta 5
(120010501, 'Sí.', False, 1200105, 1),
(120010502, 'No.', True, 1200105, 1),
(120010503, 'Puede ser.', False, 1200105, 1),
(120010504, 'Ninguna de las anteriores.', False, 1200105, 1);