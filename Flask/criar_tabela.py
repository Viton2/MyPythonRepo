from Flask import bd

comando = '''
   DROP TABLE IF EXISTS tb_pessoa;
'''
mysql = bd.SQL("root", "uniceub", "tb_pessoa")
if mysql.executar(comando, []):
    print('Tabela tb_pessoa excluida!')

comando = '''
   create table tb_pessoa(
   idt_pessoa int primary key auto_increment,
   nme_pessoa varchar(50) not null,
   end_pessoa varchar(120) not null,
   tel_pessoa varchar(20),
   dsc_path_imagem varchar(100) not null
);
       '''
if mysql.executar(comando, ()):
    print('Tabela tb_pessoa criada!')
