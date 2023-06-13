create database db_studies;
use db_studies;
-- drop database db_studies;-- 

CREATE TABLE tb_disciplina(
	idt_disc int primary key not null auto_increment,
    sgl_disc varchar(10) not null,
    nme_disc varchar(100) not null,
    crg_hor int not null
);

CREATE TABLE tb_aluno(
	idt_aluno int primary key not null auto_increment,
    nme_aluno varchar(100) not null,
    dta_nasc date
);

CREATE TABLE ta_matricula (
	idt_matricula int primary key not null auto_increment,
    cod_disc int not null,
    cod_aluno int not null,
    mencao varchar(2),
    nmr_faltas int not null,
    CONSTRAINT fk_matricula_disciplina
		foreign key (cod_disc)
			REFERENCES tb_disciplina (idt_disc),
	CONSTRAINT fk_matricula_aluno
		foreign key (cod_aluno)
			REFERENCES tb_aluno (idt_aluno)
);

INSERT INTO tb_disciplina VALUES (default, "MC", "Matematica para Computacao", 75);
INSERT INTO tb_disciplina VALUES (default, "LP", "Logica de Programacao", 75);
INSERT INTO tb_disciplina VALUES (default, "LTPI", "Linguagens e Tecnicas de Programacao I", 75);
INSERT INTO tb_disciplina VALUES (default, "LTPII", "Linguagens e Tecnicas de Programacao II", 75);
INSERT INTO tb_disciplina VALUES (default, "ALGA", "Algebra e Geometria Analitica", 75);

INSERT INTO tb_aluno VALUES (default, "Vitor Castro de Oliveira", "2003-02-11");
INSERT INTO tb_aluno VALUES (default, "Guilherme", "2003-07-22");
INSERT INTO tb_aluno VALUES (default, "Leonardo", "2002-11-15");
INSERT INTO tb_aluno VALUES (default, "Aline", "2002-01-03");
INSERT INTO tb_aluno VALUES (default, "Gabriel", "2003-05-29");
INSERT INTO tb_aluno VALUES (default, "Felipe", "2002-06-19");
INSERT INTO tb_aluno VALUES (default, "Natalia", "2004-10-11");

INSERT INTO ta_matricula VALUES (default, 5, 1, "MS", 0);
INSERT INTO ta_matricula VALUES (default, 5, 3, "SS", 0);
INSERT INTO ta_matricula VALUES (default, 5, 7, "MM", 3);
INSERT INTO ta_matricula VALUES (default, 1, 6, "MI", 9);
INSERT INTO ta_matricula VALUES (default, 1, 4, "MM", 12);
INSERT INTO ta_matricula VALUES (default, 3, 2, "MS", 0);
INSERT INTO ta_matricula VALUES (default, 2, 4, "SS", 0);
INSERT INTO ta_matricula VALUES (default, 2, 5, "MS", 6);
INSERT INTO ta_matricula VALUES (default, 3, 5, "MI", 15);
INSERT INTO ta_matricula VALUES (default, 1, 1, "SS", 0);
INSERT INTO ta_matricula VALUES (default, 4, 7, "MS", 0);
INSERT INTO ta_matricula VALUES (default, 4, 1, "MS", 0);

select * from ta_matricula;

select * from ta_matricula M
	join tb_disciplina D on M.cod_disc = D.idt_disc
    join tb_aluno A on M.cod_aluno = A.idt_aluno
    order by M.idt_matricula;


