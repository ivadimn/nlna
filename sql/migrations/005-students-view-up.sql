START TRANSACTION ;


CREATE FUNCTION new_teacher(p_login text,
            p_fio text, p_phone text, p_email text, p_comment text)

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


COMMIT TRANSACTION ;