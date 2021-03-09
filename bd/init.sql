/* Table 'Pacientes' */
CREATE TABLE "Pacientes" (
id serial NOT NULL,
nome varchar NOT NULL,
idade smallint NOT NULL,
data_nascimento date NOT NULL,
data_diagnostico date,
nome_mae varchar NOT NULL,
sexo varchar(1) NOT NULL,
"Doencas_id" serial,
uf_id integer NOT NULL,
"Login_id" serial NOT NULL,
"Medico_id" serial,
PRIMARY KEY(id));

/* Table 'Doencas' */
CREATE TABLE "Doencas" (
id serial NOT NULL,
nome varchar NOT NULL,
PRIMARY KEY(id));

/* Table 'uf' */
CREATE TABLE uf (
id serial NOT NULL,
sigla varchar(2) NOT NULL,
nome varchar NOT NULL,
PRIMARY KEY(id));

/* Table 'Municipio' */
CREATE TABLE "Municipio" (
id serial NOT NULL,
nome varchar NOT NULL,
uf_id integer NOT NULL,
PRIMARY KEY(id));

/* Table 'Medico' */
CREATE TABLE "Medico" (
id serial NOT NULL,
nome varchar NOT NULL,
crm varchar NOT NULL,
"Login_id" serial NOT NULL,
PRIMARY KEY(id));

/* Table 'Login' */
CREATE TABLE "Login" (
id serial NOT NULL,
"Tipo_Usuario_id" serial NOT NULL,
login varchar NOT NULL,
senha integer NOT NULL,
PRIMARY KEY(id));

/* Table 'Tipo_Usuario' */
CREATE TABLE "Tipo_Usuario" (
id serial NOT NULL,
tipo varchar NOT NULL,
PRIMARY KEY(id));

/* Table 'Gestor' */
CREATE TABLE "Gestor" (
id serial NOT NULL,
nome integer NOT NULL,
"Login_id" serial NOT NULL,
PRIMARY KEY(id));

/* Relation 'Doencas-Pacientes' */
ALTER TABLE "Pacientes" ADD CONSTRAINT "Doencas-Pacientes"
FOREIGN KEY ("Doencas_id")
REFERENCES "Doencas"(id);

/* Relation 'uf-Pacientes' */
ALTER TABLE "Pacientes" ADD CONSTRAINT "uf-Pacientes"
FOREIGN KEY (uf_id)
REFERENCES uf(id);

/* Relation 'uf-Municipio' */
ALTER TABLE "Municipio" ADD CONSTRAINT "uf-Municipio"
FOREIGN KEY (uf_id)
REFERENCES uf(id);

/* Relation 'Tipo_Usuario-Login' */
ALTER TABLE "Login" ADD CONSTRAINT "Tipo_Usuario-Login"
FOREIGN KEY ("Tipo_Usuario_id")
REFERENCES "Tipo_Usuario"(id);

/* Relation 'Login-Medico' */
ALTER TABLE "Medico" ADD CONSTRAINT "Login-Medico"
FOREIGN KEY ("Login_id")
REFERENCES "Login"(id);

/* Relation 'Login-Pacientes' */
ALTER TABLE "Pacientes" ADD CONSTRAINT "Login-Pacientes"
FOREIGN KEY ("Login_id")
REFERENCES "Login"(id);

/* Relation 'Medico-Pacientes' */
ALTER TABLE "Pacientes" ADD CONSTRAINT "Medico-Pacientes"
FOREIGN KEY ("Medico_id")
REFERENCES "Medico"(id);

/* Relation 'Login-Gestor' */
ALTER TABLE "Gestor" ADD CONSTRAINT "Login-Gestor"
FOREIGN KEY ("Login_id")
REFERENCES "Login"(id);

