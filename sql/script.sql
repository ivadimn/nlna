-- DROP TABLE public.teacher;

CREATE TABLE public.teacher (
	id serial4 NOT NULL,
	f_fio varchar NOT NULL,
	f_phone varchar NULL,
	f_email varchar NULL,
	f_comment text NULL,
	CONSTRAINT teacher_pk PRIMARY KEY (id)
);

CREATE TABLE public.task (
	id serial4 NOT NULL,
	f_name varchar NULL,
	f_content text NOT NULL,
	f_created timestamp NULL DEFAULT CURRENT_TIMESTAMP,
	teacher_id int4 NULL,
	CONSTRAINT task_pk PRIMARY KEY (id)
);
-- public.task foreign keys
ALTER TABLE public.task ADD CONSTRAINT task_fk FOREIGN KEY (teacher_id) REFERENCES public.teacher(id);

-- DROP TABLE public.variant;

CREATE TABLE public.variant (
	id serial4 NOT NULL,
	f_name varchar NULL,
	f_created timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	teacher_id int4 NOT NULL,
	CONSTRAINT variant_pk PRIMARY KEY (id)
);
-- public.variant foreign keys
ALTER TABLE public.variant ADD CONSTRAINT variant_fk FOREIGN KEY (teacher_id) REFERENCES public.teacher(id);


-- DROP TABLE public.task_variant;

CREATE TABLE public.task_variant (
	id serial4 NOT NULL,
	variant_id int4 NOT NULL,
	task_id int4 NOT NULL,
	f_ordinal int4 NULL,
	CONSTRAINT task_variant_pk PRIMARY KEY (id),
	CONSTRAINT task_variant_un UNIQUE (variant_id, task_id)
);
-- public.task_variant foreign keys
ALTER TABLE public.task_variant ADD CONSTRAINT task_variant_fk FOREIGN KEY (task_id) REFERENCES public.task(id);
ALTER TABLE public.task_variant ADD CONSTRAINT task_variant_fk_1 FOREIGN KEY (variant_id) REFERENCES public.variant(id);
