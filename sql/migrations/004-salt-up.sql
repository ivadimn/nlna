START TRANSACTION ;

ALTER TABLE appuser ALTER COLUMN f_salt SET DEFAULT md5(random()::text) ;

UPDATE appuser SET
    f_salt = md5(random()::text),
    f_password_hash = NULL
    WHERE f_salt is NULL ;

ALTER TABLE appuser ALTER COLUMN f_salt SET NOT NULL ;


COMMIT TRANSACTION ;