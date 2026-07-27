import openpyxl

customers = [
    ("JD1001", "佳輪工業股份有限公司"),
    ("JD1002", "順騎車業有限公司"),
    ("JD1003", "全鑫五金行"),
    ("JD1004", "東昇企業社"),
    ("JD1005", "慶豐車料行"),
    ("JD1006", "永安車業有限公司"),
    ("JD1007", "台鴻工業有限公司"),
    ("JD1008", "大立車材行"),
    ("JD1009", "昌益企業有限公司"),
    ("JD1010", "立勤五金車料行"),
    ("JD1011", "宏泰車業股份有限公司"),
    ("JD1012", "新和興車行"),
]

# 24組虛構姓名（12業務員 + 12主管），純虛構、不對應任何真實個人
sales_names = ["王志明", "李佩珊", "陳建宏", "張淑芬", "林俊傑", "黃詩涵",
               "吳承翰", "劉美玲", "蔡明哲", "楊雅婷", "許志豪", "鄭雅芳"]
manager_names = ["洪文彬", "彭淑惠", "曾國強", "邱美玉", "潘信宏", "蕭雅琪",
                  "賴俊良", "顏惠雯", "康志偉", "施秀蘭", "范文豪", "游佩玲"]

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "經銷商員工子聯絡人"
ws.append(["客戶代號", "名稱", "職稱", "標籤", "外部識別碼"])

for i, (code, name) in enumerate(customers):
    sales = sales_names[i]
    mgr = manager_names[i]
    ws.append([code, sales, "業務專員", "基層", f"{code}_STAFF_SALES"])
    ws.append([code, mgr, "業務主管", "主管", f"{code}_STAFF_MGR"])

path = r"C:\Users\jenny.lu\Documents\艾創點數位-ERP顧問\經銷商業態案例_去識別化Demo環境建置\02_Demo環境建置紀錄\經銷商員工子聯絡人.xlsx"
wb.save(path)
print("saved", path, "rows:", ws.max_row - 1)
