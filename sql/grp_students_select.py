SELECT_STUDENTS = """
    select vs.pk, vs.f_fio, vs.f_comment  
        from student_group sg
        inner join v_student vs on vs.pk  = sg.student_id  
        where sg.group_id  = ? ;
"""