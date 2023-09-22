START TRANSACTION ;


/*------------------------------------------------------------------------------------------------------------------*/
CREATE VIEW v_teacher AS
    SELECT t.id as pk,
        t.user_id as user_id,
        au.f_login as f_login,
        au.f_enabled as f_enabled,
        au.f_created as f_created,
        au.f_expire as f_expire,
        au.f_role as f_role,
	    au.f_fio as f_fio,
	    t.f_phone as f_phone,
	    au.f_email as f_email,
	    au.f_comment as f_comment
	FROM appuser au
	INNER JOIN teacher t on t.user_id = au.id ;

/*------------------------------------------------------------------------------------------------------------------*/
CREATE VIEW v_student AS
    SELECT s.id as pk,
        s.user_id as user_id,
        au.f_login as f_login,
        au.f_enabled as f_enabled,
        au.f_created as f_created,
        au.f_expire as f_expire,
        au.f_role as f_role,
	    au.f_fio as f_fio,
	    au.f_email as f_email,
	    au.f_comment as f_comment
	FROM appuser au
	INNER JOIN student s on s.user_id = au.id ;

/*---------------------------------------------------------------------------------------------------*/

CREATE FUNCTION new_teacher(p_login text,
            p_fio text, p_phone text, p_email text, p_comment text) RETURNS text
LANGUAGE plpgsql
SECURITY definer
CALLED ON NULL INPUT
VOLATILE
AS $BODY$
DECLARE
    d_user_id int ;
    d_pk int;
BEGIN
   INSERT INTO appuser(f_login, f_role, f_fio, f_email, f_comment)
        VALUES(p_login, 'teacher', p_fio, p_email, p_comment)
         returning id into strict d_user_id ;
   INSERT INTO teacher (f_phone, user_id)
        VALUES(p_phone, d_user_id)
        returning id into strict d_pk ;
   RETURN d_pk ;
END;
$BODY$;

/*--------------------------------------------------------------------------------------------------------*/

CREATE FUNCTION new_student(p_login text,
            p_fio text, p_email text, p_comment text) RETURNS text
LANGUAGE plpgsql
SECURITY definer
CALLED ON NULL INPUT
VOLATILE
AS $BODY$
DECLARE
    d_user_id int ;
    d_pk int;
BEGIN
   INSERT INTO appuser(f_login, f_role, f_fio, f_email, f_comment)
        VALUES(p_login, 'student', p_fio, p_email, p_comment)
         returning id into strict d_user_id ;
   INSERT INTO student (user_id)
        VALUES(d_user_id)
        returning id into strict d_pk ;
   RETURN d_pk ;
END;
$BODY$;

/*-------------------------------------------------------------------------------------------------------------*/

CREATE FUNCTION update_teacher(pk int,
        p_fio text, p_phone text, p_email text, p_comment text) RETURNS int
LANGUAGE plpgsql
SECURITY definer
CALLED ON NULL INPUT
VOLATILE
AS $BODY$
DECLARE
    d_user_id int;
BEGIN
    SELECT user_id FROM teacher WHERE id = pk INTO strict d_user_id ;
    UPDATE appuser SET
            f_fio = p_fio,
            f_email = p_email,
            f_comment = p_comment
        WHERE id = d_user_id ;
    UPDATE teacher SET
            f_phone = p_phone
        WHERE id = pk ;
    return pk ;
END ;
$BODY$;

/*-----------------------------------------------------------------------------------------------------------------*/

CREATE FUNCTION delete_teacher(pk int) RETURNS int
LANGUAGE plpgsql
SECURITY definer
CALLED ON NULL INPUT
VOLATILE
AS $BODY$
DECLARE
    d_user_id int;
BEGIN
    SELECT user_id FROM teacher WHERE id = pk INTO strict d_user_id ;
    DELETE FROM teacher WHERE id = pk ;
    DELETE FROM appuser WHERE id = d_user_id ;
    return pk ;
END ;
$BODY$;

/*---------------------------------------------------------------------------------------------------*/
create function update_student(pk int, p_fio text, p_email text, p_comment text) returns int
LANGUAGE plpgsql
SECURITY definer
CALLED ON NULL INPUT
VOLATILE
AS $BODY$
DECLARE
    d_user_id int ;
BEGIN
    SELECT user_id FROM student WHERE id = pk INTO strict d_user_id ;
    UPDATE appuser SET
            f_fio = p_fio,
            f_email = p_email,
            f_comment = p_comment
        WHERE id = d_user_id ;
    return pk ;
END ;
$BODY$;

/*----------------------------------------------------------------------------------------------------*/

create function delete_student(pk int) returns int
LANGUAGE plpgsql
SECURITY definer
CALLED ON NULL INPUT
VOLATILE
AS $BODY$
DECLARE
    d_user_id int ;
BEGIN
    SELECT user_id FROM student WHERE id = pk INTO strict d_user_id ;
    DELETE FROM student WHERE id = pk ;
    DELETE FROM appuser WHERE id = d_user_id ;
    return pk ;
END;
$BODY$ ;

/*----------------------------------------------------------------------------------------------------*/
COMMIT TRANSACTION ;