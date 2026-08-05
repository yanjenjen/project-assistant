import fs from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';

const outDir = new URL('../01_成長管理中心/', import.meta.url);
const qaDir = new URL('../_qa/xlsx/', import.meta.url);
await fs.mkdir(outDir, { recursive: true });
await fs.mkdir(qaDir, { recursive: true });

const wb = Workbook.create();
const names = ['首頁','成長戰略','能力盤點','證據紀錄','專案組合','12週計畫','每週執行','月季檢討','儀表板','設定'];
for (const n of names) wb.worksheets.add(n);

const navy = '#17365D', blue = '#2F75B5', pale = '#D9EAF7', green = '#70AD47', gold = '#FFC000', red = '#C00000', gray = '#F2F2F2', ink = '#1F2937', white = '#FFFFFF';
function title(sheet, text, end='H1') {
  const r = sheet.getRange(`A1:${end}`); r.merge(); r.values=[[text]];
  r.format.fill=navy; r.format.font={bold:true,color:white,size:18}; r.format.rowHeight=34; r.format.verticalAlignment='center';
}
function header(range) {
  range.format.fill=blue; range.format.font={bold:true,color:white}; range.format.verticalAlignment='center'; range.format.wrapText=true; range.format.rowHeight=28;
}
function note(range) { range.format.fill='#FFF2CC'; range.format.font={color:'#7F6000'}; range.format.wrapText=true; }
function tableBody(range) { range.format.borders={preset:'inside',style:'thin',color:'#D9E2F3'}; range.format.verticalAlignment='center'; }
function widths(sheet, map) { for (const [col,w] of Object.entries(map)) sheet.getRange(`${col}:${col}`).format.columnWidth=w; }

// 首頁
{
 const s=wb.worksheets.getItem('首頁'); s.showGridLines=false; title(s,'個人成長作業系統 PGOS｜2026 V1.0','J1');
 s.getRange('A3:J4').merge(); s.getRange('A3').values=[['目的：以 ERP 顧問實戰為根，持續發展思維、專業、AI、顧問、軟實力、執行及市場能力；所有能力升級均以證據為準。']];
 s.getRange('A3:J4').format={fill:pale,font:{bold:true,color:navy,size:12},wrapText:true,verticalAlignment:'center'};
 s.getRange('A6:B12').values=[['使用順序','行動'],['1','填寫「成長戰略」'],['2','完成「能力盤點」自評與證據'],['3','在「專案組合」選一個高價值實戰'],['4','設定一個「12週計畫」'],['5','每週更新成果與證據'],['6','每月／季正式檢討']]; header(s.getRange('A6:B6')); tableBody(s.getRange('A7:B12'));
 s.getRange('D6:J12').values=[['營運原則','','','','','',''],['每季主動發展','1項核心能力＋1–2項支援能力','','','','',''],['能力升級','至少具備 E3 真實實戰；L4 需多次例外情境','','','','',''],['學習方式','70%實戰／20%回饋／10%輸入（原則）','','','','',''],['管理上限','週20分鐘／月60分鐘／季3小時','','','','',''],['資料安全','Git 僅保存去識別化案例與證據','','','','',''],['狀態','V1.0 試運轉；首次季檢後校準','','','','','']];
 s.getRange('D6:J6').merge(); header(s.getRange('D6:J6')); for(let r=7;r<=12;r++) s.getRange(`E${r}:J${r}`).merge(); tableBody(s.getRange('D7:J12'));
 widths(s,{A:14,B:34,C:3,D:18,E:18,F:12,G:12,H:12,I:12,J:12});
}

// 成長戰略
{
 const s=wb.worksheets.getItem('成長戰略'); s.showGridLines=false; title(s,'成長戰略與選擇原則','H1');
 s.getRange('A3:B14').values=[['欄位','內容'],['三年定位','資深 ERP 顧問＋流程／制度顧問＋AI／自動化顧問；採分階段疊加，不同時全面展開。'],['定位狀態','本人已提出方向；第一期季度考核依實戰證據校準'],['本年度主題','建立系統導入顧問基本功：Odoo進銷存、商業流程、八大循環、訪談與專案跟進'],['年度核心成果','完成至少2個12週循環；形成新手顧問導入基礎包與一項可獨立處理的流程能力'],['優先服務問題','新手如何把Odoo功能、商業進銷存、八大循環與真實專案串起來'],['主要領域／流程','Odoo銷售、採購、庫存；建大復盤與興宇貿易導入'],['希望增加的工作','流程理解、需求訪談、專案跟進、實際操作、案例復盤'],['希望降低的工作','無目的全面學習、只看課不操作、晚間長期高負荷學習'],['每週可投入時間','主要使用上班學習時段；暫估10–15小時，兩週後校準；晚上不強制'],['外部回饋者','待指定主管、資深顧問或專案同事'],['年度限制條件','工作與生活平衡、動力維持、專案時程與資料機密']];
 header(s.getRange('A3:B3')); tableBody(s.getRange('A4:B14')); s.getRange('B4:B14').format.wrapText=true;
 s.getRange('D3:H9').values=[['新學習項目評選','','','',''],['評選問題','是/否','說明','',''],['是否支援三年定位？','','','',''],['六個月內有使用場景？','','','',''],['能形成成果或證據？','','','',''],['能與ERP經驗結合？','','','',''],['AI進步後仍有互補價值？','','','','']];
 s.getRange('D3:H3').merge(); header(s.getRange('D3:H3')); s.getRange('D4:F4').merge(); s.getRange('G4:H4').merge(); header(s.getRange('D4:H4')); for(let r=5;r<=9;r++){s.getRange(`D${r}:F${r}`).merge();s.getRange(`H${r}:H${r}`);}
 s.getRange('G5:G9').dataValidation={rule:{type:'list',values:['是','否','待確認']}}; tableBody(s.getRange('D5:H9'));
 widths(s,{A:20,B:66,C:3,D:22,E:12,F:12,G:12,H:26});
}

const caps = [
['思維與決策','系統思考','辨識流程、角色、資訊與回饋迴路的相互影響'],['思維與決策','問題定義','將模糊抱怨轉成可查證、可決策的問題'],['思維與決策','因果與根因分析','區分相關、症狀與根因，設計查證'],['思維與決策','機率與不確定性','呈現假設、信心與風險，不把推測當事實'],['思維與決策','批判思考','檢查來源、反例、偏誤與替代解釋'],['思維與決策','優先順序與取捨','依價值、風險、成本與可行性排序'],['思維與決策','復盤能力','從結果反推判斷與流程的改善點'],
['ERP與流程','Odoo核心模組操作','能在測試環境完成銷售、採購、庫存端到端流程'],['ERP與流程','商業進銷存基礎','理解單據、狀態、主資料、物流與帳務的基本關係'],['ERP與流程','八大循環與內控基礎','理解各循環目的、風險、控制點及與系統的連結'],['ERP與流程','跨模組流程理解','理解訂單、採購、庫存、財會等資料連動'],['ERP與流程','主資料治理','辨識編碼、責任、品質與變更控制'],['ERP與流程','內控與權責','設計授權、核准、勾稽、追溯及例外'],['ERP與流程','流程異常診斷','區分系統、資料、流程及人的原因'],['ERP與流程','產業情境理解','將標準流程調整為可落地產業作法'],
['資料與AI','Excel與資料整理','可重現地清理、比對及彙總資料'],['資料與AI','SQL查詢','跨單據查核差異並解釋結果'],['資料與AI','資料品質','檢查完整性、一致性、正確性與時效'],['資料與AI','API與整合概念','理解事件、欄位、錯誤、重送與權限'],['資料與AI','AI協作設計','定義輸入、上下文、工具及人工判斷點'],['資料與AI','AI評測與驗證','建立測試案例、門檻、抽查及復原方式'],['資料與AI','工作流自動化','將重複任務改為可監控、可維護流程'],
['顧問能力','訪談與提問','取得事實、例外、矛盾及利害關係'],['顧問能力','需求分析','把需求轉成範圍、規則、驗收與限制'],['顧問能力','流程設計','區分現行、建議、系統、權責及例外'],['顧問能力','方案評估','比較效益、成本、風險及副作用'],['顧問能力','測試與驗收','建立案例並追蹤缺陷與通過條件'],['顧問能力','導入與變更管理','讓使用者理解、採用並維持新作法'],
['軟實力','傾聽與同理','理解對方意圖、限制及未明說顧慮'],['軟實力','口頭表達','依對象清楚說明結論、依據與行動'],['軟實力','書面表達','產出可執行、可追溯的正式文件'],['軟實力','說服與談判','在利益不同時形成可接受方案'],['軟實力','衝突處理','區分事實、立場與利益並促成決策'],['軟實力','跨部門協作','管理依賴、承諾、資訊與責任'],['軟實力','建立信任','保持一致、透明、守密並對承諾負責'],
['執行與身心','專注與時間配置','保護高價值工作時間並減少切換'],['執行與身心','情緒與壓力調節','在高壓下保持判斷並適時求助'],['執行與身心','韌性與復原','從失敗恢復且調整方法'],['執行與身心','持續學習','以真實問題驅動輸入、練習與反饋'],
['職涯與市場','作品與案例','以去識別化成果證明能力'],['職涯與市場','方法論資產','將經驗形成可重用、可教導的方法'],['職涯與市場','專業關係網絡','建立可交換知識、機會與回饋的關係'],['職涯與市場','職涯選擇權','降低對單一公司、工具或產品的依賴']
];

// 能力盤點
{
 const s=wb.worksheets.getItem('能力盤點'); s.showGridLines=false; title(s,'七大能力盤點｜分數必須搭配證據','J1');
 s.getRange('A3:J3').values=[['領域','能力','行為定義','現況L0–L5','12月目標','差距','證據等級','信心','本季優先','證據／備註']]; header(s.getRange('A3:J3'));
 const provisional = {
  'Odoo核心模組操作':[1,3,null,'E1','中','是','新手學習中；已有部分專案接觸，待操作證據校準'],
  '商業進銷存基礎':[0,3,null,'E0','高','是','本人明確表示為主要痛點'],
  '八大循環與內控基礎':[0,2,null,'E0','高','否','第一期先建立定位圖，不要求深入精通'],
  '跨模組流程理解':[0,2,null,'E0','高','否','隨進銷存實作逐步建立'],
  '訪談與提問':[0,2,null,'E0','中','是','興宇貿易專案作為實戰情境'],
  '持續學習':[1,3,null,'E1','中','否','作為執行機制持續觀察，不占用本季三項主動能力名額'],
  'Excel與資料整理':[1,2,null,'E1','低','否','本人表示已有使用能力，程度待實作校準'],
  'AI協作設計':[1,2,null,'E1','低','否','本人表示已有AI工具能力，程度待實作校準'],
  '作品與案例':[1,2,null,'E1','中','否','建大專案可作第一筆去識別化復盤']
 };
 const rows=caps.map(x=>{const p=provisional[x[1]]; return p?[...x,...p]:[...x,null,3,null,'E0','低','否','待優勢測評與實戰盤點'];}); s.getRange(`A4:J${3+rows.length}`).values=rows;
 s.getRange(`F4:F${3+rows.length}`).formulas=rows.map((_,i)=>[`=IF(OR(D${i+4}="",E${i+4}=""),"",E${i+4}-D${i+4})`]);
 s.getRange(`D4:E${3+rows.length}`).dataValidation={rule:{type:'whole',operator:'between',formula1:0,formula2:5}};
 s.getRange(`G4:G${3+rows.length}`).dataValidation={rule:{type:'list',values:['E0','E1','E2','E3','E4']}};
 s.getRange(`H4:H${3+rows.length}`).dataValidation={rule:{type:'list',values:['低','中','高']}};
 s.getRange(`I4:I${3+rows.length}`).dataValidation={rule:{type:'list',values:['是','否']}};
 tableBody(s.getRange(`A4:J${3+rows.length}`)); s.getRange(`C4:C${3+rows.length}`).format.wrapText=true; s.getRange(`J4:J${3+rows.length}`).format.wrapText=true;
 s.freezePanes.freezeRows(3); s.getRange('D4:D50').format.fill='#FFF2CC'; s.getRange('E4:E50').format.fill='#E2F0D9';
 widths(s,{A:16,B:22,C:46,D:13,E:13,F:10,G:12,H:10,I:12,J:34});
}

// 證據紀錄
{
 const s=wb.worksheets.getItem('證據紀錄'); s.showGridLines=false; title(s,'能力證據紀錄','L1');
 s.getRange('A3:L3').values=[['證據ID','日期','能力領域','能力','證據等級','情境／任務','實際行動','結果','外部回饋','檔案連結','去識別化','下次改善']]; header(s.getRange('A3:L3'));
 s.getRange('A4:L53').format.rowHeight=32; tableBody(s.getRange('A4:L53')); s.getRange('B4:B53').setNumberFormat('yyyy-mm-dd');
 s.getRange('E4:E53').dataValidation={rule:{type:'list',values:['E1','E2','E3','E4']}}; s.getRange('K4:K53').dataValidation={rule:{type:'list',values:['是','否','不適用']}};
 s.freezePanes.freezeRows(3); widths(s,{A:12,B:13,C:16,D:20,E:12,F:34,G:34,H:28,I:28,J:36,K:13,L:30});
}

// 專案組合
{
 const s=wb.worksheets.getItem('專案組合'); s.showGridLines=false; title(s,'成長型專案組合與優先排序','M1');
 s.getRange('A3:M3').values=[['專案ID','專案名稱','類型','關聯能力','工作頻率','工作價值','未來定位','可形成證據','可重用','8週可完成','總分','狀態','下一步']]; header(s.getRange('A3:M3'));
 s.getRange('A4:M23').format.rowHeight=28; tableBody(s.getRange('A4:M23'));
 s.getRange('C4:C23').dataValidation={rule:{type:'list',values:['效率型','能力型','資產型','複合型']}}; s.getRange('E4:J23').dataValidation={rule:{type:'whole',operator:'between',formula1:1,formula2:5}};
 s.getRange('K4:K23').formulas=Array.from({length:20},(_,i)=>[`=IF(COUNTA(E${i+4}:J${i+4})=0,"",SUM(E${i+4}:J${i+4}))`]);
 s.getRange('L4:L23').dataValidation={rule:{type:'list',values:['候選','評估中','本季執行','暫停','完成']}};
 s.getRange('A4:J5').values=[['PG-001','新手顧問導入基礎包','複合型','Odoo／進銷存／訪談／專案跟進',5,5,5,5,5,3],['PG-002','建大專案去識別化復盤','資產型','作品與案例／復盤能力',3,4,4,5,5,5]];
 s.getRange('L4:M5').values=[['本季執行','依12週計畫逐週完成，以興宇貿易作實戰主線'],['候選','第7週完成案例紀錄，敏感資料不得進Git']];
 s.freezePanes.freezeRows(3); widths(s,{A:12,B:32,C:14,D:24,E:11,F:11,G:11,H:12,I:11,J:12,K:10,L:14,M:34});
}

// 12週計畫
{
 const s=wb.worksheets.getItem('12週計畫'); s.showGridLines=false; title(s,'12週成長循環','J1');
 s.getRange('A3:B11').values=[['欄位','內容'],['循環期間','2026-08-10 至 2026-11-01（依專案時程可順延）'],['核心成果','形成新手顧問導入基礎包，並能在指導下參與興宇貿易的流程理解、訪談準備、跟進或需求整理'],['核心能力','Odoo核心進銷存流程理解與操作'],['支援能力1','需求訪談與提問'],['支援能力2','專案跟進與知識沉澱'],['實戰專案','建大專案復盤＋興宇貿易導入準備／參與'],['可重用資產','進銷存總圖、八大循環定位圖、訪談前置包、新手顧問導入基礎包'],['成功標準','完成3條Odoo端到端流程、2張流程圖、1份建大復盤、1份興宇訪談前置包及至少6筆E2/E3證據候選']]; header(s.getRange('A3:B3')); tableBody(s.getRange('A4:B11')); s.getRange('B4:B11').format.fill='#FFF2CC'; s.getRange('B4:B11').format.wrapText=true;
 s.getRange('A14:J14').values=[['週次','週成果','關鍵行動','實戰情境','所需學習','回饋來源','證據／資產','狀態','風險／阻礙','完成率']]; header(s.getRange('A14:J14'));
 const weeks=[
 [1,'建立導入學習地圖','盤點專案階段、Odoo模組、進銷存與八大循環關係','建大與興宇已知情境','專案生命週期與Odoo模組概覽','主管／資深顧問','個人學習地圖','未開始','避免只收藏資料',0],
 [2,'完成銷售到收款基本流程','在測試環境走完客戶、報價、訂單、出貨、發票','Odoo測試公司','銷售主資料、單據與狀態','同事／AI反例檢查','操作紀錄＋流程圖','未開始','會計細節先標待確認',0],
 [3,'完成採購到付款基本流程','走完供應商、詢價、採購、收貨、帳單','Odoo測試公司','採購主資料、單據與狀態','同事／AI反例檢查','操作紀錄＋流程圖','未開始','不要只看操作影片',0],
 [4,'完成庫存與主資料基本流程','練習倉庫、位置、調撥、盤點與產品資料','Odoo測試公司','庫存移動與主資料','資深顧問','庫存／主資料檢核表','未開始','保留專案插單緩衝',0],
 [5,'串接進銷存跨模組關係','找出單據、狀態、資料與異常的前後影響','建大或測試資料','端到端流程與例外','資深顧問','進銷存端到端總圖','未開始','圖先求可解釋再求完整',0],
 [6,'建立八大循環基礎地圖','整理目的、常見風險、控制點及Odoo連結','公司制度範本與案例','八大循環概覽','主管／制度資料','八大循環定位圖','未開始','本期只建骨架',0],
 [7,'完成建大專案復盤','整理參與工作、困難、判斷、結果與改善','建大專案去識別化資料','案例復盤方法','專案同事','去識別化案例','未開始','提交Git前去識別化',0],
 [8,'建立需求訪談基本方法','練習現況、問題、規則、資料、例外與驗收提問','模擬情境','訪談結構與追問','資深顧問／模擬對象','通用訪談題綱','未開始','不要把問卷當訪談',0],
 [9,'完成興宇貿易訪談前置包','整理背景、假設、資料、流程與待確認事項','興宇貿易專案','貿易業進銷存情境','專案負責人','訪談前置包V1','未開始','資料不足必須標示',0],
 [10,'參與或模擬一次訪談','觀察提問、矛盾、缺口及後續事項','興宇真實或模擬訪談','傾聽、記錄與追問','訪談主持人','訪談紀錄＋回饋','未開始','專案未啟動則使用模擬',0],
 [11,'整理需求與流程差異','區分現行、建議、系統、權責與例外','興宇或去識別化案例','需求與流程整理','專案負責人','需求／流程整理稿','未開始','不自行承諾系統方案',0],
 [12,'完成季度考核與基礎包','依證據校準能力並決定第二期題目','PGOS季度考核','證據評量與復盤','主管／AI教練','新手顧問導入基礎包V1','未開始','分數不得脫離證據',0]
 ]; s.getRange('A15:J26').values=weeks; s.getRange('H15:H26').dataValidation={rule:{type:'list',values:['未開始','進行中','完成','延後','取消']}}; s.getRange('J15:J26').dataValidation={rule:{type:'decimal',operator:'between',formula1:0,formula2:1}}; s.getRange('J15:J26').setNumberFormat('0%'); tableBody(s.getRange('A15:J26')); s.getRange('B15:I26').format.wrapText=true; s.getRange('A15:J26').format.rowHeight=42;
 s.getRange('D4:J4').merge(); s.getRange('D4').values=[['規則：12週只設定1項核心能力、1個實戰專案及1項資產成果。沒有實戰情境的學習不得成為核心項目。']]; note(s.getRange('D4:J4'));
 widths(s,{A:12,B:30,C:32,D:24,E:24,F:22,G:26,H:13,I:26,J:12});
}

// 每週執行
{
 const s=wb.worksheets.getItem('每週執行'); s.showGridLines=false; title(s,'每週執行與狀態追蹤','M1');
 s.getRange('A3:M3').values=[['週起日','本週唯一成果','預計時數','實際時數','實戰時數','純學習時數','完成率','新增證據數','新增資產數','能量1–5','壓力1–5','主要障礙','下週重點']]; header(s.getRange('A3:M3'));
 s.getRange('A4:M55').format.rowHeight=30; tableBody(s.getRange('A4:M55')); s.getRange('A4:A55').setNumberFormat('yyyy-mm-dd'); s.getRange('G4:G55').setNumberFormat('0%');
 s.getRange('C4:F55').dataValidation={rule:{type:'decimal',operator:'between',formula1:0,formula2:80}}; s.getRange('G4:G55').dataValidation={rule:{type:'decimal',operator:'between',formula1:0,formula2:1}}; s.getRange('H4:K55').dataValidation={rule:{type:'whole',operator:'between',formula1:0,formula2:20}};
 s.freezePanes.freezeRows(3); widths(s,{A:14,B:36,C:12,D:12,E:12,F:13,G:11,H:12,I:12,J:11,K:11,L:30,M:30});
}

// 月季檢討
{
 const s=wb.worksheets.getItem('月季檢討'); s.showGridLines=false; title(s,'月度與季度治理紀錄','L1');
 s.getRange('A3:L3').values=[['期間','類型','最重要成果','未完成與原因','E3/E4證據','外部回饋','工作結構變化','身心狀態','繼續','停止','開始','下一期唯一重點']]; header(s.getRange('A3:L3'));
 s.getRange('A4:L31').format.rowHeight=45; s.getRange('A4:L31').format.wrapText=true; tableBody(s.getRange('A4:L31')); s.getRange('B4:B31').dataValidation={rule:{type:'list',values:['月檢討','季考核','年度檢討']}};
 widths(s,{A:14,B:13,C:34,D:32,E:26,F:26,G:30,H:24,I:22,J:22,K:22,L:34});
}

// 設定
{
 const s=wb.worksheets.getItem('設定'); s.showGridLines=false; title(s,'評分規則與能力證據定義','F1');
 s.getRange('A3:C9').values=[['能力等級','名稱','判定標準'],[0,'尚未理解','無法辨識或說明'],[1,'能說明','可說明概念，尚無法穩定使用'],[2,'能協作完成','在模板、AI或他人提醒下完成'],[3,'能獨立完成','一般真實情境可獨立完成'],[4,'能處理例外','複雜、高壓或例外情境仍有效'],[5,'能建立方法','可教導他人並持續改善方法']]; header(s.getRange('A3:C3')); tableBody(s.getRange('A4:C9'));
 s.getRange('A12:C17').values=[['證據等級','名稱','例子'],['E0','無證據','純自我感覺'],['E1','知識證據','筆記、測驗、概念說明'],['E2','模擬證據','練習、模擬案例'],['E3','實戰證據','真實專案交付物'],['E4','結果證據','時間、品質、採用或外部成果']]; header(s.getRange('A12:C12')); tableBody(s.getRange('A13:C17'));
 s.getRange('E3:F10').values=[['七大領域','說明'],['思維與決策','如何辨識、推理、取捨及復盤'],['ERP與流程','企業流程、資料、制度與系統'],['資料與AI','資料分析、AI、整合與自動化'],['顧問能力','訪談、診斷、設計及導入'],['軟實力','溝通、關係、協作與影響'],['執行與身心','專注、韌性、壓力與持續學習'],['職涯與市場','作品、方法、聲譽與選擇權']]; header(s.getRange('E3:F3')); tableBody(s.getRange('E4:F10'));
 widths(s,{A:14,B:18,C:52,D:4,E:18,F:52});
}

// 儀表板
{
 const s=wb.worksheets.getItem('儀表板'); s.showGridLines=false; title(s,'PGOS 成長儀表板','N1');
 s.getRange('A3:B10').values=[['核心指標','目前值'],['已盤點能力數',null],['本季優先能力數',null],['E3/E4證據數',null],['候選／執行專案數',null],['完成專案數',null],['累計實際時數',null],['累計新增資產',null]]; header(s.getRange('A3:B3'));
 s.getRange('B4:B10').formulas=[['=COUNT(\'能力盤點\'!D4:D50)'],['=COUNTIF(\'能力盤點\'!I4:I50,"是")'],['=COUNTIF(\'證據紀錄\'!E4:E53,"E3")+COUNTIF(\'證據紀錄\'!E4:E53,"E4")'],['=COUNTIF(\'專案組合\'!L4:L23,"候選")+COUNTIF(\'專案組合\'!L4:L23,"本季執行")'],['=COUNTIF(\'專案組合\'!L4:L23,"完成")'],['=SUM(\'每週執行\'!D4:D55)'],['=SUM(\'每週執行\'!I4:I55)']]; s.getRange('B4:B10').format.fill='#E2F0D9'; s.getRange('B4:B10').format.font={bold:true,color:navy,size:14}; tableBody(s.getRange('A4:B10'));
 const domains=['思維與決策','ERP與流程','資料與AI','顧問能力','軟實力','執行與身心','職涯與市場']; s.getRange('D3:F3').values=[['能力領域','目前平均','12月目標平均']]; header(s.getRange('D3:F3')); s.getRange('D4:D10').values=domains.map(x=>[x]);
 s.getRange('E4:E10').formulas=domains.map((_,i)=>[`=IFERROR(AVERAGEIF(\'能力盤點\'!A4:A50,D${i+4},\'能力盤點\'!D4:D50),0)`]);
 s.getRange('F4:F10').formulas=domains.map((_,i)=>[`=IFERROR(AVERAGEIF(\'能力盤點\'!A4:A50,D${i+4},\'能力盤點\'!E4:E50),0)`]); s.getRange('E4:F10').setNumberFormat('0.0'); tableBody(s.getRange('D4:F10'));
 const c=s.charts.add('bar',s.getRange('D3:F10')); c.title='七大能力：現況與12月目標'; c.hasLegend=true; c.setPosition('H3','N18');
 s.getRange('D13:G13').values=[['最近週次','實際時數','新增證據','新增資產']]; header(s.getRange('D13:G13'));
 for(let i=0;i<12;i++){const r=14+i;s.getRange(`D${r}:G${r}`).formulas=[[`=IF(\'每週執行\'!A${4+i}="","",\'每週執行\'!A${4+i})`,`=IF(\'每週執行\'!A${4+i}="","",\'每週執行\'!D${4+i})`,`=IF(\'每週執行\'!A${4+i}="","",\'每週執行\'!H${4+i})`,`=IF(\'每週執行\'!A${4+i}="","",\'每週執行\'!I${4+i})`]];} s.getRange('D14:D25').setNumberFormat('yyyy-mm-dd'); tableBody(s.getRange('D14:G25'));
 const t=s.charts.add('line',s.getRange('D13:G25')); t.title='每週投入與成果趨勢'; t.hasLegend=true; t.setPosition('H20','N36');
 s.getRange('A13:B17').values=[['資料品質檢查','結果'],['能力未附證據',null],['未去識別化證據',null],['本季優先能力>3',null],['12週核心成果未填',null]]; header(s.getRange('A13:B13'));
 s.getRange('B14:B17').formulas=[['=COUNTIFS(\'能力盤點\'!D4:D50,">0",\'能力盤點\'!J4:J50,"待本人盤點")'],['=COUNTIF(\'證據紀錄\'!K4:K53,"否")'],['=MAX(0,COUNTIF(\'能力盤點\'!I4:I50,"是")-3)'],['=IF(OR(\'12週計畫\'!B5="",\'12週計畫\'!B5="待填寫"),1,0)']]; tableBody(s.getRange('A14:B17')); note(s.getRange('A19:F20')); s.getRange('A19').values=[['提醒：分數是導航工具，不是人格評價。思維與軟實力以真實情境、外部回饋及長期趨勢判定。']];
 widths(s,{A:24,B:16,C:4,D:20,E:14,F:16,G:14,H:12,I:12,J:12,K:12,L:12,M:12,N:12});
}

const output = await SpreadsheetFile.exportXlsx(wb);
await output.save(fileURLToPath(new URL('個人成長管理中心_2026_V1.0.xlsx', outDir)));

for (const sname of names) {
  const preview = await wb.render({sheetName:sname, autoCrop:'all', scale:1, format:'png'});
  await fs.writeFile(new URL(`${sname}.png`,qaDir),new Uint8Array(await preview.arrayBuffer()));
}

const key = await wb.inspect({kind:'table',range:'儀表板!A1:N25',include:'values,formulas',tableMaxRows:25,tableMaxCols:14,maxChars:7000});
const errors = await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A',options:{useRegex:true,maxResults:100},summary:'final formula error scan'});
await fs.writeFile(new URL('inspect_dashboard.txt',qaDir),key.ndjson,'utf8');
await fs.writeFile(new URL('formula_errors.txt',qaDir),errors.ndjson,'utf8');
console.log('Workbook created and rendered:', names.join(', '));
