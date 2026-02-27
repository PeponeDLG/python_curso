-- libros definition

CREATE TABLE libros (
	isbn TEXT NOT NULL,
	titulo TEXT NOT NULL,
	autor TEXT NOT NULL, disp INTEGER NOT NULL,
	CONSTRAINT libros_pk PRIMARY KEY (isbn)
);

INSERT INTO libros (isbn,titulo,autor,disp) VALUES
	 ('1','El quijote','Cervantes',1),
	 ('2','1984','George Orwell',0);
