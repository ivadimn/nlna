SELECT_GROUPS = """
    select s.id as pk, s.f_title  
        from student_group sg 
        inner join stgroup s on s.id = sg.group_id 
        where sg.student_id = ? ;
"""
