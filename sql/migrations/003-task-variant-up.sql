BEGIN TRANSACTION ;

CREATE TABLE public.variant (
	"id" serial4 NOT NULL PRIMARY KEY,
	f_title text NOT NULL,
	f_created timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	teacher_id int4 NOT NULL,
	CONSTRAINT variant_teacher_fk FOREIGN KEY (teacher_id) REFERENCES public.teacher("id")
);
COMMENT ON TABLE variant IS 'Cведения о варианте перечня задач';
COMMENT ON COLUMN variant.f_title IS 'Наименование варианта';
COMMENT ON COLUMN variant.f_created IS 'время создание варианта';
COMMENT ON COLUMN variant.teacher_id IS 'дентификатор составителя варианта';

/*-----------------------------------------------------------------------------------------------------*/

CREATE TABLE public.task (
	"id" serial4 NOT NULL PRIMARY KEY,
	f_title text NULL,
	f_content text NOT NULL,
	f_created timestamp NULL DEFAULT CURRENT_TIMESTAMP,
	teacher_id int4 NULL,
	CONSTRAINT task_teacher_fk FOREIGN KEY (teacher_id) REFERENCES public.teacher("id")
);

COMMENT ON TABLE task IS 'Cведения о задачt';
COMMENT ON COLUMN task.f_title IS 'Наименование задачи';
COMMENT ON COLUMN task.f_content IS 'Содержание задания ';
COMMENT ON COLUMN task.f_created IS 'Время создание задачи';
COMMENT ON COLUMN task.teacher_id IS 'дентификатор автора задачи';

/*-----------------------------------------------------------------------------------------------------------*/


CREATE TABLE public.task_variant (
	"id" serial4 NOT NULL PRIMARY KEY,
	variant_id int4 NOT NULL,
	task_id int4 NOT NULL,
	f_ordinal int4 NULL,
	CONSTRAINT task_variant_variant_fk FOREIGN KEY (variant_id) REFERENCES public.variant("id"),
	CONSTRAINT task_variant_task_fk FOREIGN KEY (task_id) REFERENCES public.task("id"),
	CONSTRAINT task_variant_un UNIQUE (variant_id, task_id)
);

COMMENT ON TABLE task_variant IS 'Cведения о задачах в вариантах';
COMMENT ON COLUMN task_variant.variant_id IS 'дентификатор варианта';
COMMENT ON COLUMN task_variant.task_id IS 'дентификатор задачи ';
COMMENT ON COLUMN task_variant.f_ordinal IS 'Порядковый номер задачи в варианте';

COMMIT TRANSACTION ;