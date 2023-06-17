create database test;
use test;

CREATE TABLE tb_exercicio(
  idt_exercicio INT AUTO_INCREMENT PRIMARY KEY,
  nme_exercicio VARCHAR(50) NOT NULL,
  dsc_exercicio TEXT NOT NULL,
  num_repeticao_exercicio INT NOT NULL,
  num_gasto_calorico_exercicio INT NOT NULL);

select * from tb_exercicio;