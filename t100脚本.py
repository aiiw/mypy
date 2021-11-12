#該程式未解開Section, 採用最新樣板產出!
#該程式非freestyle程式!
{<section id="asfr302_x01.description" type="s" >}


{</section>}

{<section id="asfr302_x01.global" readonly="Y" type="s" >}

 
IMPORT os
#add-point:增加匯入項目 name="global.import"

#end add-point
 
SCHEMA ds
 
GLOBALS "../../cfg/top_global.inc"
GLOBALS "../../cfg/top_report.inc"                  #報表使用的global
 
#報表 type 宣告
DEFINE tm RECORD
       wc STRING,                  #where condition 
       chk01 LIKE type_t.chr5          #判斷列印子報
       END RECORD
 
DEFINE g_str           STRING,                      #列印條件回傳值              
       g_sql           STRING  
 
#add-point:自定義環境變數(Global Variable)(客製用) name="global.variable_customerization"

#end add-point
#add-point:自定義環境變數(Global Variable)(請盡量不要在客製環境修改此段落內容, 否則將後續patch的調整需人工處理) name="global.variable"

#end add-point

{</section>}

{<section id="asfr302_x01.main" readonly="Y" type="s" >}
PUBLIC FUNCTION asfr302_x01(p_arg1,p_arg2)
DEFINE  p_arg1 STRING                  #tm.wc  where condition 
DEFINE  p_arg2 LIKE type_t.chr5         #tm.chk01  判斷列印子報
#add-point:init段define(客製用) name="component.define_customerization"

#end add-point
#add-point:init段define(請盡量不要在客製環境修改此段落內容, 否則將後續patch的調整需人工處理) name="component.define"

#end add-point
 
   LET tm.wc = p_arg1
   LET tm.chk01 = p_arg2
 
   #add-point:報表元件參數準備 name="component.arg.prep"

   #end add-point
   
   #設定SQL錯誤記錄方式 (模組內定義有效)
   WHENEVER ERROR CALL cl_err_msg_log
 
   ##報表元件執行期間是否有錯誤代碼
   LET g_rep_success = 'Y'
   
   #報表元件代號      
   LET g_rep_code = "asfr302_x01"
   IF cl_null(tm.wc) THEN LET tm.wc = " 1=1" END IF
 
   #create 暫存檔
   CALL asfr302_x01_create_tmptable()
 
   IF g_rep_success = 'N' THEN
      RETURN
   END IF
   #報表select欄位準備
   CALL asfr302_x01_sel_prep()
 
   IF g_rep_success = 'N' THEN
      RETURN
   END IF   
   #報表insert的prepare
   CALL asfr302_x01_ins_prep()  
 
   IF g_rep_success = 'N' THEN
      RETURN
   END IF
   #將資料存入tmptable
   CALL asfr302_x01_ins_data() 
 
   IF g_rep_success = 'N' THEN
      RETURN
   END IF   
   #將tmptable資料印出
   CALL asfr302_x01_rep_data()
 
END FUNCTION

{</section>}

{<section id="asfr302_x01.create_tmptable" readonly="Y" type="s" >}
PRIVATE FUNCTION asfr302_x01_create_tmptable()
 
   #清除temptable 陣列
   CALL g_rep_tmpname.clear()
   
   #可切換資料庫，避免大量資料佔資源及空間
   #add-point:create_tmp.before name="create_tmp.before"

   #end add-point:create_tmp.before
 
   #主報表TEMP TABLE的欄位SQL   
   LET g_sql = "sfaadocno.sfaa_t.sfaadocno,sfaadocdt.sfaa_t.sfaadocdt,l_sfaastus.type_t.chr30,l_sfaastus_ref.type_t.chr30,sfaa002.sfaa_t.sfaa002,sfaa002_desc.type_t.chr30,l_sfaa003.type_t.chr30,l_sfaa003_ref.type_t.chr30,l_sfaa057.type_t.chr30,l_sfaa057_ref.type_t.chr30,sfaa006.sfaa_t.sfaa006,sfaa007.sfaa_t.sfaa007,sfaa008.sfaa_t.sfaa008,sfaa009.sfaa_t.sfaa009,sfaa009_desc.type_t.chr30,sfaa021.sfaa_t.sfaa021,sfaa010.sfaa_t.sfaa010,sfaa010_desc.type_t.chr80,sfaa010_desc_1.type_t.chr80,sfaa012.sfaa_t.sfaa012,sfaa013.sfaa_t.sfaa013,sfaa013_desc.type_t.chr30,sfaa017.sfaa_t.sfaa017,sfaa017_desc.type_t.chr80,sfaa019.sfaa_t.sfaa019,sfaa020.sfaa_t.sfaa020,ooff013.type_t.chr500,sfaasite.sfaa_t.sfaasite,sfbaseq.sfba_t.sfbaseq,sfbaseq1.sfba_t.sfbaseq1,sfaa003.sfaa_t.sfaa003,sfba002.sfba_t.sfba002,sfba002_desc.type_t.chr30,sfba003.sfba_t.sfba003,sfba003_desc.type_t.chr30,sfba004.sfba_t.sfba004,sfba006.sfba_t.sfba006,sfba006_desc.type_t.chr80,sfba006_desc_1.type_t.chr80,sfba021.sfba_t.sfba021,sfba021_desc.type_t.chr80,l_sfba008.type_t.chr30,sfba009.sfba_t.sfba009,sfba010.sfba_t.sfba010,sfba011.sfba_t.sfba011,sfba012.sfba_t.sfba012,sfba023.sfba_t.sfba023,sfba024.sfba_t.sfba024,sfba013.sfba_t.sfba013,sfba014.sfba_t.sfba014,sfba014_desc.type_t.chr30,sfba015.sfba_t.sfba015,sfba016.sfba_t.sfba016,sfba025.sfba_t.sfba025,l_qty1.type_t.num20_6,sfba017.sfba_t.sfba017,l_qty2.type_t.num20_6,sfba028.sfba_t.sfba028,l_imaf034.type_t.chr1,l_imae092.type_t.chr1,ooff013_sfba.type_t.chr500,sfaa004.sfaa_t.sfaa004,sfaa057.sfaa_t.sfaa057,sfaastus.sfaa_t.sfaastus,sfaa005.sfaa_t.sfaa005,sfaa011.sfaa_t.sfaa011,sfaa018.sfaa_t.sfaa018,sfaa022.sfaa_t.sfaa022,sfaa058.sfaa_t.sfaa058,sfaa060.sfaa_t.sfaa060,sfaa068.sfaa_t.sfaa068,sfaa049.sfaa_t.sfaa049,sfaa050.sfaa_t.sfaa050,sfaa051.sfaa_t.sfaa051,sfaa055.sfaa_t.sfaa055,sfaa056.sfaa_t.sfaa056,sfba008.sfba_t.sfba008,sfba018.sfba_t.sfba018,sfba022.sfba_t.sfba022,sfba026.sfba_t.sfba026,sfba027.sfba_t.sfba027,l_sfaa004_desc.type_t.chr30,l_sfaa005_desc.type_t.chr30,l_sfaa018_desc.type_t.chr30,l_sfaa060_desc.type_t.chr30,l_sfaa068_desc.type_t.chr30,l_sfaa029_desc.type_t.chr50,l_sfaa030_desc.type_t.chr50,sfaaua003.sfaa_t.sfaaua003,sfaaua033.sfaa_t.sfaaua033" 
   
   #建立TEMP TABLE,主報表序號1 
   IF NOT cl_xg_create_tmptable(g_sql,1) THEN
      LET g_rep_success = 'N'            
   END IF
   #可切換資料庫，避免大量資料佔資源及空間
   #add-point:create_tmp.after name="create_tmp.after"
 
   #end add-point:create_tmp.after
END FUNCTION

{</section>}

{<section id="asfr302_x01.ins_prep" readonly="Y" type="s" >}
PRIVATE FUNCTION asfr302_x01_ins_prep()
DEFINE i              INTEGER
DEFINE l_prep_str     STRING

 
   FOR i = 1 TO g_rep_tmpname.getLength()
      CALL cl_xg_del_data(g_rep_tmpname[i])
      #LET g_sql = g_rep_ins_prep[i]              #透過此lib取得prepare字串 lib精簡
      CASE i
         WHEN 1
         #INSERT INTO PREP
         LET g_sql = " INSERT INTO ",g_rep_db CLIPPED,g_rep_tmpname[1] CLIPPED," VALUES(?,?,?,?,?,?, 
             ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?, 
             ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
         PREPARE insert_prep FROM g_sql
         IF STATUS THEN
            LET l_prep_str ="insert_prep",i
            INITIALIZE g_errparam TO NULL
            LET g_errparam.extend = l_prep_str
            LET g_errparam.code = status
            LET g_errparam.popup = TRUE
            CALL cl_err()
            CALL cl_xg_drop_tmptable()
            LET g_rep_success = 'N'           
         END IF 
         #add-point:insert_prep段 name="insert_prep"

         #end add-point                  
 
 
      END CASE
   END FOR
END FUNCTION

{</section>}

{<section id="asfr302_x01.sel_prep" readonly="Y" type="s" >}
#+ 選單功能實際執行處
PRIVATE FUNCTION asfr302_x01_sel_prep()
DEFINE g_select      STRING
DEFINE g_from        STRING
DEFINE g_where       STRING

   LET g_select = " SELECT sfaadocno,sfaadocdt,",
                  "        sfaastus,",  
                  "        (SELECT gzcbl004 FROM gzcbl_t WHERE gzcbl001 = '13' AND gzcbl002 = sfaastus AND gzcbl003 = '",g_dlang,"') ,",
                  "        sfaa002,",
                  "        (SELECT ooag011 FROM ooag_t WHERE ooagent = sfaaent AND ooag001 = sfaa002) ,",   
                  "        sfaa003,",
                  "        (SELECT gzcbl004 FROM gzcbl_t WHERE gzcbl001 = '4007' AND gzcbl002 = sfaa003 AND gzcbl003 = '",g_dlang,"') ,",
                  "        sfaa057,",
                  "        (SELECT gzcbl004 FROM gzcbl_t WHERE gzcbl001 = '4010' AND gzcbl002 = sfaa057 AND gzcbl003 = '",g_dlang,"') ,",
                  "        sfaa006,sfaa007,sfaa008,",
                  "        sfaa009,",
                  "        (SELECT pmaal004 FROM pmaal_t WHERE pmaalent = sfaaent AND pmaal001 = sfaa009 AND pmaal002 = '",g_dlang,"') ,",
                  "        sfaa021,",  
                  "        sfaa010,a6.imaal003,a6.imaal004,",  
                  "        sfaa012,sfaa013,",
                  "        (SELECT oocal003 FROM oocal_t WHERE oocalent = sfaaent AND oocal001 = sfaa013 AND oocal002 = '",g_dlang,"') ,",
                  "        sfaa017,",
                  "        (SELECT ooefl003 FROM ooefl_t WHERE ooeflent = sfaaent AND ooefl001 = sfaa017 AND ooefl002 = '"||g_dlang||"' ) ooefl003,",  
                  "        sfaa019,",
                  "        sfaa020,",
                 #"        (SELECT ooff013 FROM ooff_t WHERE ooffent = sfaaent AND ooff001 = '6' AND ooff002 = sfaadocno AND ooff012 = '2'),",  #170526-00065#3 add 把備註寫成子查詢  #170719-00019#1 mark
                 #"        '', ",  #170719-00019#1    #170912-00052#1 mark
                 #170912-00052#1 -S  add
                  "       LTRIM((SELECT ooff013 FROM ooff_t WHERE ooffent = sfaaent AND ooff001 = '6' AND ooff002='asft300' AND ooff003 = sfaadocno AND ",
                  "        ooff004 = '0' AND ooff012 = '1')||' '||",
                  "        (SELECT ooff013 FROM ooff_t WHERE ooffent = sfaaent AND ooff001 = '6' AND ooff002='asft300' AND ooff003 = sfaadocno AND ",
                  "        ooff004 = '0' AND ooff012 = '2')||' '|| ",
                  "        (SELECT ooff013 FROM ooff_t WHERE ooffent = sfaaent AND ooff001 = '6' AND ooff002='asft300' AND ooff003 = sfaadocno AND ",
                  "        ooff004 = '0' AND ooff012 = '4')),",
                  #170912-00052#1 -E  add
                  "        sfaasite,",
						"        sfbaseq,sfbaseq1,sfaa003,",
                  "        sfba002,",
                  "        (SELECT oocql004 FROM oocql_t WHERE oocqlent = sfbaent AND oocql001 = '215' AND oocql002 = sfba002 AND oocql003 = '",g_dlang,"') ,",
                  "        sfba003,",
                  "        (SELECT oocql004 FROM oocql_t WHERE oocqlent = sfbaent AND oocql001 = '221' AND oocql002 = sfba003 AND oocql003 = '",g_dlang,"') ,",
                  "        sfba004,",
                  "        sfba006,a10.imaal003,a10.imaal004,",          
                  "        sfba021,", 
                  "        (SELECT inaml004 FROM inaml_t WHERE inamlent=sfbaent AND inaml001=sfba006 AND inaml002=sfba021 AND inaml003='"||g_dlang||"') inaml004,", 
                  "        trim(a11.gzcb002)||':'||trim(a11.gzcbl004),",
                  "        sfba009,sfba010,sfba011,sfba012/100,sfba023,sfba024,sfba013,",  #170525-00154#10 mod 把允许误差率字段sfba012在sql中直接除以100 
                  "        sfba014,",
                  "        (SELECT oocal003 FROM oocal_t WHERE oocalent = sfbaent AND oocal001 = sfba014 AND oocal002 = '",g_dlang,"') ,",  
                  "        sfba015,sfba016,",
                  "        sfba025,(sfba013-sfba016),",  
                  "        sfba017,NULL,   sfba019,sfba020,sfba029,sfba030,",   
                  "        sfba028,",
                  "        (SELECT imaf034 FROM imaf_t WHERE imafent = sfbaent AND imafsite = sfbasite AND imaf001 = sfba006 ),",
                  "        (SELECT imae092 FROM imae_t WHERE imaeent = sfbaent AND imaesite = sfbasite AND imae001 = sfba006 ),",
                 #"        (SELECT ooff013 FROM ooff_t WHERE ooffent = sfaaent AND ooff001 = '7' AND ooff002 = sfaadocno AND ooff003 = sfbaseq AND ooff004 = sfbaseq1 AND ooff012 = '2'),",  #170526-00065#3 add 把備註寫成子查詢  #170719-00019#1 mark
                 #"        (SELECT ooff013 FROM ooff_t WHERE ooffent = sfaaent AND ooff001 = '7' AND ooff003 = sfaadocno AND ooff004 = sfbaseq AND ooff005 = sfbaseq1 AND ooff012 = '1'),",  #170719-00019#1                           #170912-00052#1 mark
                  "        (SELECT ooff013 FROM ooff_t WHERE ooffent = sfaaent AND ooff001 = '7' AND ooff002 = 'asft300' AND ooff003 = sfaadocno AND ooff004 = to_char(sfbaseq) AND ooff005 = to_char(sfbaseq1) AND ooff012 = '1'),",  #170912-00052#1  add
                  "        sfaa004,sfaa057,sfaastus,sfaa005,sfaa011,sfaa018,sfaa022,sfaa058,sfaa060,",
                  "        sfaa068,",   
                  "        sfaa049,sfaa050,sfaa051,sfaa055,sfaa056,",
                  "        sfba008,sfba018,sfba022,sfba026,",  
                  "        sfba027,",  
                  "        (SELECT gzcbl004 FROM gzcbl_t WHERE gzcbl001 = '4008' AND gzcbl002 = sfaa004 AND gzcbl003 = '",g_dlang,"') ,",  
                  "        (SELECT gzcbl004 FROM gzcbl_t WHERE gzcbl001 = '4009' AND gzcbl002 = sfaa005 AND gzcbl003 = '",g_dlang,"') ,",
                  #"        (SELECT ooeal003 FROM ooeal_t WHERE ooealent = sfaaent AND ooeal001 = sfaa018 AND ooeal002 = '",g_dlang,"') l_sfaa018_desc,",       #170425-00037#10 mark by wanghaoz 2017/09/08
                  "        (SELECT ooefl003 FROM ooefl_t WHERE ooeflent = sfaaent AND ooefl001 = sfaa018 AND ooefl002 = '",g_dlang,"') l_sfaa018_desc,",       #170425-00037#10 add by wanghaoz 2017/09/08
                  "        (SELECT oocal003 FROM oocal_t WHERE oocalent = sfaaent AND oocal001 = sfaa060 AND oocal002 = '",g_dlang,"') ,",  
                  "        (SELECt ooefl003 FROM ooefl_t WHERE ooeflent = sfaaent AND ooefl001 = sfaa068 AND ooefl002 = '",g_dlang,"') l_sfaa068_desc,",
                  "        (SELECT pjbbl004 FROM pjbbl_t WHERE pjbblent = sfaaent AND pjbbl001 = sfaa028 AND pjbbl002 = sfaa029 AND pjbbl003 = '",g_dlang,"') ,",        
                  "        (SELECT pjbml004 FROM pjbml_t WHERE pjbmlent = sfaaent AND pjbml001 = sfaa028 AND pjbml002 = sfaa030 AND pjbml003 = '",g_dlang,"') ,",
                  "        sfaaent,sfaaua003,sfaaua033 "     #这一段要手工添加 aiiw                    

   LET g_from = " FROM sfaa_t ",
                " LEFT OUTER JOIN imaal_t a6 ON a6.imaalent = sfaaent AND a6.imaal001 = sfaa010 AND a6.imaal002 = '",g_dlang,"' ",
                " ,sfba_t ",
                " LEFT OUTER JOIN imaal_t a10 ON a10.imaalent = sfbaent AND a10.imaal001 = sfba006 AND a10.imaal002 = '",g_dlang,"' ",
                " LEFT OUTER JOIN (SELECT gzcb001,gzcb002,gzcbl004 ", 
                "                    FROM gzcb_t  ",
                "                    LEFT JOIN gzcbl_t ON gzcb002 = gzcbl002 AND gzcb001 = gzcbl001 AND gzcb001 = '1101' AND gzcbl003 = '",g_dlang,"' ",                                                                                                                                                                      
                "                  ) a11 ON a11.gzcb001 = '1101' AND a11.gzcb002 = sfba008 "
   #160411-00027#12 20160420 add by beckxie ---E
#   #end add-point
#    LET g_from = " FROM sfaa_t,sfba_t"
# 
   #add-point:sel_prep g_where name="sel_prep.g_where"

   #end add-point
    LET g_where = " WHERE " ,tm.wc CLIPPED
 
   #add-point:sel_prep g_order name="sel_prep.g_order"
   LET g_where = " WHERE sfaaent = sfbaent AND sfaadocno = sfbadocno AND " ,tm.wc CLIPPED
   #end add-point
 
   #add-point:sel_prep.sql.before name="sel_prep.sql.before"
 
   #end add-point:sel_prep.sql.before
   LET g_where = g_where ,cl_sql_add_filter("sfaa_t")   #資料過濾功能
   LET g_sql = g_select CLIPPED ," ",g_from CLIPPED ," ",g_where CLIPPED
   LET g_sql = cl_sql_add_mask(g_sql)    #遮蔽特定資料, 若寫至add-point也需複製此段
 
   #add-point:sel_prep.sql.after name="sel_prep.sql.after"
   LET g_sql = g_sql," ORDER BY sfaadocno,sfbaseq,sfbaseq1"
   #DISPLAY "g_sql:" , g_sql
   #end add-point
   PREPARE asfr302_x01_prepare FROM g_sql
   IF STATUS THEN
      INITIALIZE g_errparam TO NULL
      LET g_errparam.extend = 'prepare:'
      LET g_errparam.code = STATUS
      LET g_errparam.popup = TRUE
      CALL cl_err()
      LET g_rep_success = 'N' 
   END IF
   DECLARE asfr302_x01_curs CURSOR FOR asfr302_x01_prepare
 
END FUNCTION

{</section>}

{<section id="asfr302_x01.ins_data" readonly="Y" type="s" >}
PRIVATE FUNCTION asfr302_x01_ins_data()
DEFINE sr RECORD 
   sfaadocno LIKE sfaa_t.sfaadocno, 
   sfaadocdt LIKE sfaa_t.sfaadocdt, 
   l_sfaastus LIKE type_t.chr30, 
   l_sfaastus_ref LIKE type_t.chr30, 
   sfaa002 LIKE sfaa_t.sfaa002, 
   sfaa002_desc LIKE type_t.chr30, 
   l_sfaa003 LIKE type_t.chr30, 
   l_sfaa003_ref LIKE type_t.chr30, 
   l_sfaa057 LIKE type_t.chr30, 
   l_sfaa057_ref LIKE type_t.chr30, 
   sfaa006 LIKE sfaa_t.sfaa006, 
   sfaa007 LIKE sfaa_t.sfaa007, 
   sfaa008 LIKE sfaa_t.sfaa008, 
   sfaa009 LIKE sfaa_t.sfaa009, 
   sfaa009_desc LIKE type_t.chr30, 
   sfaa021 LIKE sfaa_t.sfaa021, 
   sfaa010 LIKE sfaa_t.sfaa010, 
   sfaa010_desc LIKE type_t.chr80, 
   sfaa010_desc_1 LIKE type_t.chr80, 
   sfaa012 LIKE sfaa_t.sfaa012, 
   sfaa013 LIKE sfaa_t.sfaa013, 
   sfaa013_desc LIKE type_t.chr30, 
   sfaa017 LIKE sfaa_t.sfaa017, 
   sfaa017_desc LIKE type_t.chr80, 
   sfaa019 LIKE sfaa_t.sfaa019, 
   sfaa020 LIKE sfaa_t.sfaa020, 
   ooff013 LIKE type_t.chr500, 
   sfaasite LIKE sfaa_t.sfaasite, 
   sfbaseq LIKE sfba_t.sfbaseq, 
   sfbaseq1 LIKE sfba_t.sfbaseq1, 
   sfaa003 LIKE sfaa_t.sfaa003, 
   sfba002 LIKE sfba_t.sfba002, 
   sfba002_desc LIKE type_t.chr30, 
   sfba003 LIKE sfba_t.sfba003, 
   sfba003_desc LIKE type_t.chr30, 
   sfba004 LIKE sfba_t.sfba004, 
   sfba006 LIKE sfba_t.sfba006, 
   sfba006_desc LIKE type_t.chr80, 
   sfba006_desc_1 LIKE type_t.chr80, 
   sfba021 LIKE sfba_t.sfba021, 
   sfba021_desc LIKE type_t.chr80, 
   l_sfba008 LIKE type_t.chr30, 
   sfba009 LIKE sfba_t.sfba009, 
   sfba010 LIKE sfba_t.sfba010, 
   sfba011 LIKE sfba_t.sfba011, 
   sfba012 LIKE sfba_t.sfba012, 
   sfba023 LIKE sfba_t.sfba023, 
   sfba024 LIKE sfba_t.sfba024, 
   sfba013 LIKE sfba_t.sfba013, 
   sfba014 LIKE sfba_t.sfba014, 
   sfba014_desc LIKE type_t.chr30, 
   sfba015 LIKE sfba_t.sfba015, 
   sfba016 LIKE sfba_t.sfba016, 
   sfba025 LIKE sfba_t.sfba025, 
   l_qty1 LIKE type_t.num20_6, 
   sfba017 LIKE sfba_t.sfba017, 
   l_qty2 LIKE type_t.num20_6, 
   sfba019 LIKE sfba_t.sfba019, 
   sfba020 LIKE sfba_t.sfba020, 
   sfba029 LIKE sfba_t.sfba029, 
   sfba030 LIKE sfba_t.sfba030, 
   sfba028 LIKE sfba_t.sfba028, 
   l_imaf034 LIKE type_t.chr1, 
   l_imae092 LIKE type_t.chr1, 
   ooff013_sfba LIKE type_t.chr500, 
   sfaa004 LIKE sfaa_t.sfaa004, 
   sfaa057 LIKE sfaa_t.sfaa057, 
   sfaastus LIKE sfaa_t.sfaastus, 
   sfaa005 LIKE sfaa_t.sfaa005, 
   sfaa011 LIKE sfaa_t.sfaa011, 
   sfaa018 LIKE sfaa_t.sfaa018, 
   sfaa022 LIKE sfaa_t.sfaa022, 
   sfaa058 LIKE sfaa_t.sfaa058, 
   sfaa060 LIKE sfaa_t.sfaa060, 
   sfaa068 LIKE sfaa_t.sfaa068, 
   sfaa049 LIKE sfaa_t.sfaa049, 
   sfaa050 LIKE sfaa_t.sfaa050, 
   sfaa051 LIKE sfaa_t.sfaa051, 
   sfaa055 LIKE sfaa_t.sfaa055, 
   sfaa056 LIKE sfaa_t.sfaa056, 
   sfba008 LIKE sfba_t.sfba008, 
   sfba018 LIKE sfba_t.sfba018, 
   sfba022 LIKE sfba_t.sfba022, 
   sfba026 LIKE sfba_t.sfba026, 
   sfba027 LIKE sfba_t.sfba027, 
   l_sfaa004_desc LIKE type_t.chr30, 
   l_sfaa005_desc LIKE type_t.chr30, 
   l_sfaa018_desc LIKE type_t.chr30, 
   l_sfaa060_desc LIKE type_t.chr30, 
   l_sfaa068_desc LIKE type_t.chr30, 
   l_sfaa029_desc LIKE type_t.chr50, 
   l_sfaa030_desc LIKE type_t.chr50, 
   sfaaent LIKE sfaa_t.sfaaent, 
   sfaaua003 LIKE sfaa_t.sfaaua003, 
   sfaaua033 LIKE sfaa_t.sfaaua033
 END RECORD
#add-point:ins_data段define (客製用) name="ins_data.define_customerization"

#end add-point
#add-point:ins_data段define (請盡量不要在客製環境修改此段落內容, 否則將後續patch的調整需人工處理) name="ins_data.define"
DEFINE l_success           LIKE type_t.num5
DEFINE l_sql               STRING
DEFINE l_str               STRING                #170719-00019#1

 
    LET g_rep_success = 'Y'
 
    FOREACH asfr302_x01_curs INTO sr.*                               
       IF STATUS THEN
          INITIALIZE g_errparam TO NULL
          LET g_errparam.extend = 'foreach:'
          LET g_errparam.code = STATUS
          LET g_errparam.popup = TRUE
          CALL cl_err()
          LET g_rep_success = 'N'
          EXIT FOREACH
       END IF
 
       
       
       ##可用库存量
       LET l_sql = "SELECT SUM(inag008) FROM inag_t WHERE inagent=",sr.sfaaent," AND inagsite='",sr.sfaasite,"'",
                   "   AND inag001='",sr.sfba006,"' AND inag002='",sr.sfba021,"' AND inag007='",sr.sfba014,"'",
                   "   AND inag010='Y'"
       
       IF sr.sfba030 IS NOT NULL THEN
          LET l_sql = l_sql," AND inag003='",sr.sfba030,"'"
       END IF
       IF sr.sfba019 IS NOT NULL THEN
          LET l_sql = l_sql," AND inag004='",sr.sfba019,"'"
       END IF
       IF sr.sfba020 IS NOT NULL THEN
          LET l_sql = l_sql," AND inag005='",sr.sfba020,"'"
       END IF
       IF sr.sfba029 IS NOT NULL THEN
          LET l_sql = l_sql," AND inag006='",sr.sfba029,"'"
       END IF
       PREPARE asfr302_x01_ins_pre FROM l_sql
       EXECUTE asfr302_x01_ins_pre INTO sr.l_qty2
       IF cl_null(sr.l_qty2) THEN
          LET sr.l_qty2 = 0 
       END IF
     
       EXECUTE insert_prep USING sr.sfaadocno,sr.sfaadocdt,sr.l_sfaastus,sr.l_sfaastus_ref,sr.sfaa002,sr.sfaa002_desc,sr.l_sfaa003,sr.l_sfaa003_ref,sr.l_sfaa057,sr.l_sfaa057_ref,sr.sfaa006,sr.sfaa007,sr.sfaa008,sr.sfaa009,sr.sfaa009_desc,sr.sfaa021,sr.sfaa010,sr.sfaa010_desc,sr.sfaa010_desc_1,sr.sfaa012,sr.sfaa013,sr.sfaa013_desc,sr.sfaa017,sr.sfaa017_desc,sr.sfaa019,sr.sfaa020,sr.ooff013,sr.sfaasite,sr.sfbaseq,sr.sfbaseq1,sr.sfaa003,sr.sfba002,sr.sfba002_desc,sr.sfba003,sr.sfba003_desc,sr.sfba004,sr.sfba006,sr.sfba006_desc,sr.sfba006_desc_1,sr.sfba021,sr.sfba021_desc,sr.l_sfba008,sr.sfba009,sr.sfba010,sr.sfba011,sr.sfba012,sr.sfba023,sr.sfba024,sr.sfba013,sr.sfba014,sr.sfba014_desc,sr.sfba015,sr.sfba016,sr.sfba025,sr.l_qty1,sr.sfba017,sr.l_qty2,sr.sfba028,sr.l_imaf034,sr.l_imae092,sr.ooff013_sfba,sr.sfaa004,sr.sfaa057,sr.sfaastus,sr.sfaa005,sr.sfaa011,sr.sfaa018,sr.sfaa022,sr.sfaa058,sr.sfaa060,sr.sfaa068,sr.sfaa049,sr.sfaa050,sr.sfaa051,sr.sfaa055,sr.sfaa056,sr.sfba008,sr.sfba018,sr.sfba022,sr.sfba026,sr.sfba027,sr.l_sfaa004_desc,sr.l_sfaa005_desc,sr.l_sfaa018_desc,sr.l_sfaa060_desc,sr.l_sfaa068_desc,sr.l_sfaa029_desc,sr.l_sfaa030_desc,sr.sfaaua003,sr.sfaaua033
 
       IF SQLCA.SQLCODE THEN
          INITIALIZE g_errparam TO NULL
          LET g_errparam.extend = "asfr302_x01_execute"
          LET g_errparam.code = SQLCA.SQLCODE
          LET g_errparam.popup = FALSE
          CALL cl_err()       
          LET g_rep_success = 'N'
          EXIT FOREACH
       END IF
 
       #add-point:ins_data段after_save name="ins_data.after.save"

       #end add-point
       
    END FOREACH
    
    #add-point:ins_data段after name="ins_data.after"

    #end add-point
 
END FUNCTION

{</section>}

{<section id="asfr302_x01.rep_data" readonly="Y" type="s" >}
PRIVATE FUNCTION asfr302_x01_rep_data()
#add-point:rep_data.define (客製用) name="rep_data.define_customerization"

#end add-point:rep_data.define
#add-point:rep_data.define (請盡量不要在客製環境修改此段落內容, 否則將後續patch的調整需人工處理) name="rep_data.define"

#end add-point:rep_data.define
 
    #add-point:rep_data.before name="rep_data.before"

    #end add-point:rep_data.before
    
    CALL cl_xg_view()
    #add-point:rep_data.after name="rep_data.after"

    #end add-point:rep_data.after
END FUNCTION

{</section>}

{<section id="asfr302_x01.other_function" readonly="Y" type="s" >}


{</section>}