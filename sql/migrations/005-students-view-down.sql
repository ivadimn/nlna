START TRANSACTION ;

DROP FUNCTION IF EXISTS new_student(text, text, text, text);
DROP FUNCTION IF EXISTS new_teacher(text, text, text, text, text);
DROP VIEW IF EXISTS v_student ;
DROP VIEW IF EXISTS v_teacher ;

COMMIT TRANSACTION ;