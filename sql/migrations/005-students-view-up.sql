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

COMMIT TRANSACTION ;