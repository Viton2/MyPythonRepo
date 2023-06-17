CREATE DATABASE bd_mapas;

USE bd_mapas;

DROP TABLE IF EXISTS tb_ponto;

CREATE TABLE tb_ponto(
  idt_ponto INT AUTO_INCREMENT PRIMARY KEY,
  nme_ponto VARCHAR(50) NOT NULL,
  lat_ponto DECIMAL(8, 6) NOT NULL,
  lng_ponto DECIMAL(9, 6) NOT NULL);

INSERT INTO tb_ponto (nme_ponto, lat_ponto, lng_ponto) VALUES
  ('Floresta Nacional', -15.78731, -48.06270),
  ('Parque Lago do Cortado', -15.81661, -48.07519),
  ('Zoológico', -15.84717, '-47.93984'),
  ('Biblioteca Nacional', -15.795888, -47.878314),
  ('Praça Portugal', -15.802400, -47.874597),
  ('UniCEUB', -15.767986, -47.892380),
  ('Represa Santa Maria', -15.693475, -47.982037);

SELECT * FROM tb_ponto;
