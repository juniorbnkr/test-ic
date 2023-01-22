SELECT  o.registro_ans,
        o.nome_fantasia,
		o.razao_social,
		ROUND(SUM(VL_SALDO_FINAL),2) as TOTAL 
from operadoras_ativas o
	LEFT JOIN demonstracoes_contabeis d ON o.registro_ans = d.REG_ANS
WHERE d.TRIMESTRE =  QUARTER(DATE_SUB(CURDATE(), INTERVAL 2 QUARTER))
	AND d.ANO =  YEAR(DATE_SUB(CURDATE(), INTERVAL 2 QUARTER))
	AND d.DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
GROUP BY o.registro_ans,
		o.nome_fantasia,
		o.razao_social
ORDER BY SUM(VL_SALDO_FINAL) DESC
LIMIT 10;