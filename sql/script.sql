CREATE TABLE public.teacher (
	id serial NOT NULL,
	f_fio varchar NOT NULL,
	f_phone varchar NULL,
	f_email varchar NULL,
	f_comment text NULL,
	CONSTRAINT teacher_pk PRIMARY KEY (id)
);
CREATE TABLE public.task (
	id serial NOT NULL,
	f_name varchar NOT NULL,
	f_description text NOT NULL,
	CONSTRAINT task_pk PRIMARY KEY (id)
);
CREATE TABLE public.variant (
	id serial NOT NULL,
	f_name varchar NOT NULL,
	f_created_at date NOT NULL,
	CONSTRAINT variant_pk PRIMARY KEY (id)
);
