def comma_split(row):
    array_data = []
    i = j = 0
    while True:
        while i<len(row) and row[i]==',':
            i+=1
        if i==len(row):                             # menangkap kasus row == '', ','
            break
        
        j = i
        i+=1
        while i<len(row) and row[i]!=',':
            i+=1
        
        if j==0 and i==len(row) and ',' not in row: # menangkap kasus tidak ada koma dalam row
            return [row]
        
        array_data.append(row[j:i])
    return array_data

f = open("temp_user.csv","r")
raw_rows = f.readlines()
f.close()
rows = [raw_row.replace("\n","") for raw_row in raw_rows]
for row in rows:
    array_data = comma_split(row)
    print(array_data)
