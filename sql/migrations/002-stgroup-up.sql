START TRANSACTION ;

CREATE TABLE public.student_group (
	"id" serial4 NOT NULL PRIMARY KEY,
	student_id INT NOT NULL,
	group_id INT NOT NULL,
	CONSTRAINT student_group_student_fk FOREIGN KEY (student_id) REFERENCES public.student("id"),
	CONSTRAINT student_group_group_fk FOREIGN KEY (group_id) REFERENCES public.stgroup("id"),
	CONSTRAINT student_group_un UNIQUE (student_id, group_id)
);

COMMIT TRANSACTION ;