START TRANSACTION ;
/*-------------------------------------------------------------------------------------*/
CREATE TYPE user_role AS ENUM ('teacher', 'student', 'admin');

COMMENT ON TYPE user_role IS 'Права пользователя в приложении';
/*--------------------------------------------------------------------------------------*/

CREATE TABLE public.appuser (
    "id" serial4 NOT NULL,
    f_login         text NOT NULL,
    f_password_hash text,
    f_salt          text,
    f_enabled       bool NOT NULL DEFAULT TRUE,
    f_created       timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    f_expire        timestamp,
    f_role          user_role NOT NULL,
    f_fio           text NOT NULL,
    f_email         text,               --добавить проверку правильности адреса
    f_comment       text,
    CONSTRAINT appuser_pk PRIMARY KEY (id),
	CONSTRAINT appuser_login_un UNIQUE (f_login)
);

COMMENT ON TABLE appuser IS 'Общие сведения о пользоветеле';
COMMENT ON COLUMN appuser.f_login IS 'логин пользователя';
COMMENT ON COLUMN appuser.f_password_hash IS 'контрольная сумма пароля';
COMMENT ON COLUMN appuser.f_salt IS 'соль пароля';
COMMENT ON COLUMN appuser.f_enabled IS 'пользователю разрешено подключение';
COMMENT ON COLUMN appuser.f_created IS 'время создание пользователя';
COMMENT ON COLUMN appuser.f_expire IS 'истечение срока действия логина';
COMMENT ON COLUMN appuser.f_role IS 'права пользователя';
COMMENT ON COLUMN appuser.f_fio IS 'имя пользователя';
COMMENT ON COLUMN appuser.f_email IS 'почтовый адрес';
COMMENT ON COLUMN appuser.f_comment IS 'комментарии';

/*--------------------------------------------------------------------------------------*/
CREATE TABLE public.teacher (
	"id" serial4 NOT NULL,
	f_phone text NULL,
	user_id INT NOT NULL ,
	CONSTRAINT teacher_pk PRIMARY KEY ("id"),
	CONSTRAINT teacher_user_id_fk FOREIGN KEY (user_id) REFERENCES public.appuser("id")
);

COMMENT ON TABLE teacher IS 'Сведения о преподавателях';
COMMENT ON COLUMN teacher.f_phone IS 'телефон преподавателя';


/*--------------------------------------------------------------------------------------*/

CREATE TABLE public.student (
	"id" serial4 NOT NULL,
	user_id INT NOT NULL ,
	CONSTRAINT student_pk PRIMARY KEY ("id"),
	CONSTRAINT student_user_id_fk FOREIGN KEY (user_id) REFERENCES public.appuser("id")
);

COMMENT ON TABLE student IS 'Сведения о студентах';

/*--------------------------------------------------------------------------------------*/
CREATE TABLE public.stgroup (
	"id" serial4 NOT NULL,
	f_title text NOT NULL,
	f_comment text,
	CONSTRAINT groups_pk PRIMARY KEY ("id")
);

COMMENT ON TABLE stgroup IS 'Сведения о группах';
COMMENT ON COLUMN stgroup.f_title IS 'наименование группы';
COMMENT ON COLUMN stgroup.f_comment IS 'комментарии';

/*--------------------------------------------------------------------------------------*/
 INSERT INTO  appuser(f_login, f_enabled, f_role, f_fio)
        VALUES('admin', true, 'admin', 'Ivanov Vadim Nikolaevich') ;

/*--------------------------------------------------------------------------------------*/
COMMIT TRANSACTION;