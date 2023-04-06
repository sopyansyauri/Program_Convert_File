import convertapi

convertapi.api_secret = 'jRpa6Vq2KAfFF3g0'
# convertapi.convert('xlsx', {
#     'File': './bensin.csv'
# }, from_format = 'csv').save_files('outputFile/')


msg1 = input("Masukan type file yang mau di convert pdf/xlsx/csv/docx: ")
msg2 = input("masukan nama file: ")
msg3 = input("Masukan ke type mana file mau di convert pdf/xlsx/csv/docx: ")


# untuk convert file pdf
if (msg1 == "pdf" and msg3 == "xlsx"):
    convertapi.convert('xlsx', {
        'File': f"{msg2}"
    }, from_format = 'pdf').save_files('outputFile/')
    print("Berhasil di Convert")
elif (msg1 == "pdf" and msg3 == "csv"):
    convertapi.convert('csv', {
        'File': f"{msg2}"
    }, from_format = 'pdf').save_files('outputFile/')
    print("Berhasil di Convert")
elif (msg1 == "pdf" and msg3 == "docx"):
    convertapi.convert('docx', {
        'File': f"{msg2}"
    }, from_format = 'pdf').save_files('outputFile/')
    print("Berhasil di Convert")
elif (msg1 == "pdf" and msg3 == "pdf"): 
        print("type anda yang ingin di convert sama")



# untuk convert file xlsx
if (msg1 == "xlsx" and msg3 == "pdf"):
    convertapi.convert('pdf', {
        'File': f"{msg2}"
    }, from_format = 'xlsx').save_files('outputFile/')
    print("Berhasil di Convert")
elif (msg1 == "xlsx" and msg3 == "csv"):
    convertapi.convert('csv', {
        'File': f"{msg2}"
    }, from_format = 'xlsx').save_files('outputFile/')
    print("Berhasil di Convert")
elif (msg1 == "xlsx" and msg3 == "docx"):
    # convertapi.convert('docx', {
    #     'File': f"{msg2}"
    # }, from_format = 'xlsx').save_files('outputFile/')
    print("Tidak di suport")
elif (msg1 == "xlsx" and msg3 == "xlsx"): 
        print("type anda yang ingin di convert sama")



# untuk convert file csv
if (msg1 == "csv" and msg3 == "pdf"):
    convertapi.convert('pdf', {
        'File': f"{msg2}"
    }, from_format = 'csv').save_files('outputFile/')
    print("Berhasil di Convert")
elif (msg1 == "csv" and msg3 == "xlsx"):
    convertapi.convert('xlsx', {
        'File': f"{msg2}"
    }, from_format = 'csv').save_files('outputFile/')
    print("Berhasil di Convert")
elif (msg1 == "csv" and msg3 == "docx"):
    # convertapi.convert('docx', {
    #     'File': f"{msg2}"
    # }, from_format = 'csv').save_files('outputFile/')
    print("Tidak di suport")
elif (msg1 == "csv" and msg3 == "csv"): 
        print("type anda yang ingin di convert sama")


# untuk convert file docx
if (msg1 == "docx" and msg3 == "pdf"):
    convertapi.convert('pdf', {
        'File': f"{msg2}"
    }, from_format = 'docx').save_files('outputFile/')
    print("Berhasil di Convert")
elif (msg1 == "docx" and msg3 == "xlsx"):
    # convertapi.convert('xlsx', {
    #     'File': f"{msg2}"
    # }, from_format = 'docx').save_files('outputFile/')
    print("Tidak di suport")
elif (msg1 == "docx" and msg3 == "csv"):
    # convertapi.convert('csv', {
    #     'File': f"{msg2}"
    # }, from_format = 'docx').save_files('outputFile/')
    print("Tidak di suport")
elif (msg1 == "docx" and msg3 == "docx"): 
        print("type anda yang ingin di convert sama")