-- EL ID DEL EXAMEN TIENE QUE SER IGUAL QUE EL CURSO
INSERT INTO examen(ExaCod, ExaCurCod, ExaEStRegCod)
VALUES
    (100, 100, 1),
    (105, 105, 1);

INSERT INTO pregunta(PreCod, PreTex, PreExaCod, PreEstRegCod)
VALUES
    (, 'Texto pre', ,1),
    ();

INSERT INTO alternativa(AltCod, AltTex, AltCor, AltEstRegCod)
VALUES
    (, 'Pregunta...', True, 1),
    (, 'Pregunta...', False, 1),
    (, 'Pregunta...', False, 1),
    (, 'Pregunta...', False, 1);