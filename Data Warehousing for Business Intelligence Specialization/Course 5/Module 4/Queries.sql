--BQ1
SELECT
	LOC.LOCATION_ID
	,LOC.LOCATION_NAME 	
	,SC.SALES_CLASS_ID 		
	,SC.SALES_CLASS_DESC 	
	,TD.TIME_YEAR 	
	,TD.TIME_MONTH
	,SC.BASE_PRICE
	,SUM(QUANTITY_ORDERED)
	,SUM(QUANTITY_ORDERED * UNIT_PRICE)
	FROM W_LOCATION_D AS LOC
	INNER JOIN W_JOB_F AS JOB ON 
		JOB.LOCATION_ID = LOC.LOCATION_ID
	INNER JOIN W_SALES_CLASS_D AS SC ON
		SC.SALES_CLASS_ID = JOB.SALES_CLASS_ID
	INNER JOIN W_TIME_D AS TD ON
		TD.TIME_ID = JOB.CONTRACT_DATE
	GROUP BY LOC.LOCATION_ID
		,LOC.LOCATION_NAME 	
		,SC.SALES_CLASS_ID 		
		,SC.SALES_CLASS_DESC 	
		,TD.TIME_YEAR 	
		,TD.TIME_MONTH
		,SC.BASE_PRICE
		
--BQ2
SELECT
	JOB.JOB_ID
	LOC.LOCATION_ID
	,LOC.LOCATION_NAME 	
	,JOB.UNIT_PRICE
	,JOB.QUANTITY_ORDERED
	,TD.TIME_YEAR 	
	,TD.TIME_MONTH
	,SUM(I.INVOICE_AMOUNT)
	,SUM(I>INVOICE_QUANTITY)
	FROM W_LOCATION_D AS LOC
	INNER JOIN W_JOB_F AS JOB ON 
		JOB.LOCATION_ID = LOC.LOCATION_ID
	INNER JOIN W_TIME_D AS TD ON
		TD.TIME_ID = JOB.CONTRACT_DATE
	INNER JOIN W_SUB_JOB_F AS SJ ON
		SJ.JOB_ID = JOB.JOB_ID
	INNER JOIN W_JOB_SHIPMENT_F AS JS ON
		JS.SUB_JOB_ID = SJ.SUB_JOB_ID
	INNER JOIN W_INVOICELINE_F AS I	
		JS.INVOICE_ID = I.INVOICE_ID
		
--BQ3
CREATE VIEW BQ3
AS
SELECT
	JOB.JOB_ID
	LOC.LOCATION_ID
	,LOC.LOCATION_NAME 	
	,JOB.UNIT_PRICE
	,JOB.QUANTITY_ORDERED
	,TD.TIME_YEAR 	
	,TD.TIME_MONTH
	,SUM(SJ.COST_LABOR) AS CL
	,SUM(SJ.COST_MATERIAL) AS CM
	,SUM(SJ.MACHINE_HOURS * M.RATE_PER_HOUR) AS MR
	,SUM(SJ.COST_OVERHEAD) AS CO
	,SUM(CL + CM + MR + CO) AS TC
	,SUM(SJ.QUANTITY_PRODUCED) AS QP
	,TC/QP AS UC	
	FROM W_LOCATION_D AS LOC
		INNER JOIN W_JOB_F AS JOB ON 
			JOB.LOCATION_ID = LOC.LOCATION_ID
		INNER JOIN W_TIME_D AS TD ON
			TD.TIME_ID = JOB.CONTRACT_DATE
		INNER JOIN W_SUB_JOB_F AS SJ ON
			SJ.JOB_ID = JOB.JOB_ID
		INNER JOIN W_MACHINE_TYPE_D  AS M ON
			SJ.MACHINE_TYPE_ID  = M.MACHINE_TYPE_ID 
	
--BQ4
CREATE VIEW BQ4
AS
SELECT 
	JOB.JOB_ID
	,LOC.LOCATION_ID
	,LOC.LOCATION_NAME
	,SC.SALES_CLASS_ID 		
	,SC.SALES_CLASS_DESC 
	,TD.TIME_YEAR 	
	,TD.TIME_MONTH
	,SUM(I.INVOICE_AMOUNT - I.INVOICE_QUANTITY ) AS [RETURN QUANTITY]
	,
	FROM W_LOCATION_D AS LOC
	INNER JOIN W_JOB_F AS JOB ON 
		JOB.LOCATION_ID = LOC.LOCATION_ID
	INNER JOIN W_SALES_CLASS_D AS SC ON
		SC.SALES_CLASS_ID = JOB.SALES_CLASS_ID
	INNER JOIN W_SUB_JOB_F AS SJ ON
		SJ.JOB_ID = JOB.JOB_ID
	INNER JOIN W_JOB_SHIPMENT_F AS JS ON
		JS.SUB_JOB_ID = SJ.SUB_JOB_ID
	INNER JOIN W_INVOICELINE_F AS I ON	
		JS.INVOICE_ID = I.INVOICE_ID
	INNER JOIN W_TIME_D AS TD ON
		TD.TIME_ID = I.INVOICE_SENT_DATE
	WHERE [RETURN QUANTITY] > 0
	GROUP BY 
	JOB.JOB_ID
	,LOC.LOCATION_ID
	,LOC.LOCATION_NAME
	,SC.SALES_CLASS_ID 		
	,SC.SALES_CLASS_DESC 
	,TD.TIME_YEAR 	
	,TD.TIME_MONTH

--BQ5
SELECT
	JOB.JOB_ID
	,LOC.LOCATION_ID
	,LOC.LOCATION_NAME 	
	,SC.SALES_CLASS_ID 		
	,SC.SALES_CLASS_DESC 	
	,JOB.DATE_PROMISED 		
	,MAX(SJ.ACTUAL_SHIP_DATE)
	,SUM(ACTUAL_QUANTITY)
	,getBusDaysDiff(MAX(SJ.ACTUAL_SHIP_DATE),JOB.DATE_PROMISED)
	FROM W_LOCATION_D AS LOC
	INNER JOIN W_JOB_F AS JOB ON 
		JOB.LOCATION_ID = LOC.LOCATION_ID
	INNER JOIN W_SALES_CLASS_D AS SC ON
		SC.SALES_CLASS_ID = JOB.SALES_CLASS_ID
	INNER JOIN W_TIME_D AS TD ON
		TD.TIME_ID = JOB.DATE_PROMISED
	INNER JOIN W_SUB_JOB_F AS SJ ON
		SJ.JOB_ID = JOB.JOB_ID
	WHERE SJ.ACTUAL_SHIP_DATE > JOB.DATE_PROMISED
	
--BQ6 baki h
SELECT
	JOB.JOB_ID
	,LOC.LOCATION_ID
	,LOC.LOCATION_NAME 	
	,SC.SALES_CLASS_ID 		
	,SC.SALES_CLASS_DESC 	
	,JOB.DATE_SHIP_BY 		 		
	,MAX(SJ.DATE_SHIP_BY)
	,getBusDaysDiff(MAX(SJ.DATE_SHIP_BY),JOB.DATE_PROMISED)
	FROM W_LOCATION_D AS LOC
	INNER JOIN W_JOB_F AS JOB ON 
		JOB.LOCATION_ID = LOC.LOCATION_ID
	INNER JOIN W_SALES_CLASS_D AS SC ON
		SC.SALES_CLASS_ID = JOB.SALES_CLASS_ID
	INNER JOIN W_TIME_D AS TD ON
		TD.TIME_ID = JOB.DATE_PROMISED
	INNER JOIN W_SUB_JOB_F AS SJ ON
		SJ.JOB_ID = JOB.JOB_ID
	WHERE SJ.ACTUAL_SHIP_DATE > JOB.DATE_PROMISED

--AQ1
SELECT
	LOC.LOCATION_ID
	,LOC.LOCATION_NAME 	
	,SC.SALES_CLASS_ID 		
	,SC.SALES_CLASS_DESC 	
	,TD.TIME_YEAR 	
	,TD.TIME_MONTH
	,SC.BASE_PRICE
	,(SUM(QUANTITY_ORDERED) OVER ORDER BY TD.TIME_MONTH ROWS UNBOUNDED PRECEEDING)
	,SUM(QUANTITY_ORDERED * UNIT_PRICE)
	FROM W_LOCATION_D AS LOC
	INNER JOIN W_JOB_F AS JOB ON 
		JOB.LOCATION_ID = LOC.LOCATION_ID
	INNER JOIN W_SALES_CLASS_D AS SC ON
		SC.SALES_CLASS_ID = JOB.SALES_CLASS_ID
	INNER JOIN W_TIME_D AS TD ON
		TD.TIME_ID = JOB.CONTRACT_DATE
	GROUP BY LOC.LOCATION_ID
		,LOC.LOCATION_NAME 	
		,SC.SALES_CLASS_ID 		
		,SC.SALES_CLASS_DESC 	
		,TD.TIME_YEAR 	
		,TD.TIME_MONTH
		,SC.BASE_PRICE
		
--AQ2
SELECT
	LOC.LOCATION_ID
	,LOC.LOCATION_NAME 	
	,SC.SALES_CLASS_ID 		
	,SC.SALES_CLASS_DESC 	
	,TD.TIME_YEAR 	
	,TD.TIME_MONTH
	,SC.BASE_PRICE
	,(AVG(QUANTITY_ORDERED) OVER ORDER BY TD.TIME_MONTH ROWS CURRENT ROW AND 11 PRECEEDING)
	,SUM(QUANTITY_ORDERED * UNIT_PRICE)
	FROM W_LOCATION_D AS LOC
	INNER JOIN W_JOB_F AS JOB ON 
		JOB.LOCATION_ID = LOC.LOCATION_ID
	INNER JOIN W_SALES_CLASS_D AS SC ON
		SC.SALES_CLASS_ID = JOB.SALES_CLASS_ID
	INNER JOIN W_TIME_D AS TD ON
		TD.TIME_ID = JOB.CONTRACT_DATE
	GROUP BY LOC.LOCATION_ID
		,LOC.LOCATION_NAME 	
		,SC.SALES_CLASS_ID 		
		,SC.SALES_CLASS_DESC 	
		,TD.TIME_YEAR 	
		,TD.TIME_MONTH
		,SC.BASE_PRICE
		
--AQ3
SELECT 
	RANK() OVER (PARTITION BY TIME_YEAR ORDER BY [RETURN QUANTITY])
	,SALES_CLASS_DESC
	,TIME_YEAR
	SUM([RETURN QUANTITY])
	FROM BQ4

--AQ4
SELECT
	RATIO_TO_REPORT([RETURN QUANTITY]) OVER (PARTITION BY TIME_YEAR)
	,SALES_CLASS_DESC
	,TIME_YEAR
	SUM([RETURN QUANTITY])
	FROM BQ4 



	






























































































