CREATE TYPE user_role AS ENUM ('teacher', 'student', 'admin');

COMMENT ON TYPE user_role IS ' '

CREATE TABLE public.appuser (
    "id" serial4 NOT NULL,
    f_login         text NOT NULL,
    f_password_hash text,
    f_enabled       bool NOT NULL DEFAULT TRUE,
    f_created       timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    f_expire        timestamp,
    f_role          user_role NOT NULL,
    f_salt          text,
    f_fio           text NOT NULL,
    f_email         text,
    f_comment       text
    CONSTRAINT appuser_pk PRIMARY KEY (id),
	CONSTRAINT appuser_login_un UNIQUE (f_login)
);
