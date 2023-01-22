CREATE TABLE `demonstracoes_contabeis` (
  `id` int NOT NULL,
  `DATA` datetime DEFAULT NULL,
  `REG_ANS` bigint DEFAULT NULL,
  `CD_CONTA_CONTABIL` bigint DEFAULT NULL,
  `DESCRICAO` text,
  `VL_SALDO_INICIAL` double DEFAULT NULL,
  `VL_SALDO_FINAL` double DEFAULT NULL,
  `ANO` bigint DEFAULT NULL,
  `TRIMESTRE` bigint DEFAULT NULL,
 KEY `ix_ic-test_demonstracoes_contabeis_index` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ;

CREATE TABLE `operadoras_ativas` (
  `id` bigint NOT NULL,
  `registro_ans` bigint DEFAULT NULL,
  `cnpj` text,
  `razao_social` text,
  `nome_fantasia` text,
  `modalidade` text,
  `logradouro` text,
  `numero` text,
  `complemento` text,
  `bairro` text,
  `cidade` text,
  `uf` text,
  `cep` text,
  `ddd` double DEFAULT NULL,
  `telefone` text,
  `fax` text,
  `email` text,
  `representante` text,
  `cargo_representante` text,
  `data_registro_ans` datetime DEFAULT NULL,
  KEY `ix_ic-test_operadoras_ativas_index` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci