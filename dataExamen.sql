-- EL ID DEL EXAMEN TIENE QUE SER IGUAL QUE EL CURSO
INSERT INTO examen(ExaCod, ExaNumPre, ExaEStRegCod)
VALUES
    (100, 20, 1),
    (105, 20, 1);

INSERT INTO pregunta(PreCod, PreTex, PreExp, PreNumMod, PreExaCod, PreEstRegCod)
VALUES
    (10501, 'Texto pregunta', 'Texto de explicacion de repta', 10501, 105, 1),
    (10502, 'Texto pregunta', 'Texto de explicacion de repta', 10502, 105, 1),
    (10503, 'Texto pregunta', 'Texto de explicacion de repta', 10501, 105, 1);

INSERT INTO alternativa(AltCod, AltTex, AltCor, AltPreCod, AltEstRegCod)
VALUES
    (1050101, 'Pregunta...', True, 10501, 1),
    (1050102, 'Pregunta...', False, 10501, 1),
    (1050103, 'Pregunta...', False, 10501, 1),
    (1050104, 'Pregunta...', False, 10501, 1),

    (1050201, 'Pregunta...', False, 10502, 1),
    (1050202, 'Pregunta...', False, 10502, 1),
    (1050203, 'Pregunta...', True, 10502, 1),
    (1050204, 'Pregunta...', False, 10502, 1),