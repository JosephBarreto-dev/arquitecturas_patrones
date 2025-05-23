CREATE TABLE estudiantes (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

CREATE TABLE docentes (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

CREATE TABLE materias (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    docente_id INTEGER REFERENCES docentes(id)
);

CREATE TABLE notas (
    id SERIAL PRIMARY KEY,
    estudiante_id INTEGER REFERENCES estudiantes(id),
    materia_id INTEGER REFERENCES materias(id),
    nota NUMERIC(3,1)
);
