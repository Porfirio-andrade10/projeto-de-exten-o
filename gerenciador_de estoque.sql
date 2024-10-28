CREATE database IF NOT EXISTS Gerenciador_de_Estoque;
use gerenciador_de_estoque; 

-- DROP DATABASE gerenciador_de_estoque;

CREATE TABLE alimentos_nao_pereciveis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    unidade_medida VARCHAR(4) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    custo DECIMAL(10, 2) NOT NULL,
    quantidade_estoque INT NOT NULL,
    data_validade DATE NOT NULL
);

CREATE TABLE  carne (
    id INT AUTO_INCREMENT PRIMARY KEY,
    unidade_medida VARCHAR(4) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    custo DECIMAL(10, 2) NOT NULL,
    quantidade_estoque INT NOT NULL,
    data_validade DATE NOT NULL
);

CREATE TABLE  Hortifruti (
    id INT AUTO_INCREMENT PRIMARY KEY,
    unidade_medida VARCHAR(4) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    custo DECIMAL(10, 2) NOT NULL,
    quantidade_estoque INT NOT NULL,
    data_validade DATE NOT NULL
);

CREATE TABLE  Descartaveis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    unidade_medida VARCHAR(4) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    custo DECIMAL(10, 2) NOT NULL,
    quantidade_estoque INT NOT NULL
);

CREATE TABLE auditoria_estoque (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tabela_nome VARCHAR(50) NOT NULL,
    operacao VARCHAR(10) NOT NULL,  
    unidade_medida_antiga VARCHAR(4),
    nome_antigo VARCHAR(50),
    custo_antigo DECIMAL(10, 2),
    quantidade_estoque_antigo INT,
    data_validade_antigo DATE,
    unidade_medida_nova VARCHAR(4),
    nome_novo VARCHAR(50),
    custo_novo DECIMAL(10, 2),
    quantidade_estoque_novo INT,
    data_validade_novo DATE,
    data_operacao DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- alimentos_não_pereciveis

CREATE TRIGGER auditoria_alimentos_nao_pereciveis_update
AFTER UPDATE ON alimentos_nao_pereciveis
FOR EACH ROW
INSERT INTO auditoria_estoque (
    tabela_nome, operacao, unidade_medida_antiga, nome_antigo, custo_antigo, quantidade_estoque_antigo, 
	data_validade_antigo, unidade_medida_nova, nome_novo, custo_novo, quantidade_estoque_novo,data_validade_novo
) VALUES (
    'alimentos_nao_pereciveis', 'UPDATE', OLD.unidade_medida, OLD.nome, OLD.custo, OLD.quantidade_estoque,OLD.data_validade, 
    NEW.unidade_medida, NEW.nome, NEW.custo, NEW.quantidade_estoque, NEW.data_validade
);

CREATE TRIGGER auditoria_alimentos_nao_pereciveis_insert
AFTER  INSERT ON alimentos_nao_pereciveis
FOR EACH ROW
INSERT INTO auditoria_estoque (
	tabela_nome, operacao,
    unidade_medida_nova, nome_novo, custo_novo, quantidade_estoque_novo, data_validade_novo
)VALUES(
	'alimentos_nao_pereciveis', 'insert',
	NEW.unidade_medida, NEW.nome, NEW.custo, NEW.quantidade_estoque, NEW.data_validade
);

CREATE TRIGGER auditoria_alimentos_nao_pereciveis_delete
BEFORE DELETE ON alimentos_nao_pereciveis
FOR EACH ROW
INSERT INTO auditoria_estoque(
	tabela_nome, operacao, 
    unidade_medida_antiga, nome_antigo, custo_antigo, quantidade_estoque_antigo, data_validade_antigo
)VALUES(
	'alimentos_nao_pereciveis','delete',
    OLD.unidade_medida, OLD.nome, OLD.custo, OLD.quantidade_estoque, OLD.data_validade
    );

-- carne

CREATE TRIGGER carne_update
AFTER UPDATE ON carne
FOR EACH ROW
INSERT INTO auditoria_estoque (
    tabela_nome, operacao, unidade_medida_antiga, nome_antigo, custo_antigo, quantidade_estoque_antigo, 
    data_validade_antigo, 
    unidade_medida_nova, nome_novo, custo_novo, quantidade_estoque_novo,
    data_validade_novo
) VALUES (
    'carne', 'UPDATE', OLD.unidade_medida, OLD.nome, OLD.custo, OLD.quantidade_estoque, 
    OLD.data_validade, 
    NEW.unidade_medida, NEW.nome, NEW.custo, NEW.quantidade_estoque,
    NEW.data_validade
);

CREATE TRIGGER carne_insert
AFTER  INSERT ON carne
FOR EACH ROW
INSERT INTO auditoria_estoque (
	tabela_nome, operacao,
    unidade_medida_nova, nome_novo, custo_novo, quantidade_estoque_novo, 
    data_validade_novo
)VALUES(
	'carne', 'insert',
	NEW.unidade_medida, NEW.nome, NEW.custo, NEW.quantidade_estoque,
    NEW.data_validade
);

CREATE TRIGGER carne_delete
BEFORE DELETE ON carne
FOR EACH ROW
INSERT INTO auditoria_estoque(
	tabela_nome, operacao, 
    unidade_medida_antiga, nome_antigo, custo_antigo, quantidade_estoque_antigo, 
    data_validade_antigo
)VALUES(
	'carne','delete',
    OLD.unidade_medida, OLD.nome, OLD.custo, OLD.quantidade_estoque, 
	OLD.data_validade
    );
    
-- hortifruti

CREATE TRIGGER hortifruti_update
AFTER UPDATE ON hortifruti
FOR EACH ROW
INSERT INTO auditoria_estoque (
    tabela_nome, operacao, unidade_medida_antiga, nome_antigo, custo_antigo, quantidade_estoque_antigo, 
    data_validade_antigo, 
    unidade_medida_nova, nome_novo, custo_novo, quantidade_estoque_novo, 
    data_validade_novo
) VALUES (
    'hortifruti', 'UPDATE', OLD.unidade_medida, OLD.nome, OLD.custo, OLD.quantidade_estoque, 
    OLD.data_validade, 
    NEW.unidade_medida, NEW.nome, NEW.custo, NEW.quantidade_estoque,
    NEW.data_validade
);

CREATE TRIGGER hortifruti_insert
AFTER  INSERT ON hortifruti
FOR EACH ROW
INSERT INTO auditoria_estoque (
	tabela_nome, operacao,
    unidade_medida_nova, nome_novo, custo_novo, quantidade_estoque_novo,
    data_validade_novo
)VALUES(
	'hortifruti', 'insert',
	NEW.unidade_medida, NEW.nome, NEW.custo, NEW.quantidade_estoque,
    NEW.data_validade
);

CREATE TRIGGER hortifruti_delete
BEFORE DELETE ON hortifruti
FOR EACH ROW
INSERT INTO auditoria_estoque(
	tabela_nome, operacao, 
    unidade_medida_antiga, nome_antigo, custo_antigo, quantidade_estoque_antigo, 
	data_validade_antigo
)VALUES(
	'hortifruti','delete',
    OLD.unidade_medida, OLD.nome, OLD.custo, OLD.quantidade_estoque, 
    OLD.data_validade
    );
    
-- descartaveis

CREATE TRIGGER descartaveis_update
AFTER UPDATE ON descartaveis
FOR EACH ROW 
INSERT INTO auditoria_estoque (
    tabela_nome, operacao, unidade_medida_antiga, nome_antigo, custo_antigo, quantidade_estoque_antigo, 
    data_validade_antigo, 
    unidade_medida_nova, nome_novo, custo_novo, quantidade_estoque_novo
) VALUES (
    'descartaveis', 'UPDATE', OLD.unidade_medida, OLD.nome, OLD.custo, OLD.quantidade_estoque, 
    NEW.unidade_medida, NEW.nome, NEW.custo, NEW.quantidade_estoque
);

CREATE TRIGGER descartaveis_insert
AFTER  INSERT ON descartaveis
FOR EACH ROW
INSERT INTO auditoria_estoque (
	tabela_nome, operacao,
    unidade_medida_nova, nome_novo, custo_novo, quantidade_estoque_novo
    
)VALUES(
	'descartaveis', 'insert',
	NEW.unidade_medida, NEW.nome, NEW.custo, NEW.quantidade_estoque
    
);

CREATE TRIGGER descartaveis_delete
BEFORE DELETE ON descartaveis
FOR EACH ROW
INSERT INTO auditoria_estoque(
	tabela_nome, operacao, 
    unidade_medida_antiga, nome_antigo, custo_antigo, quantidade_estoque_antigo
	
)VALUES(
	'descartaveis','delete',
    OLD.unidade_medida, OLD.nome, OLD.custo, OLD.quantidade_estoque
    );

-- Inserindo todos os itens na tabela alimentos_nao_pereciveis
INSERT INTO alimentos_nao_pereciveis (unidade_medida, nome, custo, quantidade_estoque, data_validade)
VALUES 
('KG', 'Açúcar grosso, tipo cristal', 5.00, 100, '2025-12-31'),
('KG', 'Amido de milho, tipo maizena', 4.50, 100, '2025-12-31'),
('KG', 'Arroz parboilizado, tipo 1', 3.80, 200, '2025-12-31'),
('UN', 'Azeitona verde sem caroço', 12.00, 50, '2025-08-31'),
('UN', 'Azeite de Oliva, Tipo Virgem', 20.00, 30, '2025-08-31'),
('UN', 'Batata palha', 10.00, 50, '2025-04-30'),
('UN', 'Condimento caldo de carne', 6.00, 40, '2025-12-31'),
('PACT', 'Condimento Chimichurri', 3.50, 30, '2025-12-31'),
('UN', 'Condimento caldo de galinha', 5.50, 40, '2025-12-31'),
('UN', 'Condimento colorau', 4.00, 60, '2025-06-30'),
('UN', 'Condimento folha de louro', 2.00, 20, '2025-06-30'),
('UN', 'Condimento maionese', 6.00, 40, '2025-12-31'),
('UN', 'Condimento mostarda', 7.00, 30, '2025-12-31'),
('UN', 'Condimento orégano', 3.50, 40, '2025-06-30'),
('UN', 'Ervilha em conserva', 5.00, 30, '2025-12-31'),
('UN', 'Extrato de tomate', 4.50, 50, '2025-08-31'),
('UN', 'Creme de leite', 3.00, 60, '2025-06-30'),
('KG', 'Farinha de Mandioca', 5.50, 80, '2025-04-30'),
('KG', 'Farinha de Trigo', 4.20, 90, '2025-04-30'),
('KG', 'Feijão mulatinho', 7.50, 100, '2025-06-30'),
('KG', 'Feijão macassar', 8.00, 70, '2025-06-30'),
('KG', 'Feijão preto', 8.50, 60, '2025-06-30'),
('PACT', 'Flocos de milho', 4.00, 50, '2025-06-30'),
('UN', 'Leite de coco', 6.00, 40, '2025-06-30'),
('KG', 'Leite em pó integral', 25.00, 30, '2025-04-30'),
('UN', 'Macarrão com ovos, tipo Espaguete', 4.50, 70, '2025-08-31'),
('UN', 'Macarrão com ovos, tipo Parafuso', 4.50, 70, '2025-08-31'),
('UN', 'Margarina vegetal cremosa', 3.50, 50, '2025-06-30'),
('UN', 'Milho Verde em conserva', 5.00, 30, '2025-12-31'),
('UN', 'Molho de Soja, tipo shoyo', 8.00, 40, '2025-12-31'),
('UN', 'Pó para gelatina', 2.00, 100, '2025-12-31'),
('UN', 'Óleo de soja', 6.50, 100, '2025-08-31'),
('UN', 'Queijo ralado, tipo parmesão', 7.00, 30, '2025-04-30'),
('KG', 'Sal refinado', 2.50, 200, '2025-12-31'),
('UN', 'Tempero completo, tipo caseiro', 5.00, 50, '2025-12-31'),
('UN', 'Vinagre de álcool', 3.00, 60, '2025-06-30'),
('PACT', 'Doce industrializado - paçoca', 8.00, 30, '2025-06-30'),
('PACT', 'Doce de fruta goiaba e banana', 8.50, 30, '2025-06-30');

-- Inserindo todos os itens na tabela carne
INSERT INTO carne (unidade_medida, nome, custo, quantidade_estoque, data_validade)
VALUES 
('KG', 'Carne Bovina, tipo acém (inteiro)', 22.00, 50, '2025-06-30'),
('KG', 'Carne Bovina, tipo acém (moído)', 23.00, 50, '2025-06-30'),
('KG', 'Carne bovina, tipo charque', 25.00, 30, '2025-06-30'),
('KG', 'Frango  Filé de Peito', 18.00, 40, '2025-06-30'),
('KG', 'Frango  Sobrecoxa', 15.00, 40, '2025-06-30'),
('UN', 'Empanado de Frango', 12.00, 100, '2025-04-30'),
('KG', 'Linguiça tipo Calabresa', 18.50, 40, '2024-12-31'),
('BND', 'Ovo de galinha tipo extra', 10.00, 30, '2024-12-31'),
('KG', 'Peixe Filé  Merluza', 30.00, 20, '2025-06-30'),
('KG', 'Queijo Mussarela', 25.00, 50, '2025-02-28');

-- Inserindo todos os itens na tabela Hortifruti
INSERT INTO Hortifruti (unidade_medida, nome, custo, quantidade_estoque, data_validade)
VALUES 
('UN', 'Abacaxi, tipo pérola', 3.50, 50, '2025-05-31'),
('KG', 'Abobrinha', 4.00, 30, '2025-05-31'),
('MACO', 'Alface crespa/lisa', 2.50, 100, '2025-05-31'),
('KG', 'Alho', 8.00, 40, '2025-05-31'),
('UN', 'Banana prata', 3.00, 50, '2025-05-31'),
('KG', 'Batata doce', 3.50, 40, '2025-05-31'),
('KG', 'Batata inglesa', 3.20, 60, '2025-05-31'),
('KG', 'Beterraba', 2.80, 40, '2025-05-31'),
('KG', 'Cebola Branca', 4.50, 30, '2025-05-31'),
('MACO', 'Cebolinha', 2.00, 50, '2025-05-31'),
('KG', 'Cenoura', 3.00, 40, '2025-05-31'),
('KG', 'Chuchu', 2.50, 30, '2025-05-31'),
('MACO', 'Coentro in natura', 1.50, 50, '2025-05-31'),
('MACO', 'Couve folha', 2.50, 50, '2025-05-31'),
('KG', 'Jerimum caboclo', 3.20, 40, '2025-05-31'),
('UN', 'Laranja pera', 3.00, 50, '2025-05-31'),
('KG', 'Manga', 4.00, 30, '2025-05-31'),
('KG', 'Macaxeira', 2.50, 40, '2025-05-31'),
('KG', 'Melancia', 4.00, 20, '2025-05-31'),
('KG', 'Melão', 4.50, 20, '2025-05-31'),
('KG', 'Pepino japonês', 3.00, 30, '2025-05-31'),
('KG', 'Pimentão verde', 3.50, 40, '2025-05-31'),
('KG', 'Repolho verde/roxo', 2.50, 30, '2025-05-31'),
('KG', 'Polpa de fruta congelada', 7.00, 30, '2025-12-31'),
('KG', 'Tomate', 4.00, 50, '2025-05-31'),
('PCT', 'Uva-passa desidratada', 5.50, 20, '2025-05-31');

-- Inserindo todos os itens na tabela Descartaveis
INSERT INTO Descartaveis (unidade_medida, nome, custo, quantidade_estoque)
VALUES 
('PCT', 'Copo descartável para água, 200ml', 10.00, 100),
('UN', 'Filme em PVC tipo película aderente', 15.00, 50),
('PCT', 'Fósforo, tipo EXTRA LONGO', 3.50, 60),
('PCT', 'Guardanapo de papel folha 23,5x22cm', 2.00, 80),
('UN', 'Papel alumínio em rolo 30x100cm', 12.00, 40),
('PCT', 'Toalha de papel picotada', 5.00, 100);






