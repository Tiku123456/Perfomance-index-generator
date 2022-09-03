from fpdf import FPDF


def Pdf(li):
    def red():
        pdf.set_text_color(220,50,50)#red color
        pdf.set_font(style="B")  # enabling bold text
    def black():
        pdf.set_font(style="")#disabling bold text 
        pdf.set_text_color(0)#black enabling
    def content(gh,h):#content creater        
        for _ in range(1):  # repeat data rows
            for row in TABLE_DATA:
                if pdf.will_page_break(40):
                    pdf.add_page()
                for datum in row:
                    if datum==tal:
                        red()
                    if datum in tosub:                        
                        red()
                    elif datum in lna:
                        pdf.cell(gh, line_height, str(datum), border=1)
                    if datum in naps:
                        pdf.cell(gh, line_height, str(datum), border=1,align="C")
                    else:
                        pdf.cell(h, line_height, str(datum), border=1,align='C')
                pdf.ln(line_height)
                
##            pdf.set_auto_page_break(True,10)
            
    def header(n):
        pdf.set_font("courier", size=25)
        pdf.set_font(style="I")  # disabling bold text 
        pdf.set_font(style="B")  # enabling bold text
        pdf.cell(pdf.epw,line_height,'KENDRIYA VIDYALAYA PAINAVU, IDUKKI',align="C")
        pdf.ln(10)
        pdf.cell(pdf.epw,line_height,'CLASS XII RESULT '+D,align="C")
        pdf.ln(10)
        pdf.cell(pdf.epw,line_height,'PERFORMANCE INDEX '+n,align="C")
        pdf.ln(10)
        pdf.cell(pdf.epw,30,'',align="C")
        pdf.ln(14)
        pdf.set_font("helvetica", size=18)
        pdf.set_font(style="")  # disabling bold text 
    def render_table_header(gh,h):
        v=0
        pdf.set_font(style="B")  # enabling bold text
        for col_name in TABLE_COL_NAMES:
            if str(col_name) == "SNO":
                pdf.cell(5, line_height, str(col_name ), border=1,align="C")                
            if str(col_name) == "NAME ":
                pdf.cell(gh, line_height, str(col_name ), border=1,align="C")
            elif str(col_name)== "Subject":
                pdf.cell(gh,line_height , str(col_name), border=1,align="C")
                v+=1
            else:
                pdf.cell(h, line_height, str(col_name), border=1,align="C")
        pdf.ln(line_height)
        pdf.set_font(style="")  # disabling bold text   
    naps=['ENG','MAT','HIN','PHY','CHE','BIO','CS','WEIGHTAGE(W)','TOTAL(N)','N*W']
    TABLE_COL_NAMES = li.pop(0)
    TABLE_DATA = li
    pdf = FPDF("L",'mm','A3')
    pdf.add_page()    
    line_height = pdf.font_size* 2
    col_width = (pdf.epw-51) / 10  # distribute content evenly
    pdf.set_line_width(0.1)
    header('(Overall)')   
    pdf.set_font("helvetica", size=18)     
    render_table_header(51,col_width)
    content(51,col_width)
    black()
    pdf.ln(30)
    pdf.cell(pdf.epw,line_height,'SCHOOL PI= (N*W)*100/n*40',align="C")
    pdf.ln(10)
    pdf.cell(pdf.epw,line_height,"Where n is the total no of students appeared in class X/XII",align="C")
    pdf.ln(20)
    pdf.cell(pdf.epw,line_height,'SCHOOL PI = ('+str(tal)+'*100)/('+str(nostu)+'*40)',align="C")
    pdf.ln(10)
    pdf.cell(pdf.epw+20,line_height,'= '+str(tal*100)+'/'+str(nostu*40),align="C")
    pdf.ln(10)
    red()
    pdf.set_font(style="B")  # enabling bold text
    pdf.cell(pdf.epw+10,line_height,'= '+str(sin[-1]),align='C')
    pdf.add_page()
#Subject wise perfomence index
    pdf.set_font(style="") 
    black()
    header('(Subject Wise)')
    tota,b,ind=[],0,0
    Sub=["(English)",'(Maths)','(Hindi)','(Physics)','(Chemistry)','(Biology)','(Computer Science)']
    for _ in range(len(inw)-3) :#subject wise
        nls=[]
        nls.append(hea)
        nls.append(inw.pop(0))
        nls.append(sin.pop(0))
        nls[2].insert(0,'TOTAL(N)')
        b+=1
        tota.append(nls[-1].pop(-1))
        TABLE_COL_NAMES =nls.pop(0)        
        TABLE_DATA = nls
        render_table_header(51,col_width)
        content(51,col_width)
        red()
        pdf.cell(pdf.epw, line_height*2,'PI'+Sub[ind]+'='+tota[ind],border=1,align='C')
        pdf.ln(3)
        pdf.cell(pdf.epw,line_height,'')
        if ind != len(tota):
            ind+=1
        black()
        pdf.ln(line_height*3)
#Mark order
    pdf.add_page()
    pdf.set_font("courier", size=25)
    pdf.set_font(style="I")  # disabling italic
    pdf.set_font(style="B")  # enabling bold text
    #Header
    pdf.cell(pdf.epw,line_height,'KENDRIYA VIDYALAYA PAINAVU, IDUKKI',align="C")
    pdf.ln(10)
    pdf.cell(pdf.epw,line_height,'CLASS XII RESULT '+D,align="C")
    pdf.ln(10)
    pdf.cell(pdf.epw,line_height,'STUDENTS REPORT (Marks Wise) ',align="C")
    pdf.ln(10)
    pdf.cell(pdf.epw,30,'',align="C")
    pdf.ln(14)
    pdf.set_font("helvetica", size=18)
    pdf.set_font(style="")  # disabling bold text 
    sd=['ENG','MAT/HIN ','PHY','CHE','BIO/CS','%']
    TABLE_COL_NAMES =Tpl.pop(0)        
    TABLE_DATA = Tpl
    pdf.set_font(style="B")  # enabling bold text
    def Header():
        pdf.cell(30, line_height, '',align="C")
        for col_name in TABLE_COL_NAMES:
            if str(col_name) == "SNO"or str(col_name) == ' TOT':
                pdf.cell(col_width/2, line_height, str(col_name ), border=1,align="C")
            if str(col_name) == "NAME ":
                pdf.cell(85, line_height, str(col_name ), border=1,align="C")
            elif col_name in sd:
                pdf.cell(col_width, line_height, str(col_name), border=1,align="C")
        pdf.ln(line_height)
        pdf.set_font(style="")  # disabling bold text
    Header()
    gh=85
    c=0
    for _ in range(1):# repeat data rows
        line_height+=1.5
        for row in TABLE_DATA:
            pdf.cell(30, line_height, '',align="C")
            v=0
            if pdf.will_page_break(10):
                pdf.add_page()
                Header()
            for datum in row:
                if str(datum) in hea:
                    pdf.cell(col_width/2, line_height, str(datum), border=1,align="C")
                if datum.isdigit() :
                    v+=1
                    if datum=='100':
                        pdf.cell(col_width/2, line_height, str(datum), border=1,align="C")
                    elif len(datum)==3 and datum[0]=='0':
                        pdf.cell(col_width/2, line_height, str(datum[1:3]), border=1,align="C")
                    else:
                        pdf.cell(col_width/2, line_height, str(datum), border=1,align="C")
                    v+=1
                elif datum == row[-1]:
                    pdf.cell(col_width, line_height, str(datum), border=1,align="C")
                if datum in lna:
                    pdf.cell(gh, line_height, str(datum), border=1)
                elif v==1:
                    pdf.cell(col_width, line_height, str(datum), border=1,align="C")
            pdf.ln(line_height)
#Teacher Performance Index
    pdf.add_page()
    header('(Teacher Wise)')
    pdf.cell(pdf.epw,30,'',align="C")
    pdf.ln(14)
    TABLE_COL_NAMES=['SNO','Name','Designation','Performance Index']
#Teacher's Names
    tname=['Mr. K Sreenivasulu','Mr. Rajeevan K','Mr. P. V. Pradeep','Mr. Vivek Kumar Kushwaha','Mrs. S Shibi','Mr. Shabin Muhammed','Mr. Rajendar G']
    TABLE_DATA=[['1',tname[0],'PGT Chemistry ',str(tota[5])],['2',tname[1],'PGT English',str(tota[0])],['3',tname[2],'PGT Biology',str(tota[6])],['4',tname[3],'PGT Hindi',str(tota[5])],['5',tname[4],'PGT Maths ',str(tota[5])],['6',tname[5],'PGT Computer Science',str(tota[6])],['7',tname[6],'PGT  Physics',str(tota[3])]]
    col_width= (pdf.epw) /4
    gh=col_width/3
    pdf.cell(34, line_height, '',align="C")
    for col_name in TABLE_COL_NAMES:
        if str(col_name) == "SNO":
            pdf.cell(gh, line_height, str(col_name ), border=1,align="C")
        else:
            pdf.cell(col_width, line_height, str(col_name ), border=1,align="C")
    pdf.ln(line_height)
    for _ in range(1):  # repeat data rows        
        for row in TABLE_DATA:
            pdf.cell(34, line_height, '',align="C")
            if pdf.will_page_break(40):
                pdf.add_page()
            for datum in row:
                if len(datum)>0 and datum[0].isdigit():
                    if len(datum)==1:
                        pdf.cell(gh, line_height, str(datum), border=1,align="C")
                    else:
                        pdf.cell(col_width, line_height, str(datum), border=1,align="C")
                else:
                    pdf.cell(col_width, line_height, str(datum), border=1)
            pdf.ln(line_height)
                    
    pdf.output("Perfomace Index.pdf")#Output pdf
def convert(n,p=5):
    n=str(n)
    for i in range(len(n)):
        if n[i]==".":
            n=n[0:i+p]
            break
    return float(n)

#Markwise order
def markar(na):
    flage=1
    index=0
    sj=['SNO','NAME ','ENG','MAT/HIN ','PHY','CHE','BIO/CS',' TOT','%']
    while True:
        if flage>34:
            break
        tpl=[]
        tp=0
        I=0
        for mark in range(len(na)):
            tm=0
            for m in range(0,len(na[mark]),2):
                tm+=int(na[mark][m])
            if tm>tp:
                tp=tm
                I=mark
        per=(tp/500)*100
        tpl.append(str(flage))
        tpl.append(ln.pop(I))
        tpl.extend(ma.pop(I)+[str(tp)]+[str(convert(per,3))])
        index+=1
        flage+=1
        Tpl.append(tpl)
    Tpl.insert(0,sj)

                
                               
#Grade Count,n*w
def gradem(code,nost):
    cl,cg,to,nw=[],[],0,[]
    for i in range(len(co)):        
        try:
            oi=co[i].index(str(code))
            cl.append(g[i][oi])
        except:
            pass   
    for i in range(len(grade)):        
        cg.append(str(cl.count(grade[i])))
        to+=cl.count(grade[i])
    cg.append(to)
    wa=8
    tow=0
    for m in cg[:len(cg)-1]:
        nw.append(str(int(m)*wa))
        tow+=int(m)*wa
        wa=wa-1
    school_pl=(tow*100)/(nost*8)
    nw.append(str(convert(school_pl))) 
    cg.insert(0,code)
    cg.append(nw)
    nw.insert(-1,tow)
    tosub.append(tow)
    return cg
#Overall weightage
def totalweightage():
    L=[]
    cf=[]
    tg=[]
    
    for i in g:
        for j in i:
            L.append(j)
    for i in range(len(grade)):        
        cf.append(L.count(grade[i]))    
    wa=8
    w=[]
    tow=0
    stg=0
    for m in cf:
        tg.append(m*wa)
        stg+=(m*wa)
        tow+=int(m)*wa
        w.append(str(wa))
        wa=wa-1
    tg.append(stg)
    school_pl=(tow*100)/(nostu*40)
    tg.append(str(convert(school_pl)))
    w.insert(0,'WEIGHTAGE(W)')
    subw.append(w)
    tg.insert(0,'N*W')
    subw.append(tg)
    cf.insert(0,'TOTAL(N)')
    if len(w)<len(hea):
         w.append(" ")
    if len(cf)<len(hea):
        cf.append(" ")
    return cf,w,tg


 # Open of File
grade=['A1','A2','B1','B2','C1','C2','D1','D2','E']
hea=['Subject','A1','A2','B1','B2','C1','C2','D1','D2','E','Total'] 
fh=open("79047.txt","r")
data=fh.readlines()
ln,co,ma,g,top,nostu,tosub=[],[],[],[],[],0,[]
nlen,Tpl,lna=0,[],['NAME']
D=''
subw=[]
for word in data:
    name=""
    p=[]
    if word[0:3]=="246":#Name
        nostu+=1
        n=word.split()
        for i in range(2,len(n)//2):            
            if n[i].isalpha():
                name=name+n[i]+" "
                if len(name)>nlen:
                    nlen=len(name)
        lna.append(name)
        ln.append(name)       
        if n[-2]=="COMP":
            c,d=10,5
        else:
            c,d=9,4
        for i in range(-c,-d):
            p.append(n[i])
        co.append(p)
    if word[0]==" ":#Mark and Grade
        if word[64]=="0"or word[64]=="1":
            l=word.split()
            la=l[1:len(l):2]
            l=l[0:len(l):2]
            ma.append(l)
            g.append(la)
    if len(D)!=9:#Date
        if word[0:4]=='DATE':
            date=word[12:16]
            D+=str(int(date)-1)+"-"+date
     
sc=['301', '041', "302",'042', '043', '044','083']
usb=['ENG','MAT','HIN','PHY','CHE','BIO','CS']
index=[]
        
for ca in sc:
    lis=[]
    for i in co:
        lis.extend(i)
    b=lis.count(ca)
    index.append(gradem(ca,b))                                   
Totalg=totalweightage()


sin=[]
inw=[]
C=0
for i in index:
    sin.append(i.pop(-1))
    i[0]=usb[C]
    if C<len(usb):
        C+=1
    inw.append(i)

for i in Totalg:
    sin.append(i.pop(-1))
    inw.append(i)
inw.insert(0,hea)

for i in range(len(inw)-1):
    if len(inw[i])<len(hea):
        inw[i].append(0)

        
r=0
for grade in g:
    i=1
    for ii in range(len(grade)):
        ma[r].insert(i,grade[ii])
        i+=2
    r+=1
tal=inw[-1][-1]
markar(ma)#Funtion call mark wise
Pdf(inw)#function call for pdf 
print("Program executed succesfully and output converted to PDF")
 
